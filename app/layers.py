# Custom L1 Distance Layer Module
# Why do we need this: it's needed to load the custom model (ie. .h5 file)

# Import dependencies
import tensorflow as tf
from tensorflow.keras.layers import Layer

# Custom L1 Distance Layer from our Jupyter notebook
class L1Dist(Layer):
    
    # Init method - inheritance
    def __init__(self, **kwargs):
        super().__init__()
        
    # Magic happens here - similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)