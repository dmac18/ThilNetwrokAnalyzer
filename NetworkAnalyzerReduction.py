import scipy
import skrf as rf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob
import os
import math


print('Enter the filepath containing the Network analyzer files')
Filepath = input();

os.chdir(Filepath);

extension = 's4p'

allFiles = [i for i in glob.glob('*.{}'.format(extension))];

dfallFiles = pd.Series(allFiles)

print(dfallFiles)

numFiles = len(allFiles)

print(numFiles)

for file in dfallFiles:
  data = rf.Network(str(file))
  port_s11 = data.s11.s_re
  arr_port_s11 = np.array(port_s11)
  port_s21 = data.s21.s_re
  arr_port_s21 = np.array(port_s21)
  port_s31 = data.s31.s_re
  arr_port_s31 = np.array(port_s31)
  port_s41 = data.s41.s_re
  arr_port_s41 = np.array(port_s41)
  port_s11_im = data.s11.s_im
  arr_im_port_s11 = np.array(port_s11_im)
  port_s21_im = data.s21.s_im
  arr_im_port_s21 = np.array(port_s21_im)
  port_s31_im = data.s31.s_im
  arr_im_port_s31 = np.array(port_s31_im)
  port_s41_im = data.s41.s_im
  arr_im_port_s41 = np.array(port_s41_im)
  s11 = np.sqrt((arr_port_s11**2)+(arr_im_port_s11**2))
  s21 = np.sqrt((arr_port_s21**2)+(arr_im_port_s21**2))
  s31 = np.sqrt((arr_port_s31**2)+(arr_im_port_s31**2))
  s41 = np.sqrt((arr_port_s41**2)+(arr_im_port_s41**2))
  THil_calc = -10 * np.log10(s11 + s21 + s31 + s41)
  Thil = THil_calc.ravel()
  portFreq = data.f
  print(Thil)
  THilData = list(Thil)
  plt.plot(portFreq,THilData)
  plt.show()
    
