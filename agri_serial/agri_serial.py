import threading
import serial
import com_getparam
import com_getmaster
import com_func
import com_logsave
import com_sensor
import com_valve

mDevice = "/dev/ttyACM0"

mOK_CODE=1
mNG_CODE=0

ER_STAT_000="000"
ER_STAT_101="101"
ER_STAT_102="102"
ER_STAT_103="103"

sHEAD="res_dat="

def init_proc():
    ret_base= "000000000000000000000000"
    ser=serial.Serial(mDevice ,9600)
    clsParam = com_getparam.getparamClass()
    clsMst = com_getmaster.getmasterClass()
    clsCom  = com_func.funcClass()
    clsLog = com_logsave.logsaveClass()
    clsSens= com_sensor.sensorClass()
    clsValve=com_valve.valveClass()

    while True:
        val=ser.readline()
        bFrom = clsParam.Is_fromMC(val)
        if bFrom==True:
        	dic= clsParam.getDict(val)
        	dMst= clsMst.getMaster(dic["mc_id"])
        	if dMst["mc_id"] ==0L:
        		print str(mNG_CODE) + ER_STAT_102 + ret_base
        	else:
        		sRes=""
        		clsLog.saveLog(dic)
        		if(clsSens.Is_addSensor(dic["mc_id"], 60)==True):
        			clsSens.saveSensor( dic, dMst)
        		if(clsValve.Is_addValve( dic["mc_id"], dMst["ck_num"])==True ):
        			clsValve.saveValve( dic, dMst)
        			sMsg= clsCom.getResponse(dic ,dMst)
        			sRes =sHEAD + str(mOK_CODE) + ER_STAT_000 +sMsg
        			ser.write(sRes)
        		else:
        			sRes =sHEAD + str(mNG_CODE) + ER_STAT_103 +ret_base
        			ser.write(sRes)
        			
        		print "OUT:" + sRes
        		
        print("IN :"  + val)

if __name__ == "__main__":
	t = threading.Timer( 60.0, init_proc)
	t.start() # after xx seconds, "hello, world" will be printed
