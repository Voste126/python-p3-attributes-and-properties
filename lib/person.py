#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            print("Name must be string between 1 and 25 characters.")  

        elif len(value) > 25: 
            print("Name must be string between 1 and 25 characters.") 

        elif len(value) < 1:
            print("Name must be string between 1 and 25 characters.")

        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.") 
        else:
            self._job = value
