def signature(a, b):
    num = a * b * (5 - a*a - b*b)
    assert num % 3 == 0
    return num // 3

def predicted(S):
    if S % 2 == 0:
        types = [(S//2 - 1, S//2 + 1)]
        value = (S**4 - 10*S**2 + 24) // 24
    else:
        types = [((S-3)//2, (S+3)//2), ((S-1)//2, (S+1)//2)]
        value = (S**4 - 10*S**2 + 9) // 24
    return types, value

checks = 0
for S in range(6, 201):
    rows = []
    for a in range(2, S//2 + 1):
        b = S - a
        sig = signature(a, b)
        assert sig < 0
        g = b - a
        via_gap_num = S**4 - 10*S**2 + 10*g*g - g**4
        assert via_gap_num % 24 == 0
        assert -sig == via_gap_num // 24
        rows.append((-sig, (a, b)))
        checks += 1
    maximum = max(v for v, _ in rows)
    maximizers = [pair for v, pair in rows if v == maximum]
    expected_types, expected_value = predicted(S)
    assert maximizers == expected_types, (S, maximizers, expected_types)
    assert maximum == expected_value, (S, maximum, expected_value)

assert checks == 9799
print('VERIFY_OK', checks)
