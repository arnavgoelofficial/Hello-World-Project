SET PATH=%PATH%;"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin"
git pull "https://github.com/arnavgoelofficial/cloudtests.git"
gcloud auth activate-service-account "service-cloudtest@arnav-cloudtest.iam.gserviceaccount.com" --key-file="D:\Google CLoud Class\New folder\arnav-cloudtest-fdc038444925.json" --project=arnav-cloudtest