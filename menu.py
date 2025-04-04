from rotulos import Rotulos
from grafoLista import Grafo

# Inicialização de Variáveis, dicionario para manter informações dos restaurantes
# a lista de adjacência apenas armazena índices e distâncias
restaurantes = {}
opcao = 0 
n = 0
m = 0 
tipo = -1
construiu = False # verifica se grafo foi criado

# loop de menu
while opcao != "j":

      print( '''-----------------------------Menu----------------------------
        [a] Ler dados do arquivo grafo.txt 
        [b] Gravar dados no arquivo grafo.txt
        [c] Inserir vertice:
        [d] Inserir aresta:
        [e] Remover vertice:
        [f] Remover aresta:
        [g] Mostrar conteudo do arquivo
        [h] Mostrar grafo
        [i] Apresentar a conexidade do grafo e o reduzido
        [j] Encerrar a aplicação
--------------------------------------------------------------
      ''')

      opcao = str(input('Selecione uma opcao: '))

      # ler dados do arquivo
      if opcao == "a":
            # abre arquivo (leitura)
            with open("grafo.txt", "r", encoding="utf-8") as arquivo:
                  i = 0 
                  sla = arquivo.readlines() # le arquivo, separando por linha

                  # percorre linha por linha
                  for linha in sla:

                        # armazena o tipo do grafo
                        if i == 0:
                              tipo = int(linha)
                        
                        # armazena a quantidade de vértices
                        elif i == 1:
                              n = int(linha)
                              construiu = True
                              grafo = Grafo(n)

                        # lê as informações de todos os restaurantes (vértices)
                        elif i >= 2 and i <= (n + 1): 
                              elementos = linha.split(',') # separa informações por ','
                              id = int(elementos[0].strip())
                              nome = str(elementos[1].strip())
                              avaliacao = elementos[2].strip()
                              preco = str(elementos[3].strip())
                              endereco = str(elementos[4].strip())

                              vertice_chave = "N" + str(i - 1) # cria uma chave para o dicionario

                              # chave : valor (vertice_chave : rotulo)
                              restaurantes[vertice_chave] = Rotulos(id, nome, avaliacao, preco, endereco)

                        # lê a quantidade de ligações entre restaurantes (arestas)
                        elif i == (n + 2):
                              m = int(linha)

                        # percorre todas as arestas
                        else:
                              elementos = linha.split(',') # separa informações por ','
                              entrada = int(elementos[0].strip())
                              saida = int(elementos[1].strip())
                              distancia = elementos[2].replace(" km", "").strip() # tira a informação "km" e retira espaços em branco ao redor
                              
                              grafo.insereA(entrada - 1, saida - 1, float(distancia)) # insere aresta no grafo
                        
                        i += 1 # atualiza contador de linha
                  print("Leitura de dados concluída.")

      # gravar dados em arquivo
      elif opcao == "b":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  with open("grafo.txt", "w", encoding="utf-8") as arquivo:

                        arquivo.write(str(tipo) + "\n")
                        arquivo.write(str(n) + "\n")

                        for nome, restaurante in restaurantes.items():
                              arquivo.write(f"{restaurante.get_id()}, {restaurante.get_nome()}, {restaurante.get_avaliacao()}, {restaurante.get_preco()}, {restaurante.get_endereco()}\n")

                        arquivo.write(str(m) + "\n")

                        grafo.gravarInfo(arquivo)
                  print("Dados gravados com sucesso.")

      # inserir vértice
      elif opcao == "c":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  # solicita informações do restaurante (vértice)
                  print("Crie um restaurante para inserir no grafo")
                  nome = input("Nome do restaurante:")
                  avaliacao = input("Avaliação do restaurante:")
                  preco = input("Índice de preço:")
                  endereco = input("Endereço do restaurante:")

                  n += 1 # incrementa número de vértices no menu
                  vertice_chave = "N" + str(n) # produz a chave pro dicionário

                  # chave : valor (vertice_chave : rotulo)
                  restaurantes[vertice_chave] = Rotulos(n, nome, avaliacao, preco, endereco)
            
                  grafo.inserirVND() # insere restaurante no grafo

                  print("Inserção de vértice concluída.")

      # inserir aresta
      elif opcao == "d":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  # solicita restaurantes da ligação e a distância
                  print("Crie uma conexão entre restaurantes para inserir no grafo")
                  entrada = input("Nome do restaurante de saída:")
                  saida = input("Nome do restaurante de chegada:")
                  distancia = float(input("Forneça a distância entre eles:"))

                  # variáveis para identificar erro
                  linha = -1
                  coluna = -1

                  # busca no dicionário os restaurante com os nomes inseridos e pega os ids deles
                  for nome, restaurante in restaurantes.items():
                        if restaurante.get_nome() == entrada.strip():
                              linha = int(restaurante.get_id() - 1)
                        if restaurante.get_nome()== saida.strip():
                              coluna = int(restaurante.get_id() - 1)

                  # se alguma variável não foi atualizada, não foi encontrado pelo menos um dos restaurantes informados
                  if (linha == -1):
                        if (coluna == -1):
                              print(f"Restaurantes {entrada} e {saida} não encontrados!")
                        else:
                              print(f"Restaurante {entrada} não encontrado!")
                  elif (coluna == -1):
                        print(f"Restaurante {saida} não encontrado!")

                  # se existir os dois restaurantes informados, adiciona aresta no grafo
                  else:
                        grafo.insereA(linha, coluna, distancia) # insere aresta no grafo
                  m += 1 # incrementa valor de arestas no menu

                  print("Inserção de aresta concluída.")

      # remover vértice
      elif opcao == "e":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  # solicita nome do restaurante a ser removido
                  restaurante_removido = input("Remova um restaurante do grafo: ").strip()
            
                  chave = ""

                  # busca o restaurante no dicionário e guarda o id e o nome
                  for nome, restaurante in restaurantes.items():
                        if restaurante.get_nome() == restaurante_removido:
                              posicao = (restaurante.get_id() - 1)
                              chave = nome
                              break
            
                  # se a variável nome não for encontrada (não existe restaurante na base de dados)
                  if chave == "":
                        print(f"Restaurante {restaurante_removido} não foi encontrado!")
            
                  # se exisitir restaurante informado, remove restaurante do grafo
                  else: 
                        n -= 1 # atualiza número de vértices no menu
                        grafo.removeVND(posicao) # remove vértice do grafo
            
                        i = 0 # indice para saber qual restaurante tem índice maior que o restaurante removido
                              # para atualizar ("puxar") os restaurantes no dicionário
                  
                        # atualiza informações dos restaurantes no dicionário
                        for nome, restaurante in restaurantes.items():
                              if i > posicao:
                                    restaurante_anterior.set_id(restaurante.get_id() - 1)
                                    restaurante_anterior.set_nome(restaurante.get_nome())
                                    restaurante_anterior.set_avaliacao(restaurante.get_avaliacao())
                                    restaurante_anterior.set_preco(restaurante.get_preco())
                                    restaurante_anterior.set_endereco(restaurante.get_endereco())
                              restaurante_anterior = restaurante
                              i += 1
                  
                        # atualiza informção do último restaurante
                        restaurante_anterior.set_id(n)
                        nova_chave = "N" + str(n)
                        restaurantes[nova_chave] = restaurante_anterior

                        # retira o restaurante com o maior índice (duplicado)
                        restaurantes.pop("N" + str(n+1))
                  print("Remoção de vértice concluída.")

      # remover aresta
      elif opcao == "f":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  # solicita restaurantes a serem removidos
                  print("Diga quais restaurantes voce quer remover a distancia:")
                  v = input("Nome do restaurante 1:")
                  w = input("Nome do restaurante 2:")
            
                  # variáveis para identificar erro
                  entrada = -1
                  saida = -1

                  # busca os id dos restaurantes no dicionário
                  for nome, restaurante in restaurantes.items():
                        if restaurante.get_nome() == v:
                              entrada = restaurante.get_id() - 1
                        if restaurante.get_nome() == w:
                              saida = restaurante.get_id() - 1
            
                  # se alguma variável não foi atualizada, não foi encontrado pelo menos um dos restaurantes informados
                  if (entrada == -1):
                        if (saida == -1):
                              print(f"Restaurantes {entrada} e {saida} não encontrados!")
                        else:
                              print(f"Restaurante {entrada} não encontrado!")
                  elif (saida == -1):
                        print(f"Restaurante {saida} não encontrado!")

                  # se existir os dois restaurantes informados, remove aresta no grafo
                  else:
                        grafo.removeA(entrada,saida) # remove a aresta do grafo
                        m -= 1 # atualiza valor de arestas no menu

                  print("Remoção de aresta concluída.")

      # mostrar conteúdo do arquivo
      elif opcao == "g":
            print("---Conteúdo do arquivo---")
            # abre o arquivo (leitura)
            with open("grafo.txt", "r", encoding="utf-8") as arquivo:
                  conteudo = arquivo.read() # lê o arquivo completo

            print(conteudo) # mostra todo o conteúdo

      # mostrar grafo
      elif opcao == "h":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  grafo.show()

      # apresentar conexidade
      elif opcao == "i":
            if construiu == False:
                  print("Grafo não foi construido(leia os dados do arquivo)")
            else:
                  # verifica se o grafo é conexo pelo percurso em profundidade
                  ehConexo = grafo.percursoProfundidade(1)
                  if (ehConexo == True):
                        print("O grafo é conexo.")
                  else:
                        print("O grafo é não conexo")

      # sair da aplicação
      elif opcao == "j":
            print("Programa Encerrado.")
            break   

      # opção inválida
      else:
            print("Opcao invilida. Tente Novamente!")






