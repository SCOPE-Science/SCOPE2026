"""Exact finite checks for alternating adjacent-sum polytope circumball contacts.

Run: python3 verify.py. Standard Python only; does not replace the proof.
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def check_case(s, d):
    r = d // 2
    bounds = [s if i % 2 == 0 else s+1 for i in range(d-1)]
    center_twice = [s] * (2*r) + ([s+1] if d % 2 else [])
    expected_4R2 = 2*r*s*s + ((s+1)**2 if d % 2 else 0)
    expected_contacts = (3**r if d % 2 == 0 else 5*3**(r-1)) if s == 1 else fib(d+2)
    expected_pairs = 2**(r-1) if s == 1 else 1
    count, max_distance, farthest = 0, -1, []
    def enumerate_prefix(prefix):
        nonlocal count, max_distance, farthest
        j = len(prefix)
        if j == d:
            count += 1
            four_d2 = sum((2*x-y)**2 for x, y in zip(prefix, center_twice))
            if four_d2 > max_distance:
                max_distance, farthest = four_d2, []
            if four_d2 == max_distance:
                farthest.append(tuple(prefix))
            return
        upper = bounds[j-1] - prefix[-1] if j > 0 else s
        if j > 0 and j < d-1:
            upper = min(upper, bounds[j])
        for x in range(upper+1):
            enumerate_prefix(prefix+[x])
    enumerate_prefix([])
    contacts = set(farthest)
    opposite_pairs = sum(1 for p in contacts
                         if (q := tuple(y-x for x, y in zip(p, center_twice))) in contacts and p < q)
    assert (max_distance, len(contacts), opposite_pairs) == \
           (expected_4R2, expected_contacts, expected_pairs), (d,s,max_distance,len(contacts),opposite_pairs)
    return count

def main():
    cases, points = 0, 0
    for d in range(2, 9):
        for s in range(1, 5):
            points += check_case(s, d)
            cases += 1
    assert (cases, points) == (28, 74364), (cases, points)
    print(f"PASS: {cases} parameter cases; {points} feasible integer points enumerated")

if __name__ == '__main__':
    main()
