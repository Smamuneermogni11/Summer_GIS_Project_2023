import cv2

# Load the pre-trained models for face and object detection
face_net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
object_net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection
    face_blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_net.setInput(face_blob)
    face_detections = face_net.forward()

    for i in range(face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        if confidence > 0.5:
            box = face_detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (x, y, w, h) = box.astype(int)
            cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Object detection
    object_blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    object_net.setInput(object_blob)
    object_detections = object_net.forward()

    for i in range(object_detections.shape[2]):
        confidence = object_detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(object_detections[0, 0, i, 1])
            class_name = class_names[class_id]
            box = object_detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (x, y, w, h) = box.astype(int)
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow('Face and Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
