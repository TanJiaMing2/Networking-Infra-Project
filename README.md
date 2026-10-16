# Network-Infra-Project
A Network Infrastructure Project during diploma, is about showcasing the basic network connection between other devices using telnet and python
The main purpose is to have a connection between devices. But you can try on single device, but it does not prove anything.


Follow the .txt file instruction on how to run it 

Prerequisites :

-Do note file sharing need to be enabled in the 
-- Window Setting - Network & Internet - Advanced Network setting - Advanced sharing setting - On all the option inside
-Suggested Python version 3.13
-Enabling Telnet feature in Control Panel\Programs\Programs and Features\ Turn Windows Features on and off (Does not require restart)
-Finding your IPv4 address - Go to cmd - type 'ipconfig' - find your ipv4 address in Wireless LAN adapter Wi-Fi: (if WIFI)/ Ethernet adapter Ethernet: (IF Wired)
-- Go to mathcross.py and replace the HOST address with the ipv4 adrress . eg :192.168.0.5 into 192.168.34.134


How to Run:
1. Open Any IDE or Python IDLE and run mathcross.py
2. Ensure the text is 'Socket binding operation completed' in your IDE
3. Open Command Prompt or Telnet to run the game
4. Enter the following command depending on :
- CMD : telnet 192.168.0.8 23   TELNET : open 192.168.0.8 23
5. Input any numeric to anwser to question
6. Rerun the whole script if you Quit the CMD or TELNET
