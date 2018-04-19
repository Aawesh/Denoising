# from datetime import datetime
#
# # fmt = '%Y-%m-%d %H:%M:%S'
# fmt = '%b %d, %Y %I:%M:%S %p'
# # d1 = datetime.strptime('2010-01-01 16:31:22', fmt)
# # d2 = datetime.strptime('2010-01-03 20:15:14', fmt)
#
# d1 = datetime.strptime('Jul 15, 2017 1:36:47 PM', fmt)
# d2 = datetime.strptime('Jul 15, 2017 1:37:29 PM', fmt)
#
# diff = d2-d1
# print diff
# print diff.seconds
# diff_minutes = diff.seconds/60.0
# print diff_minutes
#
# print

#!python

from numpy import cos, sin, pi, absolute, arange
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
import pandas as pd
import matplotlib.pyplot as plt



def read_data(file_path):
    column_names = ['speed', 'acc_x', 'acc_y', 'acc_z', 'acc_mag', 'gyro_x', 'gyro_y', 'gyro_z',"gyro_mag"]
    data = pd.read_csv(file_path, header=None, names=column_names)
    return data


#------------------------------------------------
# Create a signal for demonstration.
#------------------------------------------------

N_SIZE = 450

dataset = read_data('./data/final.csv')

acc_x = dataset['acc_x'].tolist();
acc_y = dataset['acc_y'].tolist();
acc_z = dataset['acc_z'].tolist();
acc_mag = dataset['acc_mag'].tolist();

gyro_x = dataset['gyro_x'].tolist();
gyro_y = dataset['gyro_y'].tolist();
gyro_z = dataset['gyro_z'].tolist();
gyro_mag = dataset['gyro_mag'].tolist();


sample_rate = len(dataset)/600.0

#------------------------------------------------
# Create a FIR filter and apply it to x.
#------------------------------------------------

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0
print nyq_rate

# The desired width of the transition from pass to stop,
# relative to the Nyquist rate.  We'll design the filter
# with a 5 Hz transition width.
width = 5.0/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 60.0

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_hz = 12

# Use firwin with a Kaiser window to create a lowpass FIR filter.
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

# Use lfilter to filter x with the FIR filter.
filtered_acc_x = lfilter(taps, 1.0, acc_x)
filtered_acc_y = lfilter(taps, 1.0, acc_y)
filtered_acc_z = lfilter(taps, 1.0, acc_z)
filtered_acc_mag = lfilter(taps, 1.0, acc_mag)

filtered_gyro_x = lfilter(taps, 1.0, gyro_x)
filtered_gyro_y = lfilter(taps, 1.0, gyro_y)
filtered_gyro_z = lfilter(taps, 1.0, gyro_z)
filtered_gyro_mag = lfilter(taps, 1.0, gyro_mag)

delay = 0.5 * (N-1) / sample_rate


# figure(1)
# plot(acc_x[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_acc_x[1:N_SIZE],'g-',linewidth=1)
#
# figure(2)
# plot(acc_y[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_acc_y[1:N_SIZE],'b-',linewidth=1)
#
# figure(3)
# plot(acc_z[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_acc_z[1:N_SIZE],'y-',linewidth=1)
#
# figure(4)
# plot(acc_mag[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_acc_mag[1:N_SIZE],'p-',linewidth=1)
# grid(True)
# show()
#
# figure(5)
# plot(gyro_x[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_gyro_x[1:N_SIZE],'g-',linewidth=1)
#
# figure(6)
# plot(gyro_y[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_gyro_y[1:N_SIZE],'b-',linewidth=1)
#
# figure(7)
# plot(gyro_z[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_gyro_z[1:N_SIZE],'y-',linewidth=1)
#
# figure(8)
# plot(gyro_mag[1:N_SIZE],'r-',linewidth=1)
# plot(filtered_gyro_mag[1:N_SIZE],'p-',linewidth=1)
# grid(True)
# show()

plt.suptitle("Acceleration vs time")

plt.subplot(221)
plt.plot(acc_x[1:N_SIZE],'r-',linewidth=1,label="raw_acc_x")
plt.plot(filtered_acc_x[1:N_SIZE],'b-',linewidth=1,label="filtered_acc_x")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration(m/s^2)")
plt.grid()
plt.legend()

plt.subplot(222)
plt.plot(acc_y[1:N_SIZE],'r-',linewidth=1,label = "raw_acc_y")
plt.plot(filtered_acc_y[1:N_SIZE],'b-',linewidth=1,label = "filtered_acc_y")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration(m/s^2)")
plt.grid()
plt.legend()


plt.subplot(223)
plot(acc_z[1:N_SIZE],'r-',linewidth=1,label = "raw_acc_z")
plot(filtered_acc_z[1:N_SIZE],'b-',linewidth=1,label="filtered_acc_z")
plt.xlabel("Time(s)")            
plt.ylabel("Acceleration(m/s^2)")
plt.grid()
plt.legend()

plt.subplot(224)
plot(acc_mag[1:N_SIZE],'r-',linewidth=1,label="raw_acc_magnitude")
plot(filtered_acc_mag[1:N_SIZE],'b-',linewidth=1,label="filtered_acc_magnitude")
plt.xlabel("Time(s)")            
plt.ylabel("Acceleration(m/s^2)")
plt.grid()
plt.legend()


plt.show()




plt.subplot(221)
plot(gyro_x[1:N_SIZE],'r-',linewidth=1,label="raw_gryo_x")
plot(filtered_gyro_x[1:N_SIZE],'g-',linewidth=1,label="filtered_gyro_x")
plt.xlabel("Time(s)")
plt.ylabel("Rate of rotation(rad/s)")
plt.grid()
plt.legend()

plt.subplot(222)
plot(gyro_y[1:N_SIZE],'r-',linewidth=1,label = "raw_gyro_y")
plot(filtered_gyro_y[1:N_SIZE],'g-',linewidth=1,label="filtered_gyro_y")
plt.xlabel("Time(s)")
plt.ylabel("Rate of rotation(rad/s)")
plt.grid()

plt.legend()

plt.subplot(223)
plt.grid()
plot(gyro_z[1:N_SIZE],'r-',linewidth=1,label = "raw_gyro_z")
plot(filtered_gyro_z[1:N_SIZE],'g-',linewidth=1,label="filtered_gyro_y")
plt.xlabel("Time(s)")
plt.ylabel("Rate of rotation(rad/s)")
plt.legend()

plt.subplot(224)
plot(gyro_mag[1:N_SIZE],'r-',linewidth=1,label = "normalized_gyro_magniude")
plot(filtered_gyro_mag[1:N_SIZE],'g-',linewidth=1,label="normalized_gyro_magnitude")
plt.xlabel("Time(s)")
plt.ylabel("Rate of rotation(rad/s)")
plt.grid()    
plt.legend()  

plt.show()


