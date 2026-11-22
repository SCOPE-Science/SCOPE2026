# Scientific review: coordinate-symmetric identifying codes in binary cubes

## Correctness

**PASS.** The proof first reduces coordinate-permutation-invariant vertex sets to unions of complete Hamming-weight layers. The exact iff characterization follows from domination together with the separating-weight support of pairs at distances one and two; pairs at distance at least three have disjoint radius-one balls. Boundary requirements are necessary (pairs of distinct weight-one vertices and their complements) and explicitly used in the sufficiency proof. The four-state recurrence is a bijective enumeration of legal binary layer profiles, with binomial weight costs and exact tie counts. The asymptotic lower bound uses a central-window three-block packing and binomial concentration, while the upper bound is an explicit residue-class construction with at most two endpoint vertices. Direct exhaustive signature testing through dimension seven, an independent pair-orbit test through dimension fourteen, and the exact DP through dimension one hundred corroborate the finite assertions. None of those computations substitutes for the all-dimensional proof.

## Originality

**PASS, subject to historical coverage risk.** The closest identified prior paper is Karpovsky–Chakrabarty–Levitin (1998), which explicitly gives the dimension-five ten-sensor construction using weight levels one and four. That case is excluded from the claim of novelty. Its general cube bounds and constructions do not establish necessary-and-sufficient constraints for every complete-layer code, a four-state exact minimization for all dimensions, or the one-third limit under full coordinate-permutation symmetry. Janson–Laihonen (2008/2009) studies general identifying codes and asymptotic problems for a different radius scaling, without the same invariance condition in the inspected parts. Other retrieved exact-cube calculations concern unrestricted optimizers or other identifying-code notions. Identical terminology could occur in inaccessible or unindexed literature; the comparison is therefore not a uniqueness certificate.

## Mathematical value

**PASS.** Interchangeability of coordinate positions forces whole Hamming-weight layers to be selected. The theorem converts a vertex-identification design problem with exponentially many vertices into an exact four-state weighted index problem and determines its unavoidable limiting sensor fraction, one-third. This exposes a structural symmetry cost rather than just a small-graph numerical example. The exact small-dimension profiles are useful cross-checks, not the sole motivation. The scope is single-fault, radius-one identification; arbitrary identifying codes, other group actions and other radii are outside the claim.

## Closest prior material and limitations

Primary sources: Karpovsky–Chakrabarty–Levitin, *IEEE Transactions on Information Theory* 44 (1998), pp. 599–611, especially Section II and the dimension-five full-layer example; Janson–Laihonen, arXiv:0804.3029, pp. 1–end, especially the definitions and main theorems; Cohen–Honkala–Lobstein–Zémor, *Electronic Journal of Combinatorics* 6 (1999), R19. A later 2010 paper on identifying codes in the binary Hamming space was accessible only in abstract/introductory text and remains an explicit coverage risk. A day-resolved 2008 open preprint provides the recorded public-source date; the earlier 1998 publication is acknowledged rather than relabeled.

No elementary closed formula for the exact minimum in every dimension is proved, and the observed small-dimension residue pattern is not extrapolated as a theorem. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
