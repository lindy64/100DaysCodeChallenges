import time
start = time.time()

import csv
from urllib.request import urlretrieve
from collections import defaultdict, namedtuple, Counter, OrderedDict
import itertools
from operator import itemgetter


MOVIE_URL = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
MOVIE_DATA = '/Users/davidythomas/PycharmProjects/100days/100days/movies/movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

urlretrieve(MOVIE_URL, MOVIE_DATA)

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    avg_scores = {}
    for k in directors.keys():
        if len(directors[k]) >= MIN_MOVIES:
            avg_scores[k] = _calc_mean(directors[k])

    avg_scores = OrderedDict(sorted(avg_scores.items(), key=itemgetter(1), reverse=True))
    return avg_scores


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total = 0
    for i in movies:
        total += i.score
    return round(total / len(movies), 1)


def print_results(directors, directors_avg_scores):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    x = itertools.islice(directors_avg_scores.items(), 0, NUM_TOP_DIRECTORS)
    position = 0
    for i in x:
        position += 1
        spacing = " " * (60 - 4 - len(i[0]) - 3)
        print(f"{format(position, '02')}. {i[0]}{spacing}{i[1]}")
        print(sep_line)

        # Order the Directors Movies
        directors[i[0]].sort(key=lambda k: (k[2]), reverse=True)
        for f in directors[i[0]]:
            spacing = " " * (60 - 6 - len(f.title) - 3)
            print(f"{f.year}] {f.title}{spacing}{f.score}")
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors_avg_scores = get_average_scores(directors)
    print_results(directors, directors_avg_scores)
    end = time.time()
    print(end - start)
    # 0.10145282745361328


if __name__ == '__main__':
    main()
