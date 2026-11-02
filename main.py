def calculate_gads_iq():
    try:
        iq = float(input("enter gads iq"))
    except TypeError:
        print ("wrong input")
    if iq > 50:
        raise ValueError ("too high of an iq")
    
calculate_gads_iq()