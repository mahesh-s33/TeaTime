def checker(phrase,list_of_words, output = []):
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            checker(phrase[len(word):], list_of_words, output)
    return output

if __name__ == '__main__':
    print(checker('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))