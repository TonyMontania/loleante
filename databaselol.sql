drop database if exists lol;
create database lol;
use lol;
  create table proveedor(
    proveedorid int not null auto_increment primary key,
    nombreprov char (100),
    descripcion char (200),
    contactoprov char (200));
    
create table producto (
	productoid int not null auto_increment,
    nombreprod varchar(255),
    descripprod varchar(255),
    proveedorid int,
    primary key (productoid),
    foreign key (proveedorid) references proveedor(proveedorid));
    
    create table cliente(
    dnicliente int primary key ,
    nombre varchar (60),
    apellido varchar(60));
    
    
    create table stock(
    idstock int auto_increment primary key,
    cantidadstock smallint,
    idproducto int,
    foreign key (idproducto) references producto(productoid));
    
    create table reserva (
    idreserva int auto_increment primary key,
    clienteid int,
    productoreser int,
    foreign key (clienteid) references cliente (dnicliente),
    foreign key (productoreser) references producto (productoid));
    