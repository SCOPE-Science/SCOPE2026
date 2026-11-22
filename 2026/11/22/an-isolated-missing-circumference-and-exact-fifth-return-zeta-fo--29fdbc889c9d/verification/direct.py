"""Independent direct state enumeration and constructive orbit splicing check."""
RULE = 73


def update(word, n):
    next_word = 0
    for i in range(n):
        abc = (((word >> ((i-1)%n))&1)<<2) | (((word>>i)&1)<<1) | ((word>>((i+1)%n))&1)
        next_word |= ((RULE>>abc)&1)<<i
    return next_word


def word_bits(x, n):
    return ''.join(str((x>>i)&1) for i in range(n))


def count_cycles(n):
    marked = 0
    for x in range(1<<n):
        y=x
        for _ in range(5):
            y=update(y,n)
        if x==y and x!=update(x,n):
            marked += 1
    assert marked % 5 == 0
    return marked//5


def verify_witness(n, seed):
    x = sum(int(ch)<<i for i,ch in enumerate(seed))
    assert len(seed) == n
    states = [x]
    for _ in range(5):
        states.append(update(states[-1],n))
    assert states[-1] == states[0] and states[1] != states[0]
    histories = [tuple((states[t]>>i)&1 for t in range(5)) for i in range(n)]
    ones=(1,1,1,1,1); zeros=(0,0,0,0,0)
    assert any(histories[i] == ones and histories[(i+1)%n] == zeros for i in range(n))
    return histories


def verify_splice():
    # All replacement paths connect temporal-constant pair 10 back to 10.
    # Each intermediate triple must satisfy the Rule-73 local temporal equation.
    # Pair-vertex 10 has admissible closed paths of lengths 3 and 4.
    short = [1, 0, 1, 1, 0]
    long = [1, 0, 0, 1, 1, 0]
    for seq in (short, long):
        assert seq[:2] == seq[-2:] == [1, 0]
        assert all(((RULE >> (4*seq[i]+2*seq[i+1]+seq[i+2])) & 1) == seq[i+1]
                   for i in range(len(seq)-2))
    # Two witnessed temporal 5-cycles share constant columns 1 -> 0.
    histories11 = verify_witness(11,'11000000000')
    histories12 = verify_witness(12,'110000000000')
    constant = lambda x: (x,)*5
    for start_histories in (histories11,histories12):
        for increments in ([3],[4],[3,4,3],[4,4,3,4]):
            histories = start_histories[:]
            for delta in increments:
                k = next(i for i in range(len(histories))
                         if histories[i] == constant(1) and histories[(i+1)%len(histories)] == constant(0))
                chosen = short if delta == 3 else long
                # Insert the closed-loop continuation after the pair (1,0).
                place=(k+2)%len(histories)
                histories[place:place] = [constant(v) for v in chosen[2:]]
                n=len(histories)
                # Directly check every local constraint of the 5-row cylinder.
                assert all(histories[i][(t+1)%5] == ((RULE >>
                       (4*histories[(i-1)%n][t]+2*histories[i][t]+histories[(i+1)%n][t]))&1)
                       for i in range(n) for t in range(5))
                assert any(len(set(history))>1 for history in histories)



def main():
    verify_splice()
    expected = {11:11,12:12,13:0,14:14,15:30,16:32,17:51}
    results = {}
    for n in range(3,18):
        results[n] = count_cycles(n)
        assert results[n] == expected.get(n,0), (n,results[n])
    print('DIRECT_OK', results)
    print('WITNESSES_AND_SPLICE_OK')

if __name__ == '__main__':
    main()
