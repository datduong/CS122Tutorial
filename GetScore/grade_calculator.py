'''
Please type in your grades below. Everything except status should be 0-100, e.g. a percentage.
For HP4, Stepik Ch5, and Final Exam, you can put in what you expect to get if you haven't done them yet.
For Stepik & Rosalind, use the info on the site to calculate the percent of points you've gotten.
For the Heroku projects, just enter your raw score for each metric as shown on the leaderboard.
'''

######################
# ENTER GRADES BELOW #
######################

status='undergrad'  # put either 'undergrad' or 'graduate'

hp1_snp=50.0  # put your SNP score on HP1, 0 to 100 scale

hp2_snp=70.0  # put your SNP score on HP2, 0 to 100 scale
hp2_indel=10.0  # put your indel score on HP2, 0 to 100 scale

hp3_coverage=50.0  # put your coverage score on HP3, 0 to 100 scale
hp3_contig_size=10.0  # put your contig sizes score on HP3, 0 to 100 scale
hp3_accuracy=50.0  # put your accuracy score on HP3, 0 to 100 scale

hp4_transcript=100.0  # put your transcript score on HP4, 0 to 100 scale
hp4_abundance=77.78  # put your abundance score on HP4, 0 to 100 scale

rosalind=100  # put the percent of the rosalind exercises you completed, 0 to 100 scale

stepik_ch3=100  # put the percent of Stepik chapter 3 you completed, 0 to 100 scale
stepik_ch5=80  # put the percent of Stepik chapter 5 you completed or plan to complete, 0 to 100 scale
stepik_ch9=100  # put the percent of Stepik chapter 9 you completed or plan to complete, 0 to 100 scale

responses=100  # put the percent of discussion forums (there were 5 total) you participated in, 0 to 100 scale

midterm=96.84  # put your percentage score on the midterm out of 100

final=-1.0  # put -1.0 if you plan to skip the final, or try out a value from 0 to 100 to see how your grade would look

############################
# DO NOT MODIFY BELOW HERE #
############################

# From the syllabus:
# GradeBreakdown:  Problem Homeworks 30%. Programming Homeworks 20%.  Midterm Exam 20%. Final Exam 20%. Paper Responses 10%.

if status == 'undergrad':
	hp1_grade = min(1.0, max(0.5, (hp1_snp - 25.0) / (45.0 - 25.0)))
	hp2_snp_subscore = min(1.0, (hp2_snp - 55.0) / (75.0 - 55.0))
	hp2_indel_subscore = min(1.0, (hp2_snp - 3.0) / (13.0 - 3.0))
	hp2_grade = min(1.0, max(0.5, (hp2_snp_subscore + hp2_indel_subscore) / 2.0))
	hp3_covg_subscore = min(1.0, hp3_coverage / 87.0)
	hp3_acc_subscore = min(1.0, hp3_accuracy / 43.0)
	hp3_size_subscore = min(1.0, hp3_contig_size / 5.0)
	hp3_grade = min(1.0, max(0.5, (hp3_covg_subscore + hp3_acc_subscore + hp3_size_subscore) / 3.0))
	hp4_grade = min(1.0, max(0.5, (hp4_transcript + hp4_abundance) / 200.0))
else:
	hp1_grade = min(1.0, max(0.5, (hp1_snp - 40.0) / (60.0 - 40.0)))
	hp2_snp_subscore = min(1.0, (hp2_snp - 70.0) / (90.0 - 70.0))
	hp2_indel_subscore = min(1.0, (hp2_snp - 15.0) / (25.0 - 15.0))
	hp2_grade = min(1.0, max(0.5, (hp2_snp_subscore + hp2_indel_subscore) / 2.0))
	hp3_covg_subscore = min(1.0, hp3_coverage / 92.0)
	hp3_acc_subscore = min(1.0, hp3_accuracy / 48.0)
	hp3_size_subscore = min(1.0, hp3_contig_size / 8.0)
	hp3_grade = min(1.0, max(0.5, (hp3_covg_subscore + hp3_acc_subscore + hp3_size_subscore) / 3.0))
	hp4_grade = min(1.0, max(0.5, (hp4_transcript + hp4_abundance) / 200.0))

all_proj_grades = [hp1_grade*100.0, hp2_grade*100.0, hp3_grade*100.0, hp4_grade*100.0]
top3_proj_grades = sorted(all_proj_grades)[1:]
project_grade = sum(top3_proj_grades) / 3.0
print('Grades for HP [1, 2, 3, 4]: ' + str(all_proj_grades))
print('Overall project grade: ' + str(project_grade))

problem_hw_grade = rosalind*0.1 + stepik_ch3*0.3 + stepik_ch5*0.3 + stepik_ch9*0.3
print('Problem Homework grade: ' + str(problem_hw_grade))
print('Paper/speaker responses grade: ' + str(responses))
print('Midterm exam grade: ' + str(midterm))

pre_final_grade = (project_grade*0.2 + problem_hw_grade*0.3 + responses*0.1 + midterm*0.2) / 80.0 * 100.0
post_final_grade = project_grade*0.2 + problem_hw_grade*0.3 + responses*0.1 + midterm*0.2 + final * 0.2
if post_final_grade < pre_final_grade:
	print('Final exam not counted.')
	print('Total grade: ' + str(pre_final_grade))
else:
	print('Final exam grade: ' + str(final))
	print('Total grade: ' + str(post_final_grade))
#
