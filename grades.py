"""Student grades: averages, letter grades and a class report."""

GRADE_A = 90
GRADE_B = 75
PASS_MARK = 60

SAMPLE_SCORES = {
    "Ali": [85, 92, 78],
    "Sara": [90, 88, 95],
    "Omar": [55, 61, 48],
    "Zara": [70, 65, 80],
}


def average(scores):
    """Return the mean of a non-empty list of scores."""
    return sum(scores) / len(scores)


def letter_grade(scores):
    """Return "A", "B", "C" or "F" for a student's average score."""
    avg = average(scores)
    if avg >= GRADE_A:
        return "A"
    if avg >= GRADE_B:
        return "B"
    if avg >= PASS_MARK:
        return "C"
    return "F"


def print_report(students):
    """Print each student's average and letter grade."""
    print("Student Report")
    print("--------------")
    for name, scores in students.items():
        print(f"{name}: average={round(average(scores), 2)} "
              f"grade={letter_grade(scores)}")


def top_student(students):
    """Return the name of the student with the highest average."""
    return max(students, key=lambda name: average(students[name]))


def class_average(students):
    """Return the mean of all the students' averages."""
    return average([average(scores) for scores in students.values()])


def add_student(students, name, raw_scores):
    """Convert raw_scores to ints and add the student.

    Raises ValueError if any score is not a whole number.
    """
    students[name] = [int(score) for score in raw_scores]


def main():
    """Build the sample class, add students and print the report."""
    students = dict(SAMPLE_SCORES)
    add_student(students, "Hamza", ["72", "68", "90"])
    try:
        add_student(students, "Bad", ["x", "y"])
    except ValueError:
        print("bad scores")

    print_report(students)
    best = top_student(students)
    print(f"Top student: {best} with average of "
          f"{round(average(students[best]), 2)} "
          "which is the highest in the class")
    print(f"Class average: {round(class_average(students), 2)}")


if __name__ == "__main__":
    main()
