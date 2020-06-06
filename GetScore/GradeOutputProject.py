import sys,re,os,pickle
import numpy as np
import pandas as pd


def GetGrade (status, hp1_snp, hp2_snp, hp2_indel, hp3_coverage, hp3_contig_size, hp3_accuracy) :
  hp1_grade, hp2_grade, hp3_grade, hp4_grade = 0, 0, 0, 0
  # hp1_snp=50.0  # put your SNP score on HP1, 0 to 100 scale
  # hp2_snp=70.0  # put your SNP score on HP2, 0 to 100 scale
  # hp2_indel=10.0  # put your indel score on HP2, 0 to 100 scale
  # hp3_coverage=50.0  # put your coverage score on HP3, 0 to 100 scale
  # hp3_contig_size=10.0  # put your contig sizes score on HP3, 0 to 100 scale
  # hp3_accuracy=50.0  # put your accuracy score on HP3, 0 to 100 scale
  if status == 'undergrad':
    # hp1_grade = min(1.0, max(0.5, (hp1_snp - 25.0) / (45.0 - 25.0)))
    # hp2_snp_subscore = min(1.0, (hp2_snp - 55.0) / (75.0 - 55.0))
    # hp2_indel_subscore = min(1.0, (hp2_snp - 3.0) / (13.0 - 3.0))
    # hp2_grade = min(1.0, max(0.5, (hp2_snp_subscore + hp2_indel_subscore) / 2.0))
    hp3_covg_subscore = min(1.0, hp3_coverage / 87.0)
    hp3_acc_subscore = min(1.0, hp3_accuracy / 43.0)
    hp3_size_subscore = min(1.0, hp3_contig_size / 5.0)
    hp3_grade = min(1.0, max(0.5, (hp3_covg_subscore + hp3_acc_subscore + hp3_size_subscore) / 3.0))
    # hp4_grade = min(1.0, max(0.5, (hp4_transcript + hp4_abundance) / 200.0))
  else:
    # hp1_grade = min(1.0, max(0.5, (hp1_snp - 40.0) / (60.0 - 40.0)))
    # hp2_snp_subscore = min(1.0, (hp2_snp - 70.0) / (90.0 - 70.0))
    # hp2_indel_subscore = min(1.0, (hp2_snp - 15.0) / (25.0 - 15.0))
    # hp2_grade = min(1.0, max(0.5, (hp2_snp_subscore + hp2_indel_subscore) / 2.0))
    hp3_covg_subscore = min(1.0, hp3_coverage / 92.0)
    hp3_acc_subscore = min(1.0, hp3_accuracy / 48.0)
    hp3_size_subscore = min(1.0, hp3_contig_size / 8.0)
    hp3_grade = min(1.0, max(0.5, (hp3_covg_subscore + hp3_acc_subscore + hp3_size_subscore) / 3.0))
    # hp4_grade = min(1.0, max(0.5, (hp4_transcript + hp4_abundance) / 200.0))
  return hp1_grade, hp2_grade, hp3_grade, hp4_grade


####

user = pd.read_csv('MidtermWithIdGradLevel.csv',dtype=str,sep='\t')

#! get score
# heroku_user = pd.read_csv('db_auth_user.csv',dtype=str)
# heroku_score = pd.read_csv('db_scores_table.csv',dtype=str)

project = pd.read_csv('HP3.csv',dtype=str,sep='\t')

user = pd.merge(user,project, left_on=['CCLE.ID'], right_on=['auth_user.studentId'])

project_score = []
for index,row in user.iterrows():
  #! hp3_coverage, hp3_contig_size, hp3_accuracy
  project_score.append ( GetGrade ( row['status'], 0, 0, 0, float(row['scores_table.assembly_coverage']), float(row['scores_table.assembly_contig_sizes']), float(row['scores_table.assembly_accuracy']) ) [2] * 100 )
  #! hp1 scores_table.snp_score
  # project_score.append ( GetGrade ( row['status'], float(row['scores_table.snp_score']), 0, 0, 0, 0, 0 ) [0] * 100 )
  #! hp2 scores_table.snp_score
  # project_score.append ( GetGrade ( row['status'], float(row['scores_table.snp_score']), float(row['scores_table.indel_score']), 0, 0, 0, 0 ) [1] * 100 )


#
user['project_score'] = project_score

#! sort remove duplicate 
user = user.sort_values('project_score',ascending=False)
user.drop_duplicates(subset ="auth_user.studentId", 
                     keep = 'first', inplace = True) 


user.to_csv('HP3Score.csv',index=False,sep='\t')

