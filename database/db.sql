drop database db_poo;

create database db_poo;

use db_poo;

CREATE TABLE usuario (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  telefono varchar(50) NOT NULL,
  email varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into usuario(nombre,telefono,email)
values ('Jaime','999888777','jaime@abc.com');




"""
Base de datos para empleados
"""

create database db_poo;

use db_poo;

CREATE TABLE empleados (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  apellido varchar(50) NOT NULL,
  email varchar(50) NOT NULL UNIQUE,
  DNI int(8) NOT NULL UNIQUE
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into empleados(nombre,apellido,email,DNI)
values ('Daniel','Montes','dan@abc.com',68382828);




