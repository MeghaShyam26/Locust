TO RUN A LOAD TEST
1) Install locust:
   pip install locust
   
   Ref: https://docs.locust.io/en/stable/installation.html


2) Either navigate to the directory where the locust script is present
   If only a  single file is present type
    locust
   If mutliple files are present then
    locust -f filename.py
   To launch with a different port add the following command line argument:
    --web-port portNumber
   To launch with a master-worker approach add the following command line argument:
    --master for one file and --worker for the number of workers required
   To find all the arguments type:
    locust --help
   Ref: https://docs.locust.io/en/stable/configuration.html

3) Links for other important aspects:
    Quick start: https://docs.locust.io/en/stable/quickstart.html
    Running without UI: https://docs.locust.io/en/stable/running-locust-without-web-ui.html
    HttpUser class: https://docs.locust.io/en/stable/api.html#httpuser-class
    Taskset class: https://docs.locust.io/en/stable/api.html#taskset-class
    Sequentialtaskset class: https://docs.locust.io/en/stable/api.html#sequentialtaskset-class
    Waittime functions: https://docs.locust.io/en/stable/api.html#module-locust.wait_time
    Master-Worker: https://docs.locust.io/en/stable/running-locust-distributed.html

4) For quick execution:
    git clone https://github.com/MeghaShyam26/Locust.git --branch locust-get
    
    cd Locust
    
    locust -f locust_get.py 
