import operator
import random
import numpy as np
import pandas as pd

from model.Chromosome import Chromosome


class Service:
    def __init__(self, repo):
        self._repo = repo
        self._mutationRatio = 0.333



    def createPath(self):
        if self._repo.get_sourceDest() == -1:
            self._repo.set_source(1)

        path1 = [self._repo.get_sourceDest()-1]
        path2 = list(range(self._repo.get_no_cities()))
        path2.remove(path1[0])
        random.shuffle(path2)
        path = path1 + path2
        path.append(path1[0])
        return path

    def initial_population(self, populationSize):
        population = []
        for i in range(0,populationSize):
            c = Chromosome(self._repo.get_graph())
            c.set_genes(self.createPath())
            population.append(c)
        return population

    '''survival fot the fittest'''
    def sort_path(self, population):
        res = {}
        for c in population:
            res[c] = c.fitness()
        return sorted(res.items(), key = operator.itemgetter(1), reverse = True)

    '''roulette wheel'''
    def select(self, population, sort_path, eliteSize):
        res = []
        info = pd.DataFrame(np.array(sort_path), columns=["PopulationChromo","Fitness"])
        info['cum_sum'] = info.Fitness.cumsum()
        info['probs'] = 100*info.cum_sum/info.Fitness.sum()

        for i in range(0,eliteSize):
            c = sort_path[i][0]
            res.append(c)

        for i in range(0, len(sort_path) - eliteSize):
            ratio = 100*random.random()
            for i in range(0, len(sort_path)):
                if ratio <= info.iat[i,3]:
                    c = sort_path[i][0]
                    res.append(c)
                    break
        return res


    def crossover_population(self, selected_population, eliteSize):
        children = []
        possible_parents = random.sample(selected_population, len(selected_population))

        for i in range(0,eliteSize):
            children.append(selected_population[i])

        for i in range(0, (len(selected_population)-eliteSize)):
            c = Chromosome(self._repo.get_graph())
            c.set_genes(c.crossover(possible_parents[i].get_genes(), possible_parents[len(selected_population) - i -1].get_genes()))
            children.append(c)
        return children

    def mutate_population(self, population):
        res=[]
        for i in range(0,len(population)):
            c = Chromosome(self._repo.get_graph())
            if random.random() < self._mutationRatio:
                c.set_genes(c.mutation(population[i].get_genes()))
            else:
                c.set_genes(population[i].get_genes())
            res.append(c)
        return res


    def create_new_population(self, population, eliteSize):
        sort_path = self.sort_path(population)
        selected_population = self.select(population,sort_path,eliteSize)
        children = self.crossover_population(selected_population, eliteSize)
        new_population = self.mutate_population(children)
        return new_population


    def simulate(self, populationSize, eliteSize, generations):
        population = self.initial_population(populationSize)
        for i in range (0, generations):
            population = self.create_new_population(population, eliteSize)

        result = self.sort_path(population)

        best_chromo = result[0][0]
        return best_chromo

    def write_to_file(self, c):
        self._repo.write_to_file(c)