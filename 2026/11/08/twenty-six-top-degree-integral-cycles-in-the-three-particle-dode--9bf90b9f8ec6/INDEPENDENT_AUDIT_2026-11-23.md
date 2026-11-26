# Independent mathematical audit

## correctness

PASS

Comparison theorem 4.5 respects weight (particle number) and computes unordered continuous configuration homology; reduction at all nonisolated vertices leaves two local half-edge differences for each cubic vertex. Weight three bounds degree by three. Independently generated the signed differential on GP(10,2), with a different reference edge (last incident edge in edge-family order) and eliminated rows over Z using smallest column pivots, not the source's column algorithm. There were 9120 columns, 22680 nonempty rows of 22800 possible, 9094 existing unit pivots and nullity 26. Replay: enumerate triples of distinct vertices and binary local choices; place (-1)^t times the selected edge minus reference edge in rows keyed by the two remaining encoded local choices and the edge. Process rows sorted by those keys, subtract the leading coefficient times the existing normalized row with the same least column until zero or a new pivot. Rank is exact over Q; the integral kernel is free of that rank difference and no degree-four boundaries occur. The source's unit-column witnesses are corroboration, not required by the alternative proof.

## originality

PASS

Bounded best-of-knowledge assessment of the fixed-weight exact invariant, not of the chain model.

## value

PASS

Top integral homology of the smallest weight where degree three can occur is a natural exact invariant of a standard symmetric cubic planar skeleton. This gives a usable reference datum for computations beyond the two-particle case, with no claim about lower groups or ring structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
