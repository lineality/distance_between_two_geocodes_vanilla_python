import math


def distance_between_two_geocodes_miles(location_tuple_1, location_tuple_2, units = "miles"):
    """
    Description:
        haversine distance:
        Calculate spherical distance between two geocodes, using "origin" and "destination."
    
    Parameters:
        lat_1: type=float, latitude of origin (location) in degrees
        lon_1: type=float, longitude of origin (location) in degrees    
        lat_2: type=float, latitude of destination (location) in degrees
        lon_2: type=float, longitude of destination (location) in degrees 
          
    Returns:
        - units: km or mile
        - type of output: float

    Adapted from:
    https://towardsdatascience.com/calculating-the-distance-between-two-locations-using-geocodes-1136d810e517    
    
    """

    units = units.lower()

    metric_flag = False

    if units == "km" or units == "metric" or units == "kilometers" or  units == "kilo" or units == "si":
        metric_flag = True


    ##################################
    # Preparing numbers and variables
    ##################################

    # separate latitude and longitude for the two geocodes:
    lat_1 = float( location_tuple_1[0] )
    lon_1 = float( location_tuple_1[1] )
    lat_2 = float( location_tuple_2[0] )
    lon_2 = float( location_tuple_2[1] )

    # convert: degrees -> radians  
    phi1 = math.radians(lat_1)
    phi2 = math.radians(lat_2)
    
    delta_phi = math.radians(lat_2 - lat_1)
    delta_lambda = math.radians(lon_2 - lon_1)
    

    ##################
    # Selecting Units
    ##################

    # r: radius of earth in Kilometers (general approximiation)
    # https://en.wikipedia.org/wiki/Earth_radius
    """
    The units of the outout (miles or Kilometers)
    depends on the units of the input.
    Here the metric flag determines the units.

    Note: for a specific geography you may want to use a different
    estimate for the radius of earth (which is an average because
    the earth is not a perfect sphere).
    """
    if metric_flag == False:
        # this is miles
        r = 3958.8

    if metric_flag == True:
        # this is metric
        r = 6371 

    #######################
    # Calculating Distance
    #######################

    # a & c
    a = math.sin( delta_phi / 2 )**2 + math.cos( phi1 ) * math.cos( phi2 ) * math.sin( delta_lambda / 2 )**2
    
    c = 2 * math.atan2( math.sqrt( a ), math.sqrt( 1 - a ) )
    
    # distance in Kilometers (as d): d = r * c
    d = r * c

    #########
    # Output
    #########

    output = d

    return output 

# Examples

tokyo = (80,170)
osaka = (24,135)

print( distance_between_two_geocodes_miles(tokyo, osaka, "mi") )
print( distance_between_two_geocodes_miles(tokyo, osaka, "si") )
 

Idaho_City = (43.828850,	115.837860)
Oneida = (43.095654,	75.669487)

print( distance_between_two_geocodes_miles(Idaho_City, Oneida) )
print( distance_between_two_geocodes_miles(Idaho_City, Oneida, "kilometers") )
