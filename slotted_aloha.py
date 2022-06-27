import numpy as np
import matplotlib.pyplot as plt 


No_of_events = 10000
Pc = 0.2 
R = 0 
T = 0 
max_R = 4
states = [] 
dropped_packets = 0
#States are represented like this : (R,T)

for i in range(No_of_events):

    if(T > 0):
        T -= 1 

    else :
        p = np.random.random()
        #if there is NO collision, then send and go back to state (0,0) 
        if (p > Pc) :
            R = 0
        #if there is collision but we've reached the max no. of retransmissions
        elif (R == max_R):
            R = 0 
            dropped_packets += 1   
        #if there is collision        
        else :
            R += 1
            curr = 2**R 
            T = np.random.randint(curr, size=1)[0] 
            
    states.append(R)
            
 
zeros = states.count(0)
ones = states.count(1)
twos = states.count(2)
threes = states.count(3)
fours = states.count(4)
n = '\n'

total = f"{n}Frequency of state zero: {zeros} {n}Frequency of state one: {ones} {n}Frequency of state two: {twos} {n}Frequency of state three: {threes} {n}Frequency of state four: {fours} {n}Number of dropped packets: {dropped_packets}{n}"
print(total)

#The following graph shows the percentage of time spent in each retransmission number

yaxis = [zeros, ones, twos, threes, fours]
plt.figure()
plt.title('Slotted ALOHA state distribution')
plt.xlabel('Retransmission number')
plt.ylabel('Frequency')
plt.plot(yaxis/np.sum(yaxis))
plt.grid()
plt.show()