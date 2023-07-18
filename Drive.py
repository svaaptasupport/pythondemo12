import psutil
import smtplib
from email.mime.text import MIMEText

# Get disk usage statistics
disk_usage = psutil.disk_usage('/')

# Calculate free space in GB
free_space_gb = disk_usage.free / (1024**3)

# Calculate used space in GB
used_space_gb = disk_usage.used / (1024**3)

# Set the email parameters
sender_email = "mytap@svaapta-it-ally.com"
receiver_email = "riteshs@svaapta.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "mytap@svaapta-it-ally.com"
smtp_password = "ondncruhruvgcekf"

# Compose the email message
subject = "Disk Space Notification:-192.168.0.93 Drive D"
message = f"Free space: {free_space_gb:.2f} GB\nUsed space: {used_space_gb:.2f} GB"

# Create a MIMEText object
email_message = MIMEText(message)
email_message["Subject"] = subject
email_message["From"] = sender_email
email_message["To"] = receiver_email

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(email_message)
    print("Notification email sent.")
