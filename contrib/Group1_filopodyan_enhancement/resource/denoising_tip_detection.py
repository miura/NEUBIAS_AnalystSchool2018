from ij import IJ, ImageStack, ImagePlus
from ij.plugin import Duplicator
import os

#@File(label="Open Image folders", style="directory") directory
#@Double(value=0.2) tubenessSigma
#@Double(value=5) rollingBallSize

duplicator = Duplicator()
def processSlice(frame):
	IJ.run(frame, "Subtract Background...", "rolling="+str(rollingBallSize));
	IJ.run(frame, "Tubeness", "sigma="+ str(tubenessSigma)+ " use");
	processed = IJ.getImage();
	processor = processed.getProcessor()
	processed.close()
	return processor

def ProcessImg(img):
	w = img.getDimensions()[0]
	h = img.getDimensions()[1]
	t = img.getDimensions()[-1]
	stack = ImageStack(w,h)
	for i in range(1, t+1):
		img.setSlice(i)
		imp2 = duplicator.run(img, i, i);
		stack.addSlice(str(i),processSlice(imp2))
	return stack

def ProcessFiles(directory):
	for r,ds,fs in os.walk(str(directory)):
		for f in fs:
			if f.endswith(extension):
				imp = IJ.openImage(r + os.sep + f)
				imp.show()
				stack = ProcessImg(imp)
				newimp = ImagePlus("newImage" + f, stack)
				newimp.show()

ProcessFiles(str(directory));