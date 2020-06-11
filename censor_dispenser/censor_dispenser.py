# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
print(email_one)
# print(email_two)
# print(email_three)
# print(email_four)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_phrase(email, phrase = 'learning algorithms'):
    if phrase in email:
        email = email.replace(phrase, '*' * len(phrase))
    return email
# print()
# print()
# print(censor_phrase(email_one))
# print()
# print()

def censor_list(email, proprietary_terms):
    proprietary_terms.sort(key=len, reverse=True)
    for term in proprietary_terms:
        email = email.replace(term, '*' * len(term))
        email = email.replace(term.title(), '*' * len(term))
    return email
# print()
# print()
# print(censor_list(email_two, proprietary_terms))
# print()
# print()

def censor_negative(email, proprietary_terms, negative_words):
    proprietary_terms.sort(key=len, reverse=True)
    negative_words.sort(key=len, reverse=True)
    for term in proprietary_terms:
        email = email.replace(term, '*' * len(term))
        email = email.replace(term.title(), '*' * len(term))
    for word in negative_words:
        email = email.replace(word, '*' * len(word))
        email = email.replace(word.title(), '*' * len(word))
    return email
# print()
# print()
# print(censor_negative(email_three, proprietary_terms, negative_words))
# print()
# print()

def censor_all(email, proprietary_terms, negative_words):
    email = censor_negative(email, proprietary_terms, negative_words)
    email = email.split()
    # print(email)
    for i in range(0, len(email)):
        if '*' in email[i]:
            email[i-1] = '*' * len(email[i-1])
        if '*' in email[i]:
            email[i] = '*' * len(email[i])
    email = ' '.join(email)
    return email
print()
print()
print(censor_all(email_four, proprietary_terms, negative_words))
print()
print()