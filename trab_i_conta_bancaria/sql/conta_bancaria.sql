DROP DATABASE tads_bancario;

CREATE DATABASE tads_bancario DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

USE tads_bancario;

CREATE TABLE conta(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	tipo VARCHAR (20) NOT NULL,
	agencia VARCHAR (10) NOT NULL,
	numero VARCHAR (20) NOT NULL UNIQUE,
	titular VARCHAR (100) NOT NULL,
	saldo DOUBLE UNSIGNED DEFAULT '0.0'
)ENGINE=InoDB DEFAULT CHARSET = utf8;

CREATE TABLE extrato(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_conta INT NOT NULL,
	tipo VARCHAR(15),
	valor DOUBLE,
	data_realizada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT Fk_id_conta FOREIGN KEY (id_conta) REFERENCES conta(id)
)ENGINE=InoDB DEFAULT CHARSET = utf8;


DELIMITER //
CREATE TRIGGER tg_nova_conta
AFTER INSERT ON conta
FOR EACH ROW 
BEGIN
	DECLARE id_temp INT DEFAULT 0;
	SELECT id INTO id_temp FROM conta WHERE agencia=NEW.agencia AND numero=NEW.numero;
	IF ((NEW.saldo >0) && (id_temp>0)) THEN
		INSERT INTO extrato (id_conta, tipo, valor) VALUES (NEW.id, 'ATIVACAO', NEW.saldo);
	END IF;
END;
//

DELIMITER //
CREATE TRIGGER tg_remove_conta
BEFORE DELETE ON conta
FOR EACH ROW
BEGIN
	DELETE FROM extrato WHERE extrato.id_conta=OLD.id;
END;
//

DELIMITER //
CREATE TRIGGER tg_extrato
AFTER INSERT ON extrato
FOR EACH ROW
BEGIN
	IF (NEW.tipo = 'DEPOSITO') THEN
		UPDATE conta SET saldo = saldo+new.valor WHERE id=NEW.id_conta;
	ELSE 
		IF((NEW.tipo = 'SAQUE') || (NEW.tipo = 'TRANSFERENCIA')) THEN
			UPDATE conta SET saldo = saldo-new.valor WHERE id=NEW.id_conta;
		END IF;
	END IF;
END;
//


DELIMITER //
CREATE PROCEDURE sp_deposita(IN sp_agencia VARCHAR(20), IN sp_numero VARCHAR(20), IN sp_valor DOUBLE)
BEGIN
	DECLARE x INT DEFAULT 0;
	IF ((sp_valor > 0) && (sp_valor != '')) THEN
		SELECT id INTO x FROM conta WHERE agencia = sp_agencia AND numero = sp_numero;
		IF(x>0) THEN
			INSERT INTO extrato (id_conta, tipo, valor) VALUES (x, 'DEPOSITO', sp_valor);
			SELECT 'DEPOSITO REALIZADO COM SUCESSO !' AS msg;
		ELSE
			SELECT 'Nenhuma conta encontrada!' AS msg;
		END IF;
	ELSE
		SELECT 'Valor informádo é invalido, digite corretamente!' AS msg;
	END IF;
END;
//

DELIMITER //
CREATE PROCEDURE sp_saque(IN sp_agencia VARCHAR(20), IN sp_numero VARCHAR(20), IN sp_valor DOUBLE)
BEGIN
	DECLARE id_temp INT DEFAULT 0;
	IF(sp_valor > 0 ) THEN
		SELECT id INTO id_temp FROM conta WHERE numero=sp_numero AND agencia=sp_agencia;
		IF(id_temp>0) THEN
			IF(SELECT COUNT(*) FROM conta WHERE id=id_temp AND saldo >= sp_valor) THEN
				INSERT INTO extrato (id_conta, tipo, valor) VALUES (id_temp, 'SAQUE', sp_valor);
				SELECT 'Saque realizado com sucesso!' AS msg;
			else
				SELECT 'Saldo insuficiente' AS msg;
			END IF;
		ELSE
			SELECT 'Conta não encontrada!' AS msg;
		END IF;
	ELSE
		SELECT 'Valor inválido!' AS msg;
	END IF;
END;
//

DELIMITER //
CREATE PROCEDURE sp_transferir (IN agencia_remetente VARCHAR(20), IN numero_remetente VARCHAR(20), IN agencia_destinatario VARCHAR(20), IN numero_destinatario VARCHAR(20), IN sp_valor DOUBLE)
BEGIN
	DECLARE cod_remetende INT DEFAULT 0;
	DECLARE cod_destinatario INT DEFAULT 0;
	IF(sp_valor > 0 ) THEN
		SELECT id INTO cod_remetende FROM conta WHERE numero=numero_remetente AND agencia=agencia_remetente;
		SELECT id INTO cod_destinatario FROM conta WHERE numero=numero_destinatario AND agencia=agencia_destinatario;
		IF((cod_destinatario>0) && (cod_remetende>0)) THEN
			IF(SELECT COUNT(*) FROM conta WHERE id=cod_remetende AND saldo >= sp_valor) THEN
				INSERT INTO extrato (id_conta, tipo, valor) VALUES (cod_remetende, 'TRANSFERENCIA', sp_valor);
				INSERT INTO extrato (id_conta, tipo, valor) VALUES (cod_destinatario, 'DEPOSITO', sp_valor);
				SELECT 'Transferencia realizada com sucesso!' AS msg;
			else
				SELECT 'Saldo insuficiente' AS msg;
			END IF;
		ELSE
			SELECT 'Conta do remetente e/ou destinatário  não encontrada!' AS msg;
		END IF;
	ELSE
		SELECT 'Valor inválido!' AS msg;
	END IF;
END;
//

DELIMITER //
CREATE PROCEDURE sp_saldo(IN sp_agencia VARCHAR(20), IN sp_numero VARCHAR(20))
BEGIN
	DECLARE id_temp INT DEFAULT 0;
	DECLARE saldo_temp DOUBLE DEFAULT 0;
	SELECT id, saldo INTO id_temp, saldo_temp FROM conta WHERE numero = sp_numero AND agencia = sp_agencia;
	IF(id_temp >0) THEN
		if(saldo_temp > 0) THEN
			SELECT data_realizada, tipo, valor, saldo_temp as saldo FROM extrato WHERE id_conta = id_temp;
		ELSE 
			SELECT 'Seu saldo é de R$ 0,00' AS msg;
		END IF;
	ELSE
		SELECT 'Conta não encontrada!' AS msg;
	END IF;
END;
//

INSERT INTO conta VALUES ('1', 'Conta Poupança', '0012', '20120024', 'Pedro Arthur Alves', 0);//
INSERT INTO conta VALUES ('2', 'Conta Poupança', '0012', '20180023', 'Cristiana Abreu', 100.0);//
INSERT INTO conta VALUES ('3', 'Conta Corrente', '0015', '20180021', 'Enoque Pedrosa', 5.0);//
INSERT INTO conta VALUES ('4', 'Conta Corrente', '0077', '20150024', 'Ronilda Pereira', 1.0);//
