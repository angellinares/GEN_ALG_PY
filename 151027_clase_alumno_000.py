#	Student class:
#	Creates a class that defines a student person with the following
#	methods and properties: Age, Repeater, Email, Qualifications, Absent.
#
#	Methods: average qualification, absent more than five classes.

class Student(object):
	"""Creates an student object with Age, Repeater counter, Email, Qualifications and Absent counter"""
	def __init__(self, age, repeater, email):
		self.age = age
		self.repeater = repeater
		self.email = email
		self.aveQualif = 0
		self.qualifications = []
		self.absentCounter = 0

	def addAbsent(self,absentNumber):

		self.absentCounter += absentNumber

		if self.absentCounter >= 5:
			print "WARNING!: the student has been absent in more than 5 sessions"
			print "AbsentCounter: %d" % self.absentCounter

	def requestAverageQ(self):

		if len(self.qualifications) == 0:

			print "Any qualification of this student was given to the system yet"
			print "Please, add qualifications using self.addQualification method"

		else:

			self.aveQualif = sum(self.qualifications)/len(self.qualifications)
			print "Average qualification: %d" %self.aveQualif

	def addQualification(self,qualification):

		self.qualifications += qualification
		self.requestAverageQ()


Pedro = Student(35,False,"Pedro@gmail.com")
Pedro.addAbsent(6)
Pedro.addQualification([5,7.25,4.5])
Pedro.addQualification([3,4.25])

