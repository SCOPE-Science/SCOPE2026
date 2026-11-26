# Independent mathematical audit

## correctness

PASS

The matrix is unimodular and cyclic: e3, Me3=e1, M²e3=e1+e2 form an integral basis. The two coprime mod-3 factors of X³−X²−1 give the rank-one and unramified rank-two summands, with residue-unit orders 2 and 8 (the quadratic root has fourth power −1). The scalar lift satisfies v3(λ+1)=1 by the simple-root Taylor expansion at −1, and M⁸−I=3B with det B=1 proves that division by 3 on the quadratic branch is a unit too. Cubing a unit at distance 3^(−s) from 1 increases that valuation by exactly one. Thus the fixed-point counts at 3^r, 2·3^r, 4·3^r and 8·3^r are respectively 1, 3^u, 3^u and 3^(3u), u=min(k,r+1); every period divides 8·3^(k−1). For r≥1, the period-8·3^r population is the difference of consecutive rank-three fixed counts less the new period-2·3^r population, yielding 26·3^(3r)−2·3^r; the initial populations are 24 and 2. Division by length gives exactly the claimed cycle counts, and the geometric sum gives the total. An independent kernel enumeration plus divisor subtraction at k=1,2,3 gave totals 5,35,299 (`python3 /workspace/frozen_review_replay.py 2`); the frozen traversal script was read, not run.

## originality

PASS

The supported distinction is a closed least-cycle census of all modular seed states, not the longest order alone, the period of a standard seed, or its output frequencies. The same-object primary comparisons and distinct catalogue findings inspected do not supply the fixed-point stratification needed to imply the census. The algebraic and divisor-counting methods are standard.

## value

PASS

The full cycle type of a natural recurrence at every 3-adic level is useful state-space information that cannot be recovered from the longest period or a standard-seed calculation. The interaction between residue orders two and eight gives two differently populated period families, and the exact count is uniform in level rather than a list of small enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
