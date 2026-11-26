# Independent mathematical audit

## correctness

PASS

A full shadow means injectivity on all indexed t-subsets with equality of outputs only up to rotation. Equal symbols joined by an arc of d≤t edges collide: erase its d−1 interiors, either endpoint, and the same t−d outside positions, which exist since n−d−1≥t−d. This covers every pair for n≤2t+1. Distinct labels make every mask recoverable from the surviving set, proving the short-length iff. In the construction the unique surviving marker labels specify the marker deletions, and any surviving marker fixes the cyclic origin so the data subsequence is read linearly. If no marker remains, the t marker positions exhaust the deletion budget. Otherwise, with r≤t data deletions, the j-th retained data index lies in [j,j+r], so its residue modulo the data period t+1 is unique in that interval; hence the data mask is determined, including the empty subsequence case. The length 2t+1 gives the universal alphabet lower bound, and at 2t+2 the data block first repeats a letter, as claimed. This is not a minimum-alphabet assertion for each larger length.

## originality

PASS

The closest prior evidence already contains the marker technique for one deletion and repetition-based linear constructions. The supported distinct content is the sharp simultaneous result for t≥2: a lower bound for arbitrary circular sources at the critical length, a marker budget that works against all masks at every length, and the exact repeat onset. Neither the one-deletion result nor source-orbit injectivity establishes these statements.

## value

PASS

The result settles when the cardinality ceiling imposed by the indexed deletion budget remains attainable despite loss of the cyclic origin. It gives a sharp universal alphabet and the first admissible repetition, with a constructive method that works uniformly in length rather than a count for a special periodic source or a finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
