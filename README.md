# DepthMap_dataset

pby_script is a Python Blender script for creating large numbers of randomized 3d scenes and corresponding sets of stereoscopic images and depth maps, for machine learning and computer vision. Everything is configurable, from the camera convergence plane or interocular distance and focus length to the color and shapes of the randomized object.

Blender is a open source 3D graphics and animation software, downloadable at "https://www.blender.org/". 

Example scene:

![alt tag](https://raw.github.com/LouisFoucard/DepthMap_dataset/master/StereoImages/Stereoscopic_195.png)

and corresponding Depth map:

![alt tag](https://raw.github.com/LouisFoucard/DepthMap_dataset/master/Depth_map/DepthMap_195.png)

Intallation:

-Download the latest blender build (script was tested on v2.72), install and open blender.

Either open with blender the .blend file in the "blender file" folder, or ,alternatively, do the following:

-Change the display button on the bottom left (represented by a cube symbol, left of the view menu) to text editor.

-Click new, then simply paste the contents of pby_script.

Usage:

-Change the saving path name "YourPath" at the end of the script to whatever directory you wish to save the output images and depth maps.

-Click run script to generate a few random 3d scenes with corresponding depth map. 

This is just a simple stater example, you can then play with the script to randomize the shapes, colors, locations, surface properties etc..


