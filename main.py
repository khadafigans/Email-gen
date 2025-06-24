import os
import random
from datetime import datetime
from pystyle import Write, Colors, Colorate, Center
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii():
    generator = r"""
███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗ ███████╗███╗   ██╗
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝ ██╔════╝████╗  ██║
█████╗  ██╔████╔██║███████║██║██║     ██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """
    by = r"""
                                 
                        ██████╗ ██╗   ██╗
                        ██╔══██╗╚██╗ ██╔╝
                        ██████╔╝ ╚████╔╝ 
                        ██╔══██╗  ╚██╔╝  
                        ██████╔╝   ██║   
                        ╚═════╝    ╚═╝   
    """
    bob_marley = r"""
██████╗  ██████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ██╗     ███████╗██╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗██╔══██╗██║     ██╔════╝╚██╗ ██╔╝
██████╔╝██║   ██║██████╔╝    ██╔████╔██║███████║██████╔╝██║     █████╗   ╚████╔╝ 
██╔══██╗██║   ██║██╔══██╗    ██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══╝    ╚██╔╝  
██████╔╝╚██████╔╝██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗███████╗   ██║   
╚═════╝  ╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   
    """
    print()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, generator, 1)))
    print(Center.XCenter(Colorate.Horizontal(Colors.yellow_to_green, by, 1)))
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, bob_marley, 1)))
    print()

def generate_usernames(first_name, last_name, email):
    usernames = []
    random_number = str(random.randint(0, 9)).zfill(1)
    random_number_two = random.randint(0, 9999)

    # Pattern 1: abdidalem08
    usernames.append(f"{first_name.lower()}{last_name.lower()}{random_number_two}@{email}")

    # Pattern 2: abdi_dalem08
    usernames.append(f"{first_name.lower()}_{last_name.lower()}{random_number_two}@{email}")

    # Pattern 3: abdi_dalem
    usernames.append(f"{first_name.lower()}_{last_name.lower()}@{email}")

    # Pattern 4: abdidalem (without numbers)
    usernames.append(f"{first_name.lower()}{last_name.lower()}@{email}")

    # Pattern 5: abdidalem08
    usernames.append(f"{first_name.lower()}{last_name.lower()}{random_number}@{email}")

    return usernames

def main():
    clear()
    print_ascii()
    
    how_much = Write.Input("How many usernames to generate (leave blank for infinite): ", Colors.green_to_yellow, interval=0.005)
    if how_much.strip() == "":
        how_much = None
    else:
        how_much = int(how_much)
    
    filename = Write.Input("Enter list file: ", Colors.green_to_yellow, interval=0.005)
    email_domain = Write.Input("What domain do you want for emails: ", Colors.green_to_yellow, interval=0.005)
    output_file = Write.Input("Output File: ", Colors.green_to_yellow, interval=0.005)

    if not os.path.exists(filename):
        Write.Print(f"\nError: The specified file does not exist.\n", Colors.red_to_yellow, interval=0.002)
        return

    with open(filename, "r") as f:
        names = [line.strip() for line in f if line.strip()]

    if not names:
        Write.Print(f"\nError: The file is empty or contains no valid names.\n", Colors.red_to_yellow, interval=0.002)
        return

    k = 1

    with open(output_file, "w") as f:
        if how_much is None:
            Write.Print("\nGenerating usernames infinitely (press Ctrl+C to stop)...\n", Colors.yellow_to_green, interval=0.005)
            try:
                while True:
                    first_name = random.choice(names)
                    last_name = random.choice(names)
                    usernames = generate_usernames(first_name, last_name, email_domain)
                    for username in usernames:
                        Write.Print(f"{k} | Generated Email: {username} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", Colors.green_to_yellow, interval=0.001)
                        f.write(f"{username}\n")
                        f.flush()  # Ensure the write is immediately saved to the file
                        k += 1
            except KeyboardInterrupt:
                Write.Print("\nStopped by user.\n", Colors.red_to_yellow, interval=0.005)
        else:
            for i in range(how_much):
                first_name = random.choice(names)
                last_name = random.choice(names)
                usernames = generate_usernames(first_name, last_name, email_domain)
                for username in usernames:
                    Write.Print(f"{k} | Generated Email: {username} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", Colors.green_to_yellow, interval=0.001)
                    f.write(f"{username}\n")
                    f.flush()  # Ensure the write is immediately saved to the file
                    k += 1
                if k > how_much:
                    break

    Write.Print(f"\nGenerated usernames saved to {output_file}\n", Colors.green_to_yellow, interval=0.005)

if __name__ == "__main__":
    main()
