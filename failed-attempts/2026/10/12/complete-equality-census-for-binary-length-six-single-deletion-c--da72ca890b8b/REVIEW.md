# Independent mathematical audit

## correctness

PASS

The compatibility graph on all 64 binary six-bit strings connects exactly disjoint one-deletion shadows. Every binary length-six single-deletion code is a clique and conversely. A NEW independent NetworkX full maximal-clique traversal found 1,473 compatibility edges, exactly 62,707 maximal cliques, largest clique size 10, exactly 9 labeled size-10 maxima. Intersection of maxima equals {000000,001100,110011,111111}; shadow-union cardinalities are [26,28,28,28,30,30,30,30,32]; sorted census SHA-256 082cb965d2fdf3639d1e269042c7b0beb4c6fc31317c3158df3d0ef89093582b. Explicit complement and reversal actions produce orbit sizes 1,1,1,2,2,2; only VT_0(6) has all 32 descendants and equals the sole maximum VT syndrome class. The target’s branch-and-bound Bron–Kerbosch pruning preserves all size-10 candidates but does NOT enumerate every maximal clique when pruning below the running best; its counter maximal_count must not be interpreted as total maximal cliques. This auxiliary limitation does not falsify the enumerated final theorem.

## originality

FAIL

**Decisively covered by an already published stronger exact result.** The 2026-10-04 published Resultary record “Complete census of maximum binary length-six single-deletion codes” (SCOPE-20261004-235d4ba50b9c) explicitly establishes the same exact number nine, the same four-word common core, the unique VT_0(6) perfect maximum, and the identical complement/reversal orbit sizes. It additionally classifies descendant coverage 26/28/30/32, so it is strictly more informative. Its published date October 4 precedes this record’s October 12 publication. The prior’s full RESULT.md and metadata were read, not inferred from a search snippet. Consequently target is implication-equivalent on all its claimed invariants; no new claimed scientific conclusion remains. Earlier Kulkarni/Kiyavash and VT optimality bounds alone do not cover the census, but the directly matching October 4 source does.

## value

FAIL

A nine-code equality classification of a natural deletion-channel extremum has mathematical value in isolation, but this submission is an exact recomputation of a published all-maximizer census, not a new motivated refinement. Re-implementing an exhaustive graph search and confirming its known numbers does not create new value under this novelty/value criterion. The earlier publication additionally proves a strictly richer shadow-size distribution. Therefore the submitted FINAL claim fails value as an original contribution; it cannot be fixed by disclaiming priority or adding the same certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
