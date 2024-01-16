from config import dbConnection
from flask import current_app
from sqlalchemy.orm.exc import NoResultFound
import uuid
from userDb import dailyattendance, employeeinfo
conn = dbConnection()

class Attedance:


    def empName(self,EmpId):

        # with conn.cursor() as cur:
        #     sql = "SELECT Name FROM employeeinfo WHERE EmpId=%s"
            
        #     cur.execute(sql,EmpId)

            # name=cur.fetchone()
        name=current_app.extensions['sqlalchemy'].db.session.query(
            employeeinfo.Name).filter_by(EmpId=EmpId).first()
        return name

    # def checkIn(self,EmpId,Name,Date,Checkin,RefId):

    #         # with conn.cursor() as cur:

    #             # sql = "INSERT INTO dailyattendance (EmpId,Name,Date,CheckinTime,ReferenceID) VALUES (%s, %s, %s, %s, %s)"
    #             # val=EmpId,Name,Date,Checkin,RefId
        
    #             # cur.execute(sql,val)

    #             # conn.commit()

    #     new_attendance = dailyattendance(
    #     EmpId=EmpId,
    #     Name=Name,
    #     Date=Date,
    #     CheckinTime=Checkin,
    #     ReferenceID=RefId
        
    #     )

    #     # Add the instance to the session and commit
    #     current_app.extensions['sqlalchemy'].db.session.add(new_attendance)
    #     current_app.extensions['sqlalchemy'].db.session.commit()

    #     # Close the session
    #     current_app.extensions['sqlalchemy'].db.session.close()
    #     return "Inserted Successfully"

    from sqlalchemy.orm.exc import NoResultFound

    def checkIn(self, EmpId, Name, Date, Checkin, RefId):
        try:
            # Check if a row with the same EmpId, Date, and RefId exists
            existing_row = dailyattendance.query.filter_by(EmpId=EmpId, Date=Date, ReferenceID=RefId).one()
        except NoResultFound:
            # If no row exists, insert a new one
            new_attendance = dailyattendance(
                EmpId=EmpId,
                Name=Name,
                Date=Date,
                CheckinTime=Checkin,
                ReferenceID=RefId
            )

            # Add the instance to the session and commit
            current_app.extensions['sqlalchemy'].db.session.add(new_attendance)
            current_app.extensions['sqlalchemy'].db.session.commit()

            # Close the session
            current_app.extensions['sqlalchemy'].db.session.close()
            return "Inserted Successfully"
    
    def fetchData(self,EmpId, date):
        # with conn.cursor() as cur:
            
        #     sql="SELECT * FROM dailyattendance WHERE EmpId=%s AND Date=%s"

        #     val=EmpId,date

        #     cur.execute(sql,val)

        #     row=cur.fetchone()

        row=current_app.extensions['sqlalchemy'].db.session.query(dailyattendance).filter_by(EmpId=EmpId,Date=date).all()
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
    
    
    def checkout(self,checkout):

    #  with conn.cursor() as cur:

    #     sql = "UPDATE dailyattendance SET CheckoutTime = %s WHERE ReferenceID = %s AND CheckoutTime IS NULL"


    #     cur.execute(sql, (checkout, ReferenceID))


    #     conn.commit()

        row=current_app.extensions['sqlalchemy'].db.session.query(dailyattendance).filter_by(CheckoutTime=None).first()
        row.CheckoutTime=checkout
        current_app.extensions['sqlalchemy'].db.session.commit()
        
        return "updated"
     
    def GenerateReferenceId(self):

        random_uuid = uuid.uuid4()

        random_string = str(random_uuid)

        return random_string
        

  

 

 

     
    
    