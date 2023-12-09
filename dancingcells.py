class DancingCells:
    def __init__(self, N):
        self.N = N
        self.dom = list(range(N))
        self.idom = list(range(N))
        self.s = N - 1
    
    def delete(self, k):
        r = self.idom[k]
        if r > self.s:
            return 
        tmp = self.dom[self.s]
        self.dom[r] = tmp
        self.dom[self.s] = k
        self.idom[tmp] = r
        self.idom[k] = self.s
        self.s -= 1
    
    def undelete(self):
        if self.s >= self.N - 1:
            return
        self.s += 1
        return self.dom[self.s]


    def undelete_elem(self, k, return_complexity=False):
        elems = []
        while not self.has(k):
            elems.append(self.undelete())
        
        for e in elems[:-1]:
            self.delete(e)
        
        if return_complexity:
            return 2 * len(elems)
        
    def has(self, k):
        return self.idom[k] <= self.s

    def dump(self):
        print("-" * 80)
        print("s: ", self.s)
        print("Dom: ", self.dom)
        print("IDom: ", self.idom)
        print("-" * 80)
