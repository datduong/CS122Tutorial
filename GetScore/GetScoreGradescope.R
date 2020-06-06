

##! stepik
setwd('C:/Users/dat/Documents/CS122Spring2020Record')

stepik = read.csv('course-65953-grade-book.csv')
stepik [, 2:3] = apply(stepik[, 2:3], 2, toupper)

##! question chapter 3
questions = "The String Reconstruction Problem	
String Reconstruction as a Walk in the Overlap Graph	
Another Graph for String Reconstruction	
Walking in the de Bruijn Graph	
From Euler.s Theorem to an Algorithm for Finding Eulerian Cycles	
Assembling Genomes from Read.Pairs	
Epilogue. Genome Assembly Faces Real Sequencing Data"

##! question chapter 5
# questions = "An Introduction to Dynamic Programming. The Change Problem	
# The Manhattan Tourist Problem Revisited	
# Backtracking in the Alignment Graph	
# From Global to Local Alignment	
# The Changing Faces of Sequence Alignment	
# Penalizing Insertions and Deletions in Sequence Alignment	
# Space.Efficient Sequence Alignment	
# Epilogue. Multiple Sequence Alignment"

##! question chapter 9
# questions = "Herding Patterns into a Trie	
# Suffix Trees	
# Suffix Arrays	
# The Burrows.Wheeler Transform	
# The First.Last Property and Burrows.Wheeler Inversion	
# Pattern Matching with the Burrows.Wheeler Transform	
# Speeding Up Burrows.Wheeler Pattern Matching	
# Burrows and Wheeler Set Up Checkpoints	
# Epilogue. Mismatch.Tolerant Read Mapping"


questions = strsplit(questions,'\n')[[1]]
questions = gsub(" ",".",questions)

coln = names(stepik)
coli = c()
for (q in questions){
  print (q)
  coli = c( coli, grep(q,coln) )
  print (coli)
}

score = rowSums ( stepik[,coli] ) 

temp = as.numeric( c('5', '5', '10', '15', '5', '15', '5', '10', '10', '10', '10') )
sum(temp)
temp = as.numeric( c('10', '10', '10', '10', '15', '10', '5', '10', '10', '10', '10', '15', '10')) # 5
sum(temp)
temp = as.numeric( c('10', '10', '15', '10', '10', '10', '10', '10', '5', '10', '10', '15', '15'))
sum(temp) #! double check

Q = cbind ( stepik [, 2:3], score)
names(Q) = c( "Last.Name", "First.Name", "score" )
# Qx = merge(Q,midterm,by=c("First.Name", "Last.Name"))
Qx = Q 

Qx = Qx [ order(Qx$score,decreasing=T), ]

Qx = Qx[ ! duplicated(Qx$First.Name), ]
Qx[ which (Qx[,1]==""), 1 ] = 'none'
Qx[ which (Qx[,2]==""), 2 ] = 'none'

write.table(Qx,file='StepikChap3Score.csv',row.names=F,quote=F,na='none',sep='\t')

####

##! project 

setwd('C:/Users/dat/Documents/CS122Spring2020Record')

project = read.csv('Algorithms_Spring_2020_scores.csv')

# #! hp3
project = project [ grep ( 'hw3' , project$scores_table.genome_type ), ]
project = project [ which (project$scores_table.chromosome_id==1 & project$scores_table.genome_id==3) , ]
where = c ( "scores_table.assembly_accuracy","scores_table.assembly_contig_sizes","scores_table.assembly_coverage")

#! hp1 
# project = project [ grep ( 'hw1' , project$scores_table.genome_type ) , ]
# project = project [ which (project$scores_table.chromosome_id==1 & project$scores_table.genome_id==2) , ]
# where = c ( "scores_table.snp_score")

#! hp2
# project = project [ grep ( 'hw2' , project$scores_table.genome_type ) , ]
# project = project [ which (project$scores_table.chromosome_id==1 & project$scores_table.genome_id==2) , ]
# where = c ( "scores_table.snp_score","scores_table.indel_score")


#! 
project = cbind ( project [ , 1:2], project[where] ) 
names (project) = c ('auth_user.id','auth_user.studentId',where)
write.table(project,'HP3.csv',row.names=F,quote=F,sep='\t')


