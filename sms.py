import os,sys,time,random


#Settings

xnhat = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong  = "\033[1;35m"
trang = "\033[1;37m"
end = '\033[0m'


def banner():
    os.system("clear")
    ban = f'''{do}
.__                          .__                   .__                   ___.            
|  |__  __ __ ___.__.   ____ |  |__  __ _______    |  | _____    _____   \_ |__   ____   
|  |  \|  |  <   |  | _/ ___\|  |  \|  |  \__  \   |  | \__  \  /     \   | __ \ /  _ \  
|   Y  \  |  /\___  | \  \___|   Y  \  |  // __ \_ |  |__/ __ \|  Y Y  \  | \_\ (  <_> ) 
|___|  /____/ / ____|  \___  >___|  /____/(____  / |____(____  /__|_|  /  |___  /\____/  
     \/       \/           \/     \/           \/            \/      \/       \/         

                                                                            ___    ___  
                                                                           |__ \  / _ \ 
                                                                      __   __ ) || | | |
                                                                      \ \ / // / | | | |
                                                                       \ V // /_ | |_| |
                                                                        \_/|____(_)___/         
'''
    for i in ban:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.005)
    print("------------------------------------------------------------------------------------------")    

def dem():
    mang = [xnhat, do, luc, vang, xduong, hong, trang ]
    for i in range(8):    
       mau = random.choice(mang)
       print(f"{mau} Done, Enjoy cai moment nay ! ", end="")
       print("\r",end="")
       time.sleep(1)
       


#datas

banner()
sdt = input(f"{luc}*Nhap sdt: ")
count = int(input(f"{hong}*Nhap so lan spam: "))





#API
#def tv360(sdt):
#    data = -->









































#Run
def runner(sdt, count):
    banner()
    dem()



runner(sdt, count)
