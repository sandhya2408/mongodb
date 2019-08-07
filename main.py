import database as db
new_faculty = {
  "name":"krish",
  "age":30,
  "exp":10,
   "subjects":[
     {
       "subname":"JAVA",
       "duration":40
     },
     {
       "subname":"PYTHON",
       "duration":35
     }
   ],
   "qualification":"M.Tech",
   "deptno":10
}
db.add_new_faculty(new_faculty)