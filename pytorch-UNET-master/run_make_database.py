import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

##
dir_data = r'C:\Users\daans\OneDrive\Documenten\TU Delft\Master\Jaar 1\Periode 4\Seminar Computer Vision by Deep Learning\Project_deep_learning_U_net\pytorch-UNET-master\data\em'


name_target = 'train-labels.tif'
name_data = 'train-volume.tif'

img_target = Image.open(os.path.join(dir_data, name_target))
img_data = Image.open(os.path.join(dir_data, name_data))

ny, nx = img_target.size
nframe = img_target.n_frames

##
nframe_train = 24   # The number of training set
nframe_val = 3      # The number of validation set
nframe_test = 3     # The number of test set

dir_save_train = os.path.join(dir_data, 'train')
dir_save_val = os.path.join(dir_data, 'val')
dir_save_test = os.path.join(dir_data, 'test')

if not os.path.exists(dir_save_train):
    os.makedirs(dir_save_train)

if not os.path.exists(dir_save_val):
    os.makedirs(dir_save_val)

if not os.path.exists(dir_save_test):
    os.makedirs(dir_save_test)

##
id_frame = np.arange(nframe)
np.random.shuffle(id_frame)

##
offset_nframe = 0

for i in range(nframe_train):
    img_target.seek(id_frame[i + offset_nframe])
    img_data.seek(id_frame[i + offset_nframe])

    target_ = np.asarray(img_target)
    data_ = np.asarray(img_data)

    np.save(os.path.join(dir_save_train, "input_%03d.npy" % i), (data_))
    np.save(os.path.join(dir_save_train, "label_%03d.npy" % i), (target_))

##
offset_nframe = nframe_train

for i in range(nframe_val):
    img_target.seek(id_frame[i + offset_nframe])
    img_data.seek(id_frame[i + offset_nframe])

    target_ = np.asarray(img_target)
    data_ = np.asarray(img_data)

    np.save(os.path.join(dir_save_val, "input_%03d.npy" % i), (data_))
    np.save(os.path.join(dir_save_val, "label_%03d.npy" % i), (target_))

##
offset_nframe = nframe_train + nframe_val

for i in range(nframe_test):
    img_target.seek(id_frame[i + offset_nframe])
    img_data.seek(id_frame[i + offset_nframe])

    target_ = np.asarray(img_target)
    data_ = np.asarray(img_data)

    np.save(os.path.join(dir_save_test, "input_%03d.npy" % i), (data_))
    np.save(os.path.join(dir_save_test, "label_%03d.npy" % i), (target_))

##
plt.subplot(121)
plt.imshow(target_)

plt.subplot(122)
plt.imshow(data_)

plt.show()