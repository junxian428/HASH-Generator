
import hashlib
import base64
import tkinter
import tkinter.messagebox
from tkinter import *


global x1, x2


top = tkinter.Tk()


message1 = tkinter.Message(top,text="Options :")
message1.place(x=370,y=80)
message2 = tkinter.Message(top,text="Insert Encrypted Number :")
message2.place(x=360,y=180)
message3 = tkinter.Message(top, text='After HASH$ :')
message3.place(x=100, y=150)


top.geometry("500x300")
Lb1 = Listbox(top)
Lb1.insert(1, "1. MD5")
Lb1.insert(2, "2. SHA1")
Lb1.insert(3, "3. SHA3_224")
Lb1.insert(4, "4. SHA256")
Lb1.insert(5, "5. SHA3_384")
Lb1.insert(6, "6. SHA512")
Lb1.insert(7, "7. BASE64")

Lb1.pack(side=TOP)


E1 = Entry(top, bd =5)
E1.place(x=370,y=100)
E2 = Entry(top, bd =5)
E2.pack(side = RIGHT)
def encryption():
    x1 = E1.get()
    x2 = E2.get()
    if x1 == '1':
       hash_object1 = hashlib.md5(str(x2).encode('utf-8'))
       message4 = tkinter.Message(top, text='MD5:\n' + hash_object1.hexdigest() )
       message4.place(x=50, y=200)

    elif x1 == '2':
        hash_object2 = hashlib.sha1(str(x2).encode('utf-8'))
        message4 = tkinter.Message(top, text='SHA1:\n' + hash_object2.hexdigest())
        message4.place(x=50, y=200)
    elif x1 == '3':
        hash_object3 = hashlib.sha224(str(x2).encode('utf-8'))
        message4 = tkinter.Message(top, text='SHA224:\n' + hash_object3.hexdigest())
        message4.place(x=50, y=200)
    elif x1 == '4':
        hash_object4 = hashlib.sha256(str(x2).encode('utf-8'))
        message4 = tkinter.Message(top, text='SHA256:\n' + hash_object4.hexdigest())
        message4.place(x=50, y=200)
    elif x1 == '5':
        hash_object5 = hashlib.sha384(str(x2).encode('utf-8'))
        message4 = tkinter.Message(top, text='SHA384:\n' + hash_object5.hexdigest())
        message4.place(x=50, y=200)
    elif x1 == '6':
        hash_object6 = hashlib.sha512(str(x2).encode('utf-8'))
        message4 = tkinter.Message(top, text='SHA512:\n' + hash_object6.hexdigest())
        message4.place(x=50, y=200)

    elif x1 == '7':
        res = bytes(x2, 'utf-8')
        encode = base64.b64encode(res)
        message4 = tkinter.Message(top, text='BASE64:\n' + str(encode))
        message4.place(x=50, y=200)

    else:
        message4 = tkinter.Message(top, text='Invalid Syntax')
        message4.place(x=50, y=200)

tkinter.Button(top, text="Conversion", command=encryption).place(x=200,y=250)
top.mainloop()




#print('Encryptor\n')
#raw = input("Enter the content you want to encrypt :")

#hash_object5 = hashlib.md5(str(raw).encode('utf-8'))
#print('md5', hash_object5.hexdigest())
#hash_object3 = hashlib.sha1(str(raw).encode('utf-8'))
#print('SHA1', hash_object3.hexdigest())
#hash_object2 = hashlib.sha3_224(str(raw).encode('utf-8'))
#print('SHA3_224', hash_object2.hexdigest())
#hash_object1 = hashlib.sha256(str(raw).encode('utf-8'))
#print('SHA256', hash_object1.hexdigest())
#hash_object6 = hashlib.sha3_384(str(raw).encode('utf-8'))
#print('SHA3_384', hash_object6.hexdigest())
#hash_object4 = hashlib.sha3_512(str(raw).encode('utf-8'))
#print('SHA3_512', hash_object4.hexdigest())








