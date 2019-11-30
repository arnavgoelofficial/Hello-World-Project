SET PATH=%PATH%;C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin
SET IMAGE_NAME=gcr.io/arnav-cloudtest/image1:%BUILD_NUMBER%
cd D:\Google CLoud Class\PyMicroservices-master\Source
kubectl set image deployment/image1 image1=%IMAGE_NAME%
