Aws management console

# Create Instance

ec2 dashboard > Launch Instance

1. Ubuntu Server 18.04 (Free Tier Elig)

2. Next

3. Next

4. 30 GB

5. Next

6. SSH HTTP HTTPS activation

7. Create a new key pair, Download Key Pair, Review & Launch

Do not forget to "Create Billing Alerts"

---

# Create Database

1. RDS

2. PostgreSQL

3. Free Tier

4. Db instance identifier
   
   ```bash
   db instance identifier: database-1
   master-username: postgres
   master-password: Thesis2020
   ```

5. Create database
   
   Endpoint `database-1.cynqbyg6scgv.us-east-2.rds.amazonaws.com `
   
   Port ` 5432`

# Connecting Running Instance & Deploy

1. Find *Public DNS* or *Public IP* to connect SSH
   
   `ssh -i dosya.pem ubuntu@publicdns`
   
   `ssh -i ServerKeyPair.pem ubuntu@ec2-3-14-66-58.us-east-2.compute.amazonaws.com`

2. Update Upgrade
   
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```

3. Install *python3-dev*, *python3-pip*, *python3-virtualenv*
   
   ```bash
   sudo apt-get install python3-dev python3-pip python3-venv
   pip3 install --upgrade pip setuptools
   ```

4. Clonning repo from Github, creating virtual env & installing requirements
   
   ```bash
   git clone https://github.com/ibrahim-dogan/cmpe-graduation-project.git
   cd cmpe-graduation-project
   python3 -m venv venv
   source venv/bin/activate
   #now we are in (venv)
   pip install --upgrade pip
   pip install wheel
   pip install -r requirements.txt
   # downloading nltk stopwords,punkt from python console
   python
   >>> import nltk
   >>> nltk.download('stopwords')
   >>> nltk.download('punkt')
   # downloading word2vec trmodel
   # model source: https://drive.google.com/drive/folders/1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww
   # below weird code source: https://medium.com/@acpanjan/download-google-drive-files-using-wget-3c2c025a8b99
   wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1q1o2sGByIaUHd7vi5IX8KJEcJw329hgY' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1q1o2sGByIaUHd7vi5IX8KJEcJw329hgY" -O trmodel && rm -rf /tmp/cookies.txt
   ```

5. ```
   python manage.py runserver 0.0.0.0:80
   #now you can visit the public id to see the page
   ```


