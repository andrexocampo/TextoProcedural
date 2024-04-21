class Nodo:
    def __init__(self,n):
        self.nombre= n
        self.vecinos=[]
        
    def añadir_vecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()
            
class Grafo:
    nodos = {}
    
    def añadir_nodo(self,nodo):
        if isinstance(nodo,Nodo) and nodo.nombre not in self.nodos:
            self.nodos[nodo.nombre]= nodo
            return True
        else:
            return False
        
    def añadir_vertice(self,u,v):
        if u in self.nodos and v in self.nodos :
            for key, value in self.nodos.items():
                if key ==u:
                    value.añadir_vecino(v)
                if key == v :
                    value.añadir_vecino(u)
            return True
        else:
            return False
        
    def mostrar_Grafo(self):
        for key in sorted(list(self.nodos.keys())):
            print(key+str(self.nodos[key].vecinos))
            
    
            
g=Grafo()

a = Nodo('A')
g.añadir_nodo(a)
g.añadir_nodo(Nodo('B'))
g.añadir_vertice('A', 'B')

g.añadir_nodo(Nodo('C'))
g.añadir_nodo(Nodo('D'))
g.añadir_vertice('A', 'D')
g.añadir_vertice('D', 'C')
g.mostrar_Grafo()
#for i in range (ord('A'),ord(''))
    
    