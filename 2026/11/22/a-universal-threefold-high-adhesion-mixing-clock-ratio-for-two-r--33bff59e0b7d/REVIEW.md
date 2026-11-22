# Scientific review

## Correctness — PASS

Each one-break event generates three possible block interleavings, exactly one outside the cyclic-rotation subgroup. The block rule selects it with probability one third, whereas the midpoint rule necessarily selects it because the three geometric midpoint keys are strictly ordered. Summation across all cuts and internal packet bonds gives an exact identity of first-order off-subgroup measures and a positive rate. A finite-state averaging argument then derives the quotient Markov generator, which is irreducible since a single supported insertion together with rotation generates every permutation. Positive-time finite-state semigroups yield strict monotonicity of the limiting total-variation profile and permit exact mixing-time scaling. Boundary layers at time zero are stated rather than suppressed. The standard-library checker reproduced exact finite event coefficients and finite quotient calculations; the infinite-family proof is analytic, not enumerative.

## Originality — PASS against checked sources

The motivating article (Jiang, arXiv:2611.02092v1) explicitly states only fixed-deck \(\Theta((1-p)^{-1})\) mixing scales, plus some insertion-event probabilities with factors one and one third. Those statements do not identify *every* first-order off-rotation permutation, derive the quotient generator, or imply the whole full-deck limiting profile and all-deck factor-three mixing-time ratio. An earlier exact four-card profile is a covered special case; it does not imply the arbitrary-deck theorem. The Palomares and Jonasson--Morris work concerns Markov-word shuffles with a different cut law. Searches of available related mathematical records did not identify a stronger theorem. Priority from inaccessible or unindexed work cannot be ruled out.

## Value — PASS

The two physically motivated block-release rules differ substantially at finite adhesion yet share a universal exact first-order speed relation as adhesion becomes extreme. An all-deck factor-three limit converts an order-only fixed-deck mixing result into an explicit comparison of *entire* total-variation profiles and sharp fixed-error mixing constants. This clarifies the structural role of single contact breaks, distinguishes the geometry of the release rule from the imposed binomial cut, and is not merely another isolated small-deck calculation. The relationship remains motivated even though generic finite-state averaging is standard.

## Closest evidence and limitations

Primary source: https://arxiv.org/abs/2611.02092, Definitions 2.2--2.3, Theorem 2.5 and Section 10. Related full-text source: Palomares (2025), University of Michigan, https://lsa.umich.edu/content/dam/math-assets/reu-su22/2025/REU_Report_Final_Mateo_Palomares.pdf. Prior four-card high-adhesion result is a strict special case. The claim is for each fixed deck size and \(s>0\), not a joint large-deck limit, and it does not imply full-deck cutoff. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
