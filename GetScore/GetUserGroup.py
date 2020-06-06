
import sys,re,os,pickle
import pandas as pd 
import numpy as np 

#! get user in grad vs undergrad groups

turn_on_record = 0 # start tracking
name = 'none'
user = {}
this_person = 0

fin = open ('UserCs122.csv','r')
for line in fin:
  if 'Picture of' in line: 
    name = line.strip().split('Picture of')[1] # 2nd half is name. 
    name = name[ 0: (int(len(name)/2) +1) ] # name is duplicated twice ... why?
    # name is last, first 
    name = name.split(',')
    name = [n.strip() for n in name]
    name = name[1] + '\t' + name[0]
    continue
  if 'Handshake Photo' in line: 
    name = line.strip().split('Handshake Photo')[1] # 2nd half is name. 
    name = name.split(',')
    name = [n.strip() for n in name]
    name = name[1] + '\t' + name[0]
    continue
  # else: 
  #   name = 'NotInFormatPictureOf'
  if ( re.match('^[0-9]{9,}',line) ) : ## check this each time.
    this_person = line.split()[0] 
    user [ this_person ] = name
    continue
  if 'DIS' in line:
    status = 'none'
    if ('122' in line) or ('160' in line):
      status = 'undergrad'
    if ('222' in line) or ('260' in line):
      status = 'grad'
    #
    user [ this_person ] = name + '\t' + status
    continue

#
def write (dict_input,name_out):
  fout = open (name_out, 'w') 
  for key,val in dict_input.items():
    if ('grad' in val) or ('undergrad' in val): 
      fout.write(key+'\t'+val+'\n')
  fout.close() 

#
write(user,'status.csv')


#! merge to midterm on grade scope. 
# R is so stupid here. 
user = pd.read_csv('status.csv',dtype=str,header=None,sep='\t')
user.columns = ['CCLE.ID',"First.Name", "Last.Name",'status']

midterm = pd.read_csv('Midterm_scores.csv',dtype=str)
for name in ["First Name",  "Last Name", 'SID']:
  temp = midterm[name]
  if name == 'SID': 
    for index,t in enumerate(temp): 
      if t is not np.nan: 
        t = re.sub('-','',t).strip() 
        t = re.sub(' ','',t).strip() 
      else: 
        t = 'none'
      temp[index] = t 
  else: 
    temp = [t.upper() for t in temp]
  midterm[name] = temp


user_with_id = pd.merge(user,midterm, left_on=['CCLE.ID'], right_on=['SID']) ##!! okay. group with easy id match
midterm_no_id = midterm[ midterm.SID == 'none'] ## take out people without id on gradescope
user_no_id_by_name = pd.merge(user,midterm_no_id, left_on=['First.Name', 'Last.Name'], right_on=['First Name','Last Name']) 

all_user = pd.concat([user_with_id,user_no_id_by_name],ignore_index=True)
all_user = all_user.sort_values('CCLE.ID',ascending=False)

all_user = all_user[['CCLE.ID','First.Name', 'Last.Name','Total Score','status']]
all_user = all_user.dropna()

all_user.to_csv('MidtermWithIdGradLevel.csv',index=False,sep='\t')


