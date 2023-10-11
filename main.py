# Function to check if the case is valid based on the delay on arrival/ departure

def check_if_valid(problem:str, departure_delay:int, arrival_delay:int, notification:str) -> bool:
    if notification not in ["0", "<7", "8-14"]:
         return False
    if (departure_delay >= -100 and notification == "<7") or (departure_delay >= -200 and notification == "8-14"):
        return True # Case valid, we first check if the flight was brought forward 
    if problem == "delay" and arrival_delay < 300:
        return False # Case not valid, flight delay less than 3h in problem (delay)
    if (problem in ["cancelation" , "denied boarding"] and arrival_delay < 200) or (problem in ["cancelation" , "denied boarding"] and notification in [8-14] and arrival_delay < 400):
            return False # Case not valid, cancellation or denied boarding, where the delay is not long enough based on the notification period
    return True # otherwise the case is valid
    
# Fuction to check for 50% reduction

def check_reduction(distance:int, departure_delay:str, arrival_delay:str) -> bool:  
    if departure_delay <= -100:
        return False # No reduction
    if (distance >= 3500 and arrival_delay < 400) or (1500 <= distance < 3500 and arrival_delay < 300):
        return True # 50% reduction       
            
# Not sure if we need to format the delay time if its type is string (e.g."03:10"). 
# Following code can be added into both functions to convert departure_delay, arrival_delay into integer:
# arrival_delay = int(arrival_delay.replace(":", ""))
# departure_delay = int(departure_delay.replace(":", ""))

# problem assumed to be in ["delay", "cancelation", "denied boarding"]
# notification assumed to be in ["0", "<7", "8-14"]

# example of the implementation
# Variables for the functions: 
problem = "cancelation"
departure_delay = 0
arrival_delay = 230
notification = "0"
distance = 1600
valid = None
reduction = None
# Check if the case valid and then check if the reduction is applicable

if check_if_valid(problem, departure_delay, arrival_delay, notification):
    if check_reduction(distance, departure_delay, arrival_delay):
         valid = True
         reduction = True 
    else:
         valid = True
         reduction = False
else:
     valid = False

print(valid, reduction)
 



    

                    


