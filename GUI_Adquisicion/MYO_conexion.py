#Mac: Variable de entorno sdk : export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/macfabian/Documents/sdk/myo.framework
from matplotlib import pyplot as plt
from collections import deque
from threading import Lock, Thread

import myo
import numpy as np
import time


class EmgCollector(myo.DeviceListener):
  """
  Collects EMG data in a queue with *n* maximum number of elements.
  """

  def __init__(self, n):
    print("init_emg")
    self.n = n
    self.lock = Lock()
    self.emg_data_queue = deque(maxlen=n)
    print(self.n)

  def get_emg_data(self):
    print("Get_emg_data")
    with self.lock:
      return list(self.emg_data_queue)

  # myo.DeviceListener

  def on_connected(self, event):
    print("on_connected")
    event.device.stream_emg(True)

  def on_emg(self, event):
    print("on_emg")
    with self.lock:
      self.emg_data_queue.append((event.timestamp, event.emg))


class Plot(object):

  def __init__(self, listener):
    print("init plot")
    self.n = listener.n
    print(self.n)
    self.listener = listener
    self.fig = plt.figure()
    self.axes = [self.fig.add_subplot('81' + str(i)) for i in range(1, 9)]
    [(ax.set_ylim([-100, 100])) for ax in self.axes]
    self.graphs = [ax.plot(np.arange(self.n), np.zeros(self.n))[0] for ax in self.axes]
    plt.ion()

  def update_plot(self):
    print("Update")
    emg_data = self.listener.get_emg_data()
    print("data puro")
    print(emg_data)
    emg_data = np.array([x[1] for x in emg_data]).T
    print("Secont data")
    print(emg_data)
    # for separa los 8 canales del emg
    for g, data in zip(self.graphs, emg_data):
      if len(data) < self.n:
        # Fill the left side with zeroes.
        data = np.concatenate([np.zeros(self.n - len(data)), data])
        print("Dato if")
        print(data)
      g.set_ydata(data)
      print("Dato canal")
      print(g)
      print(data)
    plt.draw()

  def main(self):
    print("maii update")
    while True:
      self.update_plot()
      plt.pause(1.0 / 30)


def main():
  print("main")
  myo.init()
  hub = myo.Hub()
  listener = EmgCollector(512)
  with hub.run_in_background(listener.on_event):
    Plot(listener).main()
    return


if __name__ == '__main__':
  main()