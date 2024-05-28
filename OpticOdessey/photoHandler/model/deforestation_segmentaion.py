# -*- coding: utf-8 -*-
"""deforestation_segmentaion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UV_QwgQTjNBngK9knuJZQn2yzDM0JKCF

Pretrained model link to Google Drive: https://drive.google.com/file/d/1Z0oIc3lc7VFNDclUnOTma2eZg4UTJmBg/view?usp=sharing

Import libs
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image

from load_model import get_model


def decode_png(path_to_image):
    image = tf.io.read_file(path_to_image)
    image = tf.io.decode_png(image)

    return image[np.newaxis, ...]


def predict(model, image):
    prediction = model.predict(image)
    prediction_class1 = np.copy(prediction[..., 0]) # Forest
    prediction_class2 = np.copy(prediction[..., 1]) # Deforest
    prediction[..., 0] = prediction_class2 # RED - Deforest
    prediction[..., 1] = prediction_class1 # GREEN - Forest

    return prediction[0]


PATH_TO_MODEL = "/content/drive/MyDrive/datasets/U6_E 1201-F1 0.7134-IOU 0.6555.h5"
PATH_TO_IMAGE = "/content/drive/MyDrive/datasets/image.png"
PATH_TO_SAVE_IMAGE = "/content/name.png"

model = get_model()

#model.load_weights(PATH_TO_MODEL)

""" image = decode_png(PATH_TO_IMAGE)

prediction = predict(model, image)

matplotlib.image.imsave(PATH_TO_SAVE_IMAGE, prediction) # save image to disk

# Show result
plt.imshow(prediction) """