# Python iterable function: Filter

tuple_values = 10, 20, 30, 40, 50

average = sum(tuple_values) / len(tuple_values)

print(average)

obj_filter = filter(lambda y: y >= average, tuple_values)

print(list(obj_filter))

# Using statitistic lib
import statistics

bitcoin_values = [51859.30, 49338.30, 42869.52, 56765.50, 44461.32, 47837.22, 41987.88]
btc_avg = sum(bitcoin_values) / len(bitcoin_values)
# or
btc_avg2 = statistics.mean(bitcoin_values)

btc_filter = filter(lambda x: x > btc_avg, bitcoin_values)
print(btc_avg)
print(btc_avg2)

print(list(btc_filter))
print(list(filter(lambda x: x > btc_avg2, bitcoin_values)))

# the filter object after used clean the memory
print(list(btc_filter))


crypto_list = ['BTC', '', '', 'ETH', 'LTC', '', 'XRP', '', '', '', 'CHZ']
print(crypto_list)

# Removing empty spaces
obj2_filter = filter(lambda x: len(x) > 0, crypto_list)
print(list(obj2_filter))

# Filtering by None
obj3_filter = filter(None, crypto_list)
print(list(obj3_filter))


users_tweets = [
    {'username': 'Matheus', 'tweets': ['Studying python', 'GO is awsome']},
    {'username': 'Makarenna', 'tweets': ['I love coffee']},
    {'username': 'Chris', 'tweets': []},
    {'username': 'Joe', 'tweets': ['Studying how to cook', 'mastercheff is good']},
    {'username': 'Cristiano', 'tweets': ['i am the best', 'the monster']},
    {'username': 'Jake', 'tweets': ['Studying how to play guitar', 'I love cookies']},
    {'username': 'Charlie', 'tweets': ['Studying how to play piano', 'i hate my brother']},
    {'username': 'Allan', 'tweets': ['I love my brother', 'my son is an idiot']},
    {'username': 'Julie', 'tweets': []},
]

# Filtering by inactive users

users_inactive = list(filter(lambda user: len(user['tweets']) == 0, users_tweets))
inactive_names = [item['username'] for item in users_inactive]

print(inactive_names)

# Another way
users_inactive = list(filter(lambda user: not user['tweets'], users_tweets))
inactive_names = [item['username'] for item in users_inactive]

print(inactive_names)
