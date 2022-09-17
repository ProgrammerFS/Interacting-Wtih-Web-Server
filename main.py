#! /usr/bin/env python3
import os
import requests
def feedbackPostRequest(dir, server):
    for x in os.listdir(f"{dir}"):
        with open(f"{dir}/"+x) as f:
            d = {}
            title = f.readline().strip("\n")
            name = f.readline().strip("\n")
            date = f.readline().strip("\n")
            feedback = f.read().strip("\n")
            d["title"] = title
            d["name"] = name
            d["date"] = date
            d["feedback"] = feedback
            response = requests.post(server, d)
            print(response.status_code)