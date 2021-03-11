import sqlite3

conn = sqlite3.connect('RRTS_DB.db')

class __ResidentsSchema:
    def __init__(self):
        self.curs = conn.cursor()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS "Complaints" (
        	"complaintId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        	"roadLocation"	TEXT NOT NULL,
        	"startLocation"	TEXT NOT NULL,
        	"endLocation"	TEXT NOT NULL,
        	"residentID"	INTEGER NOT NULL,
        	FOREIGN KEY("residentID") REFERENCES "Residents"("ResidentsID")
        )
        ''')
        conn.commit()

    def insertNewResident(self, name, idCardNo, Address, PhoneNo):
        curs = self.curs.execute('''INSERT INTO Residents(Name,IdCard,Address,PhoneNo) 
                    VALUES (? ,? ,? ,?);''', (name, idCardNo, Address, PhoneNo))
        val = curs.lastrowid
        conn.commit()
        return val

    def getAllResident(self):
        curs = self.curs.execute('SELECT * FROM Residents;')
        return curs.fetchall()

    def getResidentById(self,id):
        curs = self.curs.execute('SELECT * FROM Residents WHERE ResidentsID = ?',(id,))
        return curs.fetchone()


class __ComplainSchema:
    def __init__(self):
        self.curs = conn.cursor()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS "Residents" (
                "ResidentsID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "Name"	TEXT NOT NULL,
                "IdCard"	TEXT NOT NULL UNIQUE,
                "Address"	TEXT DEFAULT 'Home',
                "PhoneNo"	INTEGER NOT NULL UNIQUE
            )
        ''')
        conn.commit()

    def makeComplaint(self, resId, roadLoc, startingPoint, endingPoint):
        curs = self.curs.execute('''
            INSERT INTO Complaints
            ("roadLocation", "startLocation", "endLocation", "residentID")
            VALUES ( ?, ?, ?, ?);
        ''', (roadLoc, startingPoint, endingPoint, resId))
        conn.commit()
        return curs.lastrowid

class __ComplaintInfoSchema:
    def __init__(self):
        conn.execute('''
            CREATE TABLE IF NOT EXISTS "ComplaintInfo" (
                "complaintId"	INTEGER,
                "priority"	INTEGER,
                "rawMaterial"	TEXT,
                "machines"	TEXT,
                "personel"	TEXT,
                PRIMARY KEY("complaintId"),
                FOREIGN KEY("complaintId") REFERENCES "Complaints"("complaintId")
            )
            ''')
        conn.commit()

    def makeComplaintInfo(self,mapping):
        conn.execute('''
        INSERT INTO ComplaintInfo 
        ("complaintId", "priority", "rawMaterial", "machines", "personel") 
        VALUES (:complainId, :priority, :rawMaterial, :machines, :personel);
        ''',mapping)
        conn.commit()

    def updateComplaintInfo(self,mapping):
        conn.execute('''
            UPDATE ComplaintInfo
            SET priority = :priority,
                rawMaterial = :rawMaterial,
                machines = :machines,
                personel = :personel
            WHERE complaintId = :complainId;
        ''',mapping)
        conn.commit()

class __ResourcesSchema:
    def __init__(self):
        conn.execute('''
            CREATE TABLE IF NOT EXISTS "Resources" (
                "manpower"	INTEGER DEFAULT '',
                "machines"	TEXT DEFAULT ''
            )
        ''')
        curs = conn.execute('SELECT * FROM Resources;')
        if curs.fetchone() is None:
            conn.execute('INSERT INTO "Resources" ("manpower", "machines") VALUES (?, ?);', ('', ''))
        conn.commit()

    def addResources(self,manpower,machines):
        conn.execute('DELETE FROM Resources')
        conn.execute('INSERT INTO "Resources" ("manpower", "machines") VALUES (?, ?);',(manpower,machines))
        conn.commit()

    def getResources(self):
        curs = conn.execute('SELECT * FROM Resources;')
        val = curs.fetchone()
        if val is not None:
            return val
        return '', ''

class __ScheduleSchema:
    def getSchedule(self):
        curs = conn.execute('''
            SELECT * FROM Complaints as c
            LEFT JOIN ComplaintInfo as ci ON c.complaintId = ci.complaintId
            ORDER BY rawMaterial IS NOT NULL , machines IS NOT NULL, personel IS NOT NULL, priority;
        ''')
        return curs.fetchall()



residentTable = __ResidentsSchema()
complainTable = __ComplainSchema()
infoTable = __ComplaintInfoSchema()
resourcesTable = __ResourcesSchema()
scheduleTable = __ScheduleSchema()