import pyfiglet

# Prints Banner with tool name
banner = pyfiglet.figlet_format("SSH Function", font="digital")
print(banner)


def ssh_write_configuration(command):
    # Call Connect Handler function from Netmiko Library
    from netmiko import ConnectHandler

    connection = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    ssh_connect = ConnectHandler(**connection)  # Establish SSH session with HOST
    if ssh_connect:  # Check if the connection established !
        print("Connection Succeeded !\n")

    output = ssh_connect.send_config_set(command)  # Send this configuration into configure terminal

    ssh_connect.save_config()
    print(output)


def ssh_show_configuration(command):
    # Call Connect Handler function from Netmiko Library
    from netmiko import ConnectHandler

    connection = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    ssh_connect = ConnectHandler(**connection)  # Establish SSH session with HOST
    if ssh_connect:  # Check if the connection established !
        print("Connection Succeeded !\n")

    output = ssh_connect.send_command(command)  # Send this command into enable mode
    print(output)


ip = input("Enter your IP: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

while True:
    inpt = input("Enter 'write' for write configuration or 'show' for show configuration :")
    user_command = input("Enter your command: ")
    if inpt == "write":
        ssh_write_configuration(user_command)
    elif inpt == "show":
        ssh_show_configuration(user_command)
    elif inpt == "exit":
        break
    else:
        print("Please choose 'write' or 'show' ")
