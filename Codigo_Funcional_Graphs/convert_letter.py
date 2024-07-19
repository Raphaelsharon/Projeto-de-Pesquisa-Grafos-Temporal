# Transformando as letras em minúsculas
class Converte():
    # Converte letras em seus respectios numeros segundo o alfabeto
    def converter_letras_numero(h):
        
        for sublist in h:
            for i in range(len(sublist)):
                if isinstance(sublist[i], str):
                    sublist[i] = sublist[i].lower()
                    
        u = []
        vetor = []

        for i in range(len(h)):
            for c in range(len(h[i])):
                if isinstance(h[i][c], str) and len(h[i][c]) > 0:
                    u.append(ord(h[i][c]) - 96)

        vetor.append(u)
        return u

    def transform_to_list_of_lists(input_list):
        # Inicializa a lista de listas vazia
        list_of_lists = []

        # Loop para agrupar os itens de dois em dois
        for i in range(0, len(input_list), 2):
            # Verifica se há pelo menos dois itens restantes
            if i + 1 < len(input_list):
                # Adiciona uma lista com dois itens à lista de listas
                list_of_lists.append([input_list[i], input_list[i + 1]])
            else:
                # Adiciona o último item como uma lista separada caso não haja um par
                list_of_lists.append([input_list[i]])
        #print(list_of_lists)
        return list_of_lists