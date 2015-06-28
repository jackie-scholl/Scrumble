# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
#from requests import get
Vnd_HMH_API_key = "60cd3fc1515eab662a3361ca5c206b00"
import unicodedata

# <codecell>

token={
  "sub": "cn=Sauron O''Rings,uid=sauron_348,uniqueIdentifier=62c40bac-aa25-4983-b3cb-e377cc9fcf43,dc=7477",
  "roles": "Instructor",
  "name": "Sauron O''Rings",
  "ref_id": "62c40bac-aa25-4983-b3cb-e377cc9fcf43",
  "expires_in": 3600,
  "preferred_username": "sauron_348",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkZW50aXR5LmFwaS5obWhjby5jb20iLCJhdWQiOiJodHRwOi8vd3d3LmhtaGNvLmNvbSIsImlhdCI6MTQzNTQzOTkzMSwic3ViIjoiY25cdTAwM2RTYXVyb24gT1x1MDAyN1x1MDAyN1JpbmdzLHVpZFx1MDAzZHNhdXJvbl8zNDgsdW5pcXVlSWRlbnRpZmllclx1MDAzZDYyYzQwYmFjLWFhMjUtNDk4My1iM2NiLWUzNzdjYzlmY2Y0MyxkY1x1MDAzZDc0NzciLCJodHRwOi8vd3d3Lmltc2dsb2JhbC5vcmcvaW1zcHVybC9saXMvdjEvdm9jYWIvcGVyc29uIjpbIkluc3RydWN0b3IiXSwiY2xpZW50X2lkIjoiZGVhYTMxYmYtMjA0MS00ZjE2LTg1MTgtMzJiZDY1OWQ0MzI5LmhtaGNvLmNvbSIsImV4cCI6MTQzNTU0MzE2N30.f-Cm3Pw3fUXsl-EF-cizBjKFHWuyYyd0IuGmVmW6X3Y",
  "access_token": "SIF_HMACSHA256 ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJsa1pXNTBhWFI1TG1Gd2FTNW9iV2hqYnk1amIyMGlMQ0poZFdRaU9pSm9kSFJ3T2k4dmQzZDNMbWh0YUdOdkxtTnZiU0lzSW1saGRDSTZNVFF6TlRRek9Ua3pNU3dpYzNWaUlqb2lZMjVjZFRBd00yUlRZWFZ5YjI0Z1QxeDFNREF5TjF4MU1EQXlOMUpwYm1kekxIVnBaRngxTURBelpITmhkWEp2Ymw4ek5EZ3NkVzVwY1hWbFNXUmxiblJwWm1sbGNseDFNREF6WkRZeVl6UXdZbUZqTFdGaE1qVXRORGs0TXkxaU0yTmlMV1V6Tnpkall6bG1ZMlkwTXl4a1kxeDFNREF6WkRjME56Y2lMQ0pvZEhSd09pOHZkM2QzTG1sdGMyZHNiMkpoYkM1dmNtY3ZhVzF6Y0hWeWJDOXNhWE12ZGpFdmRtOWpZV0l2Y0dWeWMyOXVJanBiSWtsdWMzUnlkV04wYjNJaVhTd2lZMnhwWlc1MFgybGtJam9pWkdWaFlUTXhZbVl0TWpBME1TMDBaakUyTFRnMU1UZ3RNekppWkRZMU9XUTBNekk1TG1odGFHTnZMbU52YlNJc0ltVjRjQ0k2TVRRek5UUTJNRE0yTjMwLlQ5NW5mSVNTRUFndEhaYXpxNTBFNkgxeU9IUXRFR2VhRHNrQkZxSGJyUHc6dDlrb1RFTStpc2xMS2NCd1BDQXE0OGpJTCtJN01LZVhGZUNsc0lFMXZIaz0K"
}
ref=token["ref_id"]
access = token["access_token"]

baseurl = "http://sandbox.api.hmhco.com/v1/"
heads = {"Vnd-HMH-Api-Key":Vnd_HMH_API_key,
           "Accept":"application/json",
#           "Content-Type":"application/x-www-form-urlencoded",
            "Authorization":access}    
staff_sections = requests.get(baseurl+'staffSectionAssociations',headers=heads).json()
student_sections = requests.get(baseurl+'studentSectionAssociations',headers=heads).json()
staff_persons = requests.get(baseurl+"staffPersons",headers=heads).json()
def get_students(teacher_name):
  ref = 0
  for teacher in staff_persons:
    if teacher["userName"]==teacher_name:
      ref = teacher["refId"]
  if ref == 0:
    raise Exception("None of the teachers match the username you provided.")
  teacher_sections = []
  for section in staff_sections:
      try:
          staffer_refid=unicodedata.normalize('NFKD', section["staffPersonRefId"]).encode('ascii','ignore')
          if staffer_refid==str(ref):
              teacher_sections.append(section)
      except TypeError:
          pass
  teacher_sections_refid = [section["refId"] for section in teacher_sections][0]
  teacher_student_refids = []
  for student_and_section in student_sections:
      if student_and_section["sectionRefId"] == teacher_sections_refid:
          teacher_student_refids.append(student_and_section["studentRefId"])
  print(0)



all_students = requests.get(baseurl+'students',headers=heads).json()
student_names_and_ids = [[stud['name']['actualNameOfRecord']['fullName'],stud['refId']] for stud in all_students]
get_students("sauron_348")