import os, fileinput

list=[]

Dict={}

#for line in fileinput.input(['20w_Makeflow.makeflowlog']):

for line in fileinput.input(['20w_MachineConfig_Makeflow.makeflowlog']):

	list=line.split(' ')

	Task_ID=list[1]

	if(len(Task_ID)<3):

		# Convert Timestamp in microsec to sec

		Timestamp_micro=list[0]

		Timestamp=Timestamp_micro[:len(Timestamp_micro)-6]

		

		if Task_ID in Dict.keys():

			val=Dict[Task_ID]+'_'+Timestamp

			Dict[Task_ID]=val

		else:

			Dict[Task_ID]=Timestamp



list1=[]

for k,v in Dict.iteritems():

#	print k+' -> '+v

	if (int(k)>=50):


		#print k

	# Get start and complete time for a Task ID
		list1=v.split('_')

		time_start=list1[0]

		time_end=list1[1]

		#os.system("date -d @"+time_start+" +'%H:%M:%S'")

		os.system("date -d @"+time_end+" +'%H:%M:%S'")



