# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
#from requests import get
Vnd_HMH_API_key = "60cd3fc1515eab662a3361ca5c206b00"
BASEURL = "http://sandbox.api.hmhco.com/v1/"
import unicodedata
TOKEN={
  "sub": "cn=Sauron O''Rings,uid=sauron_348,uniqueIdentifier=62c40bac-aa25-4983-b3cb-e377cc9fcf43,dc=7477",
  "roles": "Instructor",
  "name": "Sauron O''Rings",
  "ref_id": "62c40bac-aa25-4983-b3cb-e377cc9fcf43",
  "expires_in": 86000,
  "preferred_username": "sauron_348",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkZW50aXR5LmFwaS5obWhjby5jb20iLCJhdWQiOiJodHRwOi8vd3d3LmhtaGNvLmNvbSIsImlhdCI6MTQzNTQ5Njk0NCwic3ViIjoiY25cdTAwM2RTYXVyb24gT1x1MDAyN1x1MDAyN1JpbmdzLHVpZFx1MDAzZHNhdXJvbl8zNDgsdW5pcXVlSWRlbnRpZmllclx1MDAzZDYyYzQwYmFjLWFhMjUtNDk4My1iM2NiLWUzNzdjYzlmY2Y0MyxkY1x1MDAzZDc0NzciLCJodHRwOi8vd3d3Lmltc2dsb2JhbC5vcmcvaW1zcHVybC9saXMvdjEvdm9jYWIvcGVyc29uIjpbIkluc3RydWN0b3IiXSwiY2xpZW50X2lkIjoiZGVhYTMxYmYtMjA0MS00ZjE2LTg1MTgtMzJiZDY1OWQ0MzI5LmhtaGNvLmNvbSIsImV4cCI6MTQzNTU4ODUwNn0.lEfVXKybGWl68KLFKEYqKPmEfSjlhebqCLDPpG59NSM",
  "access_token": "SIF_HMACSHA256 ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJsa1pXNTBhWFI1TG1Gd2FTNW9iV2hqYnk1amIyMGlMQ0poZFdRaU9pSm9kSFJ3T2k4dmQzZDNMbWh0YUdOdkxtTnZiU0lzSW1saGRDSTZNVFF6TlRRNU5qazBOQ3dpYzNWaUlqb2lZMjVjZFRBd00yUlRZWFZ5YjI0Z1QxeDFNREF5TjF4MU1EQXlOMUpwYm1kekxIVnBaRngxTURBelpITmhkWEp2Ymw4ek5EZ3NkVzVwY1hWbFNXUmxiblJwWm1sbGNseDFNREF6WkRZeVl6UXdZbUZqTFdGaE1qVXRORGs0TXkxaU0yTmlMV1V6Tnpkall6bG1ZMlkwTXl4a1kxeDFNREF6WkRjME56Y2lMQ0pvZEhSd09pOHZkM2QzTG1sdGMyZHNiMkpoYkM1dmNtY3ZhVzF6Y0hWeWJDOXNhWE12ZGpFdmRtOWpZV0l2Y0dWeWMyOXVJanBiSWtsdWMzUnlkV04wYjNJaVhTd2lZMnhwWlc1MFgybGtJam9pWkdWaFlUTXhZbVl0TWpBME1TMDBaakUyTFRnMU1UZ3RNekppWkRZMU9XUTBNekk1TG1odGFHTnZMbU52YlNJc0ltVjRjQ0k2TVRRek5UVTRPREV3Tm4wLjJfSG1DRGMxSjR3aGl0NllYOEFpYVhYdzBHbElwd0JucUh4OHFXazZWTEU6L2IwNTJZOVh0SUJsbTVjT1IyU0F3WTRUdnp6MC9qcFFGbWN3WGVTNFJTbz0K"
}
#TOKEN=requests.get(BASEURL+"token",headers={"Vnd-HMH-Api-Key":Vnd_HMH_API_key,"Accept":"application/json"},params={
#	"client_id":"deaa31bf-2041-4f16-8518-32bd659d4329.hmhco.com","grant_type":"password","username":"sauron_348","password":"password"}).json()

# access = token["access_token"]



HEADS = {"Vnd-HMH-Api-Key":Vnd_HMH_API_key,
 			 "Accept":"application/json",
#           "Content-Type":"application/x-www-form-urlencoded",
 			"Authorization":TOKEN["access_token"]} 

STAFF_SECTIONS = requests.get(BASEURL+'staffSectionAssociations',headers=HEADS).json()
STUDENT_SECTIONS = requests.get(BASEURL+'studentSectionAssociations',headers=HEADS).json()
STAFF_PERSONS = requests.get(BASEURL+"staffPersons",headers=HEADS).json()
STUDENTS = requests.get(BASEURL+"students",headers=HEADS).json()
glob = {"token":TOKEN,"access":TOKEN["access_token"],"base":"http://sandbox.api.hmhco.com/v1/","heads":HEADS,
				"staff_sections":STAFF_SECTIONS,"student_sections":STUDENT_SECTIONS,"staff_persons":STAFF_PERSONS,"students":STUDENTS}
def get_students(teacher_name):
	ref = get_teacherRefId_from_name(teacher_name)
	teacher_sections = get_sections_of_teacher(ref)
	#Currently works for teachers who teach one section only.
	student_refids=get_student_refids([section["sectionRefId"] for section in teacher_sections][0])
	return get_student_names_from_refids(student_refids)

def get_student_refids(section_id):
	teacher_student_refids = []
	for student_and_section in glob["student_sections"]:
		if student_and_section["sectionRefId"] == section_id:
			teacher_student_refids.append(student_and_section["studentRefId"])
	return teacher_student_refids

def get_sections_of_teacher(teacherRefId):
	teacher_sections = []
	for section in STAFF_SECTIONS:
		try:
			staffer_refid=unicodedata.normalize('NFKD', section["staffPersonRefId"]).encode('ascii','ignore')
			if staffer_refid==str(teacherRefId):
				teacher_sections.append(section)
		except TypeError:
			pass
	return teacher_sections

def get_teacherRefId_from_name(teacherName):
	ref = 0
	for teacher in glob["staff_persons"]:
		if teacher["userName"]==teacherName:
			ref = teacher["refId"]
	if ref == 0:
		raise Exception("None of the teachers match the username you provided.")
	return ref

def get_student_names_from_refids(student_refid_list):
	return [requests.get(glob["base"]+"students/"+refid,headers=HEADS).json(
		)['name']['actualNameOfRecord']['fullName'] for refid in student_refid_list]

def save_file(fileName):
	"""Saves a file of a given name, and returns the json response."""
	return requests.post(BASEURL+"documents",headers=HEADS,files={'requester.py': open('requester.py', 'rb')})
def make_assignment(assignment_dictionary):
	#h=HEADS.copy()
	#h.update(assignment_dictionary)
	return requests.post(BASEURL+"assignments",headers=HEADS,data=assignment_dictionary)
def edit_assignment(assignment_dictionary,id):
	return requests.post(BASEURL+"assignments/"+id,headers=HEADS,data=assignment_dictionary)
def del_assignment(id):
	return requests.delete(BASEURL+"assignments/"+id,headers=HEADS)
#all_students = requests.get(BASEURL+'students',headers=HEADS).json()
#student_names_and_ids = [[stud['name']['actualNameOfRecord']['fullName'],stud['refId']] for stud in all_students]

if __name__ == "__main__":
	print(get_students("sauron_348"))
	print(get_students("gandalf_348"))
	#print(get_students("galadriel_348"))
