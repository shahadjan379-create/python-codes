temp = float(input("Enter todays weather: "))
if temp > 40:
    print ("It's too hot outside.")
elif temp > 30:
    print ("The weather today is normal.")
elif temp > 20:
    print ("Today's weather is cool.")
elif temp > 10:
    print ("OMG, today's weather is so cool.")
else:
    print ("It's freezing today.")