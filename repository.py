
def calculate(param, param1, param2, param3):
    xDis = abs(param - param2)
    yDis = abs(param1 - param3)
    from pandas import np
    distance = np.sqrt((xDis ** 2) + (yDis ** 2))
    return int(distance)


class Repository:

    def __init__(self, fileName):
        self._fileName = fileName
        self._graph = []
        self._noCities = 0
        self._sourceDest = -1
        if fileName == "data/150p_eil51.txt":
            self.read_from_file2()
        else:
            self.read_from_file()

    def get_graph(self):
        return self._graph

    def get_no_cities(self):
        return self._noCities

    def get_sourceDest(self):
        return self._sourceDest

    def set_source(self, v):
        self._sourceDest = v


    def read_from_file(self):
        f = open(self._fileName,"r")
        self._noCities = int(f.readline())
        ct=1
        while ct <= self._noCities:
            line = f.readline()
            atr = line.split(",")
            l=[]
            for i in range(0,len(atr)):
                l.append(int(atr[i]))
            self._graph.append(l)
            ct = ct+1
        self._sourceDest = int(f.readline())

    def read_from_file2(self):
        f = open(self._fileName, "r")
        f.readline()
        f.readline()
        f.readline()
        line = f.readline()
        atr = line.split(" ")
        self._noCities = int(atr[2])
        f.readline()
        f.readline()
        ct = 0
        l = []
        while ct < self._noCities:
            line = f.readline()
            atr = line.split(" ")
            l.append(atr)
            ct = ct + 1

        for i in range(0, len(l)):
            ll = []
            for j in range(0, len(l)):
                distance = calculate(int(l[i][1]),int(l[i][2]),int(l[j][1]),int(l[j][2]))
                ll.append(distance)
            self._graph.append(ll)
        f.readline()





    def write_to_file(self,c):
        fileName = self._fileName.split(".")
        solutionFileName = fileName[0] + "_solution." + fileName[1]
        f = open(solutionFileName, "w")
        cost = c.get_distance()
        path = c.get_genes()
        s = str(path[0] + 1)
        for i in range(1, len(path)-1):
            city = path[i] + 1
            s = s + "," + str(city)
        f.write(str(self._noCities) + "\n")
        f.write(s + "\n")
        f.writelines(str(cost)+"\n")