/*
Created		20/11/2017
Modified		20/11/2017
Project		
Model			
Company		
Author		
Version		
Database		PostgreSQL 8.1 
*/


/* Create Domains */


/* Create Tables */


Create table "ALUMNO"
(
	"DNI_alumno" Char(20) NOT NULL,
	"Nombre" Char(20),
	"Apellidos" Char(20),
	"Titulacion" Char(30),
	"Curso" Integer,
	"Correo_electronico" Char(30),
	"Expediente" Integer,
	"Creditos_Obligatorios" Integer,
	"Creditos_Transversales" Integer,
	"Creditos_Optativos" Integer,
 primary key ("DNI_alumno")
) Without Oids;


Create table "PAGO"
(
	"DNI_alumno" Char(20) NOT NULL,
	"Plazo_de_Pago" Integer,
	"Reserva_Plaza" Integer,
	"Importe" Integer,
	"Pagado" Char(20),
 primary key ("DNI_alumno")
) Without Oids;


Create table "CENTRO"
(
	"Edificio" Char(20) NOT NULL,
	"Titulacion" Char(30),
 primary key ("Edificio")
) Without Oids;


Create table "ASIGNATURA"
(
	"Codigo_asignatura" Integer NOT NULL,
	"Nombre" Char(20),
	"Titulacion" Char(30),
	"Tipo" Char(20),
	"Nota" Real,
	"Codigo_departamento" Integer NOT NULL,
	"Edificio" Char(20) NOT NULL,
 primary key ("Codigo_asignatura","Codigo_departamento","Edificio")
) Without Oids;


Create table "DEPARTAMENTO"
(
	"Codigo_departamento" Integer NOT NULL,
	"Nombre" Char(20),
	"Edificio" Char(20) NOT NULL,
 primary key ("Codigo_departamento","Edificio")
) Without Oids;


Create table "PROFESOR"
(
	"DNI_profesor" Char(20) NOT NULL,
	"Nombre" Char(20),
	"Apellidos" Char(30),
 primary key ("DNI_profesor")
) Without Oids;


Create table "NOMINAS"
(
	"DNI_profesor" Char(20) NOT NULL,
	"Categoria" Char(20),
	"Antiguedad" Integer,
	"Tramos_Docentes" Char(20),
	"Tramos_investigacion" Char(20),
	"Nomina" Char(20),
 primary key ("DNI_profesor")
) Without Oids;


Create table "ENSE_A"
(
	"Codigo_asignatura" Integer NOT NULL,
	"DNI_profesor" Char(20) NOT NULL,
	"Codigo_departamento" Integer NOT NULL,
	"Edificio" Char(20) NOT NULL,
 primary key ("Codigo_asignatura","DNI_profesor","Codigo_departamento","Edificio")
) Without Oids;


Create table "Entity10"
(
	"Codigo_asignatura" Integer NOT NULL,
	"Codigo_departamento" Integer NOT NULL,
	"DNI_alumno" Char(20) NOT NULL,
	"Edificio" Char(20) NOT NULL,
 primary key ("Codigo_asignatura","Codigo_departamento","DNI_alumno","Edificio")
) Without Oids;


/* Create Tab 'Others' for Selected Tables */


/* Create Alternate Keys */


/* Create Indexes */


/* Create Foreign Keys */

Alter table "PAGO" add  foreign key ("DNI_alumno") references "ALUMNO" ("DNI_alumno") on update restrict on delete restrict;

Alter table "Entity10" add  foreign key ("DNI_alumno") references "ALUMNO" ("DNI_alumno") on update restrict on delete restrict;

Alter table "DEPARTAMENTO" add  foreign key ("Edificio") references "CENTRO" ("Edificio") on update restrict on delete restrict;

Alter table "ENSE_A" add  foreign key ("Codigo_asignatura","Codigo_departamento","Edificio") references "ASIGNATURA" ("Codigo_asignatura","Codigo_departamento","Edificio") on update restrict on delete restrict;

Alter table "Entity10" add  foreign key ("Codigo_asignatura","Codigo_departamento","Edificio") references "ASIGNATURA" ("Codigo_asignatura","Codigo_departamento","Edificio") on update restrict on delete restrict;

Alter table "ASIGNATURA" add  foreign key ("Codigo_departamento","Edificio") references "DEPARTAMENTO" ("Codigo_departamento","Edificio") on update restrict on delete restrict;

Alter table "NOMINAS" add  foreign key ("DNI_profesor") references "PROFESOR" ("DNI_profesor") on update restrict on delete restrict;

Alter table "ENSE_A" add  foreign key ("DNI_profesor") references "PROFESOR" ("DNI_profesor") on update restrict on delete restrict;


/* Create Procedures */


/* Create Views */


/* Create Referential Integrity Triggers */


/* Create User-Defined Triggers */


/* Create Roles */


/* Create Role Permissions */
/* Role permissions on tables */

/* Role permissions on views */

/* Role permissions on procedures */


