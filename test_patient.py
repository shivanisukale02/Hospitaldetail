import unittest
import sqlite3

class Patients(unittest.TestCase):
    def setUp(self):
        self.connection=sqlite3.connect("hospital.db")
        self.patientCode="124"
        self.name="sachin"

    def tearDown(self):
        self.patientCode="0"
        self.name=""
        self.connection.close()

    def test_pat1(self):
        result=self.connection.execute("SELECT name from Patient_detail where patientCode="+self.patientCode)
        for i in result:
            fetchname=i[0]
        self.assertEqual(fetchname,self.name)



if __name__=="__main__":
    unittest.main()