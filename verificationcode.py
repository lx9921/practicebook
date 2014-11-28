import uuid
f=open('d:/uuid1.txt','w')

for a in range(200):
    a=str(uuid.uuid4())+'\n'
    print a
    f.write(str(a))
f.close()

