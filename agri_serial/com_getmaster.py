# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst

#define

#com_getmaster
class getmasterClass:

    def __init__(self):
        print ""
        
    def getMaster(self, sId):
    	cls = com_appConst.appConstClass()
    	
    	ret = {"mc_id": 0L, "moi_num" : 0
    	, "kai_num_1": 0, "vnum_1": 0
    	, "kai_num_2": 0, "vnum_2": 0
    	, "kai_num_3": 0, "vnum_3": 0
    	, "kai_num_4": 0, "vnum_4": 0
    	, "ck_num":0  , "created":0
    	}
        connection = MySQLdb.connect(host=cls.mHost, db= cls.mDB_NAME, user=cls.mUser, passwd=cls.mPass, charset="utf8")
        cursor = connection.cursor()
        sSql ="select id, moi_num"
        sSql =sSql+", kai_num_1, vnum_1"
        sSql =sSql+", kai_num_2, vnum_2"
        sSql =sSql+", kai_num_3, vnum_3"
        sSql =sSql+", kai_num_4, vnum_4"
        sSql =sSql+", ck_num, created"
        sSql =sSql+" from m_mcs"
        sSql =sSql+" where id="+ sId
        sSql =sSql+" limit 1"
        #print sSql
        cursor.execute( sSql )
        result = cursor.fetchall()
        for row in result:
        	#print row
        	ret["mc_id"]   = row[0]
        	ret["moi_num"] = row[1]
        	ret["kai_num_1"] = row[2]
        	ret["vnum_1"]    = row[3]
        	ret["kai_num_2"] = row[4]
        	ret["vnum_2"]    = row[5]
        	ret["kai_num_3"] = row[6]
        	ret["vnum_3"]    = row[7]
        	ret["kai_num_4"] = row[8]
        	ret["vnum_4"]    = row[9]
        	ret["ck_num"]    = row[10]
        	ret["created"]   = row[11]
        cursor.close()
        connection.close()
        return ret
