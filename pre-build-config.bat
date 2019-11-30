SET PATH=%PATH%;C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin
git pull
gcloud auth activate-service-account jenkins@handle-books.iam.gserviceaccount.com --key-file=c:\Users\nvmur\Downloads\handle-books-2a419c24f2ac.json --project=handle-books
