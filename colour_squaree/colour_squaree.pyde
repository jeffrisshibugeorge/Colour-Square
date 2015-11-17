add_library('serial')
add_library('arduino')

ard = Arduino(this,"/dev/cu.wchusbserial1410",57600)
 
def setup():
    global ard
    size(400,600)
    ard.pinMode(13, ard.OUTPUT)
    
#Serial.begin(9600)
#ard.pinMode(0,ard.INPUT)
 
def draw():
    global ard
    sensor = ard.analogRead(0)
    println(sensor)
    background(sensor/3, sensor/2, sensor/5)
    fill(sensor/6, sensor/4, sensor/2)
    rect(45, 56, sensor/2, sensor/2)
    
