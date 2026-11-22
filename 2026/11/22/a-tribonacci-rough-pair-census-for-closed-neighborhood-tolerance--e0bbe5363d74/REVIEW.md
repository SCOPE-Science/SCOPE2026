# Scientific review

## Correctness — PASS

The three-symbol approximation encoding is exact, including endpoints; the twelve-state deterministic subset construction and seven-state complement quotient prove the generating function for every length, not just the enumerated cases. The elimination and initial values were checked independently, and `verify.py` passed \(16\) complete finite subset enumerations (through \(n=16\)), \(36\) independent automaton/quotient counts, and \(31\) recurrence equalities. The proof gives the infinitely quantified statement; finite tests only corroborate.

## Originality — PASS within inspected evidence

The 2016 path and cycle rough-set literature [2] uses equivalence classes induced by an adjacency information table; this differs from the nontransitive closed-neighborhood tolerance. The 2026 relational-duality source [1] provides algebraic principles rather than a path census. Published results on complete multipartite tolerances and incidence-order rough sets concern genuinely different structures. No inspected theorem implies this exact path-pair count. An abstract-only related path paper [4] and two uninspected full texts leave residual historical-priority risk.

## Value — PASS

The exact number of distinguishable upper/lower observations is an intrinsic capacity invariant for a simple nontransitive approximation space. The rational generating function, full recurrence and sharp exponential compression are structural statements for every path size, supported by a small canonical finite automaton, not a routine enumeration of a few cases. Its finite-state characterization enables reproducible computation and provides a baseline for more general tolerance graphs.

## Sources and limitations

1. I. Düntsch and E. Orłowska, *Discrete dualities for some algebras from rough sets*, arXiv:2601.05843v1, first public version January 9, 2026, https://arxiv.org/html/2601.05843v1. Section 2 defines lower and upper relational operators; its main focus is algebraic duality, not path enumeration.
2. G. Chiaselotti, T. Gentile, F. Infusino and P. A. Oliverio, *Rough Sets for n-Cycles and n-Paths*, *Applied Mathematics & Information Sciences* 10 (2016), 117–124, https://doi.org/10.18576/amis/100111. Its lower/upper approximations are induced by adjacency-information-table equivalence classes, not the reflexive closed-neighborhood tolerance used here.
3. G. Chiaselotti, T. Gentile and F. Infusino, *Granular Computing on Basic Digraphs*, *Applicable Analysis and Discrete Mathematics* 16 (2022), 23–54, https://doi.org/10.2298/AADM180615001C. A related graph-information-table formalism.
4. S. M. Sanahuja, *New rough approximations for n-cycles and n-paths*, *Applied Mathematics and Computation* (2016), https://doi.org/10.1016/j.amc.2015.11.052. Only abstract-level access was obtained; a residual historical-priority risk is noted.

The result does not enumerate fibers or establish a theorem for general graphs. Independent mathematical or historical-priority validation is not represented as having occurred.

Self-review: passed. Independent audit: not yet performed.
