1. Cloud Habit – Simple AWS S3 Webpage
This project demonstrates how to deploy a simple static webpage on Amazon Web Services (AWS) using Amazon S3 and Python (Boto3).
It was developed as part of a Cloud Programming course project and focuses on understanding basic cloud deployment concepts.

2. Project Overview
The goal of this project is to:
•	Create an Amazon S3 bucket using Python
•	Upload a simple HTML webpage
•	Configure the bucket for static website hosting
•	Access the webpage through an AWS public URL
The result is a working “Hello World” webpage hosted in the cloud, without using any traditional web server.
3.  Technologies Used
•	Python 3.13
•	AWS S3 (Simple Storage Service)
•	Boto3 – AWS SDK for Python
•	Windows Command Line
•	AWS Free Tier

4.  Project Structure
cloud-habit-webpage/
│
├── aws_deploy.py     # Python script for deployment
├── README.md         # Project documentation

5.  Prerequisites
Before running the project, make sure you have:
•	Python installed
Check with:
•	python --version
•	An AWS account
•	AWS credentials configured as environment variables
(Credentials are NOT hard-coded for security reasons)
On Windows (CMD):
setx AWS_ACCESS_KEY_ID "AKIAZKPB3Y752K76XBWI"
setx AWS_SECRET_ACCESS_KEY "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"
setx AWS_DEFAULT_REGION eu-central-1
•	Required Python libraries installed
•	pip install boto3 botocore

6.  How to Run the Project
•	Navigate to the project folder:
•	cd cloud-habit-webpage
•	Run the deployment script:
•	python aws_deploy.py
•	If successful, you will see a message similar to:
•	Deployment successful!
•	Webpage URL:
•	http://rusingiza-cloud-simple-webpage-2025.s3-website.eu-central-1.amazonaws.com
•	Open the URL in your browser 🎉

7.  Live Demo
The deployed webpage displays:
Hello World from AWS S3!
This webpage is hosted using Amazon S3.
This confirms that the deployment was successful.

8. Security Considerations
•	AWS credentials are never stored in the source code
•	Environment variables are used instead
•	This follows AWS security best practices

9. Cloud Concepts Demonstrated
•	Cloud storage using Amazon S3
•	Static website hosting
•	Scalability without managing servers
•	High availability
•	Infrastructure automation with Python

10. Learning Outcome
Through this project, I learned how:
•	Cloud services can replace traditional servers
•	AWS S3 can be used to host static websites
•	Python can automate cloud resource management
•	Small configuration mistakes (such as region settings) can impact deployment
This project helped strengthen my understanding of practical cloud programming.

11.  License
This project is created for educational purposes as part of a university assignment.


Author
Rusingiza Nshuti Braille
B.Sc. Applied Artificial Intelligence
IU International University of Applied Sciences
