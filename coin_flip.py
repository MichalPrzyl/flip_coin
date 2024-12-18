import random
import matplotlib.pyplot as plt

SIZES = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

data = []

for SIZE in SIZES:
    counter = 1
    values = []
    heads = 0
    tails = 0
    while counter < SIZE + 1:
        x = random.randrange(0, 101)
        if x < 50:
            heads += 1
        else:
            tails +=1 
        values.append(x)
        counter += 1
    difference = abs(heads - tails)
    relative_difference = difference / SIZE
    data.append({
        'size': SIZE,
        'relative_difference': f"{relative_difference/SIZE * 100}",
        'difference': difference,
        'tails': tails,
        'heads': heads
    })

x = [data[el]['size'] for el in range(0, len(SIZES))]
y = [float(data[el]['relative_difference']) for el in range(0, len(SIZES))]
plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('FLIP THE COIN')
plt.show()