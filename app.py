candidatos = {}

# siglas = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','RJ','RN','RS','RO','RR','SC','SP','SE','TO']; 	
siglas = ['AC','AL','AP','AM','BA','CE','ES','GO']

def add_bens(key, value):
	if not key in candidatos: 
		candidatos[key]['bens']   = float(value)
	else:
		candidatos[key]['bens']  += float(value)
	

def create_row(codigo, candidato): 
	candidatos[codigo] = candidato


#primeira parte
for sigla in siglas: 
	arq = open('consulta_cand_2016/consulta_cand_2016_'+sigla+'.txt', 'r')
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

	for linha in texto:
		temp = linha.split(';')

		# limpando sujeira
		temp = [ x.replace('"', '') for x in temp ]
		
		candidato = {
			'estado'  : temp[5], 
			'cidade'  : temp[7], 
			'cargo'   : temp[9], 
			'nome'    : temp[10], 
			'codigo'  : temp[11], 
			'ocupacao': temp[25],
			'partido' : temp[18], 
			'sexo'    : temp[30], 
			'educacao': temp[32], 
			'raca'    : temp[36], 
			'bens'    : 0
		}

		create_row(candidato['codigo'], candidato); 

		print('running..\n')
	

# segunda etapa
for sigla in siglas:
	arq = open('bem_candidato_2016/bem_candidato_2016_'+sigla+'.txt', 'r')
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

		print('running..\n')

	arq.close()


milionarios = [ candidatos[x] for x in candidatos if candidatos[x]['bens'] >= 1000000 ]

arq = open('output/milionarios.txt','w+')
for milionario in milionarios: 
	arq.write(str(milionario)+'\n')

arq.close()


arq = open('output/todos.txt','w+')
for codigo in candidatos : 
	arq.write(str(candidatos[codigo])+'\n')

arq.close()
# print('chave valor')
# for key in candidatos: 
# 	print('código: '+ key +' = '+  str(candidatos[key])+'\n')

# print('total de candidatos processadors ')
# print(len(candidatos))

