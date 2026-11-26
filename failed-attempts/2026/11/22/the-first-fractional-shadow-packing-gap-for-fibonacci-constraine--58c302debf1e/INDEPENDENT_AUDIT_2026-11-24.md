# Independent mathematical audit

## correctness

PASS

For 1≤n≤6, disjoint-shadow codebooks and hitting sets of equal size certify both optima by weak duality. At n=7, rational primal and dual vectors both sum to 9 and satisfy every inequality, so U_7=9. Independently regenerated the words and shadows with integer masks and checked every supplied certificate, including all eight confusability cliques. Distinct words conflict iff each word has at most one 1 outside the other: their bitwise intersection then belongs to both shadows. Counting every compatible subset once in increasing mask order gave counts by size 0 through 8 of 1,34,401,2068,4860,5004,2048,282,10, with none larger. This independently proves M_7=8 and precisely ten labeled maximizing codebooks. Replay: python3 /workspace/branches/replay145.py (FIB lines); output /workspace/branches/replay145.txt.

## originality

FAIL

A distinct indexed record, e6be4e5db641, explicitly gives the same family, channel, LP, complete initial integer and fractional values, threshold and ten optimizers, and goes further by classifying those optimizers. The exact n=7 rational primal and dual vectors in its proof also match the frozen ones. This is demonstrated coverage by a separate record, not a determination of which result came first: the common date does not resolve chronology. No distinct central claim survives.

## value

FAIL

An integer-valued fractional optimum that still overestimates the code size is a motivated boundary. However, the complete stated threshold, capacities, and optimizer count are already documented together in a distinct exact result, with a stronger classification. The alternative clique-cover and counting certificates improve checkability but the frozen claim does not give a distinct structural or quantitative conclusion; certificate substitution alone is not a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
