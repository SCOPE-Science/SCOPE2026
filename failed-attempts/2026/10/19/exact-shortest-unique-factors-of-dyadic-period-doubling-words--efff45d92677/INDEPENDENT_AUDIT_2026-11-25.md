# Independent mathematical audit

## correctness

PASS

The simultaneous induction is valid. In either target word every length-four window contains a 1 (its two odd global positions complement consecutive source letters, which cannot both be 1). Thus multiplicities for lengths at least four separate by start parity. Odd lengths 2m−1 read m source letters at odd starts and m−1 at even starts; even lengths 2m read m in both. Imposing the target's end bound gives exactly X or its truncation Y as in RESULT.md:26. Below 2L−1 this reads at most L−1 source letters; uniqueness at a shorter length than four would also give a unique length-four extension. At 2L−1 only odd starts can be unique, with source X for P and Y for Q and position map j→2j+1. The k=4 base and this map give all stated lengths and positions. An independent exact check generated P by substitution, truncated for Q, and counted overlapping slices at every length through the first singleton for k=1–10; it confirmed all claimed cases k=4–10. This is bounded corroboration, not a substitute for the induction. Replay: generate from 0 using 0→01, 1→00 and count the slices X[i:i+ell] for 0≤i≤len(X)−ell separately for each ell and for each of P and Q.

## originality

FAIL

A distinct, stronger Resultary record together with its terminal-suffix lemma covers the entire frozen result, not just the complete-word half. This is demonstrable mathematical coverage in the current catalogue, not a claim that the November record predates the October record or that the October author had access to it. No earlier publication of the full claim was established.

## value

FAIL

The shortest identifying factor in a finite morphic iterate and stability under deletion are natural exact invariants. However, the complete-word answer is already contained in the stronger catalogue theorem, and deleting a terminal occurrence is an immediate application of that record's odd-multiplicity lemma. Thus no distinct exact invariant or structural content survives as an independent finding under review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
