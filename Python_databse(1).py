#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)

cursorObject = dataBase.cursor()

cursorObject.execute ("CREATE DATABASE Latihan_Python1")


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)

cursorObject = dataBase.cursor()

cursorObject.execute ("CREATE DATABASE MHS_TI_D")


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

mahasiswaRecord="""CREATE TABLE MAHASISWA(
                    NIM VARCHAR(10) NOT NULL,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR (255) NOT NULL,
                    MATA_KULIAH_YANG_DIKUTI VARCHAR(10),
                    UMUR INT NOT NULL,
                    PRIMARY KEY(NIM)
                    )"""
cursorObject.execute(mahasiswaRecord)

dataBase.close()


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

sql ="INSERT INTO MAHASISWA(NIM, NAMA, ALAMAT, MATA_KULIAH_YANG_DIKUTI, UMUR)\
VALUES(%s, %s, %s, %s, %s)"
val = [('1212', 'Habib Ainur', 'Madiun', 'Py12', 19),
       ('1313', 'Habib Maruf', 'Malang', 'Py13', 19),
       ('1414', 'Ainur Maruf', 'Magelang', 'Py14', 20),
       ('1515', 'Bibam Maruf', 'Medan', 'Py15', 19),
       ('1616', 'Maruf Bib', 'Minang', 'Py16', 19),
       ('1717', 'BibAM', 'Manado', 'Py17', 19),
       
      ]
cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

dosenRecord="""CREATE TABLE DOSEN(
                    NIP VARCHAR(20) NOT NULL,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATA_KULIAH_YANG_DIAJAR VARCHAR(50),
                    ASAL_DAERAH VARCHAR(50),
                    PRIMARY KEY(NIP)
                    )"""
cursorObject.execute(dosenRecord)

dataBase.close()


# In[9]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

sql ="INSERT INTO DOSEN(NIP, NAMA_DOSEN, MATA_KULIAH_YANG_DIAJAR, ASAL_DAERAH)\
VALUES(%s, %s, %s, %s)"
val = [('2121', 'DR.Habib', 'Algoritma', 'Madiun'),
       ('3131', 'Prof.Maruf', 'Matematika Informatika', 'Surakarta'),
       ('4141', 'Ir.Bibam', 'Desain UI/UX', 'Surabaya'),
       ('5151', 'Habib.M.kom', 'Iot', 'Magetan'),
       ('6161','Prof. Ainur S.kom', 'Basis Data', 'Wonogiri'),
       ('7171', 'Habib Ainur Maruf Amd.Kom', 'Sistem Operasi', 'Caruban'),
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[10]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

matkulRecord="""CREATE TABLE MATA_KULIAH (
                    KODE_MATA_KULIAH VARCHAR(10) NOT NULL,
                    NAMA_MATA_KULIAH VARCHAR(50) NOT NULL,
                    WAKTU DATE,
                    RUANGAN VARCHAR (10),
                    PRIMARY KEY(KODE_MATA_KULIAH)
                    )"""
cursorObject.execute(matkulRecord)

dataBase.close()


# In[11]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

sql ="INSERT INTO MATA_KULIAH(KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU,RUANGAN)\
VALUES(%s, %s, %s, %s)"
val = [('PY21', 'Sistem Informasi', '2024-03-07', 'Lab21'),
       ('PY31', 'Analisis Data', '2024-03-06', 'Lab31'),
       ('PY41', 'Pengembangan Aplikasi', '2024-03-05', 'Lab41'),
       ('PY51', 'Analisis SI', '2024-03-04', 'Lab51'),
       ('PY61','Keamanan Data', '2024-03-03', 'Lab61'),
       ('PY71', 'Pengembangan AI', '2024-03-02', 'Lab71'),
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

# executing the SELECT query for mahasiswa data
select_mahasiswa_query = """SELECT *
                            FROM MAHASISWA"""

cursorObject.execute(select_mahasiswa_query)

# fetching all rows
mahasiswa_rows = cursorObject.fetchall()

# displaying the data
for row in mahasiswa_rows:
    print(row)

# disconnecting from server
dataBase.close()


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

# executing the SELECT query for mahasiswa data
select_mahasiswa_query = """SELECT *
                            FROM DOSEN"""

cursorObject.execute(select_mahasiswa_query)

# fetching all rows
mahasiswa_rows = cursorObject.fetchall()

# displaying the data
for row in mahasiswa_rows:
    print(row)

# disconnecting from server
dataBase.close()


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

# executing the SELECT query for mahasiswa data
select_mahasiswa_query = """SELECT *
                            FROM MATA_KULIAH"""

cursorObject.execute(select_mahasiswa_query)

# fetching all rows
mahasiswa_rows = cursorObject.fetchall()

# displaying the data
for row in mahasiswa_rows:
    print(row)

# disconnecting from server
dataBase.close()


# In[2]:





# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mhs_ti_d"
)

cursorObject = dataBase.cursor()

select_query = """SELECT 
                    MAHASISWA.NIM,
                    MAHASISWA.NAMA AS NAMA_MAHASISWA,
                    MATA_KULIAH.KODE_MATA_KULIAH,
                    MATA_KULIAH.NAMA_MATA_KULIAH,
                    MATA_KULIAH.RUANGAN,
                    DOSEN.NAMA_DOSEN
                  FROM 
                    MAHASISWA
                  JOIN 
                    MATA_KULIAH ON MAHASISWA.MATA_KULIAH_YANG_DIKUTI = MATA_KULIAH.KODE_MATA_KULIAH
                  JOIN 
                    DOSEN ON MATA_KULIAH.NAMA_MATA_KULIAH = DOSEN.MATA_KULIAH_YANG_DIAJAR"""

cursorObject.execute(select_query)

rows = cursorObject.fetchall()

for row in rows:
    print(row)

dataBase.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




