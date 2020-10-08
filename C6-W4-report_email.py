#!/usr/bin/env python3

import os, sys
import reports
from datetime import date
import emails

def process_data(path):
    '''Process data for generating a report.'''
    text = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                lines = f.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                text += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return text

def main():
    '''Main function for generating report and send email.'''
    txt_path = "supplier-data/descriptions/"
    text = process_data(txt_path)
    title = 'Processed Update on ' +  str(date.today())
    attachment = '/tmp/processed.pdf'
    reports.generate_report(attachment, title, text_description)
    
    sender = 'automation@example.com'
    recipient = 'student-00-6b1ee97c681a@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    email = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(email)


if __name__ == "__main__":
    main()