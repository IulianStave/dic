def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("how","who","what")
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input('Say something:')
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))
print(" ".join(results))

