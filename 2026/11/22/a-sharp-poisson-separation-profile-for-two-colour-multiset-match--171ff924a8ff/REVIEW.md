# Review of a sharp Poisson-separation profile for two-colour multiset matches

## Correctness — PASS

The finite matching count is exactly an affine hypergeometric variable, with explicit support, mean and variance. Compact-uniform local Gaussian expansions follow from Stirling's formula with positive limiting proportions; the central-limit meshes are two for matches and one for the Poisson comparator. Chebyshev tightness justifies summation outside growing central windows. The parity-conditioned comparison uses the exact Poisson parity probability. Both density-crossing formulas have been re-derived from the normal densities. Sharpness and strict uniqueness follow by applying a strictly positivity-improving Gaussian Markov kernel to the signed normal differences. The bundled independent enumeration checked 660 exact finite arithmetic assertions. Finite checks supplement but do not replace the infinite proof.

## Originality — PASS against examined sources

The motivating 2026 multiset fixed-point paper analyzes Poisson bounds and first moments but does not give the macroscopic two-colour whole-law total-variation profile. The published all-multiplicity support theorem proves the parity restriction, not its strictly larger total-variation constant or the parity-corrected residual. The published one-large-block Poisson–Charlier expansion concerns a different scaling with a bounded mean and vanishing error. Targeted searches for the exact hypergeometric/Poisson comparison and its Gaussian crossings did not find equivalent statements. Generic hypergeometric and Poisson local limit tools underlie the proof, so an unlocated general lattice total-variation theorem could still imply some or all of the profile; historical priority has not been independently certified.

## Value — PASS

Poisson fixed-point approximation is natural for multiset shuffling, but no uniform Poisson approximation is possible with just two macroscopically occupied colours. The result quantifies that failure, proves a nontrivial *sharp universal minimum* \(0.533230687960\ldots\) across all asymptotically positive binary proportions, and separates the parity obstruction from a second irreducible variance mismatch. Even after removing parity, the optimal universal residual is \(0.166064074983\ldots\). These precise gap constants and their extremizers provide benchmarks for whether an approximation respecting the support is necessary, rather than just restating a qualitative parity counterexample.

## Closest literature and limitations

- D. Stark, *Poisson approximations of the number of fixed points in random multiset permutations* (2026), https://arxiv.org/abs/2608.00710 . Full HTML text of its Sections 1–4 inspected.
- *Exact fixed-point support and constructive mismatch spectrum for multiset permutations*, published result https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fixed-point-support-and-constructive-mismatch-spectrum-for--3698ed40fe98 . Full RESULT.md inspected; proves the relevant parity support but no probability profile.
- *Sharp Poisson approximation for one square-root multiset block*, published result https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-poisson-approximation-for-one-square-root-multiset-block--b21e06270e4c . Full RESULT.md inspected; bounded-mean distinct-singleton scaling, not the macroscopic two-colour regime.

Only interior limiting proportions are covered. There is no finite-size convergence rate, multicolour classification, or uniform endpoint theorem. An independent historical-priority or mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
