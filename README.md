疫苗管理系统

creat database 
sql 
create table vaccine_info(
    vaccine_num    char(50) not null primary key,
    vaccine_name   char(50) not null,
    company_name   char(50) not null,
    company_num    char(50) not null,
size           char(50) null,
    buy_price      char(50) not null,
    pre_sale_price char(20) not null,
    limit_up       char(50) not null,
    limit_down     char(50) not null
);

create table user_info(
id int auto_increment primary key,
    user_name char(50) NOT NULL ,
    user_code char(50) NOT NULL
);

create table if not exists vaccine_distr_info (
    vaccine_distr_num char(50) primary key,
date date not null ,
    vaccine_num char(50) not null ,
    vaccine_name char(50) not null ,
    company_num char(50) not null ,
    operator_num char(50) not null ,
num int not null
);

create table if not exists vaccine_maintenance_info (
    vaccine_maintenance_num char(50) primary key ,
    vaccine_maintenance_name char(50) not null ,
    admin_num char(50) not null ,
    admin_name char(50) not null ,
    maintenance_time date,
    cold_storage_temp char(20) not null ,
    freezer_temp char(20) not null ,
    equipment_operation char(50) not null ,
    alter_info char(50) not null
);

create table if not exists vaccination_person_info(
id int auto_increment primary key,
name char(20) not null ,
    sexy char(10) not null ,
    age char(10) not null ,
    ID_num char(50) not null ,
    address char(70) not null ,
    allergy char(10) not null ,
date date
);

