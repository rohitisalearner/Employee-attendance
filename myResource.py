from flask_restful import Api, Resource, reqparse,request
from datetime import date, datetime
from fun import Attedance
from config import dbConnection
from flask import current_app
from userDb import dailyattendance, employeeinfo
obj=Attedance()

conn=dbConnection()

class ItemListResource(Resource):
    def get(self):
        EmpId=[]
        # payload = request.get_json()

        # EmpId=payload['EmpId']
        # with conn.cursor() as cur:
        #     EmpId=[]
        #     sql = "SELECT * FROM employeeinfo"

        #     cur.execute(sql)

        #     row=cur.fetchall()
        #     for i in row:
        #         EmpId.append(i[1])
        #     data={'EmpId':EmpId}
        data=current_app.extensions['sqlalchemy'].db.session.query(employeeinfo).all()
        print(data)
        for i in data:
            EmpId.append(i.EmpId)
        data={'EmpId':EmpId}
        return data
    
    def post(self):
        payload = request.get_json()
        EmpId=payload['EmpId']
        date = datetime.now().date()
        stringdate = str(date)
        splitnewdate = stringdate.split(' ')
        print(splitnewdate[0],"==================>>>>>")
        
        
        row=obj.fetchData(EmpId, date)
        # print(row,"This is class-----") 
        # print(row[1].Date,"This is row ka one indeixjng=========")
        # print(row[0],"----------this is rowki zero indexing") 
        Type=''
        if row != []:
            print(row,"===============>>>>>>")
            
            CheckinTime=row[0].CheckinTime
            print(CheckinTime,"This is checking time")
            checkOut=row[0].CheckoutTime
            print(checkOut,"This is checkOut time")
            date=row[0].Date
            print(date,"=====This is date")
            strdate = str(date)
            # print(type(strdate))
            splitdate = strdate.split(' ')
            newsplitteddate=splitdate[0]
            print(newsplitteddate,"===>>this is splite date")
        
        if row==[]:
            Type='off'
        elif row[0].CheckinTime !=None and row[0].CheckoutTime ==None:
            Type='onn'

        elif row[0]!=None:
            Type='off'

        elif row[1]==None:
            Type='onn'
        elif row[1].CheckoutTime!=None:
            Type='off'
        else:
            Type='off'
        

            # if row==None:
            #     Type='off'
            # elif row.CheckoutTime==None and row.checkinTime != None:
            #     Type="onn"
            # else:
            #     Type="off"

        # with conn.cursor() as cur:

        #     sql = "SELECT * FROM employeeinfo WHERE EmpId=%s"

        #     cur.execute(sql,EmpId)

        #     row=cur.fetchone()
        row=current_app.extensions['sqlalchemy'].db.session.query(employeeinfo).filter_by(EmpId=EmpId).first()
        current_app.extensions['sqlalchemy'].db.session.commit()

        Empid=row.EmpId
        Name=row.Name
        Date=row.DOJ
        Phone=row.Phone
        Designation=row.Designation
        Email=row.Email

        data={'EmpId':Empid,'Name':Name,'Date':Date,'Phone':Phone,'Designation':Designation,'Email':Email,'Type':Type}

        return data
    
class createItem(Resource):
    def post(self):
        
        payload = request.get_json()

        EmpId=payload['EmpId']

        Type=payload['Type']
        # RefID=payload['Refid']

        Name=obj.empName(EmpId)

        date = datetime.now().date()
        print(date,"...............This is inserting date...............")

        RefId = obj.GenerateReferenceId()

        CheckIn=datetime.now()

        CheckOut=datetime.now()

        row=obj.fetchData(EmpId,date)
        CheckoutTime=''
        if row != None:
            for i in row:
                
            # Name=row.Name
            # Date=row.Date
            # CheckinTime=row[4]
                ReferenceID=i.ReferenceID
                CheckoutTime=i.CheckoutTime
                
                print(row)

        data={}

        if Type== 'off' and row==None:
            
            obj.checkIn(EmpId,Name,date,CheckIn,RefId)
            # data={'RefId':RefId,'CheckinTime':str(CheckIn)}

        elif Type=='off' and CheckoutTime!=None:
            obj.checkIn(EmpId,Name,date,CheckIn,RefId)
            # data={'RefId':ReferenceID,'CheckinTime':str(CheckIn)}

        elif Type=='onn':
            obj.checkout(CheckOut)
            # data={'RefId':RefId,'CheckoutTime':str(CheckOut)}
           
        else:
            print("value Error: value you provided is not valid, Make sure to provide value you suggested")

        return data