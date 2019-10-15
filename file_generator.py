import os
import sys
import image_pb2
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description = 'Face Recognition using Triplet Loss')
parser.add_argument('--image-dir', default = '/scratch/nodespecific/int1/mhouben/cifar_sorted_by_label/train/', type = str,
                    help = 'path to image directory')
parser.add_argument('--destination-dir', default = '/lustre2/0/wsdarts/datasets/cifar/train/', type = str,
                    help = 'path to destination directory, where .pid files will be placed')                    
args    = parser.parse_args()
dir_path = args.image_dir
destination_path = args.destination_dir
print(destination_path)

for person_dir in os.listdir(dir_path):
    print(person_dir)
    person_path = Path(dir_path + person_dir)
    if os.path.isdir(person_path):
        person = image_pb2.Person()
        person.name = person_dir
        for person_image in os.listdir(person_path):
            if (person_image.endswith(".png") or person_image.endswith(".jpg")):
                print(person_image)
                image = person.images.add()            
                person_image_path = person_path.joinpath(person_image)
                file = open(person_image_path, "rb")
                image.contents = file.read()
                image.name = person_image
                file.close()
            
        person_filename = Path(destination_path + person.name + ".pid")
        print(person_filename)
        out_file = open(person_filename, "wb")
        out_file.write(person.SerializeToString())
        out_file.close()
