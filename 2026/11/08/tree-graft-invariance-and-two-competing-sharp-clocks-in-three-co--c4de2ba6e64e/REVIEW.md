# Scientific review

## Correctness — PASS

The explicit graph decomposition is essential: the only cycles are in the clique. For a clique coloring with at most two colors, a globally consistent one-Lipschitz integral lift exists and updates by closed-neighborhood maxima, giving the diameter bound and a distance-function sharpness witness. For a rainbow clique, each clique vertex increments every step. A forced integer-root comparison on each attached tree proves both \(h_t(v)\ge b_a+t-d(a,v)\) and \(h_t(v)\le\max\{M_a,b_a+t-d(a,v)\}\); since \(M_a\le b_a+H_a\), phase-locking occurs by \(H_a+d(a,v)\). A deepest-leaf monotone initial height witnesses failure of phase locking at time \(2H-1\). The count of rainbow clique colorings and independence of all initial tree colors determine each entire periodic-orbit basin. Exact checks cover 269,811 labelled configurations on thirteen graph instances and 7,000 independent seeded random instances of the height comparison. These finite checks corroborate the mathematical proof.

## Originality — PASS, qualified

Gravner–Lyu–Sivakoff (arXiv:1610.07320v1, 2016) supplies the governing local rule, a general monotone walk comparison, the conservative 1-form characterization, and the diameter synchronization upper bound; none is claimed as new. A previously available one-leaf special-case calculation gives nine-state basins for that restricted graph, which is included here. The assessed additional claim is the full arbitrary multi-root rooted-forest classification with individual basin formulas and a sharp \(\max\{D,2H\}\) temporal law, especially the sharp doubled-height nonconservative term. The inspected primary material does not tabulate or state this all-family result. Possible unindexed equivalents, and the ease of deriving special statements from the general comparison method, remain priority risks.

## Mathematical value — PASS

Trees grafted to a clique are a natural controlled family separating cycle-supported oscillations from acyclic transport. The theorem identifies a topology-insensitive orbit/basin law and a competing topology-sensitive sharp transient cutoff; two trees with the same number of added vertices can have radically different maximum transient lengths, while the eventual periodic basin fractions remain identical. This is an exact classification over unbounded clique size and unrestricted tree branching, not an arbitrary small instance or a routine one-vertex increment. The comparison also separates the known conservative diameter clock from the additional nonconservative doubled-height clock.

## Related sources and limitations

Primary: Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, especially Lemma 1, Theorem 3, and its proof; the theorem already establishes synchronization in the conservative regime. A previous one-leaf calculation gives a special case, not the arbitrary-forest classification. The earlier odd phase-clock literature concerns related synchronization rules; unexamined material can still contain an equivalent formulation. The exact within-basin first-entry-time histograms are not established here. Verification is same-model only.

Self-review: passed. Independent audit: not yet performed.
