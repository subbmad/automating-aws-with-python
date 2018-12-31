#!/usr/bin/env python3
import boto3

session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

