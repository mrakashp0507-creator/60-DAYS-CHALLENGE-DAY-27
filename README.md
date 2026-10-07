# Day 27 - Hashing Systems

## Social Media Duplicate Activity Detector

This project simulates a social media platform that wants to detect
repeated activity within a limited time/distance window.

The system uses hashing with a sliding window to detect duplicates
efficiently.

---

## Problem

Bots and suspicious accounts may repeatedly perform the same activity.

The goal is to detect whether the same activity appears within K positions
of its previous occurrence.

Example:

    A B C A

If K = 3:

    Duplicate detected

---

## Approach

The solution uses:

- Hash Set
- Sliding Window

The set stores only recent events within the K-distance window.

For every new event:

1. Remove events that are outside the window.
2. Check whether the current event already exists in the set.
3. If it exists, report suspicious activity.
4. Otherwise, add the event to the set.

---

## Example

Events:

    A
    B
    C
    A

K:

    3

The second A is within 3 positions of the first A.

Result:

    Duplicate detected

---

## Why Hashing?

A brute-force solution would repeatedly compare the current event with
previous events.

That can require O(n * k) comparisons.

Using a hash set provides approximately O(1) average lookup time.

Therefore, the complete sliding-window solution runs in:

    O(n)

time.

---

## Complexity

Time Complexity:

    O(n)

Average hash-set lookup is O(1).

Space Complexity:

    O(k)

Only the recent K events are stored.

---

## Real-World Applications

Hashing is widely used in:

- Fraud detection
- Spam filtering
- Bot detection
- Cybersecurity
- Duplicate detection
- Caching
- Database indexing
- Social media monitoring

---

## How to Run

Open the VS Code terminal:

    python day27_duplicate_activity.py

Enter the maximum K distance when prompted.

---

## Learning Outcomes

- Learned hash-set based lookup.
- Implemented a sliding window.
- Detected duplicates within K distance.
- Simulated suspicious social media activity.
- Compared hashing with brute-force searching.
- Understood O(n) average-time duplicate detection.
