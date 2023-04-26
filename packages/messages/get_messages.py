


def main(args):
    # This function works fine

    username = args.get('name', None)

    if username is None:
        return {"body": "you need a \'name\' parameter!"}


    # TODO get messages from DB

    # structure messages into appropriate response

    response = dict()

    person1 = "Sally"
    person2 = "Bob Rossy"

    # placeholder info
    p1_msg1 = {"to": username, "from": person1, "timestamp": "2023-04-01T14:20:30+01:00", "content": "hello! hows it going?",}
    p1_msg2 = {"to": username,"from": person1,"timestamp": "2023-04-01T14:20:30+47:00","content": "I like your content and would like to work with you!",}
    p1_msg3 = {"to": person1,"from": username,"timestamp": "2023-04-01T14:20:47+23:00", "content": "Its going good! Lets work together, jolly chap.",}
    p1_msgs = [p1_msg1, p1_msg2, p1_msg3]

    dm1 = {"with": person1, "messages": p1_msgs}

    p2_msg1 = {"to": person2,"from": username,"timestamp": "2023-04-03T14:20:30+01:00","content": "Yo I like how your art makes me feel. I get all tingly n shii",}
    p2_msg2 = {"to": username,"from": person2,"timestamp": "2023-04-03T14:20:30+47:00","content": "Thanks dawg thats a weird comment but I appreicate it. Keep on #tinglin",}
    p2_msg3 = {"to": person2,"from": username,"timestamp": "2023-04-03T14:20:47+23:00","content": "I will for you, big hoss",}
    p2_msgs = [p2_msg1, p2_msg2, p2_msg3]

    dm2 = {"with": person2, "messages": p2_msgs}

    response["body"] = [dm1, dm2]

    return response
