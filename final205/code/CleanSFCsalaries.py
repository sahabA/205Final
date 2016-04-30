import numpy as np
import pandas as pd
import sexmachine.detector as gender
#load data
data = pd.read_csv('Salaries.csv', header=0)
#placeholder 
data['Gender'] = data['EmployeeName']
d = gender.Detector(case_sensitive=False)
data['Name'] = data['EmployeeName'].str.split()
#this will take forever- assign gender
for i in range(0, 148654):
    data['Gender'][i] = d.get_gender(data['Name'][i][0])
#andy = non-gender specific
#combine all males and females
data = data[data.Gender != 'andy']
data['Gender'] = data['Gender'].map({'male': 'male', 'female':
                                     
                                     'female', 'mostly_male': 
                                     'male','mostly_female': 'female'})
def find_grade(row):
    
    title = row.lower()
    #if deputy court clerk / mark clerk, court and deputy
    #if only deputy ignore
    executive = ['assitant chief', 'assistant director', 'assistant deputy', 'gen mgr',
                     'asst dir', 'asst ch', 'deputy director', 'dpty', 'board secretary', 'general manager',
                 'dep dir', 'dept head', 'deputy chief', 'deputy dir',
                     'dep chf', 'department head']
    upperM = ['chief', 'chf', 'deputy', 'sherif',   'head', 'director', 'captain']
    grade = ['intern', 'apprentice', 'prinipal', 'associate', 'junior','senior','sergeant', 'officer', 'lieut',' commander'
             '1','2', '3', '4',  'iii', ' iv', 'ii', ' i']
    manager = ['manag', 'mgr']  
    sup = ['supervisor', 'supv', 'sprv']
    asst = ['assitant', 'asst']
    #if assistant job has not other category
    adm = ['aide', 'secretary','sctry', 'attendant']
    for t in executive:        
        if t in title:
            #set other stuff the same
            return 'executive'        
    for t in upperM:
        if t in title:
            return'upperManagement'
    for t in manager:
        if t in title:
            return 'manager'
    for t in sup:
        if t in title:
            return'supervisor'
    for t in asst:
        if t in title:
            return'assistant'
    for t in adm:
        if t in title:
            return'aide'
    for t in grade:
        if t in title:
            return t
    return 'other'
	
def find_job_title(row):
    title = row.lower()
    #if deputy court clerk / mark clerk, court and deputy
    #if only deputy ignore
    executive = [  'assistant deputy',  'dpty', 'board secretary'                 
                      ] 
    gm = ['general manager', 'gen mgr']
    dep_dir = ['dep dir','deputy director', 'deputy dir',]
    dep_head = ['dept head','department head']
    dep_chief = ['deputy chief','dep chf']
    asst_dir= ['asst dir','assistant director']
    asst_chf = ['assitant chief',  'asst ch']
                     #'special assistant', manually
    #generic - serparating the same ones
    gen_title = ['sherif', 'probation', 'sergeant', 'officer', 'lieut', 'chemist', 'tech', 'nurs','captain',
                 'pharm', 'inspector','accountant', 'clerk', 'examiner', 'analyst',
                    'paramedic', 'head', 'director', 'sergent', 'senior', 'associate', 'assistant', 'archticet',
                 'electrician',  'investigator',  'carpenter', 'mason', 'worker', 'disp', 'tech',
                 'battalion' ,         'commander', 'plumber', 'painter',  
                      'laborer', 'maintenance', 'repairer', 'cook', 'food',   'gardner', 
                 'auditor', 'commander', 'curator', 'custod', 'specialist',
                      'staff', 'guard', 'attendent', 'nutrionist', 'nurs', 'planner', 'porter', 'lifeguard', 
                 'social worker', 'therap'] #assoc    
    chief = ['chief', 'chf']
    manager = ['manag', 'mgr']
    cordinator = ['cordinator', 'coord']
    counselor = ['couns', 'cnslr']
    mechanic = ['auto', 'mech']    
    sup = ['supervisor', 'supv', 'sprv']
    asst = ['assitant', 'asst']
    engineer = ['engineer', 'engr','eng', 'program']
    attorney = [ 'public defender', 'attorney', 'attr', 'atty']
    #medical - use this for medical iteration tooo
    phyician = ['physician', 'orthopedic', 'Epidemiologist', 'anesth']
    #if assistant job has not other category
    adm = ['aide', 'assistant', 'secretary','sctry', 'attendant', 'asst'] #assistant and attendent are in gen
    #management = ['manage', "superv", "sup"]
    #communications?
    #medical - use this for medical iteration tooo    
    for t in executive:        
        if t in title:
            #set other stuff the same
            return t   
    for t in gm:
        if t in title:
            return "general manager"        
    for t in gen_title:
        if t in title:
            return t
    for t in chief:
        if t in title:
            return'chief'
    for t in manager:
        if t in title:
            return'manager'
    for t in cordinator:
        if t in title:
            return'cordinator'
    for t in counselor:
        if t in title:
            return'counselor'
    for t in mechanic:
        if t in title:
            return'mechanic'
    for t in sup:
        if t in title:
            return'supervisor'
    for t in asst:
        if t in title:
            return'assistant'
    for t in engineer:
        if t in title:
            return'engineer'
    for t in attorney:
        if t in title:
            return'attorney'
    for t in phyician:
        if t in title:
            return'physician'
    for t in adm:
        if t in title:
            return'aide'
    return 'other'
    
