#---------------------------------------------------------------------VIKAS KUMAR -------------------------------------------------------------------------------#
#Time module is required to provide a seed to the xorshift* algorithm
import time





#Class Used to generate a seed according to the system time
class TimeSeed():
    def generate_seed(self):
        return time.time()








#Random class
class Random():
    #----------------------------------------------------------XORSHIFT* Algorithm used to generate random numbers with equal distribution. The algorithm is famous and reliable and is described well in Wikipedia...
    def random(self, start, end, seed):
        random_number = seed & 0xffffffffffffffff
        random_number ^= (random_number >> 12); #Arithmetic Shift and XOR Operation on the initial seed
        random_number ^= (random_number << 25);
        random_number ^= (random_number >> 27);
        random_number = random_number * 0x2545F4914F6CDD1D # modulo word size resulting in a non-linear transformation
        random_number = random_number % (end-start) #adjust to the given range
        random_number = random_number + start
        return random_number










    #-----------------------------------------------------------------------------generate and check accuracy for a list of numbers with 73% bias for higher numbers
    def generate_biased_list(self,total_numbers,start,end):
        i = total_numbers
        counter1 = 0 #for finding no-of-elemnts generated which lie in the upper half
        counter2 = 0
        bin_num = []
        while i > 0:
            check_bias = self.u_next(1, 10000)   #generate a unbiased number from 1 to 10000
            if check_bias > 2700: #if number is smaller 2700, generate from the lower bin, otherwise generate from the upper bin (change to change the bias)
                num = self.u_next((start + (end-start)/2)*1000, (end)*1000)  
            else:
                num = self.u_next(start*1000, start + (end-start)/2*1000)

            #upto three decimal places precision    
            num = num /float(1000)
            #counter for total numbers in the upper half
            if(num>start+(end-start)/2):
                counter2 = counter2 + 1
            elif(num>=start+(end-start)/2):
                counter1 = counter1 + 1

            i = i - 1 #while loop counter
            bin_num.append(num) #list for storing numbers

        #print accuracy, distinctiveness and list_of_numbers
        percentage_of_higher_num = counter1 if abs(counter1/float(total_numbers)*100-73)<abs(counter2/float(total_numbers)*100-73) else counter2    
        print("\n\n-----------Percentage of numbers in the higher half----") 
        print(str(percentage_of_higher_num/float(total_numbers)*100)+"%")
        print("\n\n-----------Percentage of distinct numbers generated----") 
        print(str(len(set(bin_num))/float(len(bin_num))*100)+"%")
        print("\n\n----------Do you want to see the list(y/n)-----------")
        if(raw_input() is 'y'):
            print(bin_num)











    #-------------------------------------------------------------------------------------for printing just one number according to 73% bias for higher numbers
    def b_next(self,start,end):
        #follows the same logic as in the previous function
        check_bias = self.u_next(1, 10000)   
        if check_bias > 2700:
            num = self.u_next((start + (end-start)/2)*1000, (end)*1000)  
        else:
            num = self.u_next((start)*1000, (start + (end-start)/2)*1000)    
        print(num/float(1000))













    #-----------------------------------------------------------------------------------------------------checking accuracy for unbiased list
    def generate_unbiased_list(self,total_numbers,start,end):
        i = total_numbers 
        counter = 0 #for finding no-of-elemnts generated which lie in the upper half
        bin_num = [] # list of numbers generated
        while i > 0:
            num = self.u_next(start*1000,end*1000)   
            num= num/float(1000) # 3 decimal precision
            if(num>=start+(end-start)/2):
                counter = counter + 1
            i = i - 1
            bin_num.append(float(num))

        #print accuracy, distinctiveness and list_of_numbers    
        print("\n\n-----------Percentage of numbers in the higher half----") 
        print(str(counter/float(total_numbers)*100)+"%")
        print("\n\n-----------Percentage of distinct numbers generated----") 
        print(str(len(set(bin_num))/float(len(bin_num))*100)+"%")
        print("\n\n----------Do you want to see the list(y/n)-----------")
        if(raw_input() is 'y'):
            print(bin_num)







    #----------------------------------------------------------------------------------------------------generates an unbiased number for a given range
    def u_next(self,start,end):
        num = self.random(start, end, int(float(str(TimeSeed().generate_seed()%1).split('.')[1])))   
        return num






print("*************************************************************************")
print("PSEUDO RANDOM NUMBER GENERATOR")
print("*************************************************************************")

while True:
    print("\n\n\n----------------Enter Your Choice----------------\n")
    print("1.Generate Biased Number (73% biased to the higher slot)")
    print("2.Generate Unbiased Number (50% biased to the higher slot)")
    print("3.Check accuracy for Biased Generator")
    print("4.Check accuracy for Unbiased Generator")
    print("5.Exit")

    choice = int(raw_input())

    print("Enter start INTEGER")
    start = int(raw_input())
    print("Enter end INTEGER (exclusive so min_range_allowed is 2)")
    end = int(raw_input())

    if end - start <=1:
        print("Please specify ah valid range of numbers")
    
    else:
        rand=Random()
        if(choice == 1):
            rand.b_next(start,end)      

        elif(choice == 2):
            print(rand.u_next(start,end))

        elif(choice == 3):
            print("Enter the length of list to determine accuracy (Enter a high number for better check)")
            number_of_numbers = int(raw_input())
            rand.generate_biased_list(number_of_numbers,start,end)

        elif(choice == 4):
            print("Enter the length of list to determine accuracy (Enter a high number for better check)")
            number_of_numbers = int(raw_input())
            rand.generate_unbiased_list(number_of_numbers,start,end)

        elif(choice ==5):
            exit()

        else:
            print("Invalid")
