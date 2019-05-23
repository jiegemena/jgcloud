import entity.Entity
import uuid

class CUserService:
    TableName = 'jguser'
    def __init__(self, *args, **kwargs):
        self.userentity = entity.Entity.Entity(CUserService.TableName)

    def getUserFromUserNameAndPwd(self,username,pwd):
        '''
        '''
        sqlstr = 'SELECT * FROM `jguser` where username = ? and password = ?'
        sqlpar = []
        sqlpar.append(username)
        sqlpar.append(pwd)
        
        user = self.userentity.query_one(sqlstr, sqlpar)
        return user

    def updateLoginGuidById(self, id1):
        sqlstr = "UPDATE `jguser` SET `loginguid` = ? WHERE id = " + str(id1)
        sqlpar = []
        sqlpar.append(str(uuid.uuid1()))
        return self.userentity.exec(sqlstr, sqlpar)

    def getUserByLoginGuid(self, guid):
        sqlstr = 'SELECT * FROM `jguser` WHERE `loginguid` = ?'
        sqlpar = []
        sqlpar.append(guid)
        user = self.userentity.query_one(sqlstr, sqlpar)
        return user



    