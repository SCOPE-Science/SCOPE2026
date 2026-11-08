# Scientific review

## Correctness — PASS

The claim is a single theorem about the centered system, not the diffusing absolute center. The self-coupling gives strict mean-square contraction at rate \(\nu N/2\), proving invariant-law uniqueness; an explicit quartic Foster drift supplies integrability. Independent binomial expansions yield all three generator identities, a nonsingular exact moment system, and exact local and distance quartic identities. Differentiation proves both strict monotonicities; the affine centered-radius generator proves its autocovariance without assuming Gaussianity. The executable checker reproduces all symbolic equations and 612 rational finite identities. Residual proof risk: the Foster argument relies on standard truncation/invariant-measure integration and is presented with its explicit drift bound.

## Originality — PASS, qualified

The original cooperative-resetting paper by Meigel and Rulands (arXiv:2312.09307, first posted 2023-12-14) introduces the exact mechanism, studies mean-field localization and asymptotic tails, and compares with external resetting; no same finite-\(N\) joint fourth-moment and gyration-correlation formula was identified in its accessible full text and appendices. Related resetting-to-distribution and reset-to-origin papers use distinct interventions. No equivalent published finding was found in claim-level semantic searches, but those searches cannot certify uniqueness. The strongest residual risk is that general noisy-gossip or model-specific moment equations in uninspected literature already imply the formulas without presenting them explicitly.

## Mathematical value — PASS

A self-organized model introduced for biological and technological noise suppression has a nontrivial gap between collective concentration and persistent *local* non-Gaussianity. The two different exact limits \(6/7\) and \(3/7\), finite-size monotonicity, and the exact gyration correlation separate observable signatures of the endogenous averaging mechanism. Solving the closed two-dimensional quartic-moment system is a structurally motivated finite-size result, not a parameter-free special-case recomputation of a known table. No generalization to distance-dependent rates or distributional limit is asserted.

## Closest literature and limitations

- Meigel and Rulands, arXiv:2312.09307, full-text model, mean-field tails, appendices; directly same mechanism but not the explicit finite-N fourth-order theorem located.
- Olsen, DOI:10.1103/PhysRevE.108.044120, exogenous resets; accessible abstract and descriptive material, not full derivational comparison.
- Vilk, Assaf and Meerson, DOI:10.1103/PhysRevE.106.024117, reset-to-origin particle processes; abstract-level comparison only.
- Boyd et al., *Randomized Gossip Algorithms*; spectral mixing for pure averaging, different source of stationary fluctuations.

Independent priority review may uncover an equivalent derivation. The theorem only asserts exact moments and covariance for the centered, constant-pair-rate complete-graph model; it does not assert a stationary law for absolute positions.

Self-review: passed. Independent audit: not yet performed.
