import smtplib
from email.MIMEBase import MIMEBase
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import getpass
import fbchat
from pyautogui import *
your_mode= confirm(text='Enter the Mode you want to work in',title='Mode details:Multi Messenger',buttons=['TERMINAL MODE','DIALOG MODE'])
if (your_mode == "TERMINAL MODE"):
		print """-------------------------------------------------------------------------
				------------------------------------------
				|	WELCOME TO MULTIMESSENGER    		  
				|								 
				|	BUILT BY:					 
				|					 
				|		Kushashwa Ravi Shrimali
				                Krutika Bapat 
				|								 		
				|	Undergraduate Students at:	 		  
				|		IIIT NAYA RAIPUR		 		 
				|		(B.Tech CSE)			 		 
				------------------------------------------
		-------------------------------------------------------------------------"""
		# DETAILS - Email
		print "-------------------------------------------------------------------------"
		print 'Enter your Email-ID details' 
		print "-------------------------------------------------------------------------"

		your_adr = raw_input("Your email-ID: ")
		pass_adr = getpass.getpass()

		# DETAILS - Facebook Message

		print "-------------------------------------------------------------------------"
		print 'Enter your Facebook Details'
		print "-------------------------------------------------------------------------"
		your_id = str(raw_input("Enter your username: "))
		pass_fb = getpass.getpass()

		# DETAILS - SMS 

		print "-------------------------------------------------------------------------"
		print 'Enter your SMS Details'
		print "-------------------------------------------------------------------------"

		ACCOUNT_SID = raw_input("Account SID: ") # <auth sid>
		AUTH_TOKEN = raw_input("Account Token: ") # <auth token>
		fromNumber = str(raw_input("Enter your number: "))
		exit_input = raw_input("""If you want to exit, type "EXIT", else Press any key.""")
		while(exit_input != "EXIT"):
			# MENU
			print " EMAIL [1]  |  FACEBOOK MESSAGE [2] |  SMS [3] " 

			number = int(raw_input("Menu Selection: "))

			if(number == 1):
			  rec_adr = raw_input("Receiver's email ID: ")

			  msg = MIMEMultipart()

			  subj = raw_input("Subject: ")
			  msg['From'] = your_adr
			  msg['To'] = rec_adr
			  msg['Subject'] = subj

			  body = raw_input("Text you want to enter: ")

			  msg.attach(MIMEText(body, 'plain'))

			  strings = raw_input("Enter file address: ")
			  if(strings != ''):
				  attachment = open(strings, "rb")
				  part = MIMEBase('application', 'octet-stream')
				  part.set_payload((attachment).read())
				  encoders.encode_base64(part)
				  part.add_header('Content-Disposition', "attachment; filename = %s" % strings)
					
			  msg.attach(part)

			  server = smtplib.SMTP('smtp.gmail.com', 587)
			  server.starttls()
			  server.login(your_adr, pass_adr)
			  text = msg.as_string()
			  server.sendmail(your_adr, rec_adr, text)
			  server.quit()
			  
			# FB CHAT
			elif(number == 2):
			  client = fbchat.Client(your_id, pass_fb);
			  print "Type your friend's name: "
			  fname = str(raw_input("Enter friend's name: "))
			  friends = client.getUsers(fname)

			  friend = friends[0]
			  messagetosend = str(raw_input("Message to send: "))
			  sent = client.send(friend.uid, messagetosend)
			  if sent:
				print("Message sent successfully")
			  else:
				print("Message Sending Failed")
				
			# SMS 
			elif(number == 3):
			  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

			  # Input details
			  ToNumber = str(raw_input("Enter the number you want to send SMS: "))
			  bodyText = str(raw_input("Enter text you want to enter: "))
			  client.messages.create(
				to = '+91' + ToNumber,
				from_ = '+' + fromNumber , #<fromNumber>
				body = bodyText,
			  )
			exit_input = raw_input("""If you want to exit, type "EXIT", else Press any key.""")
