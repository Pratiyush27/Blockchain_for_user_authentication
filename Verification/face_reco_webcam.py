import numpy as np
import face_recognition as fr
import cv2


Abel_image = fr.load_image_file("Abel.jpg")
Abel_face_encoding = fr.face_encodings(Abel_image)[0]

known_face_encondings = [Abel_face_encoding]
known_face_names = ["Abel"]

i=3
name = "Unknown"
while True: 
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = fr.compare_faces(known_face_encondings, face_encoding)

        face_distances = fr.face_distance(known_face_encondings, face_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Webcam_facerecognition', frame)
    if name == 'Abel':
        cv2.waitKey(1360)
        print("Match")
        val="Match"
        break
    else :
        print("Mismatch\nChance left: " + str(i) + "\n")
        cv2.waitKey(1360)
        val="Mismatch"
        i=i-1
        video_capture.release()
        cv2.destroyAllWindows()

    if i==0:
        break
    	    
    	  	
video_capture.release()
cv2.destroyAllWindows()


