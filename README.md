# Lambda Sentiment

## Setup
Make sure you have the following installed in your env:
  * Python 3.6
  * Chalice

You will also need to have your AWS credential configured. If you have
previously configured your machine to run boto3 (the AWS SDK for Python) or the
AWS CLI then you can skip this section. Otherwise, you will need to do the
following:
```
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
```

## Project Structure
`app.py` is the heart of the code, it is a flask-esque file that routes/handles
incoming requests; this is where we would call `ModelInterface` to generate
predictions for incoming requests.

`chalicelib/` is where all the supplementary code files live i.e. the project files
which are imported in `app.py`. For us, this is where the `modelinterface.py` for
an app would live.

`requirements.txt` is the app's requirements file; nothing different here.

## Deploying a Lambda Function
First, install the app's dependencies:
```
$ pip install -r requirements.txt
```

Next, create and deploy a lambda function:
```
$ chalice deploy
Creating deployment package.
Creating IAM role: sentiment-dev
Creating lambda function: sentiment-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-1:017491206004:function:sentiment-dev
  - Rest API URL: https://s26c58spfj.execute-api.us-east-1.amazonaws.com/api/
```

You can now get predictions by sending Doppler requests to the REST API URL. Note, you can 
also find the ARN and REST API URL in the `.chalice/deployed` folder.
