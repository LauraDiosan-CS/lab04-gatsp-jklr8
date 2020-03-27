from repository.repository import Repository
from service.service import Service

def runTest1():
    repo = Repository("test1.txt")
    service = Service(repo)
    c = service.simulate(20, 10, 30)
    assert(c.get_genes()==[0,1,2,3,0])
    assert(c.get_distance()==4)
    assert(c.fitness() == 1/c.get_distance())

def runTest2():
    repo = Repository("test2.txt")
    service = Service(repo)
    c = service.simulate(50, 10, 100)
    assert (c.get_genes() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    assert (c.get_distance() == 10)
    assert (c.fitness() == 1 / c.get_distance())

def runAllTest():
    runTest1()
    runTest2()


repo = Repository("data/150p_eil51.txt")
service = Service(repo)
c = service.simulate(70,10,250)
service.write_to_file(c)
