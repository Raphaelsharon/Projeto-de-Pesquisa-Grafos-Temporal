import networkx as nx
import matplotlib.pyplot as plt
class Plotar_Grafo():

    def plot_graph_with_connections(edges):

        # Cria um grafo vazio
        G = nx.Graph()
        
        # Adiciona as arestas ao grafo
        G.add_edges_from(edges)
        
        # Desenha o grafo
        pos = nx.spring_layout(G)  # Layout para melhor visualização
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_weight='bold')
        
        # Exibe o plot
        plt.show()