import re

def calculate_profanity(tweet, profanity_words):
    profanity_count = 0
    words = re.findall(r'\b\w+\b', tweet)
    for word in words:
        if word in profanity_words:
            profanity_count += 1
    return profanity_count

def main():
    profanity_words = [' racial', ' slurs']

    with open('tweets.txt', 'r') as file:
        tweets = file.readlines()
    for tweet in tweets:
        profanity_score = calculate_profanity(tweet, profanity_words)
        print(f"Tweet: {tweet}Profanity Score: {profanity_score}")

if __name__ == '__main__':
    main()
