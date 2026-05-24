# Importing key modules for things to work moving forward
import subprocess

### Defining key functions for the program moving forward.
# Simple clearing function to main tidiness throughout the code
def Clear():
    subprocess.run("cls", shell=True)

# Value to return a boolean through a try...except block to see if it was valid or not



# Declaring important variables and arrays for the algorithm (i.e. initialising the database)
hostTeam = [
            [ "Abdul Ahad", "M", "Purple", "IT", "Member" ],
            [ "Abdul Hadi", "M", "White", "Security", "Member" ],
            [ "Abdul Mateen", "M", "Purple", "Outreach", "Member" ],
            [ "Abdul Qadir", "M", "Orange", "Marketing", "Co-director" ],
            [ "Abdul Rehman", "M", "White", "Media", "Member" ],
            [ "Abdullah Irfan", "M", "White", "Security", "Member" ],
            [ "Abdul Wasae", "M", "White", "Security", "Member" ],
            [ "Adeel Anjum", "M", "Orange", "Liaison", "Director" ],
            [ "Ahad Shehzad", "M", "Green", "Registration", "Director" ],
            [ "Ahmed Hasen Khan", "M", "Blue", "Security", "Member" ],
            [ "Ahmed Salauddin", "M", "Green", "Security", "Member" ],
            [ "Ahmed Salar", "M", "Mauve", "Publications", "Member" ],
            [ "Aimal Khakan", "G", "", "Registration", "Member" ],
            [ "Aimel Khan", "M", "White", "Security", "Director" ],
            [ "Alia Zahoor", "G", "", "EC", "Head of Host Team" ],
            [ "Alizaad", "M", "Green", "Finance", "Member" ],
            [ "Alveena Zahoor", "G", "", "EC", "Under Secretary General" ],
            [ "Anas Khalid", "M", "Silver", "Logistics", "Member" ],
            [ "Anaya Hayat", "G", "", "Logistics", "Co-director" ],
            [ "Anoshka John", "G", "", "Security", "Co-director" ],
            [ "Anum Khurram", "G", "", "Logistics", "Member" ],
            [ "Arfa Tanveer", "G", "", "Committee Affairs", "Member" ],
            [ "Arham", "M", "Orange", "Liaison", "Member" ],
            [ "Arham Shafi", "M", "Mauve", "Logistics", "Member" ],
            [ "Arnawa", "G", "", "IT", "Member" ],
            [ "Aryam Fatima", "G", "", "Logistics", "Member" ],
            [ "Asbah Iqbal", "G", "", "Security", "Member" ],
            [ "Ayan Bin Amir", "M", "Purple", "Socials", "Member" ],
            [ "Ayeza Fatima", "G", "", "Socials", "Member" ],
            [ "Azain Atif", "M", "Mauve", "Liaison", "Co-director" ],
            [ "Azlan Faisal", "M", "Orange", "Finance", "Member" ],
            [ "Azlan Khan", "M", "Green", "Security", "Member" ],
            [ "Balaj Ali", "M", "Yellow", "Logistics", "Member" ],
            [ "Dania Faisal", "G", "", "Logistics", "Member" ],
            [ "Dawood Ul Hasen", "M", "Purple", "Registration", "Member" ],
            [ "Dayyan Ahmed Panezai", "M", "Blue", "EC", "Head of Host Team" ],
            [ "Dilskash Rehamn", "G", "", "Media", "Member" ],
            [ "Eitezaz Ali", "M", "White", "Security", "Member" ],
            [ "Eman Ali", "G", "", "Security", "Member" ],
            [ "Eman Zeenat", "G", "", "Publications", "Director" ],
            [ "Eshal Ashfaq", "G", "", "Media", "Member" ],
            [ "Eshal Nouman", "G", "", "Committee Affairs", "Member" ],
            [ "Eshal Oman", "G", "", "Registration", "Member" ],
            [ "Eshal Yasir", "G", "", "Publications", "Member" ],
            [ "Ezaan Shahid", "M", "Orange", "Outreach", "Member" ],
            [ "Faiza Dawood", "G", "", "Security", "Member" ],
            [ "Faiza Qazi", "G", "", "Marketing", "Member" ],
            [ "Farrukh Nihad", "M", "Red", "Outreach", "Member" ],
            [ "Fatima Alvi", "G", "", "Socials", "Member" ],
            [ "Fatima Ali Syed", "G", "", "Media", "Co-director" ],
            [ "Fatima Iqbal", "G", "", "Committee Affairs", "Co-director" ],
            [ "Fatima Khan", "G", "", "IT", "Member" ],
            [ "Fatima Nadeem", "G", "", "Marketing", "Member" ],
            [ "Fatima Shaukat", "G", "", "Finance", "Member" ],
            [ "Fatima Tuz Zehra", "G", "", "Socials", "Co-director" ],
            [ "Hadia Ahmed", "G", "", "Logistics", "Member" ],
            [ "Hafsa Ali", "G", "", "Publications", "Member" ],
            [ "Haiqa Rizwan", "G", "", "Liaison", "Director" ],
            [ "Hamdan Ishaq", "M", "Blue", "Logistics", "Co-director" ],
            [ "Hamza Ali", "M", "Orange", "Registration", "Co-director" ],
            [ "Hania Hawwa", "G", "", "Security", "Member" ],
            [ "Hasan Yasir Abbasi", "M", "White", "Security", "Member" ],
            [ "Hayyan Rasheed", "M", "Yellow", "Outreach", "Member" ],
            [ "Hooriya Javed", "G", "", "Socials", "Director" ],
            [ "Ibrahim Imtiaz", "M", "Green", "Security", "Co-director" ],
            [ "Inaya Binte Kshif", "G", "", "Security", "Member" ],
            [ "Izan Ishtiaq", "M", "Green", "Publications", "Director" ],
            [ "Izaan Qamar", "M", "Blue", "Finance", "Director" ],
            [ "Izhan Shoukat", "M", "White", "Finance", "Member" ],
            [ "Jannat Ahmad", "G", "", "Outreach", "Member" ],
            [ "Jannat Haroon", "G", "", "Outreach", "Co-director" ],
            [ "Jannat Nasir", "G", "", "Registration", "Director" ],
            [ "Javeria Naveed", "G", "", "Liaison", "Member" ],
            [ "Khadija Noor", "G", "", "Registration", "Member" ],
            [ "Khadijah farrukh", "G", "", "Marketing", "Member" ],
            [ "Khajista Zainab", "G", "", "Finance", "Director" ],
            [ "Khawaja Haris", "M", "Green", "Socials", "Director" ],
            [ "Layma Shah", "G", "", "Security", "Member" ],
            [ "Arham Goroya", "M", "Mauve", "Publications", "Member" ],
            [ "Ayan", "M", "Silver", "Liaison", "Member" ],
            [ "Ayan", "M", "White", "Outreach", "Co-director" ],
            [ "Ayan Khan", "M", "Red", "Marketing", "Director" ],
            [ "Hasen Waqar", "M", "Yellow", "Logistics", "Member" ],
            [ "Mohib", "M", "Green", "IT", "Co-director" ],
            [ "Rafay Abbasi", "M", "Purple", "Registration", "Member" ],
            [ "Zayyan Zohaib", "M", "Silver", "IT", "Member" ],
            [ "Maaz Affan", "M", "Silver", "Security", "Member" ],
            [ "Maha Zulfiqar", "G", "", "Publications", "Member" ],
            [ "Mahad Ehtesham", "M", "Blue", "Outreach", "Director" ],
            [ "Mahad Zeeshan", "M", "Orange", "Marketing", "Member" ],
            [ "Maham Ahmad", "G", "", "Marketing", "Director" ],
            [ "Mahin Ayaz", "G", "", "Finance", "Member" ],
            [ "Maryam Rehan", "G", "", "Committee Affairs", "Member" ],
            [ "Maryam Tariq", "G", "", "Outreach", "Member" ],
            [ "Mazen Touqeer", "M", "Orange", "Marketing", "Member" ],
            [ "Meerub fatima", "G", "", "IT", "Director" ],
            [ "Abdullah Malhi", "M", "Mauve", "EC", "Under Secretary General" ],
            [ "Momina Rehab", "G", "", "Registration", "Member" ],
            [ "Moosa Obaid", "M", "Purple", "Committee Affairs", "Member" ],
            [ "Essa Hashmi", "M", "Silver", "Media", "Member" ],
            [ "Haris", "M", "Silver", "IT", "Member" ],
            [ "Sagheer", "M", "Mauve", "Socials", "Co-director" ],
            [ "Shahmeer", "M", "Mauve", "Security", "Member" ],
            [ "Suleman Kamal", "M", "Blue", "Socials", "Member" ],
            [ "Muqeet Bux", "M", "Mauve", "Media", "Co-director" ],
            [ "Musa Mubashir", "M", "Yellow", "Finance", "Co-director" ],
            [ "Mustafa", "M", "White", "Security", "Member" ],
            [ "Mustafa Hussain", "M", "Blue", "Committee Affairs", "Director" ],
            [ "Myesha Irfan", "G", "", "EC", "Director General" ],
            [ "Nabeela Naveed", "G", "", "Socials", "Member" ],
            [ "Najeeb ur Rehman", "M", "Red", "EC", "Secretary General" ],
            [ "Natasha Fida", "G", "", "Publications", "Member" ],
            [ "Naveen Ahmed Yar", "G", "", "Socials", "Member" ],
            [ "Neha Amir", "G", "", "Media", "Member" ],
            [ "Omar Abdullah", "M", "Mauve", "Liaison", "Member" ],
            [ "Omar Zakir", "M", "Purple", "Committee Affairs", "Member" ],
            [ "Omer Abbasi", "M", "Yellow", "Logistics", "Member" ],
            [ "Qirat Zehra", "G", "", "Security", "Member" ],
            [ "Raja Shumail", "M", "Mauve", "Security", "Member" ],
            [ "Raja Uzair Younis", "M", "Purple", "EC", "Director General" ],
            [ "Rania Wadood", "G", "", "Socials", "Member" ],
            [ "Razan Naji", "G", "", "IT", "Co-director" ],
            [ "Rida Alam Khan", "G", "", "Outreach", "Director" ],
            [ "Romaisa Nizami", "G", "", "EC", "Secretary General" ],
            [ "Saad Abbasi", "M", "Red", "Logistics", "Director" ],
            [ "Saim Khan", "M", "Orange", "IT", "Director" ],
            [ "Samiullah", "M", "Silver", "Outreach", "Member" ],
            [ "Sana Murtaza", "G", "", "Security", "Member" ],
            [ "Sara Raza", "G", "", "Registration", "Co-director" ],
            [ "Sara Sarmad", "G", "", "Liaison", "Co-director" ],
            [ "Sehr Abbasi", "G", "", "Security", "Director" ],
            [ "Shanze Khan", "G", "", "Media", "Member" ],
            [ "Shanzay Omer", "G", "", "Logistics", "Director" ],
            [ "Shiza Usman", "G", "", "Marketing", "Co-director" ],
            [ "Shujauddin", "M", "Purple", "Publications", "Co-director" ],
            [ "Sophe Patafi", "G", "", "Liaison", "Member" ],
            [ "Syed M Ayan", "M", "Blue", "Finance", "Member" ],
            [ "Taha Habib", "M", "Red", "Socials", "Member" ],
            [ "Talal Khan Ghori", "M", "Red", "Media", "Director" ],
            [ "Talal Khawaja", "M", "Silver", "Socials", "Member" ],
            [ "Talha Khan", "M", "Red", "Media", "Member" ],
            [ "Tamiya Faisal", "G", "", "Outreach", "Member" ],
            [ "Tayyab Ashfaq", "M", "White", "Media", "Member" ],
            [ "Usna Raja", "G", "", "Security", "Member" ],
            [ "Usarim Nabeel", "M", "Blue", "Committee Affairs", "Co-director" ],
            [ "Ushna Shah", "G", "", "Finance", "Co-director" ],
            [ "Wasma Zahra", "G", "", "Security", "Member" ],
            [ "Yamna Farhan", "G", "", "Finance", "Member" ],
            [ "Yashfa Maheen", "G", "", "IT", "Member" ],
            [ "Yumainah Maryam", "M", "White", "Security", "Member" ],
            [ "Yusra Iqbal", "G", "", "Media", "Director" ],
            [ "Zahid", "M", "Blue", "Outreach", "Member" ],
            [ "Zain Ali", "M", "Green", "Security", "Member" ],
            [ "Zaina Zeeshan", "G", "", "Liaison", "Member" ],
            [ "Zaina Zeeshan ", "G", "", "Liaison", "Member" ],
            [ "Zainab sajjad", "G", "", "Committee Affairs", "Member" ],
            [ "Zeerak Hussain", "M", "Silver", "Registration", "Member" ],
            [ "Zimal Nisar", "G", "", "Committee Affairs", "Director" ],
            [ "Zoha Aziz", "G", "", "Marketing", "Member" ],
            [ "Zoha Sardar", "G", "", "Security", "Member" ],
            [ "Zohair Zulfiqar", "M", "Red", "Publications", "Member" ],
            [ "Zoraiz Jashal", "M", "Green", "IT", "Member" ],
            [ "Zunaira Hasan", "G", "", "Logistics", "Member" ],
            [ "Zyna Malik", "G", "", "IT", "Member" ] ]

# Important menu variables 
menuChoice = ""
choiceInteger = 0
gender = ""
firstName = ""
post = ""
dept = ""
section = ""

# Loop booleans
mainLoop = True
errorDiplay = False
mainMenuErrorDisplay = False

while mainLoop:
    Clear()

    print("BMIDC Rebirth Edition")
    print("Host Team Database")

    # Displaying the fields that the user can pick from
    print("\nHere are a list of fields and their associated number: ")
    print("1. First Name\n2. Position\n3. Department\n4. Gender\n5. Section\n6. Clear fields\n\n7. Begin Search\n")

    # If the previous value entered into menuChoice for the main menu wasn't valid, this error message will be displayed
    if mainMenuErrorDisplay:
        print("Invalid value entered! Please enter a valid value from the options given above. Only enter a number.")
    
    # Clearing appropriate variables to use further in the search
    mainMenuErrorDisplay = False

    # Taking input from the user regarding which field they want to pick from above and storing it in menuChoice
    menuChoice = input("Enter the number associated with the field you would like to set: ")

