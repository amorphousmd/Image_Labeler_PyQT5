import cv2
import os
import re
import numpy as np

pattern = re.compile(r'\S*\.(mp4|MP4)')
skipFrameNum = 300
frameCnt = 0
segXNum = 3
segYNum = 3

def getVideoName(path, nameList):
    fileList = os.listdir(path)
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isdir(filePath):          #is a dir
            continue
            #getVideoName(filePath, nameList)  #rescursive search
        elif re.match(pattern, file) != None:          #is a video in mp4 format
            nameList.append(filePath)
    return nameList

def videoToFrame(videoName):
    print(videoName)
    cap = cv2.VideoCapture(videoName)
    flag, frame = cap.read()
    global frameCnt
    skipCnt = 0
    width, height = np.shape(frame)[1], np.shape(frame)[0]

    while flag:
        for i in range(segXNum):
            for j in range(segYNum):
                frame2 = frame[j * height // segYNum : (j + 1) * height // segYNum,
                               i * width // segXNum : (i + 1) * width // segXNum] #get ROI
                #第二种写法不支持中文路径
                cv2.imencode('.jpg', frame2)[1].tofile("E:\\traffic\\苏交科视频\\无人机\\image\\" + '{:0>6}'.format(str(frameCnt + 1)) + '.jpg')
                #cv2.imwrite("E:\\traffic\\苏交科视频\\无人机\\image\\" + '{:0>6}'.format(str(frameCnt // skipFrameNum + 1)) + '.jpg', frame)
                frameCnt += 1
        skipCnt += 1
        cap.set(1, skipCnt * skipFrameNum)
        flag, frame = cap.read()
    return

if __name__ == "__main__":
    videoNameList = getVideoName("E:\\traffic\\苏交科视频\\无人机",[])
    print("video Num: %d" %len(videoNameList))
    for video in videoNameList:
        videoToFrame(video)

