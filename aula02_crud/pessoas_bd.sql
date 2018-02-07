DROP DATABASE pessoas_db;
CREATE DATABASE pessoas_db DEFAULT CHARACTER SET utf8;
USE pessoas_db;

CREATE TABLE pessoas(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100),
	idade INT(2) UNSIGNED,
	genero VARCHAR(10)
)ENGINE = InoDB DEFAULT CHARACTER SET utf8;

INSERT INTO pessoas (nome, idade, genero) VALUES
('Joab Torres Alencar', 24, 'Masculino'),
('Bruna Apinages', 15, 'Feminino'),
('Maria Lucia de Abreu Torres', 51, 'Feminino'),
('Jose Felicio Alencar', 64, 'Masculino'),
('Jani Clei Torres Alencar', 25, 'Feminino');

SELECT * FROM pessoas;

UPDATE pessoas SET nome='nome', idade='idade', genero='genero' WHERE id = 'id';
DELETE FROM pessoas WHERE id='id';