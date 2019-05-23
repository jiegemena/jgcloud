import entity.Entity


class CJGServer:
    TableName = 'jguser'

    def __init__(self, *args, **kwargs):
        self.jgserverEntity = entity.Entity.Entity(CJGServer.TableName)

    def add(self,jgname, jghost, jgport):
        jgserver = {}
        jgserver['jgname'] = jgname
        jgserver['jghost'] = jghost
        jgserver['jgport'] = jgport
        return self.jgserverEntity.add(jgserver)

    def getJGServes(self):
        '''
        get all services
        - par:
            - jgname: server name
        '''

        sql = ""
        sqlpar = []

        return self.jgserverEntity.query_all(sql,sqlpar)

    def getJGServerByJGName(self,jgname):
        '''
        get all services by name
        - par:
            - jgname: server name
        '''
        sql = ""
        sqlpar = []

        return self.jgserverEntity.query_all(sql,sqlpar)

    def getJGServerByJGNameOne(self,jgname):
        '''
        random acquisition of an item
        - par:
            - jgname: server name
        '''
        sql = ""
        sqlpar = []

        return self.jgserverEntity.query_all(sql,sqlpar)