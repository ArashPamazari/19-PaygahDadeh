import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

random.shuffle(boys)
random.shuffle(girls)

results = []
for boy, girl in zip(boys, girls):
    results.append((boy, girl))

print(results)
