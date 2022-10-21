create table if not exists person(
	id integer not null primary key autoincrement,
	nombre text not null,
	apellido text,
	fecha_nacimiento datetime not null default current_timestamp,
	telefono text unique,
	estatus integer not null default 1
);

-- Personas de prueba
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Margarita', 'La Torre', '1970-08-12', '0000-0000');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Alma', 'Valdes', '2000-12-12', '1111-1111');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Salvador', 'Luengo', '1978-07-14', '2222-2222');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Alexia', 'Requena', '1982-12-20', '3333-3333');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Jaume', 'Roca', '1962-02-18', '4444-4444');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Glória', 'Zhu', '1995-06-08', '5555-5555');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Andrei', 'García', '1962-06-12', '6666-6666');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Bernat', 'Portillo', '1969-12-30', '7777-7777');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Elvira', 'Cervantes', '1969-11-12', '8888-8888');
insert into person(nombre, apellido, fecha_nacimiento, telefono) VALUES('Michelle', 'Chavez', '1988-08-24', '9999-9999');
