def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # matchingWords("this is good","Python is good")
    sentences = ["This is good","Python is good","user is Narendra and narendra","and narendra love good python",]

    query = input("Please enter the string\n")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)

    sortedsentscore = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True)]

    # print(sortedsentscore)

    print(f"{len(sortedsentscore)} results found!")
    for score, item in sortedsentscore:
        print(f'"{item}": with a score of {score}')
