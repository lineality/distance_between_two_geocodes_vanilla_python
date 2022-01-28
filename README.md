# distance_between_two_geocodes_vanilla_python

This is a python function to calculate the distance between two geocodes (two pairs of latitude longitude coordinates) 
- does not require installed libraries, so this is compatible with AWS lambda functions
- can output metric (kilometers) or miles (not nauticle miles)
- note: the number for the radius of the earth is a generalization and you may want to fine tune it for use in specific areas https://en.wikipedia.org/wiki/Earth_radius


#### Compare results here to check 
(select statute miles (sm) NOT "n mi" for nauticle miles):
https://www.nhc.noaa.gov/gccalc.shtml
