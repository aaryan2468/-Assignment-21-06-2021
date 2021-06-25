test_str = str(input("Enter any input : "))

all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
print ("Frequency is :\n "+  str(all_freq))
