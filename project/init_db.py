import sqlite3

conn = sqlite3.connect("feedback.db")
c = conn.cursor()

# Delete old tables and data
c.execute("DROP TABLE IF EXISTS feedback")
c.execute("DROP TABLE IF EXISTS students")

# Create students table
c.execute("""
CREATE TABLE students(
    student_id TEXT PRIMARY KEY,
    name TEXT,
    password TEXT
)
""")

# Create feedback table
c.execute("""
CREATE TABLE feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    giver_id TEXT,
    receiver_id TEXT,
    rating INTEGER,
    comment TEXT
)
""")

# Students data
c.execute("INSERT INTO students VALUES('b221595','N.Sai prasanna','1234')")
c.execute("INSERT INTO students VALUES('b230006','J.Mohan','1234')")
c.execute("INSERT INTO students VALUES('b230050','S.Vyshnavi','1234')")
c.execute("INSERT INTO students VALUES('b230051','G.Rohith','1234')")
c.execute("INSERT INTO students VALUES('b230089','S.Vennela','1234')")
c.execute("INSERT INTO students VALUES('b230113','B.Ajay Kumar','1234')")
c.execute("INSERT INTO students VALUES('b230143','P.Rakshitha','1234')")
c.execute("INSERT INTO students VALUES('b230190','K.Spurthi','1234')")
c.execute("INSERT INTO students VALUES('b230199','M.Rakesh','1234')")
c.execute("INSERT INTO students VALUES('b230239','A.Chandrika','1234')")
c.execute("INSERT INTO students VALUES('b230258','K.Hansika','1234')")
c.execute("INSERT INTO students VALUES('b230280','K.Rajeshwari','1234')")
c.execute("INSERT INTO students VALUES('b230297','L.Rekha','1234')")
c.execute("INSERT INTO students VALUES('b230298','A.Nithish Kumar','1234')")
c.execute("INSERT INTO students VALUES('b230321','V.Bhavana','1234')")
c.execute("INSERT INTO students VALUES('b230367','S.Sreeja','1234')")
c.execute("INSERT INTO students VALUES('b230430','K.Nikhil Chary','1234')")
c.execute("INSERT INTO students VALUES('b230452','Samrin','1234')")
c.execute("INSERT INTO students VALUES('b230458','V.Shravan Kumar Reddy','1234')")
c.execute("INSERT INTO students VALUES('b230489','P.Vaishnavi','1234')")
c.execute("INSERT INTO students VALUES('b230495','K.vinay','1234')")
c.execute("INSERT INTO students VALUES('b230501','R.Sanjana','1234')")
c.execute("INSERT INTO students VALUES('b230521','B.Kavya','1234')")
c.execute("INSERT INTO students VALUES('b230543','J.Vaishnavi','1234')")
c.execute("INSERT INTO students VALUES('b230573','A.Mahendar Reddy','1234')")
c.execute("INSERT INTO students VALUES('b230577','A.Maneesha','1234')")
c.execute("INSERT INTO students VALUES('b230626','P.Madhupriya','1234')")
c.execute("INSERT INTO students VALUES('b230658','M.Kondal Reddy','1234')")
c.execute("INSERT INTO students VALUES('b230678','T.Thirumala','1234')")
c.execute("INSERT INTO students VALUES('b230709','T.Hemavardini','1234')")
c.execute("INSERT INTO students VALUES('b230728','S.Spoorthi','1234')")
c.execute("INSERT INTO students VALUES('b230750','P.Ruchi','1234')")
c.execute("INSERT INTO students VALUES('b230769','C.Sanjana','1234')")
c.execute("INSERT INTO students VALUES('b230788','R.Anil','1234')")
c.execute("INSERT INTO students VALUES('b230860','P.Shivani','1234')")
c.execute("INSERT INTO students VALUES('b230941','J.Shyamala','1234')")
c.execute("INSERT INTO students VALUES('b230983','A.Sai Kiran','1234')")
c.execute("INSERT INTO students VALUES('b230990','G.Akshaya','1234')")
c.execute("INSERT INTO students VALUES('b231012','P.Sravani','1234')")
c.execute("INSERT INTO students VALUES('b231062','Muskan','1234')")
c.execute("INSERT INTO students VALUES('b231066','Sk.Shabeer Pasha','1234')")
c.execute("INSERT INTO students VALUES('b231104','Sk.Noushin','1234')")
c.execute("INSERT INTO students VALUES('b231134','M.Selvamani','1234')")
c.execute("INSERT INTO students VALUES('b231136','N.Aaradhya','1234')")
c.execute("INSERT INTO students VALUES('b231171','M.Deena','1234')")
c.execute("INSERT INTO students VALUES('b231216','J.Ram','1234')")
c.execute("INSERT INTO students VALUES('b231239','G.Sai Charan','1234')")
c.execute("INSERT INTO students VALUES('b231273','K.Asini','1234')")
c.execute("INSERT INTO students VALUES('b231290','R.Amber Singh','1234')")
c.execute("INSERT INTO students VALUES('b231324','D.Devilal','1234')")
c.execute("INSERT INTO students VALUES('b231345','D.Kailash','1234')")
c.execute("INSERT INTO students VALUES('b231354','K.Srimai','1234')")
c.execute("INSERT INTO students VALUES('b231392','B.Siddartha','1234')")
c.execute("INSERT INTO students VALUES('b231463','G.Ishwarya','1234')")
c.execute("INSERT INTO students VALUES('b231489','K.Ganesh','1234')")
c.execute("INSERT INTO students VALUES('b231519','P.Charani','1234')")
c.execute("INSERT INTO students VALUES('b231586','N.Harshavardhan','1234')")
c.execute("INSERT INTO students VALUES('b231595','K.Meenakshi','1234')")
c.execute("INSERT INTO students VALUES('b231660','T.Manohar','1234')")
c.execute("INSERT INTO students VALUES('b231697','R.Maithri Reddy','1234')")
c.execute("INSERT INTO students VALUES('b231706','C.Sunil','1234')")
c.execute("INSERT INTO students VALUES('b231745','C.Aditya','1234')")
c.execute("INSERT INTO students VALUES('b231787','M.Amulya','1234')")
c.execute("INSERT INTO students VALUES('b231831','J.kalyan','1234')")

conn.commit()
conn.close()

print("Database created successfully!")