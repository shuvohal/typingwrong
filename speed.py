from time import*
import random as r


def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except :
            error=error+1
    return error
def spped_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)



test=["daffordil international universityi","my name is shuvo","I am 21 years old","my id is 213-15-4369","i am a python lover","i will practice day by day to improve my skil","i love my mother","i love my family","always ready to fight"]
test1=r.choice(test)
print("*****typing speed calculator*****")
print(test1)
print()
print()
time_1=time()
testinput=input(" Enter: ")
time_2=time()

print('speed: ',spped_time(time_1,time_2,testinput),"w/sec")
print("Error: ",mistake(test1,testinput))