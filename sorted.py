"""
Python iterable function: Sorted

Differences between sort() and sorted()
sort()
- only works with lists
- modify the list

sorted()
- works with any kind of iterable
- generate a new list]
- Always return a list

"""

number_list = [1, 6, 3, 9, 4, 2]
print (number_list)

# Return a list by default
print(sorted(number_list))

# Return a tuple
print(tuple(sorted(number_list)))

# Return a set
print(set(sorted(number_list)))

# Using sorted params:
print(sorted(number_list, reverse=True))

# Exemple

users_tweets = [
    {'username': 'Matheus', 'tweets': ['Studying python', 'GO is awsome']},
    {'username': 'Makarenna', 'tweets': ['I love coffee']},
    {'username': 'Chris', 'tweets': []},
    {'username': 'Joe', 'tweets': ['Studying how to cook', 'mastercheff is good']},
    {'username': 'Charlie', 'tweets': ['Studying how to play piano', 'i hate my brother']},
    {'username': 'Julie', 'tweets': []},
]

print(users_tweets)

# By default print sorts the list by lenght
print(sorted(users_tweets, key=len))

# sorted() using lambda functions
print(sorted(users_tweets, key=lambda user: user['username']))

# sorted() reverse param:
print(sorted(users_tweets, key=lambda user: user['username'], reverse=True))

# sorting by number of tweets
print(sorted(users_tweets, key=lambda user: len(user['tweets'])))

# sorting by number of tweets using reverse
print(sorted(users_tweets, key=lambda user: len(user['tweets']), reverse=True))



# Youtube Exemple

youtube_video = [
    {'video_name': 'The HU - Yuve Yuve Yu (Official Music Video)', 'views': 82938592},
    {'video_name': 'Garmarna - Herr Mannelig', 'views': 23723705 },
    {'video_name': 'System Of A Down - Toxicity (Official Video)', 'views': 582769226},
    {'video_name': 'Aurora - Runaway (Live on the Honda Stage)', 'views': 10043545},
    {'video_name': 'AURORA - Scarborough Fair | LEGENDADO + Lyrics', 'views': 1700688},
    {'video_name': 'Pearl Jam - Black (Prague 1.7.2018)', 'views': 20894983},
]

# sorting by number of views
print(sorted(youtube_video, key=lambda video: video['views']))

# sorting by number of views using reverse
print(sorted(youtube_video, key=lambda video: video['views'], reverse=True))

# sorting by first letter
print(sorted(youtube_video, key=lambda video: video['video_name'][0]))
