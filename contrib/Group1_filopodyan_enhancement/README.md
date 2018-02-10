# Group 1 members :<br> 
Dyankova Teodora ([dyankova@bio21.bas.bg](dyankova@bio21.bas.bg), Bulgaria)<br>
Molodij Guillaume ([guillaume.molodij@weizmann.ac.il](guillaume.molodij@weizmann.ac.il), Israel)<br>
Huang, Ziqiang ([ziqiang.huang@cruk.cam.ac.uk](ziqiang.huang@cruk.cam.ac.uk), United Kingdom)<br>
Šoštar Marko ([msostar@irb.hr](msostar@irb.hr), Croatia)<br>
LI Tong ([tongli.bioinfo@gmail.com](tongli.bioinfo@gmail.com), France)<br>

Briefly, we use a [rolling ball denoising method](https://imagej.net/Rolling_Ball_Background_Subtraction) to remove the cell body noisy background and enhance the tubular-like signals with [tubeness plugin](https://www.longair.net/edinburgh/imagej/tubeness/) in Fiji.<br>
The following image shows the differences between Filopodyan(left) and our method (right).
![][processed]
### __Bad thing that we did and you should not do this__:
Create a binary mask from the enhanced filopodia detection and filter it on the original image to keep signals only inside the mask.<br>
Then use [Trackmate](https://imagej.net/TrackMate) to detect dots inside this region (this can be very slow). <br>
The reason you __should not do__ this is because we used the LoG detector for dot-like signal detection and it is very sensitive to the edge also. Thus, in the end, all detected signals are located at the mask border but not inside the filopodia.<br>
### __The good way to do this__ <br>
is to use Trackmate to detection dots first and then keep only the ones inside the mask with custom script.

In the [resource folder](resource), you can find denoising script (ij1 macro and Python version) and some methods to convert Trackmate XML output to pandas dataframe for further analysis in python.
[processed]: resource/processed.png