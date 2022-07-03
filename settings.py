# Input CSV, see example.csv to see what each field is. The first field is the team number.
input_csv_path = "csv/example.csv"

sender_email = 'quango@student.unimelb.edu.au'

email_body = """
Dear all,

Thank you again for registering your school in the SMO, and congratulations to all the students for their effort and results!

I would still like to forward some things to the students. You'll find your students' participation certificates attached to this email, as well as an editorial for all the problems so students can learn from the problems they didn't solve. (This will go up soon on the website at https://www.melbunimathsstats.org/mathsolympics).

Additionally, plenty of students requested the playlist of math parodies that I played at the start of the session, so please forward them too! Don't worry, they're all G-rated!
https://www.youtube.com/watch?v=uqwC41RDPyg
https://www.youtube.com/watch?v=P9dpTTpjymE
https://www.youtube.com/watch?v=nYXxqX9hbnw
https://www.youtube.com/watch?v=5RefXjF6i7I
https://www.youtube.com/watch?v=-T-0N7X8nMU

If there are any issues/mistakes with the certificates, please let me know and I will fix them!

All the best,
Quang Ong.
"""

# A list of paths to attachments that you would like included in every email. 
# example:  initial_attachment_list = ["attachments/SMO_2021_UPDATED editorials.pdf"]
initial_attachment_list = []
