#This code does a get request to the hostname given
from locust import HttpUser, task, between

""" WORKING OF on_start:
     This method will be invoked only once for a new user invoked i.e, only at the time of the creation of a new user this method is invoked and 
     not repeated throughout the test.
     So, if we want the number of requests to be equal to the number of users mentioned we define the get request in this method.
    WORKING OF task:
     This task will be executed repetitively with the time interval of (3,15) seconds defined in the wait time.
     This task will be happening repetitively for each use invoked i.e, if 2 users are invoked and 3rd user is freshly invoked then
     the requests made my locust would be 2 requests(depending on the wait time for concurrency) each from the previous users and one new request the new user
     So, if we want to invoke many users where each user makes a get request repetitively with a time interval then we use this method.
     However, atleast one task should be defined for running a test.
    WORKING OF wait_time
     used to determine how long a simulated user should wait between executing tasks 
     For example, to make each user wait between 3 and 15 seconds between every task execution
     if there are multiple tasks then this will act as the interval b/n each task execution
    
    HttpUser class: https://docs.locust.io/en/stable/api.html#httpuser-class
     """



class QuickstartUser(HttpUser):
    
    #intiating the hostname(can be initiated in the UI as well)
    hostname=''

    # defining wait time of 3,15 seconds wherein the value is choosen randomly
    wait_time = between(3,15)

    #defining an on_start method
    def on_start(self):
        self.client.get("")

    #defining a task
    @task
    def index_page(self):
        self.client.get("")
    
