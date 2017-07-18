import requests, timing

def action1(user, password, blogURL, message):

    data = {
            "subject": "Automatic post test...", "type": "post",
            "content": {
                "type": "text/html",
                "text": """<p>%s
                           <p>This is <b>test post</b>.
                           <p>Sent by script at %s""" %
                           (message, timing.time_now())
            }}

    r = requests.post(blogURL, auth=(user, password), json=data)

    return r.status_code, r.text
