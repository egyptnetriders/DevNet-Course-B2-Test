""" Send configuration to device using Netmiko """


def ssh():
    # Call Connect Handler function from Netmiko Library
    from netmiko import ConnectHandler
    ip = input("Enter your IP: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    connection = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    ssh_connect = ConnectHandler(**connection)  # Establish SSH session with HOST
    if ssh_connect:  # Check if the connection established !
        print("Connection Succeeded !\n")

    output = ssh_connect.send_config_set("hostname x")  # Send this configuration into configure terminal
    output = ssh_connect.send_command("show version")  # Send this command into enable mode

    ssh_connect.save_config()
    print(output)

#
# def telnet():
#     # Call Connect Handler function from Netmiko Library
#     from netmiko import ConnectHandler
#     ip = input("Enter your IP: ")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     connection = {
#         "device_type": "cisco_ios",
#         "host": ip,
#         "username": username,
#         "password": password,
#     }
#     ssh_connect = ConnectHandler(**connection)  # Establish SSH session with HOST
#     if ssh_connect:  # Check if the connection established !
#         print("Connection Succeeded !\n")
#
#     output = ssh_connect.send_config_set("hostname x")
#     # output = ssh_connect.send_command("show ip int br")
#     ssh_connect.save_config()
#     print(output)
#
#
# user = input("Please choose 'telnet' or 'ssh': ")
# if user == "telnet":
#     telnet()
# else:
#     ssh()
