dagscheduler
============

How to schedule a DAG onto a given number of machines
dag_evaluator and task_scheduler are both python scripts.

dag_evaluator takes task description file as the input and provides the optimal machine number for executing a makeflow.
Usage examples of dag_evaluator:
The task dependency relationship and task length is known in advance.
./dag_evaluator -d full bwamf_list2
./dag_evaluator -d full case1_list
./dag_evaluator -d full case2_list

The task dependency relationship is known in advance, and the tasks in the same level take similar time, but task length is not known in advance.
./dag_evaluator -d half case1_list_no_length 
./dag_evaluator -d half case2_list_no_length
./dag_evaluator -d half case3_list 
./dag_evaluator -d half case4_1 

The task dependency relationship is known in advance, and the tasks in the same level take different times, but task length is not known in advance.
Optimized Machine Number = max{dag_width, average_dag_width}.
./dag_evaluator -d zero case1_list_no_length 
./dag_evaluator -d zero case2_list_no_length
./dag_evaluator -d zero case3_list 
./dag_evaluator -d zero case4_1 

The task dependency relationship is known in advance, and the tasks in the same level take different times, but task length is not known in advance.
Optimized Machine Number = maximal parallel running task number (brute force algorithm, expensive)
./dag_evaluator -d zero_brute_force case2_list_no_length
./dag_evaluator -d zero_brute_force case3_list 
./dag_evaluator -d zero_brute_force case4_1 

task_scheduler takes task description file and a list of achine number as the input, and calculates the execution time, cost, wastage of running the makeflow on each machine number.
Usage examples of task_scheduler:
./task_scheduler -m '45, 50, 55' bwamf_list2
./task_scheduler -m '30, 40, 50, 60' case1_list
./task_scheduler -m '3, 4, 5' case2_list
