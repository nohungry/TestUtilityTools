import cv2

EXTRACT_FREQUENCY = 50

def extract_frames(inputfile, outputfolder, index=1):
    extract_frequency = 50
    videofile = cv2.VideoCapture(inputfile)
    count = 1
    while True:
        rval, frame = videofile.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            fileName = "{}/testImage{:>03d}.jpg".format(outputfolder, index)
            cv2.imwrite(fileName, frame)
            index += 1
        if index >= 501:
            break
        count += 1
    videofile.release()
    print("Total save {} pics".format(index-1))