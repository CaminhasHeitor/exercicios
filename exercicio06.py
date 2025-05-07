def cadastrar_filmes(nome, descricao, classificacao, categoria_01, categoria_02, categoria_03):

   filmes = []

   filme = {
      "nome": nome,
      "descricao": descricao,
      "classificacao": classificacao,
      "categoria": [categoria_01, categoria_02, categoria_03]
   }
   filmes.append(filme)
   return(filmes)
    
print(cadastrar_filmes("ate o ultimo homem", "guerra", 16, "ficção historica", "drama", "documentario"))


