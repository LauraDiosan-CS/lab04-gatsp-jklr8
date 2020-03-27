from random import random, randrange


class Chromosome:
    def __init__(self, allCosts):
        self._allCosts = allCosts
        self._genes = []
        self._distance = 0
        self._fitness = 0

    def set_genes(self, genes):
        self._genes = genes

    def get_genes(self):
        return self._genes

    def get_distance(self):
        return self._distance

    def crossover(self, p1, p2):
        child =[p1[0]]
        idx1 = randrange(1,len(p1)-1)
        idx2 = randrange(1,len(p2)-1)

        start_idx = min(idx1,idx2)
        end_idx = max(idx1,idx2)

        c1=[]
        c2=[]
        for i in range(start_idx, end_idx):
            c1.append(p1[i])
        c2 = [gene for gene in p2 if gene not in c1 and gene not in child]
        child =child + c1 + c2 + child
        return child

    '''c is a list of genes of a chromosome'''
    def mutation(self, c):
        for gene in range(1,len(c)-1):
            pos = randrange(1,len(c)-1)
            c[gene], c[pos] = c[pos], c[gene]
        return c

    def fitness(self):
        if self._fitness == 0:
            return self.calculate_fitness()
        return self._fitness

    def calculate_fitness(self):
        if self._distance == 0:
            dist = 0
            for i in range (0, len(self._genes)):
                start = self._genes[i]
                if i+1 >= len(self._genes):
                    break
                else:
                    end = self._genes[i+1]
                dist = dist + self._allCosts[start][end]
            self._distance = dist
        self._fitness = 1/self._distance
        return self._fitness



