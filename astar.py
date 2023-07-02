class Estacao():
    

    def __init__(self, nome, linha=None):
        
        self.nome = nome
        self.linha = linha

        self.g = 0
        self.h = 0
        self.f = 0
    def set_g(self,num):
        self.g = num
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
def astar (e_inicial,e_final):
    fronteira = [e_incial]
    visitados = []
    e_atual = None
    def compara_linha(e_x,e_y):
        
        for i in range(len(e_x)):
            for j in range(len(e_y)):
                if e_x[i] == e_y[j]:
                    
                    return e_x[i]
           
    index = 0
    while index != 3:
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
                    aux.set_g(tempo + e_atual.g + 4)
                else:
                    aux.set_g(tempo + e_atual.g)
                fronteira.append(aux)
        fronteira.sort(key=lambda x:x.g)
        
        visitados.append(e_atual)
        index+=1
        for i in visitados:
            print(f"visitados: {i.nome, i.linha}")
        for i in fronteira:
            print(f"estacao: {i.nome}, linha: {i.linha}, valor g: {i.g}")
     
    
e_incial = Estacao('E12','verde')
e_final = Estacao('E7','amarelo')
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

diretas = [
            [ 0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6,  9.1, 16.7, 27.3, 27.6, 29.8],
            [-1,  0,  8.5, 14.8, 26.6, 29.1, 26.1, 17.3,   10,  3.5, 15.5, 20.9, 19.1, 21.8],
            [-1, -1,    0,  6.3, 18.2, 20.6, 17.6, 13.6,  9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
            [-1, -1,   -1,    0,   12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
            [-1, -1,   -1,   -1,    0,    3,  2.4, 19.6, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
            [-1, -1,   -1,   -1,   -1,    0,  3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   20,   23, 27.3, 34.2, 25.7, 12.4, 15.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,    0,  8.2, 20.3, 16.1,  6.4, 22.7, 27.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 13.5, 11.2, 10.9, 21.2, 26.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 17.6, 24.2, 18.7, 21.2],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 14.2, 31.5, 35.5],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 28.8, 33.6],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,    0,  5.1],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,   -1,    0],
        ]
print(diretas*2)
#astar(e_incial,e_final)
