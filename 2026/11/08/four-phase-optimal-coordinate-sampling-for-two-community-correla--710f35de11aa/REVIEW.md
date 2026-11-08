# Scientific review

## Correctness — PASS

For the unit-diagonal positive definite two-community matrix, the exact expected decrement is a smallest eigenvalue. This is concave in coordinate probabilities in its equivalent \(C^{1/2}DC^{1/2}\) form, so community-permutation averaging is globally valid. On the averaged simplex, the full spectrum consists of two contrast eigenvalues and a two-by-two community-mean matrix. Strict concavity of the latter's smallest eigenvalue and its exact determinant identities prove the four exhaustive cases with boundary conventions. The unbounded uniform-sampling gap follows from a displayed positive-semidefinite decomposition. The included self-contained standard-library checker completed 13,070 exact attainment checks, 91,843 exact non-improvement checks, four rational regime witnesses, and the growing-dimension sequence through \(q=24\). These finite tests do not prove the infinite assertion; the proof does.

## Originality — PASS on inspected evidence

Gower and Richtárik (arXiv:1506.03296, Section 5.1) give a general optimal-sampling semidefinite formulation but no evaluation for this two-community parameter family. Richtárik and Takáč (arXiv:1310.3438) and Qu and Richtárik (arXiv:1412.8060) use other bounds or a general sampling framework. The E-optimal-design work of Pukelsheim and Torsney (1991) provides an implicit general criterion, not the four explicitly evaluated regimes in the portions checked. The published inverse-positive SPD sampling theorem concerns \(C^{-1}\ge0\), impossible for the present dense positive off-diagonal \(C\). Equivalent treatments in older optimal-design or diagonal-scaling literature cannot be completely excluded; further literature review could change publication-priority assessment.

## Value — PASS

The block-exchangeable positive correlation family is a natural model for two interacting homogeneous communities. The result is a complete analytic design classification, not a numeric optimizer or a single arbitrary instance; its four spectral regimes have exact rational witnesses, a sharp structural threshold \(c^2=ab\), and a construction where optimizing the sampling law improves the guaranteed decrement by an unbounded factor over uniform sampling. The claim is deliberately restricted to fixed iid exact coordinate updates and expected one-step squared-energy reduction.

## Limits and closest source

The closest broad foundations are the 2015 general semidefinite sampling formulation and the 1991 E-optimal-design optimal-weight results. No independence or novelty beyond the inspected literature is certified. Exact rational tests supplement the analytic proof and do not establish it by enumeration.

Self-review: passed. Independent audit: not yet performed.
