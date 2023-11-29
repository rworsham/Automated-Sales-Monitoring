# What is this?

### This program will check if the designated folder has a new/updated file in its directory. It will then store this information and send an email of the completed files to the helpdesk email.

# Why is this needed?

### This program should shorten the amount of time needed to verify sales have imported and stores have closed by automating the process.

# Planned implementation/Research

### I am creating a testing environment and once everything test successfully will work with management to test on a customer. I am aware certain boards have a later polling time so deciding what time to have this program run will be needed as it wont run 24/7. I plan to convert this into an executable application and utilize NSSM to have it run as a service. currently planned email implementation is through a gmail account and app password this will need testing as im not sure if firewall/AV rules would block this on these systems.

# Current Version
### Testing was successful and the output is cleaner, compiled the program into single executable and set automated task to run the program at 9PM nightly, the application is board specific and set to end approx 20 minutes after polling gets done giving plenty of time for everything to come in. Leaving copy of standalone executable and python file on file server in case changes/modificatons are needed. FileServer\Software\Misc Software\Rob

# Progress Tracker
### all progress will be noted in commits

## No changes have/will be made without manager approval 


