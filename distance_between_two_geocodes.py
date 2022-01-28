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
        km or mile
        type or output: float

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
    lat_1 = location_tuple_1[0]
    lon_1 = location_tuple_1[1]
    lat_2 = location_tuple_2[0]
    lon_2 = location_tuple_2[1]

    # convert: degrees -> radians  
    phi1 = math.radians(lat_1)
    phi2 = math.radians(lat_2)
    
    delta_phi = math.radians(lat_2 - lat_1)
    delta_lambda = math.radians(lon_2 - lon_1)
    

    #######################
    # Calculating Distance
    #######################

    # r: radius of earth in Kilometers (general approximiation)
    # https://en.wikipedia.org/wiki/Earth_radius
    r = 6371 
    
    # a & c
    a = math.sin( delta_phi / 2 )**2 + math.cos( phi1 ) * math.cos( phi2 ) * math.sin( delta_lambda / 2 )**2
    
    c = 2 * math.atan2( math.sqrt( a ), math.sqrt( 1 - a ) )
    
    # distance in Kilometers (as d): d = r * c
    d = r * c


    ######################
    # Kilometers to Miles
    ######################

    kilometers = d

    # conversion factor
    conv_factor = 0.621371

    # calculate miles
    miles = kilometers * conv_factor

    # # inspection
    # # print Kilometers  
    print (f'{kilometers:.2f} Kilometers')
    # # print Miles  
    print (f'{miles:.2f} Miles')

    if metric_flag == False:
        output = miles

    if metric_flag == True:
        output = kilometers

    #########
    # Output
    #########

    return output 
