from zipfile import ZipFile
from os import get_terminal_size as aterm
import zipfile,sys


try:
    file=ZipFile(sys.argv[1])
except IndexError as inde:
    raise ValueError(f"{sys.argv[0]} need a \033[31mZip file\n\n\033[33m{sys.argv[0]} 'path/to/file'") from inde
    exit()

trf=None


def try_this(password):
    file.pwd=bytes(str(password),encoding='utf-8')
    try:
        file.testzip()
        print("\r\033[K"+str(password)," "*(aterm()[0]-18-len(str(password))
),"[   \033[32mMatching\033[37m  ]",flush=True)
        print("\nRun CODE:",password,"   \033[32mAlmost matching....\033[37m\n\ncontinue to extract? (y/n)",end='',sep='',flush=True)
        x=input()
        if x=="y":pass
        else :
            print("        [    \033[31mAborted\033[37m   ]")
            print(f"\r\033[K\n\033[36mPASSWORD identify\033[31med  \033[32m{password}\033[37m [ \033[33mNote: not conformed \033[37m]",flush=True)
            exit()
        for i in file.namelist():
            print("[*] Extracting...  | "+str(i),' '*(aterm()[0]-34-len(str(i))),end='',sep='',flush=True)
            file.extract(i)
            print("[    \033[32mOK\033[37m    ]",flush=True)
        global trf
        trf=False
        print("\033[33mSuccessfully decompressed \033[36mwithout Errors!")
        print(f"\r\033[K\n\033[36mPASSWORD identify\033[31med  \033[32m{password}",flush=True)
        exit()
    except RuntimeError :
        print("\r\033[K\033[31mRun_Time_Error\033[37m: "+str(password)," "*(aterm()[0]-34-len(str(password))),"[    \033[31mfault\033[37m    ] ",end='',flush=True)
    except zipfile.BadZipFile :
        print("\r\033[K"+str(password)," "*(aterm()[0]-18-len(str(password))),"[     \033[33m#Bad\033[37m    ]",flush=True)
    except zipfile.zlib.error:
        print("\r\033[K"+str(password)," "*(aterm()[0]-18-len(str(password))),"[  \033[33mError zip\033[37m  ]",flush=True)





def number_attack():
    def zero_attack():
        for i in range(1,30):
            try_this(password="0"*i)
    zero_attack()
    global trf
    trf=True
    i=0
    while trf:
        try_this(password=i)
        i=int(i)+1

number_attack()
