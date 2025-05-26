DROP DATABASE IF EXISTS db_poo;
CREATE DATABASE db_poo;
USE db_poo;

-- Tabla usuarios
CREATE TABLE usuario (
  id INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  telefono VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

INSERT INTO usuario(nombre, telefono, email)
VALUES ('Jaime', '999888777', 'jaime@abc.com');

-- Tabla empleados
CREATE TABLE empleados (
  id INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE,
  DNI INT(8) NOT NULL UNIQUE
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

INSERT INTO empleados(nombre, apellido, email, DNI)
VALUES ('Daniel', 'Montes', 'dan@abc.com', 68382828);




