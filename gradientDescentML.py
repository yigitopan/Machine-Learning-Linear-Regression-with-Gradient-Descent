import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', '--data', type=str)
parser.add_argument('--eta', '--eta', type=float)
parser.add_argument('-threshold', '--threshold', type=float)
args = parser.parse_args()


feature1 = []
feature2 = []
target = []

with open(args.data, 'r') as file:
    array = file.readlines()
    array = [row.split(',') for row in array]

feature0 = []


for i in range(1, len(array)):
    feature1.append(float(array[i][0]))
    feature2.append(float(array[i][1]))
    target.append(float(array[i][2]))

X0 = []
X1 = []
X2 = []
for i in range(1000):
    feature0.append(1)

targetList = []
for i in range(len(array)-1):
    X0.append(feature0[i])
    X1.append(feature1[i])
    X2.append(feature2[i])
    targetList.append(target)

l_rate = args.eta

gradientw0 = 0
gradientw1 = 0
gradientw2 = 0
gradientWi = 0

w0 = 0
w1 = 0
w2 = 0
error = 0
error2 = 100000
# threshold = 0.0001
threshold = args.threshold
i2 = 0

for i2 in range(len(feature0)):
    for i in range(len(target)):

        fyi = ((w0 * X0[i]) + (w1 * X1[i]) + (w2 * X2[i]))
        error = error + (target[i] - fyi)*(target[i] - fyi)
        gradientw0 = gradientw0 + X0[i] * (target[i] - fyi)
        gradientw1 = gradientw1 + X1[i] * (target[i] - fyi)
        gradientw2 = gradientw2 + X2[i] * (target[i] - fyi)

    w0 = round(w0, 9)
    w1 = round(w1, 9)
    w2 = round(w2, 9)


    print(i2,",",w0,",",w1,",",w2,",",error, sep="")

    w0 = 0 + (l_rate * gradientw0)
    w1 = 0 + (l_rate * gradientw1)
    w2 = 0 + (l_rate * gradientw2)

    if error2-error<threshold:
        break;
    error2 = error
    error = 0


