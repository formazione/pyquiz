# pyquiz 0.1 # 00 # 01
from random import shuffle
import sys, time
import os

class Dic:
	def __init__(self, filename):
		self.filename = filename
		self.list_from_file()
		self.dic_from_list()

	def list_from_file(self):
		"Create a list from the file with data"
		self.list_of_questions = []
		text = ""
		with open(self.filename) as file:
			for line in file:
				text += line.strip()
				if line == "\n":
					self.list_of_questions.append(text[:-1])
					text = ""
				else:
					text += "#"
			self.list_of_questions.append(text[:-1])
	
	def dic_from_list(self):
		"Create a dictionary from self.questions"
		self.dict_of_questions = {}
		counter = 0
		for q in self.list_of_questions:
			counter += 1
			qna = q.split("#")
			self.dict_of_questions[f"question{counter}"] = qna
	
	def print_at_console(self):
		"Print at console"
		for x in self.dict_of_questions:
			print("=====================")
			self.texttime(self.dict_of_questions[x][0])
			print("=====================")
			rnd_ans = self.dict_of_questions[x][1:]
			shuffle(rnd_ans)
			for qna in rnd_ans:
				print(qna)
			print("---------\n")
			ans = input("What you choose? ")
			print("\n"*10)
			if ans == self.dict_of_questions[x][1]:
				self.texttime("> You are right\n")
			else:
				self.texttime("> No, your are wrong\n")
			input("Hit enter")
			print("\n"*10)

	def texttime(self, words):
		for c in words:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.1)

	def shuffle(self):
		shuffle(self.list_of_questions)
		self.dic_from_list()


questions1 = Dic("questions\\tourism.txt")
questions1.shuffle()
questions1.print_at_console()
