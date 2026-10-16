import socket
import sys
import random #for generating rdm int

# Specify Host and Port
HOST = '192.168.0.5'
PORT = 23

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # With the help of bind() function
    # binding host and port
    soc.bind((HOST, PORT))

except socket.error as message:

    # if any error occurs then with the
    # help of sys.exit() exit from the program
    print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
    sys.exit()

# print if Socket binding operation completed
print('Socket binding operation completed')

# With the help of listening() function
# starts listening
soc.listen(9)

conn, address = soc.accept()
# print the address of connection
print('Connected with ' + address[0] + ':'
      + str(address[1]))

def generate_question(): ##To generate random number and create question
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*']) # random operator can add , '/'
    question = f'Solve the math question\r\n\r\n\r\n||=======|=======|=======||\
\r\n\
\r\n||   {num1}   |   {operator:}   |   {num2}   ||\
\r\n\
\r\n||=======|=======|=======||\r\n\r\n\r\n'
    answer = eval(f"{num1} {operator} {num2}") ## calculate ans and return with an int output
    return question, answer

while True:
    # generate a random math question
    question, answer = generate_question()

    # send/output the question to the client
    conn.sendall(question.encode('utf-8'))

    # receive the client's answer
    client_input = ""
    while True:
        data = conn.recv(1024).decode('utf-8')
        if '\n' in data: #to see whether the user has entered a string, if not. The code will run in a loop
            break
        client_input += data


    #  check / verify the answer
    try:
        if float(client_input) == answer:
            response = "Correct!\r\n\r\n"
        else:
            response = f"Incorrect. The correct answer is {answer}.\r\n\r\n"
    except ValueError: #if the input is str or other value
        response = "Invalid input. Please enter a valid number.\r\n\r\n"

    # Respond to the client
    conn.sendall(response.encode('utf-8'))
