"""Independent, full labelled-valuation check for three-by-m frames, m=1..5.

Unlike checker.py, this constructs the full frame for each fixed number of
columns without column-type compression.  It computes complete modal-depth
signatures for every pointed valuation simultaneously.
"""

def check(m):
    n = 3*m
    models = 1 << n
    rows = [[i*m+j for j in range(m)] for i in range(3)]
    columns = [[i*m+j for i in range(3)] for j in range(m)]
    # Enumerate all 2^(3m) Boolean valuations with named points.
    atoms = [((v >> w) & 1) for v in range(models) for w in range(n)]
    groups = [list(range(v*n,(v+1)*n)) for v in range(models)]
    colors = atoms[:]
    depths = [len(set(colors))]
    for d in range(1,6):
        sigs = []
        for v in range(models):
            offset = v*n
            # The row/column modalities include reflexive points.
            h = [frozenset(colors[offset+j] for j in members) for members in rows]
            t = [frozenset(colors[offset+j] for j in members) for members in columns]
            sigs.extend((atoms[offset+i],h[i//m],t[i%m]) for i in range(n))
        # Relabel by first occurrence, a different implementation strategy.
        dictionary = {}
        fresh = []
        for sig in sigs:
            if sig not in dictionary:
                dictionary[sig] = len(dictionary)
            fresh.append(dictionary[sig])
        assert len(dictionary) >= len(set(colors))
        colors = fresh
        depths.append(len(dictionary))
    return depths

expected = {
   1:[2,4,4,4,4,4],
   2:[2,8,28,28,28,28],
   3:[2,8,60,88,88,88],
   4:[2,8,64,136,146,146],
   5:[2,8,64,140,164,164],
}
for m in range(1,6):
    result = check(m)
    assert result == expected[m],(m,result,expected[m])
    print('DIRECT_FRAME_OK',m,3*m,1<<(3*m), result)
