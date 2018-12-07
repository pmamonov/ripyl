import csv
import numpy as np
import ripyl.streaming as stream
import ripyl.protocol.usb as usb
import ripyl.util.plot as rplot
from collections import OrderedDict

def read_csv(fn, n):
	T = 0.
	d = np.zeros(n)

	with open(fn, 'rb') as f:
		c = csv.reader(f)
		i = 0
		for r in c:
			d[i] = float(r[1])
			if i == 0:
				t0 = float(r[0])
			if i == 1:
				t1 = float(r[0])
			i += 1
			if i >= n:
				break

	T = t1 - t0
	return d, T

def usb_decode(d, T, lvl=(-.2, .2)):
	ss = stream.samples_to_sample_stream(d, T)
	r = usb.usb_diff_decode(ss, logic_levels=lvl)
	return list(r)

def plot(r, d, T):
	ss = stream.samples_to_sample_stream(d, T)
	plotter = rplot.Plotter()
	plotter.plot(OrderedDict([('D+ - D-, V', ss)]),	r, "",
			label_format=stream.AnnotationFormat.String)
