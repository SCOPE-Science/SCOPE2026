# Self-review

## Correctness — PASS

The root-lattice dual is explicitly identified with integer potentials modulo constants. Each allowable second-hub difference \(s\) gives \(2t+1-|s|\) independent choices at every leaf; the exact count follows. The degree and magic-basis conversion are justified by the Bernoulli-polynomial identity and triangular elimination. The first three coefficient identities were re-derived from derivatives of Bernoulli polynomials and independently checked with exact rational interpolation. The infinite conclusion separates all four residue classes modulo four using the rigorous ratio \(|B_{m+4}|/|B_m|>2\) for even \(m\ge14\), and exact base values. The complete finite range is checked in `verify.py`, whose 344 exact assertions passed; the infinite conclusion rests on proof, not enumeration.

## Originality — PASS (best-knowledge, independent priority unverified)

Higashitani–Mori identify the graph family through Minkowski decomposability, not polar Ehrhart coefficients. Kounoike treats trees, complete graphs, cycles and complete bipartite examples, not this family. Ohsugi–Tsuchiya prove positivity for pseudo-symmetric simplicial/smooth polytopes and cycle polars, which does not cover the negative book-graph examples. The analogous complete-bipartite thresholds concern different graphs and different lattice-count formulas and do not entail the tripartite threshold. Explicit searches for graph aliases, coefficient formulas, and positivity cutoffs in published records and accessible prior-claim records found no equivalent or stronger statement. Search failure is not historical proof; an independent priority check remains necessary.

## Mathematical value — PASS

A 2026 structural theorem isolates just three Minkowski-decomposable graph families. Determining the exact magic-positivity boundary of the book-graph family complements known complete and complete-bipartite cases, and distinguishes a genuine loss of magic positivity from the existence of a highly structured Minkowski decomposition. The result is a sharp all-parameter classification of a natural, independently motivated geometric invariant, not an arbitrary finite search or trivial parameter shift.

## Limitations

The theorem is for polar symmetric edge polytopes, not symmetric edge polytopes themselves. Bernoulli-growth estimates establish eventual failure without locating every negative coefficient in high dimensions. Priority has not been independently verified, and `verify.py` does not certify the infinite tail.

Self-review: passed. Independent audit: not yet performed.
