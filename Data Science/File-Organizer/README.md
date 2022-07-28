# File organizer and picture processing  

This project is about automating a managing process  
It has one notebook and one python script  
<h1>Python script</h1>
Code <a href="https://github.com/federoccco/Start2Impact/blob/main/Data%20Science/File-Organizer/addfile_v2.py">HERE</a>
It will automatically manage files based on their extension by putting them in the related folder 
(e.g. "Audio" folder if the extension is    .mp3, .wma and so on) if the folder doesn't exist, 
the script will automatically create it and then move the file, this will be done for audio, 
text and images files if  the file extension is supported    
<br>
<br> 
  To correctly use the script do the following:
<ol>
<br>
  <li>
    Open any cmd:
<br>
<br>
    <img src="readme images\1.PNG">
  </li>
  <br>
  <li>
    Type <i>cd</i> followed by the path where the python file is located:
    <br>
    <br>
    <img src="readme images\2.PNG">
  </li>
  <br>
  <li>
    You should have a folder full of files of any extension like this
    <br>
    <br>
    <img src="readme images\files.PNG">
  </li>
  <br>
  <li>
    Type the name of the python file and the name of the file you want to move:
  <br>
  <br>
    <img src="readme images\3.PNG">
  </li>
  <br>
  <li>
    You should get something like this
  <br>
  <br>
    <img src="readme images\4.PNG">
  </li>
  <br>
  <li>
    And the file folder will be created (if not existant) and the file moved in
  <br>
  <br>
    <img src="readme images\folder.PNG">
    <img src="readme images\image.PNG">
  </li>
</ol>
<br>
<h1> Notebook Part 1</h1>

Full code <a href="https://nbviewer.org/github/federoccco/Start2Impact/blob/main/Data%20Science/File-Organizer/fileorganizer_v2.ipynb">HERE</a>
<br>
It's the same concept of the above python script with the only difference that 
it will move all the files at once without having to specify an argument, just call 
the python file name and it will immediately move every file.  
<h1> Notebook Part 2</h1>
Images are just pixels, the more they are the more the image has a high resolution. 
A gray scale image is made by a 2x2 matrix with width and height equal to its resolution. 
Every pixel has a value from 0 to 255. 
<br>
<br>
A colored image its a 2x2 matrix with pixels that has 3 values each i.e. (0, 0, 0) or (255, 255, 255)
Each of this value represent one level of color: <i style="color:#ff6363;">Red</i>, <i style="color:turquoise;">Blue</i> and <i style="color:lightgreen;">Green</i> (RGB)
<br>
<hr>
In this part the script will process the images moved into the Images folder created with the part 1 of the notebook. Then it will process them and it will return:
<br>
<br>
<ul>
<li>
Name: The name of the image without the extension
</li>
<li>
Height: The number of pixels vertically
</li>
<li>
Width: The number of pixels horizontally
</li>
<li>
Grayscale: If gray the mean value of the pixels (0-255), else 0
</li>
<li>
R: The mean value of reds if colored image else 0
</li>
<li>
G: The mean value of greens if colored image else 0
</li>
<li>
B: The mean value of blues if colored image else 0
</li>
<li>
ALPHA: The mean value of the alpha channel if present, else 0
</li>
<br>
It should look like something like this:
<br>
<br>
<img src="readme images\table.PNG">






