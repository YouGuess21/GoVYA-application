create database if not exists flaskdb;
use flaskdb;
create table user (
    user_id int primary key,
    password varchar(16),
    name varchar(50),
    email varchar(50)
);
create table customer (
    c_id int primary key,
    c_homeaddr varchar(255),
    c_phoneno varchar(15),
    foreign key (c_id) references user(user_id) on delete cascade
);
create table provider (
    p_id int primary key,
    p_scale varchar(50),
    p_officeaddr varchar(255),
    p_phoneno varchar(15),
    p_multiplier float,
    p_pan varchar(20),
    p_gst varchar(20),
    verified boolean,
    foreign key (p_id) references user(user_id) on delete cascade
);
create table admin (
    adm_id int primary key,
    adm_join_date date,
    foreign key (adm_id) references user(user_id) on delete cascade
);
create table requests (
    req_id int primary key,
    c_id int,
    req_weight float,
    req_size float,
    req_speed int,
    req_dist float,
    req_type varchar(50),
    start varchar(50),
    end varchar (50),
    foreign key (c_id) references customer(c_id) on delete cascade
);
create table quotes (
    quote_id int primary key,
    p_id int,
    quote_amt float,
    quote_speed int,
    req_id int,
    foreign key (p_id) references provider(p_id) on delete cascade,
    foreign key (req_id) references requests(req_id) on delete cascade
);
create table orders (
    c_id int,
    p_id int,
    order_id int,
    weight float,
    size float,
    type varchar(50),
    speed int,
    status varchar(50),
    dist float,
    bill float,
    start varchar(50),
    end varchar (50),
    primary key (c_id, p_id, order_id),
    foreign key (c_id) references customer(c_id) on delete cascade,
    foreign key (p_id) references provider(p_id) on delete cascade
);
create table employee (
    emp_id int primary key,
    emp_email varchar(50),
    emp_salary float,
    isassisting int default 0
);
create table emp_phoneno (
    emp_id int,
    emp_phoneno varchar(15),
    primary key (emp_id, emp_phoneno),
    foreign key (emp_id) references employee(emp_id) on delete cascade
);

-- inserts for user table
insert into user (user_id, name, password, email) values
(1000, 'vansh', 'password123', 'john@example.com'),
(1001, 'jane smith', 'securepass', 'jane@example.com'),
(2000, 'ashwin', 'adminpass', 'admin1@example.com'),
(2001, 'yogesh', 'adminpass', 'admin2@example.com'),
(3000, 'apm', 'providerpass', 'provider1@example.com'),
(3001, 'dtdc', 'providerpass', 'provider2@example.com');

-- inserts for customer table
insert into customer (c_id, c_homeaddr, c_phoneno) values
(1000, '123 main st', '555-1234'),
(1001, '456 oak st', '555-5678');

-- inserts for provider table
insert into provider (p_id, p_scale, p_officeaddr, p_phoneno, p_multiplier, p_pan, p_gst, verified) values
(3000, 'large', '789 elm st', '555-9876', 1.5, 'abc123', 'gst456', true),
(3001, 'small', '321 maple st', '555-4321', 1.2, 'def456', 'gst789', true);

-- inserts for admin table
insert into admin (adm_id, adm_join_date) values
(2000, '2024-01-15'),
(2001, '2024-02-20');

-- inserts for requests table
insert into requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, start, end) values
(1, 1000, 10.5, 3.2, 5, 20.5, 'large', 'delhi', 'haryana'),
(2, 1001, 8.2, 2.5, 3, 15.7, 'small', 'manipal', 'udupi');

-- inserts for quotes table
insert into quotes (quote_id, p_id, quote_amt, quote_speed, req_id) values
(1, 3000, 1500.0, 3, 2),
(2, 3001, 1200.0, 2, 2);

-- inserts for orders table
insert into orders (c_id, p_id, order_id, weight, size, type, speed, status, dist, bill, start, end) values
(1000, 3000, 1, 10.5, 3.2, 'large', 3, 'reached delhi hub', 20.5, 1500, 'delhi', 'delhi'),
(1001, 3001, 2, 8.2, 2.5, 'small', 2, 'processing', 15.7, 2000, 'goa', 'goa'),
(1001, 3000, 3, 56.3, 15, 'medium', 5, 'completed', 27.3, 2500, 'mangalore', 'mangalore');

-- inserts for employee table
insert into employee (emp_id, emp_email, emp_salary, isassisting) values
(4001, 'employee1@example.com', 50000.00, 0),
(4002, 'employee2@example.com', 60000.00, 0);

-- inserts for emp_phoneno table
insert into emp_phoneno (emp_id, emp_phoneno) values
(4001, '555-1111'),
(4001, '555-2222'),
(4002, '555-3333');

delimiter //
drop procedure if exists addrequest;
create procedure addrequest(cid int, weight float, size float, speed float, dist float, strt varchar(50), endpt varchar(50))
begin
    declare r_id int;
    select max(req_id) into r_id from requests;
    if r_id is null then
        set r_id = 1;
    else
        set r_id = r_id + 1;
    end if;
    
    if weight < 50 and dist < 15 then
        insert into requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, start, end) 
        values (r_id, cid, weight, size, speed, dist, 'small', strt, endpt);
    elseif weight < 100 and dist < 50 then
        insert into requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, start, end) 
        values (r_id, cid, weight, size, speed, dist, 'medium', strt, endpt);
    else
        insert into requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, start, end) 
        values (r_id, cid, weight, size, speed, dist, 'large', strt, endpt);
    end if;
    commit;
end//
delimiter ;

delimiter //
drop trigger if exists set_isassisting_to_zero//
create trigger set_isassisting_to_zero
after delete on user
for each row
begin
    update employee
    set isassisting = 0
    where isassisting = old.user_id;
end//
delimiter ;