import streamlit as st
import numpy as np
import pandas as pd
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

#loading the model
model=Sequential()
model.load_model('model.json')