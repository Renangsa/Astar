class Estacao():
    

    def __init__(self, nome, linha=None):
        
        self.nome = nome
        self.linha = linha

        self.g = 0
        self.h = 0
        self.f = 0
    def set_g(self,num):
        self.g = num
    def set_h(self,num):
        self.h = num
    def set_f(self,num):
        self.f = num


def baldeacao(linha1,linha2):
    if linha1== linha2:
        return False  
    return True
#estacao, distancia em tempo
def compara_visitados(visitados, estacao, linha):
    for i in visitados:
        if i.nome == estacao and i.linha == linha:
            return False
    
    return True
def distancia(na,nf):
    return distancia_diretas[na-1][nf-1]
def att_g(aux,tempo,e_atual):
    aux.set_g(tempo + e_atual.g)

def att_h(aux,e_final):
    na = int(aux.nome.split('E')[1])
    nf = int(e_final.nome.split('E')[1])
    if na > nf:
        nf,na = na, nf
    
    d = distancia(na,nf)
    aux.set_h(d)
def att_f(aux):
    aux.set_f(aux.g+aux.h)
def compara_linha(e_x,e_y):
        
        for i in range(len(e_x)):
            for j in range(len(e_y)):
                if e_x[i] == e_y[j]:
                    
                    return e_x[i]
                
def astar (e_inicial,e_final):
    fronteira = [e_incial]
    visitados = []
    e_atual = fronteira[0]

   
           
    index = 0
    while e_atual.nome != e_final.nome and e_atual.linha != e_final.linha:
        e_atual = fronteira[0]
        
        e_num =e_atual.nome.split('E')[1]
        del fronteira[0]
        print(f"tamanho da fronteira {len(fronteira)}")
        
        print(f"Numero da estacao atual {e_num}")
        for estacao, tempo in matriz_Adjacencia[int(e_num) - 1]:
            linha = compara_linha(linhas[estacao],linhas[e_atual.nome])
            if compara_visitados(visitados,estacao,linha):
                print(f"vizinho: {estacao}")
                aux = Estacao(estacao,linha)
                if baldeacao(linha, e_atual.linha):
                    att_g(aux,tempo + 4,e_atual)
                else:
                    att_g(aux,tempo,e_atual)
                att_h(aux,e_final)
                att_f(aux)
                fronteira.append(aux)
        fronteira.sort(key=lambda x:x.f)
        
        visitados.append(e_atual)
        
        for i in visitados:
            print(f"visitados: {i.nome, i.linha}")
        for i in fronteira:
            print(f"estacao: {i.nome}, linha: {i.linha}, valor g: {i.g}, valor h: {i.h}, valor f: {i.f}")

    
e_incial = Estacao('E12','verde')
e_final = Estacao('E5','amarela')
matriz_Adjacencia = [[('E2',20)],
                     [('E3',17),('E9',20),('E10',7),('E1',20)],                                                    
                     [('E4',12.6),('E9',18.8),('E13',37.4),('E2',17)],
                     [('E5',26),('E8',30.6),('E13',25.6),('E3',12.6)],
                     [('E6',6),('E7',4.8),('E8',60),('E4',26)],
                     [('E5',6)],
                     [('E5',4.8)],
                     [('E9',19.2),('E12',12.8),('E4',30.6),('E5',60)],
                     [('E11',24.4),('E2',20),('E3',18.8)],
                     [('E10',7)],
                     [('E9',24.4)],
                     [('E8',12.8)],
                     [('E14',10.2),('E3',37.4),('E4',25.6)],
                     [('E13',10.2)]]

linhas = {"E1": ["azul"],
            "E2": ["azul", "amarela"],
            "E3": ["azul", "vermelha"],
            "E4": ["azul", "verde"],
            "E5": ["azul", "amarela"],
            "E6": ["azul"],
            "E7": ["amarela"],
            "E8": ["amarela", "verde"],
            "E9": ["amarela", "vermelha"],
            "E10": ["amarela"],
            "E11": ["vermelha"],
            "E12": ["verde"],
            "E13": ["verde", "vermelha"],
            "E14": ["verde"],}



distancia_diretas = [
            [0, 20, 37.0, 49.6, 72.8, 77.6, 71.6, 50.8, 35.2, 18.2, 33.4, 54.6, 55.2, 59.6],
            [-1, 0, 17.0, 29.6, 53.2, 58.2, 52.2, 34.6,   20,  7.0, 31.0, 41.8, 38.2, 43.6],
            [-1, -1,   0, 12.6, 36.4, 41.2, 35.2, 27.2, 18.8, 20.6, 39.0, 38.2, 24.2, 33.2], 
            [-1, -1,  -1,    0,   24, 28.8, 23.0, 24.8, 25.2, 33.4, 47.2, 37.2, 21.2, 30.8],
            [-1, -1,  -1,   -1,    0,    6,  4.8, 39.2, 46.6, 56.4, 68.4, 49.6, 29.0, 35.8],
            [-1, -1,  -1,  - 1,   -1,    0,  6.6, 44.6, 51.4, 60.6, 73.4, 55.2, 30.4, 36.4], 
            [-1, -1,  -1,   -1,   -1,   -1,    0,   40,   46, 54.6, 68.4, 51.4, 24.8, 31.2],
            [-1, -1,  -1,   -1,   -1,   -1,   -1,    0, 16.4, 40.6, 32.2, 12.8, 45.4, 55.2], 
            [-1, -1,  -1,   -1,   -1,   -1,   -1,   -1,    0, 27.0, 22.4, 21.8, 42.4, 53.2],
            [-1, -1,  -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 35.2, 48.4, 37.4, 42.4], 
            [-1, -1,  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 28.4, 63.0, 71.0], 
            [-1, -1,  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 57.6, 67.2], 
            [-1, -1,  -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,    0, 10.2], 
            [-1, -1,  -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,   -1,    0]
            ] 

astar(e_incial,e_final)
