# distance_between_two_geocodes_vanilla_python

This is a python function that calculates the distance between two geocodes (two pairs of latitude longitude coordinates) 
- does not require installed libraries, so this is compatible with AWS lambda functions
- can output metric (kilometers) or miles (not nauticle miles)
- input form is (1,2)(3,4)
- note: the number for the radius of the earth is a generalization and you may want to fine tune it for use in specific areas https://en.wikipedia.org/wiki/Earth_radius


#### Compare results here to check 
(select statute miles (sm) NOT "n mi" for nauticle miles):

https://www.nhc.noaa.gov/gccalc.shtml

#### Example Input and Use
```
Idaho_City = (43.828850, 115.837860)
Oneida = (43.095654, 75.669487)

distance_between_two_geocodes_miles(Idaho_City, Oneida)
distance_between_two_geocodes_miles(Idaho_City, Oneida, "kilometers")
```
