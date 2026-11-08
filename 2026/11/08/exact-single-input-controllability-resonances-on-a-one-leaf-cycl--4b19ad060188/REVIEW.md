# Review of the weighted one-leaf cycle controllability theorem

## Correctness (PASS)

The claim concerns the exact rank for every integer cycle length at least three and every strictly positive pendant conductance. The proof checks both reflection sectors: odd-sector eigenvectors have nonzero actuated coordinate and distinct eigenvalues; the even-sector restriction is a simple-spectrum irreducible Jacobi matrix. A cosine orthogonality argument excludes any common eigenvalue between sectors. Thus the Laplacian's entire spectrum is simple. With PBH, an uncontrollable eigenmode must be reflection-even and must vanish at both cycle vertices adjacent to the leaf attachment. The intervening Dirichlet recurrence forces an odd-index sine mode, while the root/leaf equations reduce exactly to \(\lambda^2-2(1+t)\lambda+2t=0\). Necessary and sufficient construction, positivity of \(t\), endpoint exclusions, and the two arithmetic corollaries are verified in the proof. The supplied verifier passed 322 exact finite-field rank tests, 785 analytic-mode residual tests and 196 size-congruence checks; these corroborate rather than replace the proof. Potential implementation error of the numerical diagnostics cannot affect the analytic argument.

## Originality (PASS on inspected evidence; residual risk)

The relevant prior literature was compared by claim implication, not only terminology. Monshizadeh–Zhang–Camlibel (arXiv:1403.4868v1) prove a zero-forcing characterization for qualitative matrix classes and discuss paths and bare cycles; they explicitly distinguish this from a single fixed Laplacian. The new result concerns one specific symmetric conductance Laplacian and a complete positive-weight resonance classification, including fixed-model controllability despite failure of singleton zero forcing. Hsu's accessible full-text treatment generalizes path-based controllable graph constructions, not a weighted one-leaf cycle. Farrugia–Sciriha address adjacency and signless-Laplacian systems; those operators do not imply the claimed Laplacian phase law. Searches of indexed mathematical findings for pendant-cycle, tadpole, single-actuator, controllability rank and spectral resonance returned related but non-dominating graph-spectral items. A Liu–Ji paper discussing graphs based on paths and cycles was only available as metadata/abstract; this uninspected full text and other unindexed sources are residual priority risks, not asserted to be negative evidence.

## Value (PASS)

A simple graph modification and a single edge conductance expose an exact controllability resonance phenomenon invisible to topology-only zero-forcing tests. The result provides a closed finite exceptional set for every cycle size, an exact rank defect at every positive coupling, and two infinite arithmetic loss families at natural conductances. The distinction between almost-everywhere controllability and exact isolated failures matters for fixed-weight actuator design, where generic or structural conclusions are insufficient. This is an all-parameter structural classification rather than a single small census or a restatement of PBH.

## Scope and risks

Only one pendant vertex, unit cycle conductances, one input at vertex \(1\), and exact symmetric combinatorial Laplacians are covered. No assertion about all actuator placements, generalized tadpoles, robustness to arbitrary edge weights, independent validation, or publication priority is made.

Self-review: passed. Independent audit: not yet performed.