def find_job_dept(row):
    title = row.lower()
    #if deputy court clerk / mark clerk, court and deputy
    #if only deputy ignore

    dept_general = [ 'fire', 'account', 'animal',   'airport', 'emergency']
    police =['police', 'finger', 'toxic', 'forensic',  'med examiner',  'sherif', 'probation', 'sergeant']
    transit = ['mta', 'transit', 'trnsp', 'transport', 'fare']
    construction = ['mason', 'const', 'building', 'housing', 'cement', 'civil', 'carpentor', 'materials', 'bricklayer',  'commercial', 'landscape', 'glazier','eqip', 'power', 'civil', 'engineer',
'electric', 'plumber', 'maint', 'repairer', 'weld', 'operat', 'planner', 'bldg', 'parts','street', 'arch']
    medical= ['anesth', 'medical', 'nurs', 'clinic', 'health',  'pharm','care', 'diagn','chemist', 'lab', 'physic','orthopedic', 'Epidemiologist', 'microb', 'dph', 'environ', 'family', 'nutri', 'social', 'pysch', 'radiol',  'therap']
    court = ['court', 'legal', 'attorney','hearing','public defender']
    municipal = ['mari','sew', 'water', 'wtrt', 'aquatics', 'port', 'industrial', 'asphalt', 'bldg', 'arbor', 'electr', 'line', 'municipal', 'port director','utlity' ]
    city = ['city', 'claim', 'community', 'collect', 'commissioner', 'mayor', 'services', 'asses', 'asr', 'benefits',  'eligibility', 'employee', 'events', 'fiscal', 'gov', 'staff', 'media', 'project', 'parking', 'payrol', 'permit', 'property', 'real', 'program','rep','rent', 'clerk',  'librar', 'educator',]
    recreation = ['recreat','parks', 'arts', 'museum', 'curator']    
    automotive = ['auto', 'mechan', 'truck' ]
    general_laborer = ['general laborer', 'painter', 'cook', 'food', 'gardner', 'custod', 'janitor', 'porter']
    #if assistant job has not other category
    executive = ['assitant chief', 'assistant director', 'assistant deputy', 'gen mgr','asst dir', 'asst ch', 'deputy director', 'dpty', 'board secretary', 'general manager', 'dep dir', 'dept head', 'deputy chief', 'deputy dir','dep chf', 'department head'] 
    dept_adm = ['aide', 'assistant', 'secretary', 'attendant', 'asst']
    
    for d in dept_general:
        if d in title:
            return d
    for d in police:
        if d in title:
            return 'police'
    for d in transit:
        if d in title:
            return 'transit'
    for d in construction:
        if d in title:
            return 'construction'
    for d in medical:
        if d in title:
            return "medical"
    for d in court:
        if d in title:
            return 'court'
    for d in municipal:
        if d in title:
            return "municpal"
    for d in city:
        if d in title:
            return "city"
    for d in recreation:
        if d in title:
            return "recreation"
    for d in general_laborer:
        if d in title:
            return "laborer"
    for d in executive:
        if d in title:
            return "exceutive"
    for d in dept_adm:
        if d in title:
            return 'administrative'
    return 'other'

#added columns for analysis	
data['title'] = data['JobTitle'].map(find_job_title)
data['grade'] = data['JobTitle'].map(find_grade)
data['dept'] = data['JobTitle'].map(find_job_dept)
	
#get rid of a few negative values and 0 total pay-which is
#sum of both basepay, overtime and other pay
data = data[(data.TotalPay > 0 ]
data.to_csv('SFC.csv', sep=',')