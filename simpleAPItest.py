import requests

# response = requests.get("https://http-me.staging-eks.codecademy.com/green")
# response = requests.get("https://http-me.staging-eks.codecademy.com/yellow")
# response = requests.get("https://http-me.staging-eks.codecademy.com/red")
response = requests.get("https://http-me.staging-eks.codecademy.com/indigo")

a = response.history
rdr = 0
for resp in a: rdr = rdr+1

if (response.status_code != 200):
    errorBool = True
    failMsg = response.json()
    redirectCount = rdr
else:
    errorBool=False
    failMsg=""
    redirectCount = rdr

responseDict = {
    "status": response.status_code,
    "error": errorBool,
    "fail_message": failMsg,
    "redirects": redirectCount
}

print(responseDict)
print(response.history)