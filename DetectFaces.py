from PIL import Image
import face_recognition
import os

class DetectFace:

    def detect_face(self,imagePath):
        """return a list containing faces numpy.ndarray, it's a 3d matrix, row,column, every pix is r,g,b values"""
        image = face_recognition.load_image_file(imagePath)
        # Find all the faces in the image using the default HOG-based model.
        # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
        face_locations = face_recognition.face_locations(image)
        faces = []
        for face_location in face_locations:
            top, right, bottom, left = face_location
            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]  #< type 'numpy.ndarray'>
            faces.append(face_image)
        return faces

    def detct_face_save(self,imagePath,desti):
        imageName = os.path.splitext(os.path.basename(imagePath))[0]
        faces = self.detect_face(imagePath)
        index = 0
        for face in faces:
            pil_image = Image.fromarray(face)
            pil_image.save(desti+'%s_f%02d.jpg' % (imageName,index))
            index += 1



