C:
cd C:\Users\Student\Documents\Spring 2021\RAH

SET /A "index = 1"
SET /A "count = 10"
:while
if %index% leq %count% (
   python simon_says.py
   python3 Pose_Recognition.py
   python Processes_Result.py
   SET /A "index = index + 1"
   goto :while
)