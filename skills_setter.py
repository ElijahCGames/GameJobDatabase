import json

job_json = "JobDatabase.json"
skill_json = "SkillDatabase.json"

def json_to_dict(json_file):
    with open(json_file,"r") as j:
        data = json.loads(j.read())
    return data

def dict_to_json(json_file,data):
    with open(json_file,"w+") as f:
        f.write(json.dumps(data,sort_keys=True,indent=4))

if __name__ == '__main__':
    jobdata = json_to_dict(job_json)
    skills = {}
    for job in jobdata:
        for skilltype,listing in job["Skills"].items():
            if(skilltype in skills):
                [skills[skilltype].append(item) for item in listing if item not in skills[skilltype]]
            else:
                {skills[skilltype][item] for item in listing}

    dict_to_json(skill_json,skills)
    print("Complete")
