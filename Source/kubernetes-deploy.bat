SET PATH=%PATH%;"C:\Users\Sanya Kapoor\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin"
SET IMAGE_NAME=gcr.io/compile-microservices/gpymicro-image:%BUILD_NUMBER%
cd "D:\Moodle\Sem 5\Cloud\PyMicroservices-master\Source"
kubectl set image deployment/py-gmicro py-gmicro=%IMAGE_NAME%
