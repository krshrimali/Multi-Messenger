from twilio.rest import TwilioRestClient
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import getpass
import fbchat
from pyautogui import *

st_input = prompt(text='Terminal/dialog', title='Multi-Messenger', default='')

if (st_input == "dialog"):
	# Alert 
	alert(text = 'You will be asked for some information now. Move on as directed.', title='Multi-Messenger', button = 'OK')
	
	# EMAIL DETAILS
	your_adr = prompt(text='Enter your Email ID', title='Gmail Details:Multi-Messenger', default='')
	pass_adr = password(text='Type your Gmail Password', title='Gmail Details:Multi-Messenger', default='', mask='*')
	
	# FB DETAILS
	your_id = prompt(text='Enter your FB Username', title='FB Details:Multi-Messenger', default='')
	pass_fb = password(text='Type your Facebook Password', title='Facebook Detials:Multi-Messenger', default='', mask='*')
	
	# TWILIO DETAILS
	ACCOUNT_SID = prompt(text='Enter your Account SID', title='Twili Details:Multi-Messenger', default='')
	AUTH_TOKEN = prompt(text='Enter your token', title='Twilio Details:Multi-Messenger', default='')
	fromNumber = prompt(text='Enter your Twilio Number', title='Twilio Details:Multi-Messenger', default='')
	
	exit_input = confirm(text='Do you want to carry on?', title='Confirm Message:Multi-Messenger', buttons=['YES','NO'])
	
	while(exit_input != "NO"):
		# MENU SELECTION
		number = confirm(text='Which Menu option do you want to select?', title='Menu Details:Multi-Messenger', buttons=['EMAIL','FB MESSAGE', 'SMS'])
		# EMAILING
		if(number == "EMAIL"):
			rec_adr = prompt(text="Enter receiver's email ID", title='EMAILING:Multi-Messenger', default='')
			msg = MIMEMultipart()
			subj = prompt(text='Subject', title='EMAILING:Multi-Messenger', default='')
			msg['From'] = your_adr
			msg['To'] = rec_adr
			msg['Subject'] = subj
			body = prompt(text='Body', title='EMAILING:Multi-Messenger', default='')
			msg.attach(MIMEText(body, 'plain'))
			ask_attach = confirm(text='Do you want to attach any files?', title='Attaching Files:Multi-Messenger', buttons=['YES','NO'])
			while(ask_attach == "YES"):
				strings = prompt(text='Enter file address', title = 'FILE ADDRESS:Multi-Messenger', default='')
				attachment = open(strings, "rb")
				part = MIMEBase('application', 'octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename = %s" % strings)

				msg.attach(part)
				ask_attach = confirm(text='Do you want to attach more files?', title='Attaching Files:Multi-Messenger', buttons=['YES','NO'])
			try:
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				server.login(your_adr, pass_adr)
				text = msg.as_string()
				server.sendmail(your_adr, rec_adr, text)
				server.quit()
				alert(text='MAIL SENT SUCCESSFULLY. THANK YOU FOR USING MULTI-MESSENGER', title='Success:Multi-Messenger', button = 'OK')
			except:
				alert(text='MAIL SENDING FAILED. PLEASE CHECK YOUR DETAILS ONCE AGAIN.', title='Failure:Multi-Messenger', button='OK')
		# FB CHAT
		elif(number == "FB MESSAGE"):
			client = fbchat.Client(your_id, pass_fb);
			fname = prompt(text="Enter friend's name", title='FB MESSAGING:Multi-Messenger', default='')
			friends = client.getUsers(fname)
			friend = friends[0]
			messagetosend = prompt(text="Enter message to send", title='FB MESSAGING:Multi-Messenger', default='')
			sent = client.send(friend.uid, messagetosend)
			if sent:
				alert(text='MESSAGE SENT SUCCESSFULLY. THANK YOU FOR USING MULTI-MESSENGER', title='Success:Multi-Messenger', button = 'OK')
			else:
				alert(text='MESSAGE SENDING FAILED. PLEASE CHECK YOUR DETAILS ONCE AGAIN.', title='Failure:Multi-Messenger', button='OK')
	
		# SMS 
		elif(number == "SMS"):
			client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
			ToNumber = prompt(text="Enter receiver's number", title='SMS:Multi-Messenger', default='')
			bodyText = prompt(text="Enter message to send", title='SMS:Multi-Messenger', default='')
			client.messages.create(
			to = '+91' + ToNumber,
			from_ = '+' + fromNumber ,
			body = bodyText,
			)
		exit_input = confirm(text='Do you want to carry on?', title='Confirm Message:Multi-Messenger', buttons=['YES','NO'])
		alert('Thank you for using Multi-Messenger. A project by Krutika Bapat and Kushashwa Ravi Shrimali.', title='Multi-Messenger', button='OK')
else:
	
	print """-------------------------------------------------------------------------
			------------------------------------------
			|	WELCOME TO MULTIMESSENGER    		  
			|								 
			|	BUILT BY:					 
			|		Krutika Bapat			 
			|		Kushashwa Ravi Shrimali
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
	exit_input = raw_input("""If you want to exit, type "EXIT", if not, type anything else.""")
	while(exit_input != "EXIT"):
		# MENU
		print " EMAIL [1]  |  FACEBOOK MESSAGE [2] |  SMS [3] " 
		
		number = int(raw_input("Menu Selection: "))
		# EMAILING
		if(number == 1):
			print  "-------------------------------------------------------------------------"
			rec_adr = raw_input("Receiver's email ID: ")
			print  "-------------------------------------------------------------------------"
			msg = MIMEMultipart()
			subj = raw_input("Subject: ")
			msg['From'] = your_adr
			msg['To'] = rec_adr
			msg['Subject'] = subj
			print  "-------------------------------------------------------------------------"
			body = raw_input("Text you want to enter: ")
			msg.attach(MIMEText(body, 'plain'))
			print  "-------------------------------------------------------------------------"
			ask_attach = raw_input("Do you want to attach any files to your mail?(YES/NO): ")
			print  "-------------------------------------------------------------------------"
			while(ask_attach.upper() != 'NO'):
				strings = raw_input("Enter file address: ")
				attachment = open(strings, "rb")
				part = MIMEBase('application', 'octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename = %s" % strings)

				msg.attach(part)
				# print  "-------------------------------------------------------------------------"
				ask_attach = raw_input("Do you want to attach any more files to your mail? (YES/NO): ")
				# print  "-------------------------------------------------------------------------"

			print "-------------------------------------------------------------------------"

			print "Sending mail process has begun!"
			try:
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				print "Logging in..."
				server.login(your_adr, pass_adr)
				text = msg.as_string()
				print "Sending mail..."
				server.sendmail(your_adr, rec_adr, text)
				server.quit()
				print "Mail sent successfully."
				print "-------------------------------------------------------------------------"
			except:
				print("Mail sending failed.")
				print "-------------------------------------------------------------------------"

		# FB CHAT
		elif(number == 2):
			client = fbchat.Client(your_id, pass_fb);
			print "-------------------------------------------------------------------------"
			print "Type your friend's name: "
			print "-------------------------------------------------------------------------"
			fname = str(raw_input("Enter friend's name: "))
			friends = client.getUsers(fname)

			friend = friends[0]
			messagetosend = str(raw_input("Message to send: "))
			sent = client.send(friend.uid, messagetosend)
			if sent:
				print ("Message sent successfully!")
			else:
				print ("Not sent")
			
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
		exit_input = raw_input("""If you want to exit, type "EXIT", if not, type anything else.""")
		print ('Thank you for using Multi-Messenger. A project by Krutika Bapat and Kushashwa Ravi Shrimali.')
