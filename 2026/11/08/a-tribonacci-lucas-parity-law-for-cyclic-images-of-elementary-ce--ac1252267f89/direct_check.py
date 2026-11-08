"""Independent exhaustive cyclic image enumeration and recurrence comparison."""

def image_set(rule, n):
    outputs = set()
    for x in range(1 << n):
        y = 0
        for i in range(n):
            a = (x >> ((i - 1) % n)) & 1
            b = (x >> i) & 1
            c = (x >> ((i + 1) % n)) & 1
            y |= ((rule >> (4*a + 2*b + c)) & 1) << i
        outputs.add(y)
    return outputs


def main():
    from verify_relation import sequence
    limit = 16
    values = {r: sequence(r, limit)[1] for r in (172, 184)}
    for n in range(1, limit + 1):
        for rule in (172, 184):
            actual = len(image_set(rule, n))
            assert actual == values[rule][n], (n, rule, actual)
        assert values[184][n]-values[172][n] == (2 if n%2 == 0 else 0)
    # At n=5, binary output 11000 is reachable for Rule 172 but not 184.
    assert 0b00011 in image_set(172, 5)
    assert 0b00011 not in image_set(184, 5)
    print('PASS: all cyclic inputs, both rules, lengths 1 through', limit)
    print('PASS: Rule 172 / Rule 184 nonidentical language witness 11000')

if __name__ == '__main__':
    main()
