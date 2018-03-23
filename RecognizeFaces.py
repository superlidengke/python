import shutil

import face_recognition
import os

class RecognizeFaces:
    def separateFaces(self,standard_face_path,faces_directory,desti):
        # Load the images files into numpy arrays
        standard_face = face_recognition.load_image_file(standard_face_path)
        standard__face_encoding = face_recognition.face_encodings(standard_face)[0]
        for subdir, dirs, files in os.walk(faces_directory):
            for image_file in files:
                image_path = os.path.join(faces_directory,image_file)
                print(image_file)
                unknown_image = face_recognition.load_image_file(os.path.join(faces_directory,image_file))
                unknown_face_encoding_list = face_recognition.face_encodings(unknown_image)
                unknown_face_encoding = None
                if len(unknown_face_encoding_list)>0:
                    unknown_face_encoding = unknown_face_encoding_list[0]
                else:
                    print('can not found face')
                    continue
                results = face_recognition.compare_faces([standard__face_encoding], unknown_face_encoding)
                print(results)
                if results[0]:
                    shutil.copyfile(image_path,os.path.join(dest_path,'same/%s' % image_file))
                else:
                    shutil.copyfile(image_path,os.path.join(dest_path,'others/%s' % image_file))

recongizeFaces = RecognizeFaces()
s_path = r"C:\temp\video\faces\faces\frame008_f01.jpg"
faces_path = r"C:\temp\video\faces\faces"
dest_path = r"C:\temp\video\faces\separate/"
recongizeFaces.separateFaces(s_path,faces_path,dest_path)