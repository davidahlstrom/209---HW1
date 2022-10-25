from datetime import date

#Task class, charged with initializing, getting, modifying, and returning a string of relevant information
class Task(object):
    x = 0

    #Initialization method
    def __init__(self,description,priority,status):
        Task.x += 1
        self.task_id = "task"+str(Task.x)
        self.description = description
        self.priority = priority
        self.status = status

    #Get ID method, returns ID of given task
    def get_id(self):
        return self.task_id

    #Get description method, returns description of given task
    def get_description(self):
        return self.description

    #Get priority method, returns priority of given task
    def get_priority(self):
        return self.priority

    #Get status method, returns status of given task
    def get_status(self):
        return self.status

    #Modify description method, modifies description of a given task
    def modify_description(self, new_description):
        self.description = new_description

    #Modify priority method, modifies priority of a given task
    def modify_priority(self, new_priority):
        self.priority = new_priority

    #Modify status method, modifies status of a given task
    def modify_status(self, new_status):
        self.status = new_status

    #String method, returns a string of the task information
    def __str__(self):
        return str(self.task_id) +"-"+ str(self.description) +"-"+ str(self.priority) +"-"+ str(self.status)
    
#Main method, creates the objects and prints information about the objects, calls the modify method and prints the modified tasks  
def main():
    t1 = Task("lab 209", "medium", "starting")
    t2 = Task("doctor", "high", "today")
    t3 = Task("library books", "low", "pending")
    print("Date:",date.today())
    print("t3 ID:",t3.get_id())
    print("t1 status:",t1.get_status())
    print("t2 priority:",t2.get_priority())
    print("**********************")
    print("")
    t3.modify_description("pick up library books")
    t1.modify_status("done")
    t2.modify_priority("low")
    print(t1)
    print(t2)
    print(t3)
    

main()
    
