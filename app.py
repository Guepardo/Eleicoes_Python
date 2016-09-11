import io

candidatos = {}

#siglas = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','RJ','RN','RS','RO','RR','SC','SP','SE','TO']; 	
siglas = ['GO']; 	

def add_bens(key, value):
	if not key in candidatos: 
		candidatos[key]['bens']   = float(value)
	else:
		candidatos[key]['bens']  += float(value)
	

def create_row(codigo, candidato): 
	candidatos[codigo] = candidato


#primeira parte
for sigla in siglas: 
	arq = io.open('consulta_cand_2016/consulta_cand_2016_'+sigla+'.txt', 'r')
	texto = arq.readlines()

	# coluna 5 estado; 
	# coluna 7 cidade;
	# coluna 9 cargo; 
	# coluna 10 nome; 
	# coluna 11 código;
	# coluna 18 partido;
	# coluna 25 ocupacao; 
	# coluna 30 sexo; 
	# coluna 32 educacao; 
	# coluna 36 raca; 
	print('running..'+sigla+'\n')

	for linha in texto:
		temp = linha.split(';')
		# limpando sujeira
		temp = [ x.replace('"', '') for x in temp ]
		candidato = {
			'codigo'  : temp[11], 
			'estado'  : temp[5], 
			'cidade'  : temp[7], 
			'cargo'   : temp[9], 
			'nome'    : temp[10], 
			'ocupacao': temp[25],
			'partido' : temp[18], 
			'sexo'    : temp[30], 
			'educacao': temp[32], 
			'raca'    : temp[36], 
			'bens'    : 0
		}
		create_row(candidato['codigo'], candidato); 
	
	arq.close()

# segunda etapa
for sigla in siglas:
	arq = io.open('bem_candidato_2016/bem_candidato_2016_'+sigla+'.txt', 'r')
	texto = arq.readlines()
	
	# coluna 9 é o valor do bem; 
	# coluna 5 é o código do candidato;
	# coluna 5 é a sigla do estado; 
	for linha in texto:
		temp = linha.split(';')
		
		# limpando sujeira que atrapalha no parse float
		temp = [ x.replace('"', '') for x in temp ]

		codigo_candidato = temp[5]
		valor_bem        = temp[9]

		add_bens(codigo_candidato, valor_bem)

	print('running..'+sigla+'\n')

	arq.close()


milionarios = [ candidatos[x] for x in candidatos if candidatos[x]['bens'] >= 1000000 ]

arq = open('output/milionarios.txt','w+')
for m in milionarios: 
	row  = m['codigo']+';'+m['estado']+';'+m['cidade']+';'+m['cargo']+';'+m['nome']+';'+m['ocupacao']+';'+m['partido']+';'+m['sexo']+';'+m['educacao']+';'+m['raca']+';'+str(int(m['bens']))+'\n'
	arq.write(row)

arq.close()


arq = open('output/todos.txt','w+')
for codigo in candidatos : 
	row  = candidatos[codigo]['codigo']+';'+candidatos[codigo]['estado']+';'+candidatos[codigo]['cidade']+';'+candidatos[codigo]['cargo']+';'+candidatos[codigo]['nome']+';'+candidatos[codigo]['ocupacao']+';'+candidatos[codigo]['partido']+';'+candidatos[codigo]['sexo']+';'+candidatos[codigo]['educacao']+';'+candidatos[codigo]['raca']+';'+str(int(candidatos[codigo]['bens']))+'\n'
	arq.write(row)

arq.close()
# print('chave valor')
# for key in candidatos: 
# 	print('código: '+ key +' = '+  str(candidatos[key])+'\n')

# print('total de candidatos processadors ')
# print(len(candidatos))

