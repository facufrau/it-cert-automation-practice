#!/usr/bin/env python3

import psutil
import shutil
import emails
import os, sys
import socket

#CPU check
def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    return not cpu_usage > 80

#Disk check
def disk_check():
    disk_usage = shutil.disk_usage("/")
    disk_total = disk_usage.total
    disk_free = disk_usage.used
    limit = disk_free / disk_total * 100
    return limit > 20

#Memory check
def memory_check():
    available = psutil.virtual_memory().available
    available_MB = available / 1024 ** 2
    return available_MB > 500
    
#Host check
def hostname_check():
    local_host_ip = socket.gethostbyname('localhost')
    return local_host_ip == '127.0.0.1'

def email_warning(error):
    sender = "automation@example.com"
    recipient = 'student-00-6b1ee97c681a@example.com'
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

if not cpu_check():
    subject = "Error - CPU usage is over 80%"
    email_warning(subject)

if not disk_check():
    subject = "Error - Available disk space is less than 20%"
    email_warning(subject)

if not memory_check():
    subject = "Error - Available memory is less than 500MB"
    email_warning(subject)

if not hostname_check():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    email_warning(subject)

