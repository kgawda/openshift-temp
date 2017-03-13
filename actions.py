import requests, datetime

def action1(user, password, blogURL, message):

    data = {
            "subject": "Test post...", "type": "post",
            "content": {
                "type": "text/html",
                "text": "<p>This is <b>scripted post</b>.<p>%s<p>Sent at %s" % (message, datetime.datetime.now())
            }}

    r = requests.post(blogURL, auth=(user, password), json=data)

    return r.status_code, r.text[:100]
