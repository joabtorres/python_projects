# TADS15 - JOAB TORRES ALENCAR - 2015790058
# PROJETO - ATIVIDADES BANCARIAS
# DISC. TOPICOS ESPECIAIS DE SISTEMA DE INFORMACAO
# 13/02/2018

import MySQLdb
def connection_db():
	conexao = MySQLdb.connect('localhost', 'root', '', 'tads_bancario')
	cursor = conexao.cursor()
	return cursor

#************************#
#		TELAS			 #
#************************#
def viewHome():
	print
	print 'TELA: INICIAL'
	print
	testeLogico = True
	while (testeLogico) :
		print '1 - DEPOSITO'
		print '2 - SAQUE'
		print '3 - TRANSFERENCIA'
		print '4 - SALDO'
		print '5 - SAIR'
		opcao = int(raw_input("Opcao: "))
		if((opcao>0) and (opcao<=5)):
			testeLogico = False
			if opcao == 1:
				viewDeposito()
			elif opcao == 2:
				viewSaque()
			elif opcao == 3:
				viewTransferencia()
			elif opcao == 4:
				viewSaldo()
			else:
				exit();
		else:
			print
			print 'Opcao invalida, tente novamente!'
			print
		

def viewDeposito():

	testeLogico = True
	while (testeLogico):
		list_clients_db()
		print "TELA: DEPOSITO"
		print 
		agencia = raw_input("Agencia: ")
		numero = raw_input('Numero: ')
		valor = raw_input("Valor do deposito: ")
		depositar_db(agencia, numero, valor)
		opcao = int(raw_input("Deseja depositar mais? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewHome()

def viewSaque():
	testeLogico = True
	while (testeLogico):
	
		list_clients_db()
		print "TELA: SAQUE"
		print 
		
		agencia = raw_input("Agencia: ")
		numero = raw_input('Numero: ')
		valor = raw_input("Valor do saque: ")
		
		saque_db(agencia, numero, valor)
		
		opcao = int(raw_input("Deseja Sacar mais? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewHome()
			
def viewTransferencia():

	testeLogico = True
	while (testeLogico):
		list_clients_db()
		print "TELA: TRANSFERENCIA"
		print 
		
		agencia1 = raw_input("Agencia (REMETENTE): ")
		numero1 = raw_input('Numero (REMETENTE): ')
		
		agencia2 = raw_input("Agencia (DESTINATARIO): ")
		numero2 = raw_input('Numero (DESTINATARIO): ')
		
		valor = raw_input("Valor da Transferencia: ")
		transferencia_db(agencia1, numero1, agencia2, numero2, valor)
		
		opcao = int(raw_input("Deseja transferir mais? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewHome()


def viewSaldo():
	testeLogico = True
	while (testeLogico):
	
		list_clients_db()
		print "TELA: SALDO"
		print 
		
		agencia = raw_input("Agencia: ")
		numero = raw_input('Numero: ')
		
		saldo_db(agencia, numero)
		
		opcao = int(raw_input("Deseja consulta outro saldo? \n 1 - SIM \n 0 - NAO \n \n Opcao: "))
		if opcao == 1:
			testeLogico = True
			print ('\n' * 2 )
		else:
			testeLogico = False
			viewHome()
#************************#
#		BANCO 			 #
#************************#

	
def list_clients_db():
	cursor = connection_db();
	sql="SELECT agencia, numero, titular, tipo FROM conta"
	try:
		cursor.execute(sql)
		print '-----INICIO DA LISTA DE CLIENTES-----'
		print
		for row in cursor.fetchall():
			print "AG: %s - Conta: %s - Titular: %s - Tipo: %s " % (row[0], row[1], row[2], row[3])
		print
		print '----- FIM DA LISTA DE CLIENTES -----'
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
	
def depositar_db(agencia, numero, valor):
	cursor = connection_db();
	sql = "CALL sp_deposita('"+agencia+"','"+numero+"','"+valor+"')"
	try:
		cursor.execute(sql)
		print
		for row in cursor.fetchall():
			print "%s" % (row[0])
		print
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
	
def saque_db(agencia, numero, valor):	
	cursor = connection_db();
	sql = "CALL sp_saque('"+agencia+"','"+numero+"','"+valor+"')"
	try:
		cursor.execute(sql)
		print
		for row in cursor.fetchall():
			print "%s" % (row[0])
		print
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
	
def transferencia_db(agencia, numero, agencia2, numero2, valor):
	cursor = connection_db();
	sql = "CALL sp_transferir('"+agencia+"','"+numero+"','"+agencia2+"','"+numero2+"','"+valor+"')"
	try:
		cursor.execute(sql)
		print
		for row in cursor.fetchall():
			print "%s" % (row[0])
		print
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

	

def saldo_db(agencia, numero):
	cursor = connection_db();
	sql = "CALL sp_saldo('"+agencia+"','"+numero+"')"
	saldo = None
	try:
		cursor.execute(sql)
		print
		for row in cursor.fetchall():
			if((len(row))>1):
				print "%s     %s     %s" % (row[0], row[1], row[2])
				if(saldo<=0):
					saldo = '%s' %(row[3])
			else:
				print "%s" % (row[0])
		print
		if(saldo>0):
			print '------------------------------------------------'
			print 'Saldo atual                           R$ '+saldo;
			print
			print
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
	
viewHome()