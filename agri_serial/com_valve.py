# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
import com_func

#com_valve
class valveClass:

    def __init__(self):
        print ""
        
    # @return TRUE: nothing.dat
    def Is_addValve(self, mc_id, nSec):
    	ret=False
    	iCt=0
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	
    	dic = {"id": 0L, "creat_dt" : ""}
    	sSql="select id, DATE_FORMAT(created,'%Y-%m-%d %H:%i:%s') as creat_dt"
    	sSql=sSql+" from t_vitems where mc_id ="+mc_id
    	sSql=sSql+" ORDER BY created desc limit 1"
    	#print( "sSql="+ sSql)
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	for row in result:
    		iCt=iCt+1
    		dic["id"]        =row[0]
    		dic["creat_dt"]  =row[1]
    		
    	cursor.close()
    	if iCt==0:
    		return True
    		
    	cursor = connection.cursor()
    	sSql="SELECT  TIMESTAMPDIFF(SECOND, '" +dic["creat_dt"] + "', now()) as sec_num;"
    	#print( "sSql="+ sSql)
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	dfSec=0
    	for row in result:
    		dfSec        =row[0]
#    	print("dfSec="+str(dfSec))
    	cursor.close()
    	connection.close()
    	
    	if(dfSec > nSec ):
    		return True
    		
    	return ret
    	
    def saveValve(self, getDat, datMc):
    	ret=False
    	clsFunc = com_func.funcClass()
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	
    	k_flg_1=clsFunc.Is_validValve( int(getDat["snum_1"]) ,datMc["moi_num"])
    	k_flg_2=clsFunc.Is_validValve( int(getDat["snum_2"]) ,datMc["moi_num"])
    	k_flg_3=clsFunc.Is_validValve( int(getDat["snum_3"]) ,datMc["moi_num"])
    	k_flg_4=clsFunc.Is_validValve( int(getDat["snum_4"]) ,datMc["moi_num"])
    	if(datMc["vnum_1"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_vitems (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",k_flg"
    		sSql=sSql+",k_kbn"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",1"
    		sSql=sSql+","+ str(k_flg_1)
    		sSql=sSql+",1"
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_2"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_vitems (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",k_flg"
    		sSql=sSql+",k_kbn"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",2"
    		sSql=sSql+","+ str(k_flg_2)
    		sSql=sSql+",1"
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_3"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_vitems (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",k_flg"
    		sSql=sSql+",k_kbn"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",3"
    		sSql=sSql+","+ str(k_flg_3)
    		sSql=sSql+",1"
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_4"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_vitems (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",k_flg"
    		sSql=sSql+",k_kbn"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",4"
    		sSql=sSql+","+ str(k_flg_4)
    		sSql=sSql+",1"
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()

    	connection.close()
    	ret=True
    	return ret
    	