"""
Copyright 2020 The OneFlow Authors. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import tensorflow as tf

from oneflow_onnx.x2oneflow.util import load_tensorflow2_module_and_check


def test_softmax():
    class Net(tf.keras.Model):
        def call(self, x):
            m = tf.keras.layers.Softmax()
            x = m(x)
            return x

    load_tensorflow2_module_and_check(Net)


def test_softmax_with_axis():
    class Net(tf.keras.Model):
        def call(self, x):
            m = tf.keras.layers.Softmax(axis=1)
            x = m(x)
            return x

    load_tensorflow2_module_and_check(Net)
