### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "e2a0c88c73bc0d43961b81433a4abd7742f2344a51e154d04b2c25edbc8edbfb"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 7
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "pcap"
#"Are encoding and encryption the same? - Yes/No": "No"
#"Is it possible to decrypt a message without a key? - Yes/No": "No"
#"Is it possible to decode a message without a key? - Yes/No": "No"
#"Is a hashed message supposed to be un-hashed? - Yes/No": "Yes"
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ": 
#"Is MD5 a secured hashing algorithm? - Yes/No": 
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number: 7" 
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3
