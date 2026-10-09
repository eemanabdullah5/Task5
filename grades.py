# student grades program
data = {"Ali": [85, 92, 78], "Sara": [90, 88, 95],
        "Omar": [55, 61, 48], "Zara": [70, 65, 80]}


def calc(scores):
    t = 0
    for i in range(len(scores)):
        t = t + scores[i]
    return t / len(scores)


def Result(n):
    a = calc(data[n])
    if a >= 60:
        return "PASS"
    else:
        return "FAIL"


def printReport():
    print("Student Report")
    print("--------------")
    for n in data:
        a = calc(data[n])
        r = Result(n)
        print(n + ": average=" + str(round(a, 2)) + " result=" + r)


def topStudent():
    best = None
    bestAvg = 0
    for n in data:
        a = calc(data[n])
        if a > bestAvg:
            bestAvg = a
            best = n
    if best is None:
        return "nobody"
    return best


def classAverage():
    total = 0
    for n in data:
        total = total + calc(data[n])
    return total / len(data)


def addStudent(n, s):
    try:
        s = [int(x) for x in s]
    except ValueError:
        print("bad scores")
        return
    data[n] = s


if __name__ == "__main__":
    addStudent("Hamza", ["72", "68", "90"])
    addStudent("Bad", ["x", "y"])
    printReport()
    print("Top student: " + topStudent() + " with average of "
          + str(round(calc(data[topStudent()]), 2))
          + " which is the highest in the class")
    print("Class average: " + str(round(classAverage(), 2)))
