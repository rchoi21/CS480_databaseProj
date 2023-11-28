import sqlite3

conn = sqlite3.connect("UIH_vaccinations.db")

conn.execute('''CREATE TABLE vaccines
                (vax_id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name        VARCHAR(100)                      NOT NULL,
                co_name     VARCHAR(100)                      NOT NULL,
                doses_req   INT                               NOT NULL,
                description TEXT,
                available   INT                               NOT NULL,
                on_hold     INT                               NOT NULL);''')

conn.execute('''CREATE TABLE nurses
                (employee_id INTEGER PRIMARY KEY AUTOINCREMENT                NOT NULL,
                fname        VARCHAR(50)                                      NOT NULL,
                mi           CHAR(1),
                lname        VARCHAR(50)                                      NOT NULL,
                age          INT                                              NOT NULL,
                gender       CHECK(gender IN ("male", "female", "other"))     NOT NULL,
                phone_num    VARCHAR(10)                                      NOT NULL,
                address      VARCHAR(200)                                     NOT NULL);''')

conn.execute('''CREATE TABLE patients
                (ssn            VARCHAR(9) PRIMARY KEY                           NOT NULL,
                fname           VARCHAR(50)                                      NOT NULL,
                mi              CHAR(1),
                lname           VARCHAR(50)                                      NOT NULL,
                age             INT                                              NOT NULL,
                gender          CHECK(gender IN ("male", "female", "other"))     NOT NULL,
                race            CHECK(race IN ("White", "African American", "Native American", "Asian", "Pacific Islander", "other")),
                occupation      VARCHAR(50),
                medical_history TEXT(500),
                phone_num       VARCHAR(10)                                      NOT NULL,
                address         VARCHAR(200)                                     NOT NULL);''')

conn.execute('''CREATE TABLE schedule
                (sched_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                slot            DATETIME                          NOT NULL,
                num_patients    INT                               NOT NULL,
                num_nurses      INT                               NOT NULL''')

conn.execute('''CREATE TABLE patient_schedule
                (P_sched_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                slot              DATETIME                          NOT NULL,
                ssn               VARCHAR(9)                        NOT NULL
                employee_id       INT                               NOT NULL,
                vax_id            INT                               NOT NULL
                vax_dose          INT                               NOT NULL''')

conn.execute('''CREATE TABLE nurse_schedule
                (N_sched_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                slot              DATETIME                          NOT NULL,
                employee_id       INT                               NOT NULL,
                num_patients      INT                               NOT NULL''')