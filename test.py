import os
SECRET = os.environ['APP_NAME']
print("SECRET***")
print(SECRET)
print("VARIABLE***")
VARIABLE_1 = os.environ['VARIABLE_1']
print(VARIABLE_1)

print("ENVIROMENT_1***")
ENVIROMENT_1 = os.environ['ENVIROMENT_1']
print(ENVIROMENT_1)

print("ENVIRONMENT_NAME** from github env***")
ENVIRONMENT_NAME = os.environ['ENVIRONMENT_NAME']
print(ENVIRONMENT_NAME)
