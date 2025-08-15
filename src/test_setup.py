import tensorflow as tf
import cv2
import numpy as np

print("TensorFlow version:", tf.__version__)
print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)
print("✅ All imports successful!")

# Test TensorFlow
print("TensorFlow test:", tf.reduce_sum(tf.random.normal([1000, 1000])))