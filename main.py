import jinja2
import os
from jinja2 import Template
import mimetypes
from email_test import send_message, gmail_authenticate
from settings import email_body, input_csv_path, initial_attachment_list
import re
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template('template/template.tex')

def make_attachment(student, school):
    file_title = "_".join(re.split(" |'",student))
    with open(f"rendering/{file_title}.tex","w") as f:
        f.write(template.render(name=student, school = school))
    
    os.system(f'latexmk -pdf -quiet "rendering/{file_title}.tex"')
    os.system(f'latexmk -c "{file_title}.pdf"')    
    os.system(f'mv "{file_title}.pdf" attachments')
    return file_title

service = gmail_authenticate()

# TODO: Make csv_file a setting
def do_everything(csv_file):
	with open(csv_file,"r") as f:
		for line in f:
			stuff = line.split(",")
			team_number = int(stuff[0])
			recipient = stuff[1]
			school = stuff[2]
			unclean_students = stuff[4:]
			students = []
			for student in unclean_students:
				student = student.strip()
				if (len(student) <= 1):
					continue
				students.append(student)

				# names = []
				# for name in student.split():
				# 	name = name.lower()
				# 	name = name[0].upper() + name[1:]
				# 	names.append(name)
				# students.append(" ".join(names))
				# print(" ".join(names))
			if (len(students) == 0):
				continue
			
			# print(students)
			attachments = initial_attachment_list.copy()
			for student in students:
				attachments.append(f"attachments/{make_attachment(student,school)}.pdf")

			print(f"Sending email for team {team_number}...")
			try:
				send_message(service, recipient, f"SMO2021 wrap-up for team {team_number}", 
				email_body, attachments)
				print(f"\n\n\n\n\n-------------------Sent email for team {team_number}")

			except Exception as e:
				print(e)

do_everything(input_csv_path)
