# -*- coding: utf-8 -*-
"""app.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1A8LCUsrgxfAFdn9D8u1rcydUrcrjPpt-
"""

import streamlit as st

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
    if a == 0:
        if b == 0: st.success('Phương trình có vô số nghiệm')
        else: st.success('Phương trình vô nghiệm')
    else:
        x = -b/a
        result = "Phương trình có một nghiệm " + str(x)
        st.success(result)
