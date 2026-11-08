# Scientific review

## Correctness — PASS
The proof first uses Euler's identity for homogeneous quadratic per-capita interactions to force the entire Jacobian row-sum vector \(w\). It then constructs every compatible first-order jet by an explicit quadratic polynomial. For nonconstant \(w\), a rank-one square-zero correction of \(-I\) is compatible with the row sums, while for constant \(w=c\mathbf1\) the eigenvalue \(c\) is unavoidable. These steps establish the complete iff statement for every finite dimension and positive target. The 960-case exact-rational checker passed; finite trials are only auxiliary verification.

## Originality — PASS (best-knowledge, qualified)
Çelik et al., arXiv:2609.09286v1, Theorem 4.2 explicitly uses both degree-two and degree-three per-capita interactions to guarantee stability for arbitrary fixed pairwise parameters. Its Example 4.1 supplies a single degree-two example, not a complete genericity/obstruction classification. Gibbs et al. (2024) study sign/sampling-constrained triples and full Jacobian effects, not the precise unrestricted row-sum if-and-only-if completion. Duran-Sala et al. (2025) use a different competitive replicator model. Indexed scientific-record searches for homogeneous-quadratic stabilization, row-sum Hurwitz completions, and minimal interaction order did not return a matching statement. Search incompleteness and latent implications in unindexed work remain risks.

## Value — PASS
The cited 2026 theorem raises a natural order-minimality question: are four-body effects actually required to restore coexistence while holding all pairwise coefficients and a positive equilibrium fixed? This theorem gives a complete answer for linear local stability: three-body effects generically suffice, the exceptional data have a precise codimension and sign, and an exact rank-one construction achieves prescribed decay eigenvalues. The obstruction distinguishes an interaction-order limitation from mere failure of a particular sampled tensor and may guide model selection; it is not claimed to be physically implementable under sign/sparsity restrictions.

## Relationship and limitations
The source's universal four-body sufficiency is credited, and the result does not claim unrestricted global stability or cover sign-constrained or repeated-index-free tensors. An equivalent prior row-sum completion theorem may exist outside inspected sources. Only the declared local, unrestricted-tensor claim is accepted.

Self-review: passed. Independent audit: not yet performed.
