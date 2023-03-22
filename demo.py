import os
import mlflow
import argparse
import time 
# log metrics   - accuracy , MAE etc..,
# log parameter - parameters like C , tree depth etc.., 
# log model     -   
# log artifacts - intermeidate files, like chekpoints etc.., 

def evaluate(param1,param2):
    metric = param1**2 + param2**2
    return metric

def main(p1,p2):
   with mlflow.start_run():
        mlflow.log_param("param1",p1)# key:value
        mlflow.log_param("param2",p2)
        metric=evaluate(param1=p1,param2=p2)
        mlflow.log_metric("somemetric",metric)

        os.makedirs("temp",exist_ok=True)
        with open("temp/sample.txt","w") as e:
            e.write(time.asctime())
        mlflow.log_artifact("temp")

if __name__=="__main__":
    arg_=argparse.ArgumentParser()
    arg_.add_argument("--param1","-p1",type=int,default=2)
    arg_.add_argument("--param2","-p2",type=int,default=5)
    parsed_arg_=arg_.parse_args()
    #print(parsed_arg_)
    #print(parsed_arg_.param1,parsed_arg_.param2)
    u=main(parsed_arg_.param1,parsed_arg_.param2)
    print(u)
