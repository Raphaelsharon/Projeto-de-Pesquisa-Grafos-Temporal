from class_graph import Ordenar_graph, Algoritmo_dijkstra
from plotar_graph import Plotar_Grafo
from convert_letter import Converte

# Cria o grafo
vetor = Algoritmo_dijkstra.create_graph()

# Ordena o grafo
ordenar = Ordenar_graph.ordenar_graph(vetor)

# Imprime o vetor ordenado
print("\nGrafo Ordenado:")
for item in vetor:
    print(item)

# Solicita os nós de origem e destino
start_node = input("Digite o nó de origem: ") # Nó origem
end_node = input("Digite o nó de destino: ") # Nó destino

# Converte para letra maiusculas
start_node = start_node.upper() 
end_node = end_node.upper() 

# Encontra o melhor caminho
tempo_total, melhor_caminho = Algoritmo_dijkstra.dijkstra(vetor, start_node, end_node)

# Imprime o resultado
if tempo_total == float('inf'):
    print("Não há caminho disponível entre os nós fornecidos.")
else:
    print(f"Melhor caminho do nó '{start_node}' para o nó '{end_node}' no menor tempo é: ")
    for i in range(len(melhor_caminho)):
      print(melhor_caminho[i], end=" -> ")

    print(f" tempo total: {tempo_total}")

pergunta = input('Deseja Criar o graph, digite 1: ')

if pergunta == '1':
    # Plotar Graph
    conveter_letras = Converte.converter_letras_numero(vetor)
    return_list = Converte.transform_to_list_of_lists(conveter_letras)
    creat_grafo = Plotar_Grafo.plot_graph_with_connections(return_list)
else:
    # Aguarda o usuário pressionar Enter para finalizar
    input("\nPressione Enter para finalizar...")