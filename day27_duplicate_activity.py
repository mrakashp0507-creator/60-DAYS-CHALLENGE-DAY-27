# Day 27 - Hashing Systems
# Detect duplicate social media activity within K distance

def contains_duplicate_within_k(events, k):
    """
    Detect whether the same event appears within k positions.
    Uses a sliding window with a set.
    """

    if k <= 0:
        return False, None

    window = set()

    for i in range(len(events)):

        # Remove the event that is now outside the window
        if i > k:
            window.remove(events[i - k - 1])

        # Check whether the current event already exists
        if events[i] in window:
            return True, (events[i], i)

        # Add current event to the window
        window.add(events[i])

    return False, None


def display_events(events):
    print("\nSocial Media Events:")

    for i in range(len(events)):
        print(f"{i}: {events[i]}")


print("======================================")
print("      SOCIAL MEDIA FRAUD DETECTOR")
print("======================================")

# Simulated social media activity
events = [
    "user101:BuyNow",
    "user205:Hello",
    "user301:GameTonight",
    "user101:BuyNow",
    "user402:Welcome",
    "user505:FollowMe",
    "user205:Hello",
    "user601:GoodMorning"
]

display_events(events)

try:
    k = int(input("\nEnter maximum K distance: "))

    found, result = contains_duplicate_within_k(events, k)

    print("\n======================================")

    if found:
        event, index = result

        print("🚨 SUSPICIOUS ACTIVITY DETECTED!")
        print("Repeated event:", event)
        print("Detected at index:", index)
        print(f"The same activity appeared within {k} positions.")

    else:
        print("✅ No suspicious duplicate activity found.")
        print(f"No duplicate was found within {k} positions.")

    print("======================================")

except ValueError:
    print("Please enter a valid integer for K.")