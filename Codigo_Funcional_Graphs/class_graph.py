import heapq
import networkx as nx
from plotar_graph import Plotar_Grafo
# Função de ordenação usando o terceiro elemento de cada sublista
class Ordenar_graph():
    def ordenar_graph(vetor):
        n = len(vetor)
        for i in range(n):
            for j in range(0, n-i-1):
                if vetor[j][2] > vetor[j+1][2]:
                    # Trocar os elementos
                    vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# Função para criar o grafo
class Create_graph():    
    def create_graph():
        graph = []
        vetor_coordenadas_u_e_v = []
        print("Digite 'done' para finalizar a construção do graph")
        print("Forma da coordenada: (i,j)")
        while True:
            try:
                u = input("De: ")
                u = u.upper()
                if u.lower() == 'done':
                    break
                v = input("Para: ")
                v = v.upper()
                start_time = int(input(f"Tempo de início da aresta ({u} -> {v}): ")) # Tempo Inicial
                end_time = int(input(f"Tempo de fim da aresta ({u} -> {v}): ")) # Tempo Final
                
                #coordenadas para plotagem do graph
                '''coordenada_u = input(f"Coordenada {u}: ")
                coordenada_v = input(f"Coordenada {v}: ")
                numeros_u = coordenada_u.replace(" ", "").split(',')
                numeros_v = coordenada_v.replace(" ", "").split(',')
                
                if (numeros_u) not in vetor_coordenadas_u_e_v:
                    vetor_coordenadas_u_e_v.append(numeros_u)
                if (numeros_v) not in vetor_coordenadas_u_e_v:
                    vetor_coordenadas_u_e_v.append(numeros_v)'''
                graph.append([u, v, start_time, end_time])
                
            except (ValueError, TypeError):
                print("Valor invalido!\nTente novamente\n")
        return graph
    def vetor_graph():
        pass
        
class Algoritmo_dijkstra(Create_graph):
    
# Função para encontrar o melhor caminho no menor tempo inicial
    def dijkstra(graph, start, end):
        # Cria um dicionário de adjacência
        adj = {}
        for edge in graph:
            u, v, start_time, end_time = edge
            if u not in adj:
                adj[u] = []
            adj[u].append((v, start_time, end_time))

        # Inicializa a fila de prioridade
        pq = [(0, start, [])]  # (tempo total, nó atual, caminho percorrido)
        visited = set()

        while pq:
            time, node, path = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]
            if node == end:
                return time, path
            for neighbor, start_time, end_time in adj.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (time + start_time, neighbor, path))
        return float('inf'), []