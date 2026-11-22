# Review of the four-sink coexistence certificate

## Correctness — PASS

The nine explicitly listed disjoint boxes have all 36 strict boundary signs of the continuous fixed-point residual; the rational-interval checker reproduces those inequalities and certifies each exponential bound with a finite positive Taylor lower sum. Poincare–Miranda proves existence for all real \(\alpha\ge6\), not just sampled gains. Exact Jacobian row-norm estimates give four sinks; det(I−J)<0 with 0<det(J)<1 gives four saddles; a strict inverse-Jacobian norm bound gives one repeller. No global uniqueness, optimality or omitted spectrum assertion is used.

The exact-arithmetic checker tests all nine boxes and the monotone inequalities used in the continuum proof. Hyperbolicity is established by inequalities rather than numerical eigenvalues. No exact-total-census claim is made.

## Originality — PASS within inspected evidence

This is an effective all-real-gain certificate at the explicit boundary \(\alpha=6\) for this precise biased, oppositely coupled sigmoid neuron pair; it yields four genuine attracting resting states, compared with only two observed in the original numerically explored region. General nine/four capacity bounds and qualitative large-gain switching existence are preexisting and are expressly not claimed as new. The two retrieved results for the same map concern respectively primitive two-cycles and global boundedness, neither of which proves even one of these nine fixed-point existence or stability inequalities.

Relevant sources include the originating 2023 article (DOI 10.1007/s11071-023-08897-7), Jin and Gupta (1996), and Duncan et al. (arXiv:2103.17184). Closest same-family indexed findings address two-cycle exclusion and compact global attraction. Their published full RESULT.md proofs were inspected and establish period-two exclusion and global absorption, neither of which implies the present gain-six nine-point certificate. Unindexed or ancillary exact gain-six results remain a publication-priority risk.

## Value — PASS

The originating numerical equilibrium study reports counts one, three, and five at gains 1, 1.666 and 1.8, and its phase diagrams emphasize no more than two stable equilibria in the explored range. A rigorously certified four-basin coexistence regime at a small explicit integer gain, persisting for all higher gains, changes the established parameter portrait for a concrete implemented spiking map, and gives a usable quantitative bound absent from qualitative steep-switching theory. Its value is not based on a mere one-parameter substitution or finite enumeration.

## Limits

Six need not be sharp, the total number of fixed points need not equal nine, and results concerning other time steps or global basins are not asserted.

Self-review: passed. Independent audit: not yet performed.
