import json
import re
import pickle


def remove_junk(text):
    linkRegex = re.compile(
        "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",
        re.IGNORECASE)
    mentionsRegex = re.compile('\B\@\w+')
    ampRegex = re.compile('\B\&\w+')
    emojisRegex = re.compile(u"[\U0001F600-\U0001F6FF]", flags=re.UNICODE)

    # Remove links
    links = linkRegex.findall(text)
    for link in links:
        text = text.replace(link, "")

    # Remove mentions
    counter = 0
    mentions = mentionsRegex.findall(text)
    for mention in mentions:
        counter += 1
        text = text.replace(mention, mention[1:])

    # Remove ampersand glitch
    amps = ampRegex.findall(text)
    for amp in amps:
        text = text.replace(amp, "&")

    # Remove emojis (Sad!)
    text = deEmojify(text)
    return text


def pad_puncutation(s):
    s = re.sub('([.,!?()])', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    return s


def clean_trump_tweets():
    # 5,104,637
    tweets_list_cleaned = []

    i = 0
    with open('../../data/trump/tweets/tweets.json') as f:
        tweets_dict = json.load(f)
    for key in tweets_dict:

        # Remove retweets
        if key["isRetweet"] == 't':
            continue

        if len(key["text"]) > 1 and key["text"][0:2] == "\"\"":
            print(key["text"])
            continue

        # # Filter out junk
        tweetText = key["text"]
        tweetText = remove_junk(tweetText)

        # Replace U.S.A with USA and U.S. with US before padding
        tweetText = tweetText.replace("U.S.A.", "USA")
        tweetText = tweetText.replace("U.S.", "USA")
        tweetText = tweetText.replace("W.H.", "White House")

        # Remove trailing space
        tweetText = pad_puncutation(tweetText)
        tweetText = tweetText.strip()

        if len(tweetText) == 0:
            continue

        tweets_list_cleaned.append(tweetText)
    print(len(tweets_list_cleaned))
    return tweets_list_cleaned


def deEmojify(text):
    regrex_pattern = re.compile(
        pattern="["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def clean_speeches():
    # 888121 words
    trump_lines = []
    with open('../../data/trump/speeches/speech.txt') as f:
        for line in f:
            if len(line) == 0 or len(line.split()) < 3:
                continue
            line = line.replace("U.S.A.", "USA")
            line = line.replace("U.S.", "USA")
            line = pad_puncutation(line)
            line = line.strip()
            trump_lines.append(line)
    return trump_lines


def write_to_file(tweets_list, speech):
    with open('../../data/trump/tweets/cln_twts.txt', 'w') as f:
        for item in tweets_list:
            f.write("%s\n" % item)

    with open('cln_twts_list', 'wb') as fp:
        print(tweets_list)
        pickle.dump(tweets_list, fp)

    # with open('../../data/trump/speeches/cln_speech.txt', 'w') as f:
    #     for line in speech:
    #         f.write("%s\n" % line)

    # with open('cln_speech_list', 'wb') as fp:
    #     pickle.dump(speech, fp)


def main():
    tweets_list_cleaned = clean_trump_tweets()
    # print(tweets_list_cleaned)
    clean_speech = clean_speeches()
    write_to_file(tweets_list_cleaned, clean_speech)


if __name__ == '__main__':
    main()