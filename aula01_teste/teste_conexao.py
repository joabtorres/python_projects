import MySQLdb

#conexao
conexao = MySQLdb.connect("localhost", "root", "", "escola")
cursor =  conexao.cursor();
	
#tela inicial


def home():
	print "------ ESCOLA X ------"
	print "1 - Cadastrar Aluno"
	print "2 - Pesquisar Aluno"
	print "3 - Alterar Aluno"
	print "4 - Excluir Aluno"
	print "5 - Sair"
	print "---------------------"
	valor = raw_input("Opcao: ")
	print
	
	if valor == '1':
		cadastrar()
	elif valor == '2':
		pesquisar()
	elif valor == '3':
		alterar()
	elif valor == '4':
		excluir()
	elif valor == '5':
		print 
		print "Programa encerrado!"
		print 
	else:
		print
		print "opcao invalida!"
		print
		
def cadastrar():
	testeLogico = None
	while testeLogico <> '0' :
		matricula = raw_input("Digite a Matricula:")
		nome = raw_input("Digite o Nome: ")
		idade = raw_input("Digite a idade:")
		rg = raw_input("Digite o RG:")
		gravarPessoa(cursor, matricula, nome, idade, rg)
		testeLogico = raw_input("#Digite '1' para cadastrar mais alunos ou '0' para sair: ")
		print "--------------"	
		print ("\n" * 5) 
	home()

def pesquisar():
	buscarPessoas(cursor)
	print ("\n" * 2)
	home()
	
def alterar():
	print '------ALTERACAO DE ALUNO------'
	matricula = raw_input("Digite a Matricula:")
	nome = raw_input("Digite o Nome: ")
	idade = raw_input("Digite a idade:")
	rg = raw_input("Digite o RG:")
	alterarPessoa(cursor, matricula, nome, idade, rg)
	print ("\n" * 2) 
	print "-------------------"
		
def excluir():
	matricula = raw_input("Digite o numero de matricula: ")
	deletaPessoa(cursor, matricula)
	print ("\n" * 2) 
	home()
	

		
#############################################
###           BANCO DE DADOS			  ###
#############################################

def gravarPessoa(cursor, matricula, nome, idade, RG):
	sql="insert into alunos values( " + matricula + ",'" + nome + "'," + idade + ", " + RG + " ) "
	try:
		cursor.execute(sql) #metodo que recebe e executa a consulta
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
def buscarPessoas(cursor):
	sql = "SELECT * FROM alunos"
	try:
		cursor.execute(sql)
		numrows = int(cursor.rowcount)
		for row in cursor.fetchall():
			print "Matricula: ",row[0],', Nome: ',row[1],", Idade: ",row[2],", RG: ",row[3] 
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 
		
def alterarPessoa(cursor, matricula, nome, idade, rg):
	sql = "UPDATE alunos SET nome="+nome+", idade="+idade+", rg="+rg+" WHERE matricula="+matricula
	try:
		cursor.execute(sql);
		print "Alteração realizada com sucesso"
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print
		print "-------ERRO--------"
		print "Dados incorretos na Sintaxe:\n" + sql
		print "Codigo do Erro no BD:"
		print e
		print "--------------------" 

def deletaPessoa(cursor, matricula):
	sql = "DELETE FROM alunos WHERE matricula="+matricula
	try:
		cursor.execute(sql);
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
		
home()