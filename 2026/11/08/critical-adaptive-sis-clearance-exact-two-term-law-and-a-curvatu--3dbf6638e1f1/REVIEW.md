# Review of critical adaptive SIS clearance

## Correctness — PASS

The theorem begins with the exact two-equation published deterministic model and explicitly restricts to positive \(C^3\) monotone response functions at \(\mathcal R_0=1\). The upper contact comparison supplies a global algebraic prevalence bound. The precise link expansion follows from stable forcing and the subexponential slow-variation estimate; substituting its first two response jets produces \(K\) and \(B\). The derivative of the residual \(1/y-Kt-B\log t\) is integrable, proving a finite constant rather than only an \(O(1)\) bound. Exact algebra, a symbolic invariant-graph defect check and full-system numerical diagnostics passed. Computation is not used to assert global convergence or convergence of the finite remainder.

## Originality — PASS on the inspected record

The initiating paper [1] defines the flow, invasion threshold and Jacobian, but leaves the equality case unresolved. The later same-author multigroup paper [2] proves global stability strictly below threshold and provides qualitative network results; it does not claim this equality-case critical coefficient. Two existing nearby results concern respectively the *supercritical* endemic damping spectrum when baseline link breaking is zero and a *multigroup critical leading* law when baseline link breaking vanishes. Neither implies the new positive-baseline, second-order coefficient law. The closest indexed logarithmic-relaxation work deals with a bullying-index threshold, not this adaptive SIS system. Relevant original articles and their key sections were read, with an explicit literature-access risk retained for earlier link-rule classifications and unindexed publications.

## Mathematical value — PASS

The theorem resolves a naturally nonhyperbolic epidemic-control boundary for a broad class of risk functions, then quantifies finite-time clearance at the level beyond the usual \(1/t\) asymptotic. Specifically, the identical leading coefficient \(K=3/2\) at every curvature in the increasing breaking family masks an exact sign reversal of \(B\) at \(\kappa=3/4\). This has a model-internal interpretation—curvature in reactive distancing changes the next-generation depletion correction while not changing basic invasion or its leading amplitude. It is not merely a renamed center-manifold expansion, an arbitrary computational slice, or a finite experiment.

## Closest literature and limits

[1] M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224v1 (2022-09-02), *Nonlinear Dynamics* 111 (2023), DOI:10.1007/s11071-023-08498-4. [2] M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639v3. The theorem is deterministic and assumes \(C^3\), strictly positive monotone link responses. It has no direct stochastic, supercritical, or parameter-uniform implication. An equivalent unindexed prior result remains a publication-priority risk.

Self-review: passed. Independent audit: not yet performed.
