# binary_search_exercise

This repo contains two scripts, one in Python and one in Ruby, that aim to illustrate the efficiency of binary search.

Each script does the same thing; they search for a number in an ordered list. The programs take user input for length of the list, which is populated with sequential numbers. A target number is chosen at random, and then the program counts the number of times it divides the list in its searches. Final output tell you
* the length of the list
* the target number
* the number of times the list was divided in half in the course of searching (i.e., the number of steps taken to arrive at the answer)
* the calculation of log<sub>2</sub>n for the search

The Python script is borrowed and amended from the book [_Grokking Algorithms_](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230) by [Aditya Bhargava](https://github.com/egonSchiele).
The Ruby adaptation was ported by me. Both will break on bad input, and there's no tests. I'll change that when time allows, or if someone submits pull requests.
