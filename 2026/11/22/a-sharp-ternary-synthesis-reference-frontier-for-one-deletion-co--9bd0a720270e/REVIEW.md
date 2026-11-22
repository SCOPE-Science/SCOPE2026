# Scientific review

## Correctness

PASS. A direct classification of five-word codes proves the global ceiling and nine-position lower bound. Pairwise length-two subsequence separation yields an embedding-incidence bound, and at six reference positions forces the \(K_4\) edge-incidence pattern. The explicit four-word code synthesized from `012021` has four disjoint deletion shadows covering all nine ternary digrams. Two differently structured exhaustive programs check all \(729\) six-position references, all reference capacities through nine positions, the twelve-reference orbit, and the unique correcting code at each optimizer. The theorem for arbitrary reference length follows from the structural proof and monotonicity, not from an unbounded computation.

## Originality

PASS relative to the available scientific evidence. The November 10, 2026 Li–Yu–Ge paper formulates the exact arbitrary-reference objective but supplies general bounds and asymptotics, not the displayed ternary finite frontier or the nonperiodic optimum. The 2023 Chrisnata–Kiah–Pham work fixes a cyclic reference, and Lenz et al.'s unrestricted subsequence maximization does not imply the deletion-correcting optimum. Published deletion-code-only tables do not classify synthesis references. The residual risk is unindexed equivalent work or a non-obvious stronger prior theorem not recovered in the checked literature; publication priority is not independently certified.

## Mathematical value

PASS. This completes the smallest ternary length-three constrained-synthesis capacity problem across *every* reference length, characterizes all minimal references for the critical four-message case, and gives a sharp counterexample to transferring cyclic-reference optimality from unrestricted subsequences to deletion-correcting subcodes. The perfect deletion-shadow partition and forced \(K_4\) incidence explain the finite boundary, making the invariant useful as a benchmark for synthesis-reference design and asymptotic analyses. No longer-blocklength generalization is claimed.

## Closest literature and limitations

The closest direct comparison is Li, Yu and Ge (arXiv:2611.13434, 2026-11-10), especially its problem definitions, finite-length bounds and later asymptotic results. Chrisnata, Kiah and Pham (arXiv:2305.07274) impose cyclic references. Earlier maximum codebook classifications over larger alphabets are related but do not imply an arbitrary-reference synthesis frontier. The new theorem concerns ternary, length-three, exactly one deletion; the originality assessment has not had independent external validation.

Self-review: passed. Independent audit: not yet performed.
