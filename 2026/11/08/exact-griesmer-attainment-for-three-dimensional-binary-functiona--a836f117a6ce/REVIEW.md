# Scientific review

## Correctness — PASS

The support-intersection argument derives distance at least \(t\) for any \(t\)-functional batch matrix. The binary three-dimensional Griesmer bound yields \(G(t)=t+\lceil t/2\rceil+\lceil t/4\rceil\). The provided exact finite witness table has 1260 cases spanning all seven nonzero requests of six finite blocks, including all 924 six-request multisets of an eleven-column realization. The checker verifies all requested vector sums and pairwise disjointness, so the finite construction is proved exhaustively, not inferred from samples. Concatenation covers every \(t\ge3\) with exactly \(G(t)\) columns. The separate four-column contradiction establishes the sole excess at \(t=2\), matched by a five-column witness.

## Originality — PASS against checked literature

Zhang–Etzion–Yaakobi (2019) establish the seven-column four-request simplex block and tabulate a nineteen-column ten-request **functional PIR** upper bound, but do not give this eleven-column six-request **functional batch** witness or the eighteen-column ten-request batch consequence. Kılıç–Ravagnani–Salizzoni (2025) provide functional-PIR recurrences and simplex-multiple exact values, not the new simultaneous mixed-request six-block. Boruchovsky–Gruica–Niemann–Yaakobi (2026) treat all-symbol recovery and small request counts rather than the full functional-batch optimum. Searched published mathematical records closest to this topic concern four- or five-request all-symbol codes and a five-request locality-two functional-batch code, none of which dominates the unrestricted six-request theorem. The remaining risk is independently unindexed equivalent batch/RIO constructions.

## Value — PASS

This is an exact all-positive-request-count solution for the smallest genuinely nontrivial dimension in functional batch retrieval. It shows that the Griesmer storage bound is attainable for every request count except exactly two, identifies a finite exception absent in functional PIR, and supplies a concrete eighteen-column ten-request design improving the *2019 construction's* nineteen-column **functional PIR** upper-bound benchmark; this is a historical comparison rather than a claim about the best later PIR bounds. That is a motivated storage-efficiency result, not a mere table recomputation.

## Limitations and relationship to prior work

This is neither a general functional batch conjecture resolution for larger dimensions nor a bounded-locality theorem. The finite recovery table is independently reproducible by checking explicit masks but has not been independently mathematically audited. Priority outside the inspected literature is not certified.

Self-review: passed. Independent audit: not yet performed.