elif(your_mode =="DIALOG MODE"):

		st_input = "Get-Started"	

		if (st_input == "Get-Started"):
			alert(text = 'You will be asked for some information now. Follow The Instructions.', title='Multi-Messenger', button = 'OK')
			# DETAILS - Email
			# print "-------------------------------------------------------------------------"
			# print 'Enter your Email-ID details' 
			# print "-------------------------------------------------------------------------"
			
			your_adr = prompt(text='Enter your Email ID', title='Gmail Details:Multi-Messenger', default='')
			#your_adr = raw_input("Your email-ID: ")
			pass_adr = password(text='Type your Gmail Password', title='Gmail Details:Multi-Messenger', default='', mask='*')

			# DETAILS - Facebook Message

			# print "-------------------------------------------------------------------------"
			# print 'Enter your Facebook Details'
			# print "-------------------------------------------------------------------------"
			your_id = prompt(text='Enter your Facebook Username', title='FB Details:Multi-Messenger', default='')
			#your_id = str(raw_input("Enter your username: "))
			pass_fb = password(text='Type your Facebook Password', title='Facebook Detials:Multi-Messenger', default='', mask='*')

			# DETAILS - SMS 

			# print "-------------------------------------------------------------------------"
			# print 'Enter your SMS Details'
			# print "-------------------------------------------------------------------------"

			ACCOUNT_SID = prompt(text='Enter your Account SID', title='Twili Details:Multi-Messenger', default='')
			# ACCOUNT_SID = raw_input("Account SID: ") # <auth sid>
			AUTH_TOKEN = prompt(text='Enter your token', title='Twilio Details:Multi-Messenger', default='')
			# AUTH_TOKEN = raw_input("Account Token: ") # <auth token>
			fromNumber = prompt(text='Enter your Twilio Number', title='Twilio Details:Multi-Messenger', default='')
			# fromNumber = str(raw_input("Enter your number: "))
			exit_input = confirm(text='Do you want to continue?', title='Confirm Message:Multi-Messenger', buttons=['YES','NO'])
			# exit_input = raw_input("""If you want to exit, type "EXIT", if not, type anything else.""")
			while(exit_input != "NO"):
				# MENU
				# print " EMAIL [1]  |  FACEBOOK MESSAGE [2] |  SMS [3] " 
			
				number = confirm(text='Select Menu Option?', title='Menu Details:Multi-Messenger', buttons=['EMAIL','FB MESSAGE', 'SMS'])
				# number = int(raw_input("Menu Selection: "))
				# EMAILING
				if(number == "EMAIL"):
					# print  "-------------------------------------------------------------------------"
					rec_adr = prompt(text="Enter receiver's email ID", title='EMAILING:Multi-Messenger', default='')
					# rec_adr = raw_input("Receiver's email ID: ")
					# print  "-------------------------------------------------------------------------"
					msg = MIMEMultipart()
					subj = prompt(text='Subject', title='EMAILING:Multi-Messenger', default='')
					#subj = raw_input("Subject: ")
					msg['From'] = your_adr
					msg['To'] = rec_adr
					msg['Subject'] = subj
					# print  "-------------------------------------------------------------------------"
					body = prompt(text='Body', title='EMAILING:Multi-Messenger', default='')
					# body = raw_input("Text you want to enter: ")
					msg.attach(MIMEText(body, 'plain'))
					# print  "-------------------------------------------------------------------------"
					ask_attach = confirm(text='Do you want to attach any files?', title='Attaching Files:Multi-Messenger', buttons=['YES','NO'])
					# ask_attach = raw_input("Do you want to attach any files to your mail?(YES/NO): ")
					print  "-------------------------------------------------------------------------"
					while(ask_attach == "YES"):
						strings = prompt(text='Enter file address', title = 'FILE ADDRESS:Multi-Messenger', default='')
						# strings = raw_input("Enter file address: ")
						attachment = open(strings, "rb")
						part = MIMEBase('application', 'octet-stream')
						part.set_payload((attachment).read())
						encoders.encode_base64(part)
						part.add_header('Content-Disposition', "attachment; filename = %s" % strings)

						msg.attach(part)
						# print  "-------------------------------------------------------------------------"
						ask_attach = confirm(text='Do you want to attach more files?', title='Attaching Files:Multi-Messenger', buttons=['YES','NO'])
						# print  "-------------------------------------------------------------------------"

					#print "-------------------------------------------------------------------------"

					#print "Sending mail process has begun!"
					try:
						server = smtplib.SMTP('smtp.gmail.com', 587)
						server.starttls()
						#print "Logging in..."
						server.login(your_adr, pass_adr)
						text = msg.as_string()
						#print "Sending mail..."
						server.sendmail(your_adr, rec_adr, text)
						server.quit()
						alert(text='MAIL SENT SUCCESSFULLY. THANK YOU FOR USING MULTI-MESSENGER', title='Success:Multi-Messenger', button = 'OK')
						#print "Mail sent successfully."
						#print "-------------------------------------------------------------------------"
					except:
						alert(text='MAIL SENDING FAILED. PLEASE CHECK YOUR DETAILS ONCE AGAIN.', title='Failure:Multi-Messenger', button='OK')
						#print("Mail sending failed.")
						#print "-------------------------------------------------------------------------"

				# FB CHAT
				elif(number == "FB MESSAGE"):
					client = fbchat.Client(your_id, pass_fb);
					#print "-------------------------------------------------------------------------"
					#print "Type your friend's name: "
					#print "-------------------------------------------------------------------------"
					fname = prompt(text="Enter friend's name", title='FB MESSAGING:Multi-Messenger', default='')
					#fname = str(raw_input("Enter friend's name: "))
					friends = client.getUsers(fname)
					friend = friends[0]
					messagetosend = prompt(text="Enter message to send", title='FB MESSAGING:Multi-Messenger', default='')
					#messagetosend = str(raw_input("Message to send: "))
					sent = client.send(friend.uid, messagetosend)
					if sent:
						alert(text='MESSAGE SENT SUCCESSFULLY. THANK YOU FOR USING MULTI-MESSENGER', title='Success:Multi-Messenger', button = 'OK')
						#print ("Message sent successfully!")
					else:
						alert(text='MESSAGE SENDING FAILED. PLEASE CHECK YOUR DETAILS ONCE AGAIN.', title='Failure:Multi-Messenger', button='OK')
						#print ("Not sent")
			
				# SMS 
				elif(number == "SMS"):
					client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
					# Input details
					ToNumber = prompt(text="Enter receiver's number", title='SMS:Multi-Messenger', default='')
					#ToNumber = str(raw_input("Enter the number you want to send SMS: "))
					bodyText = prompt(text="Enter message to send", title='SMS:Multi-Messenger', default='')
					#bodyText = str(raw_input("Enter text you want to enter: "))
					client.messages.create(
					to = '+91' + ToNumber,
					from_ = '+' + fromNumber , #<fromNumber>
					body = bodyText,
					)
				exit_input = confirm(text='Do You Want To Continue?', title='Confirm Message:Multi-Messenger', buttons=['YES','NO'])
