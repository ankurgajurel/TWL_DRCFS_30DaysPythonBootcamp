# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 

# READ_FILE = input("Enter relative path of the file with the contacts: ")
READ_FILE = 'Users-Pwds(10).txt'
WRITE_FILE = "Users-Pwds-Chked.txt"

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here

    bool_list = list()
    print(bool_list)
    rank_score = 0

    bool_list.append(any(elem in string.ascii_uppercase for elem in pwd))
    bool_list.append(any(elem in string.ascii_lowercase for elem in pwd))
    bool_list.append(any(elem in string.digits for elem in pwd))
    bool_list.append(any(elem in string.punctuation for elem in pwd))

    for temp_bool in bool_list:
        if temp_bool:
            rank_score += 1
    
    if rank_score < 3 or len(pwd) < 8:
        rank = "POOR"
    elif rank_score < 4 or len(pwd) < 10:
        rank = "MODERATE"
    else:
        rank = "STRONG"

    # print("success")

    ## End code here
    return rank

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE

    with open(READ_FILE, 'r') as f:
        usrpwds = list(f.readlines())

    all_vals = list()

    rank_scores = list()
    for each_line in usrpwds:
                
        seperated_vals = each_line.split(",")
        # print(seperated_vals)
        
        username = seperated_vals[0]
        password = seperated_vals[1].replace("\n", "") #i dont know why tara password ko end ma euta \n airako thyo so teslai replace gareko .. this toook ma 10 min to find kina extra \n aairako cha bhanera haha
        pwd_rank = rank(password)

        all_vals.append([username, password, pwd_rank])     

    # print(all_vals) 

    with open(WRITE_FILE, 'w') as f:
        for each_element in all_vals:
            what_to_write = ",".join(each_element)
            f.write(what_to_write)
            f.write("\n")

    # print("bhayo")

    ## END CODE HERE

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE
        sample_lst = list()

        sample_lst.append([random.choice(Ualphabets) for i in range(5)])
        sample_lst.append([random.choice(Lalphabets) for i in range(5)])
        sample_lst.append([random.choice(digits) for i in range(5)])
        sample_lst.append([random.choice(chars) for i in range(5)])


        pwd = "".join("".join(map(str, l)) for l in sample_lst)

        ## END CODE HERE
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE
    sample_username = str(input("Enter the username: "))
    if len(sample_username) >= 20:
        print("sorry invalid username")
        raise ValueError("Username is invalid")
    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE
    sample_password = generate()
    sample_password_rank = rank(sample_password)

    print(f"The password is {sample_password} and the rank is {sample_password_rank}")

    write_to_file = int(input("Add this username and password to file? 1 for Yes and 0 for No:  "))
    if write_to_file == 1:
        with open(WRITE_FILE, 'a') as f:
            temp  = ",".join(sample_username, sample_password, sample_password_rank)
            f.write(temp)
    elif write_to_file == 0:
        main()
        pass
    else:
        print("Enter either 1 or 0")


    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
        try:
            inp = int(inp)
            if inp == 1:
                option1()
            elif inp == 2:
                option2()
            elif inp == 3:
                print("Program stopped")
                break
            else:
                print("Enter either 1 or 2 or 3\n\n")

        except Exception as exception:
            print("Error: {}".format(exception))
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()

option2()