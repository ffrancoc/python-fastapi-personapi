create table if not exists person(
	id integer not null primary key autoincrement,
	nombre text not null,
	apellido text,
	fecha_nacimiento datetime not null default current_timestamp,
	telefono text unique,
	estatus integer not null default 1
);