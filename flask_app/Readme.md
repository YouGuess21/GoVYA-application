To run this locally, make sure you are in Backend directory and have the required packages installed and then

```flask run```

Change the password to your sql password in line 6 of app.py

And run the following queries in MySQL command Line
```
create database sql_college;
use sql_college;
CREATE TABLE USER (
    user_ID INT PRIMARY KEY,
    password VARCHAR(16),
    name VARCHAR(50),
    email VARCHAR(50)
);
CREATE TABLE CUSTOMER (
    c_ID INT PRIMARY KEY,
    c_homeaddr VARCHAR(255),
    c_phoneNo VARCHAR(15),
    FOREIGN KEY (c_ID) REFERENCES USER(user_ID) on DELETE CASCADE
);
CREATE TABLE PROVIDER (
    p_ID INT PRIMARY KEY,
    p_scale VARCHAR(50),
    p_officeaddr VARCHAR(255),
    p_phoneNo VARCHAR(15),
    p_multiplier FLOAT,
    p_PAN VARCHAR(20),
    p_GST VARCHAR(20),
    verified boolean,
    FOREIGN KEY (p_ID) REFERENCES USER(user_ID) on DELETE CASCADE
);
CREATE TABLE ADMIN (
    adm_ID INT PRIMARY KEY,
    adm_join_date DATE,
    FOREIGN KEY (adm_ID) REFERENCES USER(user_ID) on DELETE CASCADE
);
CREATE TABLE REQUESTS (
    req_ID INT PRIMARY KEY,
    c_ID INT,
    req_weight FLOAT,
    req_size FLOAT,
    req_speed INT,
    req_dist FLOAT,
    req_type VARCHAR(50),
    start varchar(50),
    end varchar (50),
    FOREIGN KEY (c_ID) REFERENCES CUSTOMER(c_ID) on DELETE CASCADE
);
CREATE TABLE QUOTES (
    quote_ID INT PRIMARY KEY,
    p_ID INT,
    quote_amt FLOAT,
    quote_speed INT,
    req_id INT,
    FOREIGN KEY (p_ID) REFERENCES PROVIDER(p_ID) on DELETE CASCADE,
    FOREIGN KEY (req_ID) REFERENCES requests(req_ID) on DELETE CASCADE
);
CREATE TABLE ORDERS (
    c_ID INT,
    p_ID INT,
    order_ID INT,
    weight FLOAT,
    size FLOAT,
    type VARCHAR(50),
    speed INT,
    status VARCHAR(50),
    dist FLOAT,
    bill float,
    start varchar(50),
    end varchar (50),
    PRIMARY KEY (c_ID, p_ID, order_ID),
    FOREIGN KEY (c_ID) REFERENCES CUSTOMER(c_ID) on DELETE CASCADE,
    FOREIGN KEY (p_ID) REFERENCES PROVIDER(p_ID) on DELETE CASCADE
);
CREATE TABLE EMPLOYEE (
    emp_ID INT PRIMARY KEY,
    emp_email VARCHAR(50),
    emp_salary FLOAT,
    isAssisting INT DEFAULT 0
);
CREATE TABLE EMP_PHONENO (
    emp_ID INT,
    emp_phoneNo VARCHAR(15),
    PRIMARY KEY (emp_ID, emp_phoneNo),
    FOREIGN KEY (emp_ID) REFERENCES EMPLOYEE(emp_ID) on DELETE CASCADE
);
-- Inserts for USER table
INSERT INTO USER (user_ID, name, password, email) VALUES
(1000, 'Vansh', 'password123', 'john@example.com'),
(1001, 'Jane Smith', 'securepass', 'jane@example.com'),
(2000, 'Ashwin', 'adminpass', 'admin1@example.com'),
(2001, 'Yogesh', 'adminpass', 'admin2@example.com'),
(3000, 'APM', 'providerpass', 'provider1@example.com'),
(3001, 'DTDC', 'providerpass', 'provider2@example.com');

-- Inserts for CUSTOMER table
INSERT INTO CUSTOMER (c_ID, c_homeaddr, c_phoneNo) VALUES
(1000, '123 Main St', '555-1234'),
(1001, '456 Oak St', '555-5678');

-- Inserts for PROVIDER table
INSERT INTO PROVIDER (p_ID, p_scale, p_officeaddr, p_phoneNo, p_multiplier, p_PAN, p_GST,verified) VALUES
(3000, 'Large', '789 Elm St', '555-9876', 1.5, 'ABC123', 'GST456',True),
(3001, 'Small', '321 Maple St', '555-4321', 1.2, 'DEF456', 'GST789',True);

-- Inserts for ADMIN table
INSERT INTO ADMIN (adm_ID, adm_join_date) VALUES
(2000, '2024-01-15'),
(2001, '2024-02-20');

-- Inserts for REQUESTS table
INSERT INTO REQUESTS (req_ID, c_ID, req_weight, req_size, req_speed, req_dist, req_type,start,end) VALUES
(1, 1000, 10.5, 3.2, 5, 20.5, 'Large','delhi','haryana'),
(2, 1001, 8.2, 2.5, 3, 15.7, 'Small','Manipal','Udupi');

-- Inserts for QUOTES table
INSERT INTO QUOTES (quote_ID, p_ID, quote_amt, quote_speed,req_id) VALUES
(1, 3000, 1500.0, 3,2),
(2, 3001, 1200.0, 2,2);

-- Inserts for ORDERS table
INSERT INTO ORDERS (c_ID, p_ID, order_ID, weight, size, type, speed, status, dist,bill,start,end) VALUES
(1000, 3000, 1, 10.5, 3.2, 'Large', 3, 'Reached Delhi HUB', 20.5,1500,'delhi','delhi'),
(1001, 3001, 2, 8.2, 2.5, 'Small', 2, 'Processing', 15.7,2000,'Goa','Goa')
(1001, 3000, 3, 56.3, 15, 'Medium', 5, 'Completed', 27.3,2500,'Mangalore','Mangalore');

-- Inserts for EMPLOYEE table
INSERT INTO EMPLOYEE (emp_ID, emp_email, emp_salary,isAssisting) VALUES
(4001, 'employee1@example.com', 50000.00,0),
(4002, 'employee2@example.com', 60000.00,0);

-- Inserts for EMP_PHONENO table
INSERT INTO EMP_PHONENO (emp_ID, emp_phoneNo) VALUES
(4001, '555-1111'),
(4001, '555-2222'),
(4002, '555-3333');


DELIMITER //
DROP PROCEDURE IF EXISTS addrequest;
CREATE PROCEDURE addrequest(cid INT, weight FLOAT, size FLOAT, speed FLOAT, dist FLOAT, strt VARCHAR(50), endpt VARCHAR(50))
BEGIN
    DECLARE r_id INT;
    SELECT MAX(req_id) INTO r_id FROM requests;
    IF r_id IS NULL THEN
        SET r_id = 1;
    ELSE
        SET r_id = r_id + 1;
    END IF;
    
    IF weight < 50 AND dist < 15 THEN
        INSERT INTO requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, `start`, `end`) 
        VALUES (r_id, cid, weight, size, speed, dist, 'Small', strt, endpt);
    ELSEIF weight < 100 AND dist < 50 THEN
        INSERT INTO requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, `start`, `end`) 
        VALUES (r_id, cid, weight, size, speed, dist, 'Medium', strt, endpt);
    ELSE
        INSERT INTO requests (req_id, c_id, req_weight, req_size, req_speed, req_dist, req_type, `start`, `end`) 
        VALUES (r_id, cid, weight, size, speed, dist, 'Large', strt, endpt);
    END IF;
    COMMIT;
END//
DELIMITER ;

DELIMITER //
DROP TRIGGER IF EXISTS set_isAssisting_to_zero//
CREATE TRIGGER set_isAssisting_to_zero
AFTER DELETE ON user
FOR EACH ROW
BEGIN
    UPDATE EMPLOYEE
    SET isAssisting = 0
    WHERE isAssisting = OLD.user_ID;
END//
DELIMITER ;

```
