import base64
import random

class User:

	def __init__(self, username="", password="", user_id=-1):
		'''
		User constructor
		:param user_id: int, default value -1
		:param username: str, default value "" (empty string)
		:param password: str, default value "" (empty string)
		:return: None
		'''
		self.user_id = user_id
		self.username = username
		self.password = self.encryption(password)

	def generate_unique_user_id(self):
		'''Generate unique id for new registered user'''

		# collect id from all registered users
		content = []
		text_files = [
			'data/user_admin.txt',
			'data/user_student.txt',
			'data/user_instructor.txt'
		]
		for file in text_files:
			with open(file,'r',encoding='utf-8') as f:
				text = f.read().split('\n')
				content.extend(text)
		ids = []
		for c in content:
			if c.strip() != "":
				existing_id = c.strip().split(';;;')[0]
				ids.append(existing_id)
		
		# find a new unique id
		new_id = random.choice(ids)
		while new_id in ids:
			new_id = "".join([str(random.randint(0,9)) for _ in range(10)])
		return new_id

	def encryption(self,password):
		'''
		User password encryption before saved into user_admin.txt, user_student.txt, or user_instructor.txt
		:param password: str
		:return:
		'''
		return base64.b64encode(bytes(password,encoding='utf-8')).decode()

	def login(self):
		pass

	def extract_info(self):
		'''Default user extract info message'''
		print('You have no premission to extract information.')

	def view_courses(self,**args):
		'''Default user view courses message'''
		print('You have no permission to view courses')

	def view_users(self):
		'''Default user view users message'''
		print('You have no permission to view users')

	def view_reviews(self,**args):
		'''Default user view reviews message'''
		print('You have no permission to view reviews')

	def remove_data(self):
		'''Default user remove data message'''
		print('You have no permission to remove data')

	def __str__(self):
		'''Object in string format'''
		return ";;;".join([str(self.user_id),self.username,self.password])