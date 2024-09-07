# fusion-scripts 

there is a helpful rust cli provided in `./new_fusion` that will let you create the script skeleton to avoid going thru the dialog in fusion.


the only useful script is the `disable all sketches` script.

pro tip use the python intepreter at 
`"C:\Users\anand\AppData\Local\Autodesk\webdeploy\production\1a197c6e79bef01edef1dc4f317d9f597820e633\Python\python.exe"`

and the python adsk code `C:\Users\anand\AppData\Local\Autodesk\webdeploy\production\1a197c6e79bef01edef1dc4f317d9f597820e633\Api\Python\packages\adsk`

the sample codes are in 
`C:\Users\anand\AppData\Local\Autodesk\webdeploy\production\1a197c6e79bef01edef1dc4f317d9f597820e633\Python\Samples\`

the `./.vscode` folder sets it up so you get a bit of docstrings 

todo see if i can find to better explore the object model 

```C++
#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>
#include <Cam/CamAll.h>
```