# Image Labeling Tool PyQT5
A tool incorporating labeling, augmenting, training, visualizing images. Currently supporting exporting and training in YOLOv7 and Keypoints RCNN.\
For a similar implementation in Tkinter, try this repo: https://github.com/danFromTelAviv/bounding-box-labeler-yolo
\
##Some demos:
![YOLOLablerDemo1](https://user-images.githubusercontent.com/20887245/234948143-ba3fa97a-faf5-4479-b657-b090a8d6a520.png)
![YOLOLablerDemo2](https://user-images.githubusercontent.com/20887245/234948131-b80115f9-8157-4d34-a3d9-8cd48ca133ea.png)
![YOLOLablerDemo3](https://user-images.githubusercontent.com/20887245/234948114-0a24f7ff-9030-49e2-bab6-b6eae562f9d8.png)

# Functionalities
## Labeling
- Arbitrary changing annotating images and working directory.
- Saving and loading annotations.
- Bounding boxes labeling and keypoints labeling.
- Labels highlighting and removing.
- Zooming and Panning images.
- Navigating in a working directory (prev, next, index jump).
## Exporting and training
- Image Augmentations (Noises, brightness changes, flipping)
- Train/Val/Test Splitting
- Training Control: Model, batch size, learn rate, epochs
- Training Visualization

# Controls

| Actions  | Shortcuts |
| ------------- |:-------------:|
| Zooming      | Control + MouseScroll     |
| Panning      | Control + Drag     |
| Draw Bounding Box      | B     |
| Draw Keypoint      | A     |
| Delete Label    | Del (On selected label)     |
