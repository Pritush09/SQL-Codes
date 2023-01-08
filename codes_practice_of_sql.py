# ALTER TABLE `users` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`);
#to change the configurationn of the id attribute


# INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES ('1', 'pritush', 'mmdihf', 'ophffhswip');
# to insert a users (table)


# CREATE TABLE users(
#     id integer NOT NULL,
#     name varchar(255),
#     email varchar(255),
#     CONSTRAINT U_email_name UNIQUE (email,name)
#     -- meaning if the email and name set(dono ko mila k) is repeating then we will not let it happen
#     -- and that constraint we give a name to it by using constraint keyword so in future if we want to remove that constraint we can do it without any problem
# )



"""
CREATE TABLE users(
    id integer NOT NULL PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    CONSTRAINT U_email_name UNIQUE (email,name),
    PRIMARY KEY (id,email)
    -- meaning if the email and name set(dono ko mila k) is repeating then we will not let it happen
    -- and that constraint we give a name to it by using constraint keyword so in future if we want to remove that constraint we can do it without any problem

)

# if there is only one primary key then we define it just beside the line and if there is a set for a primary key then define it seperately
"""


"""
CREATE TABLE orders(
    oid integer PRIMARY KEY,
    usr_id integer,
    time_of_order datetime,
    FOREIGN KEY (usr_id) REFERENCES users(id)
)
# for forign key code 
"""


"""
# Check wala k liye


CREATE TABLE students(
    sid integer PRIMARY KEY,
    sname varchar(255) not null,
    email varchar(255) not null UNIQUE,
    age integer CHECK (age > 6 and age < 25)
)
"""


"""
# default k use k liye

CREATE TABLE passanger(
    pid integer PRIMARY KEY,
    pname varchar(255) not null,
    gender varchar(255) DEFAULT "others"
)

CREATE TABLE passanger(
    pid integer PRIMARY KEY,
    pname varchar(255) not null,
    gender varchar(255) DEFAULT "others",
    journey_date datetime DEFAULT CURRENT_TIMESTAMP
)
"""

"""
auto incriment 

CREATE TABLE passanger(
    pid integer PRIMARY KEY AUTO_INCREMENT,
    pname varchar(255) not null,
    gender varchar(255) DEFAULT "others",
    journey_date datetime DEFAULT CURRENT_TIMESTAMP
)
"""



"""
                              ALTER TABLE COMMANDS
 1. add columns (
                  alter table (table name) add column (column name) (datatype of the column) (not null) (auto_incriment) and rest to add on                                      
                )
 
 2.   Delete columns   (
                            alter table (table name) drop (column name)
                        )
 
 3.   modify columns   (
                            alter table (table name) modify column (column name) (jis data type m convert karnah ya kuch aur change karna h toh uske yaha p aega)
                        )
 
 4.  add remove constrains    (
                                    alter table (table name) add constraint (contraint name) then constraint
                                    
                                    alter table (table name) drop constraint (constraint name) 
 )
"""


'--------------------------------------------------  END OF DDL COMMAND ------------------------------------------------------'


" -----------------------------------------------------  DATA MANUPULATION LANGUAGE  (DML)  ------------------------------------------------------------"


"""

INSERT ( 
            1   -    INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
          
          2   -  INSERT INTO `users` VALUES (NULL, '{}', '{}', '{}');
          
          3 (For multiple values)    -    INSERT INTO `users` (),(),()
       )

"""



"""

RETRIEVE (Practice on the titanic dataset)

Select all columns  -   (SELECT * FROM (table name))

Filtering the columns we want     -     SELECT `COL 1`,`COL 2` FROM tested;  #if the columns have spaces between them otherwise simply name no string type structure required

Getting the column with different names(Alias)   -   SELECT `COL 1`as (jo bhi nam se bulana chahte ho),`COL 2` as (same thing here) FROM tested;

Calculating the expression   -   SELECT `COL 4`,`COL 7`+`COL 8` AS Family FROM tested;  name and family he

Constants   -   SELECT `COL 4`,(`COL 7`+`COL 8`)*10000 AS Compensation FROM tested;

Distinct single col   -    Select DISTINCT `COL 5` FROM tested

Distinct multiple col   -    Select DISTINCT `COL 5`,`COL 3` FROM tested

Comparison operator   -   SELECT * FROM `tested` WHERE `COL 2`=0;


"""

