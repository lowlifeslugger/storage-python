# timer
import time
def secondsstopclock():
    hours = int(input("how many hours : "))
    mins = int(input("how many minutes : "))
    secs = int(input("how many seconds (if applicable) : "))
    sechour = 3600*hours
    secmin = 60*mins
    secsec = secs
    seconds = secsec + secmin + sechour
    for sec in reversed(range(0,seconds)):
        print(sec)
        time.sleep(1)

def properstopclock():
    hours = int(input("how many hours : "))
    mins = int(input("how many minutes : "))
    secs = int(input("how many seconds (if applicable) : "))
    times = hours*3600 + mins*60 + secs
    for t in reversed(range(0,times)):
        hr = (t//3600)
        mn = (t%3600)//60
        sc = t%60
        print(f"\r{hr:02d}:{mn:02d}:{sc:02d}", end="")
        time.sleep(1)
        
    print("times up")

