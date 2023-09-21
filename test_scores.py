#!/usr/bin/env python3

print("The Test Scores Application")
print()

more_tests = "y"

while more_tests.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("========================")

    counter = 0
    score_total = 0
    test_score = 0

    while (test_score := input("Enter test score: ").lower()) != "end":
        test_score = int(test_score)
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print("Test score must be between 0 and 100. Try Again")

    average_score = round(score_total / counter, 2)

    print("====================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()

    more_tests = input("Enter another set of test scores (y/n)? ")

print("bye")
