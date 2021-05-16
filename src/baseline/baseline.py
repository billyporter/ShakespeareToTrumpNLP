#!/usr/bin/env python3
import pickle
import random


def get_potential(shake_line, trump_speech, trump_tweets):
    shake_words = shake_line.split()
    shake_length = len(shake_words)
    potential = []
    combined_trump = trump_speech + trump_tweets
    margin = 3
    while len(potential) == 0:
        for line in combined_trump:
            trump_words = line.split()
            if len(trump_words) < shake_length + margin and len(
                    trump_words) > shake_length - margin:
                potential.append(trump_words)
        margin += 1
    return potential


def assign_score(shake_line, potential):
    scores = []
    shake_words = shake_line.split()
    for line in potential:
        score = 0
        for shake, trump in zip(shake_line, line):
            if shake == trump:
                score += 1
        scores.append(score)
    return scores


def get_best(scores, potential):
    max_sentences = []
    max_score = 0
    for i, score in enumerate(scores):
        if score > max_score:
            max_score = score
            max_sentences = []
        if score == max_score:
            max_sentences.append(potential[i])
    return random.choice(max_sentences)


def main():
    shake_lines = ''
    trump_speech = ''
    trump_tweets = ''
    with open("../../data/shakespeare/pickled/proc_original", "rb") as f:
        shake_lines = pickle.load(f)
    with open("../../data/trump/pickled/cln_speech_list", "rb") as f:
        trump_speech = pickle.load(f)
    with open("../../data/trump/pickled/cln_twts_list", "rb") as f:
        trump_tweets = pickle.load(f)

    random.shuffle(shake_lines)
    for line in shake_lines:
        print(line)
        potential_sentences = get_potential(line, trump_speech, trump_tweets)
        scores = assign_score(line, potential_sentences)
        best_sentence = get_best(scores, potential_sentences)
        print(" ".join(best_sentence))
        break


if __name__ == '__main__':
    main()