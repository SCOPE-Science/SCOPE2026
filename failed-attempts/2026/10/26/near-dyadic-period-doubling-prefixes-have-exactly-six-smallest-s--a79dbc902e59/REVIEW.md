# Independent mathematical audit

## correctness

PASS

The base and finite parity certificate reproduced using a separately written check, not the frozen verifier. On P4 it exhausted 105 candidate pairs against all 75 distinct factors and returned exactly (4,8),(4,10),(5,10),(6,11),(6,12),(8,12). It found all six test factors in P5 and six odd/eight even signature types from the aligned two-block contexts, with the first four one-sided centers checked separately. No odd signature and second signature cover the required factors. Length-nine windows fit inside at most two aligned length-sixteen blocks; finite right truncation can only remove crossing occurrences. The infinite induction is sound: P_n=φ(P_(n−1))0; each factor with even positions lifts from a consecutive source interval, and the appended zero handles a trailing odd zero. The singletons lift because the source contains both letters. Conversely every source factor of length at least two contains a zero, so its image has a one at a relative even position and must begin at an odd absolute position wherever it occurs. An even marked position therefore projects to a marked source occurrence. Target 1 and target 00 check the source singleton 0 and 1 respectively. The local exclusion and projection force halving at every level n≥5, and the two distinct singleton factors rule out cardinality one. Replay: /workspace/branches/0ea0c230-e2c0-4dd9-935e-0b3f4e0e5065/independent_check.py and independent_check.out.

## originality

FAIL

A distinct indexed Resultary record gives exactly the same complete six-pair classification, with the same domain and essentially the same lifting/parity/projection strategy (using a different finite signature test). It even states the six-to-two contrast with the full dyadic word. The frozen claim has no supported distinct mathematical remainder. This is a finding of exact catalogue coverage, not a finding about which author obtained the result first; the duplicate's path date is later than the frozen source's, and no derivation or priority relation was established.

## value

PASS

The mathematical result is a natural infinite structural classification, not just another computation of a known minimum size: it locates all optimal pairs and gives the scaling at the boundary immediately before dyadic length. That intrinsic value does not turn a duplicate classification into a distinct contribution; acceptance fails on originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
