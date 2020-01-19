"""
Takes in the supplied csv file and converts the file into a JSON file.

Also: Cleans the csv to put items like skills into their own level of the JSON file
Removes spaces from the end of the headers
"""

import csv
import json

#File names
csv_file_path = "datas.csv"
json_file_path = "JobDatabase.json"

# List of skills for the skills step
list_items = ["Soft Skills ","Writing Hard Skills Required","Art Hard Skills Required","Audio Hard Skills Required","Design Hard Skills Required","Production Hard Skills Required","Programming Hard Skills Required"]

# Imports the csv file into a dictionaries
def read_in_csv():
    """
    Converts job csv to dictionary.

    Outputs:
        job_data (List of Dicts)
    """
    with open(csv_file_path,'r') as f:
        job_data = [dict(x) for x in csv.DictReader(f)]
    return job_data

def add_hard(job,i):
    """
    Adds Additional Hard Skills to Skills item.

    Inputs:
        job (Dict)
        i (integer) - Index for the string

    Output:
        job
    """
    hard_label = "Additional Hard Skill " + str(i+1)
    if(job[hard_label] != ""):
        job["Skills"]["Hard"].append(job[hard_label])
    job.pop(hard_label)
    return job

def add_soft(job,i):
    """
    Adds Additional Soft Skills to Skills item.

    Inputs:
        job (Dict)
        i (integer) - Index for the string

    Output:
        job
    """
    soft_label = "Additional Soft Skill " + str(i+1)
    if(job[soft_label] != ""):
        job["Skills"]["Soft"].append(job[soft_label])
    job.pop(soft_label)
    return job

def add_id(job_data):
    for job in job_data:
        job["ID"] = int(abs(hash(job["Link to Post"]))/10**10)
# SKILLS STEP
def clean_data(job_data):
    """
    Cleans up the data, focusing on compacting skills information

    Inputs:
        job_data (List of Dicts)
    Ouptus:
        job_data
    """
    #For single job in the data
    for job in job_data:
        # Add a skills item
        job["Skills"] = {}
        job["Skills"]["Hard"] = []
        # Loop through the skills list
        for item in list_items:
            if(len(job[item])>0):
                #If there are skills, add them to the skills item
                job["Skills"][item.replace(" Hard Skills Required","").replace(" Skills ","")] = job[item].split(", ")
            # Remove the skills rows
            job.pop(item)

        # Manage those sneaky Additional Skills
        for i in range(12):
            job = add_hard(job,i)
            if(i<6):
                job = add_soft(job,i)
    add_id(job_data);
    return job_data

def to_json(job_data):
    """
    Takes a list of jobs and turns it into a json file

    Input:
        job_data (List of dicts)
    """
    with open(json_file_path,'w+') as j:
        j.write(json.dumps(job_data,sort_keys=True,indent=4))

if __name__ == "__main__":
    to_json(clean_data(read_in_csv()))
