import os
from sklearn.model_selection import train_test_split

if not os.path.exists("./AugmentedImages"):
    os.makedirs("./AugmentedImages")

dict_data = {'1.jpg': {'0': [(298.15, 178.38, 40.23, 47.44)],
                       '1': [(212.66, 211.82, 68.65, 67.82),
                             (170.37, 48.56, 27.25, 27.48),
                             (415.18, 259.62, 11.2, 10.82),
                             (166.74, 258.06, 12.46, 11.23)]},
             '2.jpg': {'0': [(207.64, 119.56, 101.47, 145.68),
                             (45.55, 97.79, 84.73, 107.17),
                             (943.75, 106.25, 84.03, 114.58)],
                       '1': [(761.0, 136.48, 96.45, 133.58)],
                       '2': [(928.82, 744.6, 102.72, 98.86)]},
             '3.jpg': {'0': [(149.17, 570.0, 210.83, 222.5)],
                       '1': [(633.33, 682.5, 295.0, 266.67)],
                       '2': [(962.5, 782.5, 256.67, 265.0)]}}

sizes = {'1.jpg': {'_size': [640, 480]},
         '2.jpg': {'_size': [1200, 900]},
         '3.jpg': {'_size': [2048, 1152]}}

normalized_dict = {}
for filename, annotations in dict_data.items():
    size = sizes[filename]['_size']
    width, height = size[0], size[1]
    normalized_annotations = {}
    for label, bboxes in annotations.items():
        normalized_bboxes = []
        for bbox in bboxes:
            x, y, w, h = bbox
            x_normalized = x / width
            y_normalized = y / height
            w_normalized = w / width
            h_normalized = h / height
            normalized_bbox = (x_normalized, y_normalized, w_normalized, h_normalized)
            normalized_bboxes.append(normalized_bbox)
        normalized_annotations[label] = normalized_bboxes
    normalized_dict[filename] = normalized_annotations

print(normalized_dict)

# Set the numbers of images for train, val, and test sets
train_size = 1
val_size = 1
test_size = 1

# Get the list of image names from normalized_dict
image_names = list(normalized_dict.keys())

# Split the image names into train, val, and test sets
train_images, val_test_images = train_test_split(image_names, train_size=train_size, test_size=val_size+test_size)
val_images, test_images = train_test_split(val_test_images, train_size=val_size, test_size=test_size)

# Create the train_normalized_dict, val_normalized_dict, and test_normalized_dict
train_normalized_dict = {img_name: normalized_dict[img_name] for img_name in train_images}
val_normalized_dict = {img_name: normalized_dict[img_name] for img_name in val_images}
test_normalized_dict = {img_name: normalized_dict[img_name] for img_name in test_images}

print(train_normalized_dict)
print(val_normalized_dict)
print(test_normalized_dict)

for img_name, bboxes in normalized_dict.items():
    with open(os.path.join("./AugmentedImages", f"{img_name.split('.')[0]}.txt"), "w") as f:
        for label, boxes in bboxes.items():
            for box in boxes:
                x, y, w, h = box
                f.write(f"{label} {x} {y} {w} {h}\n")
