# SAGA PLANER

For this assignment we used pddl to to model and simulate what might happen in a busy town square.

####The predicates that we resued from the exapmle code that was given to us were: 
  ```pddl
  - IS_AT
  - HAS
  - HUNGRY
  - EDIBLE
  ```

####The actions that we resued were: 
  ```pddl
  - MOVE
  ```
 
####The objects that we reused were:
  ```pddl
  - MAN
  - WOMAN
  - RESTURANT
  - FOUNTAIN
  ```
  
The rest we created our selfs.

In order for us to use conditional-effects we has to change the heuristics that the planner is using be chenging the planDP.sh script that resides in JSaga/scripts.
We changed the heuristics from landmark cut to ff

####We have 5 different goals:
  ```pddl
  HAS_JOB DAVID
  
  not (HUNGRY MAN)
  
  HERO BOY
  
  SAD GUNNI
  SAD DAVID
      
  MARRIED MAN WAITRESS
  MARRIED WAITRESS MAN
  ```
      
