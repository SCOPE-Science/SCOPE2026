# Scientific review

## Correctness — PASS

The result follows from a complete classification of nontrivial states fixed by three updates on connected graphs, followed by a finite exact 27-state transfer for the two-row ladder. The five-row component table in RESULT.md establishes the critical integer identity \(M^3b=4M^2b-Mb-2b\); this is checked componentwise by `verify_transfer.py`. Initial vector contractions give the first cases and the recurrence without infinite extrapolation. The independent dynamics program exhaustively compares \(597861\) labelled states with an unnormalized transfer. The code and output files are present and runnable in the package. The domain and both end boundaries are fixed explicitly.

## Originality — PASS, qualified

The closest inspected primary sources concern general Greenberg–Hastings patterns and eventual three-periodic states, not the present exact initial-state census. Durrett–Steif (1991), Section 5, Lemma 6 treats eventual clocks, whereas the target statement is the exact rational generating function for the labelled open ladder. Gravner–Lyu–Sivakoff (2016), introductory and theorem sections, treats asymptotic activity on arbitrary graphs; its framework can establish qualitative oscillation, but not the stated numerical counts without additional transfer analysis. Exact-count, recurrence, graph-alias, and sequence searches and comparisons against accessible historical claims did not identify an equivalent or stronger result. An especially relevant Greenberg–Greene–Hastings (1980) paper could not be checked beyond its abstract; institutional access was unavailable. Its abstract indicates a general winding-number criterion rather than exact counts, but this priority risk is not ruled out. Unindexed formulations of directed successor-domination also remain possible.

## Value — PASS

This census resolves an invariant for every two-row finite strip, the narrowest open rectangular lattice family admitting primitive-three excitation (single-row paths do not support them). It exposes an unexpectedly low-order transfer law despite the growing \(3^{2n}\)-state dynamical space, yields the exact number of recurrent three-cycles, and quantifies exponential rarity under random initial states. The exact growth base \((3+\sqrt{17})/2\) and full rational series are natural in the study of finite-size waves, not a post-hoc arbitrary parameter slice.

## Scope and remaining risks

The claim does not address transient basins, other primitive periods, or periodic/cylindrical strips. The finite verification supports but is not the general proof. The full 1980 primary article and unindexed stronger recurrence results have not been excluded. No external expert has independently validated this result.

Self-review: passed. Independent audit: not yet performed.
