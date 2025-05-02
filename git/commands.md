# Reverting changes at different stages of Git

## Working Directory

- You want to discard the changes made to your file(s) but you didnt move it to staging area (git add)

  1. for a single file
     ```bash
       git restore <file name>
     ```


   ### for all files
   ### git restore .

# Staging Area

   ## You want to move from staging area to working directory (after running git add .)

   ### for a single file
   ### git restore --staged filename

   ### for all files
   ### git restore --staged .

# Local Repository

   ## You want to undo last commit but keep the changes staged because you might want to change the commit message or forgot to include a file

   ### git reset --soft HEAD~1

   ### git commit -m "Better commit message"


   ## You want undo last commit, unstage the changes but keep the changes in your working directory
   ### git reset --mixed HEAD~1




