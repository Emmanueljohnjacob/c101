import time
def mytimer(s):
    while s > 0:
        mins=int(s/60)
        secs=int(s%60)
        timer=f'{mins}:{secs}'
        print(timer)
        s=s-1
    print('times up')
secs=input("enter the time in seconds: ")
mytimer(int(secs))    