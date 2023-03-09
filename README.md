# MultiplyUnitCellMultiFrameXYZ

This script allows you to read in a multi-frame .xyz file and multiply the unit cell or simulation cell of your structure. You can choose to only extract certain atoms and multiply those atoms. To use the code use:

```
from read import openStruct

coordinates = openStruct("Structure_File.xyz",start,end)

from multiCell import increaseCell

increaseCell(coordinates,[a1,a2,a3],[b1,b2,b3],[c1,c2,c3],ux,uy,uz,atom_selection,"Output_File.xyz")
```

where ```start``` is the start frame number from the file, default is 0.
```end``` is the last frame number you want to use from the file, default is -1.
```[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]``` are the cell vectors
```ux,yu,uz``` are the multiplication factors, for example 3x3x1 would be 3,3,1.
```atom_selection``` is the atoms you want to extract and multiply. This could be range(130), [1,2,3,8,9,12], etc.
