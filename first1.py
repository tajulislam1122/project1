# email validation in python .
# using string function . 
email=input("enter your email ?")
k,j,d=0,0,0
if len(email)>=6: # this line chick the email langth .
    if email[0].isalpha(): # this line chick the email first latter with alphbate yes or no . 
        if ("@"in email) and (email.count("@")==1): # this line chick the @ with this email only one not more .
            if (email[-3]==".") ^ (email[-4]=="."):# this line chick the "." posetion now, but we used the XOR oprater (.com)this one is writh , but (..in) this one is worng this like we used the XOR oprater . 
                for i in email:# this line iterat the email for chicking the space we want to no space .
                    if i ==i.isspace():#this line exatle chick the space erea.
                        k=1
                    elif i.isalpha():# this line chick the all email have the alpha latter yes or no . 
                        if i==i.upper():# this line chick the all email have tha upper case . yes or no . 
                            j=1
                    elif i.isdigit():# this line chick the all email digit or special cracter . 
                        continue
                    elif i=="_" or i=="." or i == "@": #this line chick the _ . @ with this email now here is it . 
                        continue
                    else:# this line chick anyone enter other cracter it's worng 
                        d=1

                if k==1 or j==1 or d==1:
                    print(" Worng Email 5")
                else:
                    print(" R  ight email ")
            else:
                print(" Worng Email 4 ")
        else:
            print(" Worng Email 3")
    else:
        print(" Worng Email 2")
else:
    print(" Worng Email 1")