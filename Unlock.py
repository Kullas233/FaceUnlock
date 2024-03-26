import face_recognition
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import CENTER, X
import keyboard


def lock():
    sec = tk.Tk()
    sec.attributes('-fullscreen',True)
    sec.attributes('-topmost',True)

    label = tk.Label( sec, text="You are locked out", justify=CENTER, font=("Arial", 50), pady=500)
    label.pack()

    def on_closing():
        pass

    sec.protocol("WM_DELETE_WINDOW", on_closing)

    # Get a reference to your webcam 
    video_capture = cv2.VideoCapture(0)
    #video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera

    # Load a sample picture of yourself and learn how to recognize it.
    dylanFace = face_recognition.load_image_file("dylanFace.jpg")
    dylanFace_encoding = face_recognition.face_encodings(dylanFace)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        dylanFace_encoding,
    ]
    known_face_names = [
        "Dylan Kullas"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    keys = []
    stop = False
    process_this_frame = True

    while True:
        sec.update_idletasks()
        sec.update()

        # Grab a frame of the video
        ret, frame = video_capture.read()

        # Resize frame of video to smaller size for faster  processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for name in face_names:
            if(name == "Dylan Kullas"):
                stop = True

        # Display the resulting image
        #cv2.imshow('Video', frame)

        try:  
            if keyboard.is_pressed('a'):  # if key 'q' is pressed 
                keys.append('a')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('b'):  # if key 'q' is pressed 
                keys.append('b')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('c'):  # if key 'q' is pressed 
                keys.clear()
            elif keyboard.is_pressed('d'):  # if key 'q' is pressed 
                keys.append('d')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('e'):  # if key 'q' is pressed 
                keys.append('e')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('f'):  # if key 'q' is pressed 
                keys.append('f')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('g'):  # if key 'q' is pressed 
                keys.append('g')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('h'):  # if key 'q' is pressed 
                keys.append('h')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('i'):  # if key 'q' is pressed 
                keys.append('i')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('j'):  # if key 'q' is pressed 
                keys.append('j')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('k'):  # if key 'q' is pressed 
                keys.append('k')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('l'):  # if key 'q' is pressed 
                keys.append('l')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('m'):  # if key 'q' is pressed 
                keys.append('m')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('n'):  # if key 'q' is pressed 
                keys.append('n')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('o'):  # if key 'q' is pressed 
                keys.append('o')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('p'):  # if key 'q' is pressed 
                keys.append('p')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('q'):  # if key 'q' is pressed 
                keys.append('q')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('r'):  # if key 'q' is pressed 
                keys.append('r')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('s'):  # if key 'q' is pressed 
                keys.append('s')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('t'):  # if key 'q' is pressed 
                keys.append('t')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('u'):  # if key 'q' is pressed 
                keys.append('u')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('v'):  # if key 'q' is pressed 
                keys.append('v')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('w'):  # if key 'q' is pressed 
                keys.append('w')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('x'):  # if key 'q' is pressed 
                keys.append('x')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('y'):  # if key 'q' is pressed 
                keys.append('y')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
            elif keyboard.is_pressed('z'):  # if key 'q' is pressed 
                keys.append('z')
                keys = [i for n, i in enumerate(keys) if i not in keys[:n]]
        except:
            continue
        
        if(''.join(keys) == "qwsdertghyuiklop"):
            return True
                
        if stop:
            video_capture.release()
            cv2.destroyAllWindows()
            return True