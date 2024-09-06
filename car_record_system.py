import csv
import os
import re



def read_db(gar_name):

    file_read = open(f"{gar_name}.csv","r")

    records = list(csv.reader(file_read))
    file_read.close()

    total_col_len = []
    temp_lens = []
    
    row = 0
    
    for x in range(len(records[0])):
        for i in range(len(records)):
            # Adds The length of each word in te column into a list
            temp_lens.append(len(records[i][row]))
            
        # Once loop finished, sorts and adds the biggest value to the length list, then clears the temp list
        temp_lens.sort()
        total_col_len.append(temp_lens[-1])
        temp_lens.clear()
        
        row += 1


    counter_len = len(str(len(records)))

    header_len = len(records[0][0]) + len(records[0][1]) + len(records[0][2]) + sum(total_col_len) + counter_len

    print("\n")
    print(f"ID\t{records[0][0]:<{total_col_len[0]}}\t{records[0][1]:<{total_col_len[1]}}\t{records[0][2]:<{total_col_len[2]}}", end="")

    print("\n"+"-"*header_len)

    rowCounter = 1
    for record in records[1:]:
        print(f"{rowCounter}\t{record[0]:<{total_col_len[0]}}\t{record[1]:<{total_col_len[1]}}\t{record[2]:<{total_col_len[2]}}")
        rowCounter += 1
        

#-------------------------------------------
#					START					
#-------------------------------------------
action = input("What do you want to do?\n(C = create garage \tA = Add \tR = Read \tD = Delete)\nEnter: ")

if (action.lower() == "c"):
    garage_name = input("Enter the garage name: ")
    header = ["Make","Model","Reg"]
    
    #"Security" but not really
    not_Allowed_Char = re.search("[^A-Za-z0-9]", garage_name)
    
    if (not_Allowed_Char):
        print("Only use a-z or 0-9 while naming!")
    
    else:
        file = open(f"{garage_name}.csv","a", newline="")
        db = csv.writer(file)

        db.writerow(header)
        file.close()
        
        print(f"Created garage called {garage_name}")

elif(action.lower() == "a"):
    garage_name = input("Enter the garage you want to add to: ")
    if(os.path.isfile(f"{garage_name}.csv")):
        record = []
        
        make = input("Enter make: ")
        model = input("Enter model: ")
        reg = input("Enter Reg: ")
        
        record.append(make)
        record.append(model)
        record.append(reg)
        
        file = open(f"{garage_name}.csv","a", newline="")
        db = csv.writer(file)
        db.writerow(record)
        file.close()
    else:
        print(f"Database called {garage_name} doesn't exist.")

elif(action.lower() == "r"):
    garage_name = input("Enter the garage you want to read: ")
    
    if(os.path.isfile(f"{garage_name}.csv")):
        read_db(garage_name)
    else:
        print(f"Database called {garage_name} doesn't exist.")
    
elif(action.lower() == "d"):
    garage_name = input("Enter the garage you want to delete from: ")
    if(os.path.isfile(f"{garage_name}.csv")):
        read_db(garage_name)
     
        del_id = int(input("Enter the row ID to delete: "))
        
        if (del_id <= 0):
            print("Error, not valid ID!")
        
        else:
        
            file = open(f"{garage_name}.csv","r")
            records = list(csv.reader(file))
            file.close()
            
            '''
            for record in records:
                print(record)
                
                if record == records[1]:
                    print("TAKE OUT")
            '''
            newtable = [e for e in records if e != records[del_id]]
            
            fileV2 = open(f"{garage_name}.csv","w", newline="")
            dbV2 = csv.writer(fileV2)
            dbV2.writerows(newtable)
            fileV2.close()
        
    else:
        print(f"Database called {garage_name} doesn't exist.")

