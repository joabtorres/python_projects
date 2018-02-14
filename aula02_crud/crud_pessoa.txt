###############################################
#			CRUD - CREATE, READ, UPDATE, DELETE - EM PYTHON
#			JOAB TORRES ALENCAR
###############################################

import MySQLdb	

def connection_db():
	conexao = MySQLdb.connect('localhost', 'root', '', 'pessoas_db')
	cursor = conexao.cursor()
	return cursor

### TELAS
def viewInicial():
	testeLogico = True
	while (testeLogico):
		print ('\n'*2)
		print '-----------------------------------'
		print "INICIAL - CRUD DE PESSOAS"
		print '-----------------------------------'
		print '1 - CADASTRAR'
		print '2 - LISTAR'
		print '3 - ALTERAR'
		print '4 - EXCLUIR'
		print '5 - SAIR'
		print '-----------------------------------'
		print 
		opcao = int(raw_input('Opcao: '))
		if opcao == 1:
			testeLogico=False
			viewCreate()
		elif opcao==2:
			testeLogico=False
			viewRead()
		elif opcao==3:
			testeLogico=False
			viewUpdate()
		elif opcao==4:
			testeLogico=False
			viewDelete()
		elif opcao==5:
			testeLogico=False
			exit();
		else:
			print ('\n'*2)
			print ('###################################')
			print "- Opcao invalida!"
			print ('###################################')
		
	print ('\n'*2)
	

def viewCreate():
	print
	testeLogico = True;
	while(testeLogico):
		print '--- Tela para cadastro ----'
		nome = raw_input("Digite o nome: ")
		idade = raw_input("Digite a idade: ")
		genero = raw_input("Digite o genero do sexo: ")
		create_db(nome, idade, genero)
		print ('\n' *2)
		opcao = int(raw_input("Deseja cadastrar mais pessoas? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewInicial()
			
def viewRead():
	print
	print '---- Tela de Consulta ----'
	read_db()
	viewInicial()
	
def viewUpdate():
	print
	testeLogico = True
	while(testeLogico):
		print '--- Tela de Alteracao ----'
		id = raw_input("Digite o ID: ")
		nome = raw_input("Digite o nome: ")
		idade = raw_input("Digite a idade: ")
		genero = raw_input("Digite o genero do sexo: ")
		update_db(nome, idade, genero, id)
		print ('\n' *2)
		opcao = int(raw_input("Deseja alterar mais pessoas? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewInicial()
	
def viewDelete():
	print
	testeLogico = True;
	while(testeLogico):
		print '--- Tela de Exclusao ----'
		id = raw_input("Digite o ID: ")
		delete_db(id)
		print ('\n' *2)
		opcao = int(raw_input("Deseja descadastrar mais pessoas? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewInicial()

################
#	BANCO DE DADOS
################

def create_db(nome, idade, genero):
	cursor = connection_db();
	sql="INSERT INTO pessoas(nome, idade, genero) VALUES ('"+nome+"','"+idade+"','"+genero+"')"
	try:
		cursor.execute(sql)
		print "Cadastro realizado com sucesso"
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 
	cursor.close()

def read_db():
	cursor = connection_db();
	sql="SELECT * FROM pessoas"
	try:
		cursor.execute(sql)
		print
		for row in cursor.fetchall():
			print "Id: %s - Nome: %s - Idade: %s - Genero: %s " % (row[0], row[1], row[2], row[3])
		print
		print '-----------------------'
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 
	cursor.close()
	
def update_db(nome, idade, genero, id):
	cursor = connection_db();
	sql="UPDATE pessoas SET nome='"+nome+"', idade='"+idade+"', genero='"+genero+"' WHERE id='"+id+"';"
	try:
		cursor.execute(sql)
		print "Alteracao realizada com sucesso"
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 
	cursor.close()
	
def delete_db(id):
	cursor = connection_db();
	sql="DELETE FROM pessoas WHERE id='"+id+"';"
	try:
		cursor.execute(sql)
		print "Exclusao realizada com sucesso"
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 
	cursor.close()

viewInicial()