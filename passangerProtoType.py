


price_per_km = 2.5
list_of_source = ["bhaktapur"]
lsit_of_destination = {"patan":10, "koteswor":5,"kirtipur":25,"kalanki":25,"buspark":30
,"ratnapark": 25}
print("--------------------------------------------------------------")
print("For now our travel service is available in following places \n")
print("from",list_of_source,"to ->",list(lsit_of_destination.keys()))
print("where you want to go?")

passenger_destination = input("enter the destination : ")
while(passenger_destination not in list(lsit_of_destination.keys())):
    passenger_destination = input("enter the destination : ")
    
def return_distance(passenger_destination):
    return lsit_of_destination.get(passenger_destination) 


print(list_of_source[0], "-> ", passenger_destination)
print("The cost per km is ",price_per_km)
distance = return_distance(passenger_destination)
print("The total distance from Bhaktapur to ",passenger_destination," is ",distance)
print("so the total cost from Bhaktapur to ",passenger_destination," is ",distance*price_per_km)



    
