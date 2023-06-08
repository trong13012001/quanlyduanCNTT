from typing import Text
from sqlalchemy import Column,Date,BLOB
from sqlalchemy.types import String, Integer, Text
from database import Base

class UserSchema(Base):
    __tablename__="user"
    userID = Column(Integer, primary_key=True, index=True)
    userName=Column(String(45),unique=True)
    userEmail=Column(String(45),unique=True)
    userPassword=Column(String(45))
    userRole=Column(Integer)

class StudentSchema(Base):
    __tablename__="student"
    studentID = Column(String(6),primary_key=True, index=True)
    studentEmail=Column(String(45),unique=True)
    studentName=Column(String(45))
    studentK=Column(Integer)
    studentDOB=Column(Date)
    studentGender=Column(String(4))
    studentAddress=Column(String(45))
    studentPhone=Column(String(10))
    studentDatejoin=Column(Date)
    studentParent=Column(String(45))
    majorID=Column(String(6))
    branchID=Column(Integer)
class TeacherSchema(Base):
    __tablename__="teacher"
    teacherID = Column(String(6),primary_key=True, index=True)
    teacherEmail=Column(String(45),unique=True)
    teacherName=Column(String(45))
    teacherDOB=Column(Date)
    teacherGender=Column(String(4))
    teacherAddress=Column(String(45))
    teacherPhone=Column(String(10))
    teacherDatejoin=Column(Date)
    majorID=Column(String(6))
    branchID=Column(Integer)
class ImageSchema(Base):
    __tablename__="image"
    userID=Column(String(6),primary_key=True, index=True)
    image=Column(String)
class MajorSchema(Base):
    __tablename__="major"
    majorID=Column(String(6),primary_key=True, index=True)
    majorName=Column(String)
class BranchSchema(Base):
    __tablename__="branch"
    branchID=Column(Integer,primary_key=True, index=True)
    branchName=Column(String)
    majorID=Column(String(6))
    majorName=Column(String)
class CourseSchema(Base):
    __tablename__="course"
    courseID=Column(Integer,primary_key=True, index=True)
    subjectID=Column(String)
    subjectName=Column(String)
    className=Column(String)
    courseDate=Column(Integer)
    courseShift=Column(String)
    courseRoom=Column(String)
    courseCredits=Column(Integer)
    teacherName=Column(String)