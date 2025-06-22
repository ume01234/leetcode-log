# Two Sum (LeetCode #1)

## ✔︎ Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

## ✔︎ My Thinking
- At first, I thought of a brute-force approach using two loops.
- But that would take O(n^2) time, which is inefficient.
- Then I remembered hash maps are useful for complement checks.

## ✔︎ Failed Attempt
I tried storing all pairs first. It worked, but was too slow.

## ✔︎ Final Solution
Used a single-pass hash map to track the complement.
(See `solution.py`)

## ✔︎ Key Takeaways
- Think of hash maps when you need quick lookups.
- Avoid brute-force unless problem size is small.
