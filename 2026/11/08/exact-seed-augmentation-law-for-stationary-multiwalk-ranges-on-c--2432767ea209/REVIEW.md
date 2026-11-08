# Scientific review: exact seed augmentation for complete-graph multiwalk ranges

## Correctness — PASS

The claim has been checked on its entire stated symbolic domain: \(n\ge2\), \(k\ge1\), \(q\in[0,1]\), and nonnegative integer lifespans. For a fixed forbidden set of size \(b<n\), each stationary walk has avoidance probability \(((n-b)/n)[1-(1-q)b/(n-1)]^t\). Independence multiplies this probability, and the one-walk-plus-seeds construction gives the identical product for every forbidden labeled subset. Möbius inversion uniquely determines the random-set law. The factorial moments and expectation gap follow by linearity; the coupling is an actual inclusion of final sets, not an inference from expectation. Boundary cases \(b=n\), \(k=1\), \(T=0\), \(q=0,1\), and \(n=2\) are explicitly handled. An independent finite-state dynamic-programming implementation and exact rational closed-form comparisons pass 5,560 checks; these checks supplement, rather than substitute for, the proof.

## Originality — PASS, with bounded historical priority risk

The closest published motivation is Dey, Kim and Terlov, *Collaboration of Random Walks on Graphs* (arXiv:2302.14241, first posted February 28, 2023). Their Theorem 1.1 concerns expected range cardinality; Question 3.2 asks about the quantitative expectation gap and Question 3.6 asks about stochastic domination. The result assessed here provides a stronger **labeled random-set identity**, exact lifetime-allocation invariance, explicit full distribution, and set-inclusion coupling on \(K_n\), including non-lazy odd total times. It does not pretend to answer the general-graph conjecture. Rivera, Sauerwald and Sylvester (arXiv:2011.07893) study cover-time bounds and geometric reset methods, not this identity; Upadhyay and collaborators (arXiv:2604.20829) determine a one-walk complete-network size distribution, not the multiwalk augmentation law. Semantic searches across available mathematical research records and published literature found no implication covering the new statement. Risk: an earlier unindexed elementary coupon-collector formulation, or content in the inaccessible 2025 journal version, might establish the same equivalence; such a source was not assumed not to exist.

## Value — PASS

An exact identity in law for labeled discovered sets is stronger than all moments and distributional range dominance. The comparison has a literal containment coupling, solves the complete-graph cases of two explicitly posed questions, and shows that **only** the number of stationary walkers and the total transition budget matter, not how that budget is split. The one-parameter family includes simple and lazy walks without time-parity conditions. The complete explicit factorial-moment sequence gives exact finite-size coverage probabilities. The three-vertex path boundary calculation proves that the lifetime-allocation invariance is genuinely structural rather than a generic independence identity. This is a motivated benchmark for the still-open heterogeneous-graph collaboration problem, not an arbitrary finite computation.

## Closest sources and limitations

- Dey, Kim and Terlov (2023), arXiv:2302.14241, Theorem 1.1 and Section 3; the principal source and directly posed questions.
- Rivera, Sauerwald and Sylvester (2020), arXiv:2011.07893, introductory claims and Section 3 on stationary cover times and geometric reset graphs.
- Upadhyay, Sandev, Kumar and Singh (2026), arXiv:2604.20829, Sections 1–2 on the single-walk complete-network distinct-range distribution.

The theorem does not compare whole evolving trajectories, arbitrary graphs, nonuniform starting laws or heterogeneous transition rules. Further independent mathematical assessment and historical-priority confirmation are outstanding.

Self-review: passed. Independent audit: not yet performed.
