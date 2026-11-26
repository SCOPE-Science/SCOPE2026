# Independent mathematical audit

## correctness

PASS

The stated open-neighborhood shatter function is correct. Generic endpoints can be obtained by first slightly enlarging every host interval and then perturbing them, preserving all adjacencies. For a query with a left-endpoint prefix of length k, right-endpoint deletions give at most k nonempty nested sets. If the earliest-ending and latest-starting marks differ, short probes just outside them recover two diagonal-deleted traces as ordinary queries. If they coincide, that mark is contained in all the others; prefixes of length <m permit no right deletions, hence at most 2m query traces in all and at most 3m−1 total, enough for m≥3. Boolean ceilings handle m≤2. The prose in RESULT.md:36 reverses before/after relative to predecessor/successor; the given coordinates themselves work: [2a−3/4,2b−1/4] hits exactly the block a,…,b in I_i=[2i−2,2i+1]. Add an empty probe and the m−2 distinct self-deleted interior patterns {i−1,i+1}. This proves the numerical claim and the stated VC consequences.

## originality

FAIL

A distinct indexed Resultary record (assigned record 5) already covers the same exact open trace maximum on the same class and additionally proves rigidity and minimum order. Coverage is demonstrable; historical priority between the two same-day records is not. The only extra boundary case is the tautology at m=0; VC dimension 3 and density 2 follow immediately from the common exact values. Fixing the witness sentence or providing a new verification would not produce a distinct finding.

## value

PASS

The mathematical question is substantive: exact classwide growth distinguishes ordinary query traces from the exceptional diagonal deletions and gives both a finite shattering boundary and a sharp quadratic invariant. This intrinsic value is not a claim that the duplicate submission adds to the corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
