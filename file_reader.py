import image_pb2
import sys
import os
from pathlib import Path

dir_path = "./images/"

def ListImageIds(person):
    print(person.name)
    for image in person.images:
        print(image.name)

def getImage(person, image):
    for person_file in os.listdir(dir_path):
        if os.path.isfile(Path(dir_path+person_file)) and person_file == person+".pid":
            f = open(Path(dir_path+person_file), "rb")
            p = image_pb2.Person()
            p.ParseFromString(f.read())
            f.close()
            for i in p.images:
                if i.name == image:
                    return i

#for file in os.listdir(dir_path):
#    if (file.endswith(".pid")):
#        f = open(Path(dir_path+file), "rb")
#        person = image_pb2.Person()
#        person.ParseFromString(f.read())
#        f.close()
#        ListImageIds(person)

x = getImage("Henk","0004_01.jpg")
f = open(Path(dir_path+"maurice1.jpg"),"wb")
f.write(x.contents)
f.close()