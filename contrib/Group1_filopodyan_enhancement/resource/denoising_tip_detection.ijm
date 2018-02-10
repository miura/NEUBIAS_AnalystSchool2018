
var CollageCh = 4;		// channel of interest 
var tubenessSigma = 0.2;	// sigma is used both for tubeness and OrientationJ, it is based on the evaluation of the maximum of coherence determined by
						// Orientation J Dominant Direction 
var ResultsSubFolder = "Results";
var fileExtention = ".tif";

directory = getDirectory("Open Image folders");
resFolder = directory + ResultsSubFolder + File.separator; 
File.makeDirectory(resFolder);
print("inDir=",directory," outDir=",resFolder);

setBatchMode(true);
ProcessFiles(directory, resFolder);



function ProcessFiles(directory, resFolder) {
	fileListArray = getFileList(directory);
	for (fileIndex = 0; fileIndex < lengthOf(fileListArray); fileIndex++) {
		if (endsWith(fileListArray[fileIndex], fileExtention)) {
			open(directory+fileListArray[fileIndex]);	
			ProcessFile(directory, resFolder);
			run("Close All");
		} 
	} 
} 

function ProcessFile(directory, resFolder) {
	y=getHeight;
	x=getWidth;
	z=nSlices;
	print(x,y,z);
	origStack=getTitle();
	for(i=0; i<nSlices; i++){
		num=toString(i+1);
		selectWindow(origStack);
		setSlice(i+1);
		//Stack.setSlice(i);
		print(i);
		run("Duplicate...", "title=curSlice");
		selectWindow("curSlice");
		run("Subtract Background...", "rolling=5");
		run("Tubeness", "sigma="+tubenessSigma+" use");
    	selectWindow("tubeness of curSlice");
		run("Duplicate...", "truc"+i);   // Do not remove this line !!
		selectWindow("curSlice");
		run("Close");
		selectWindow("tubeness of curSlice");
		run("Close");
		selectWindow(origStack);
//		Stack.setSlice(i+1);
//		setSlice(i+1);
	}
	waitForUser;
	run("Images to Stack", "name=[Filter] title=curSlice use");
	saveAs("Tiff", resFolder+origStack);
	//run("Close All");
}	


