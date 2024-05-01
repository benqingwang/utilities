import extract_msg
from datetime import datetime

try:
    # Open the .msg file
    with extract_msg.openMsg(msg_file_path) as msg:
        # Extract the date the email was sent
        sent_date = msg.date
        # Format the date
        formatted_date = datetime.strftime(sent_date, '%Y-%m-%d %H:%M:%S')

        print('Formatted Sent Date:', formatted_date)

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)
