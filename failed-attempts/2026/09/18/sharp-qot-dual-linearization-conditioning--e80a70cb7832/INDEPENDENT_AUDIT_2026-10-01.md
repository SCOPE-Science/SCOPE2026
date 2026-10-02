# Independent audit — 2026-10-01

## Final claim

In smooth continuous quadratically regularized optimal transport, the optimizer dual-curvature spectrum has lower edge of order one, upper edge of order \(\varepsilon^{-2/(d+2)}\), and condition number of the same order, yielding the stated local scalar-step stability and iteration scales.

## Correctness — PASS

The support-thickness scaling was reconstructed: a two-step local Markov kernel has an order-\(\ell^2\) spectral gap, which combined with density/support comparison yields order-one soft curvature after dividing by \(\varepsilon=\ell^{d+2}\). Section-volume control yields the order-\(\ell^{-2}\) upper edge, while constant and transport-canceling Lipschitz directions give matching witnesses. The algorithmic local step and iteration scales follow from the condition number.

## Originality — FAIL

Originality fails because a separately published same-date record, Natural-scale strong concavity and sharp Hessian conditioning for quadratically regularized optimal transport, contains the same \(\lambda_{\min}\asymp1\), \(\lambda_{\max}\asymp\varepsilon^{-2/(d+2)}\), condition-number and local-step conclusions as part of a strictly broader strong-concavity and PL theorem.

### Equivalent formulations

Searches: Resultary: quadratically regularized optimal transport dual linearization conditioning epsilon exponent support Poincare; full published natural-scale QOT record

Evidence: The broader record explicitly states the same spectral-edge estimates and condition number as equations (8)-(9), plus a larger theorem on a full natural-scale neighborhood.

Reasoning: The assigned optimizer-linearization theorem is a direct special case of that broader published result.

### Broader coverage

Searches: Natural-scale strong concavity and sharp Hessian conditioning for quadratically regularized optimal transport

Evidence: The inspected full record proves core coercivity, local strong concavity, PL, and the same sharp Hessian spectrum.

Reasoning: This is strict broader coverage, not just parameter overlap.

### Exact database or table

Searches: Resultary exact QOT conditioning search

Evidence: The broader record is a separate published entry with the same exponent and both spectral edges.

Reasoning: An exact duplicate table is unnecessary because the theorem-level implication is decisive.

### Claim versus prior implication

Searches: Compare assigned final claim to equations (8)-(9) of the broader published record

Evidence: Those equations state \(\lambda_{\min}\asymp1\), \(\lambda_{\max}\asymp\ell^{-2}\), and \(\kappa\asymp\varepsilon^{-2/(d+2)}\); the same record also states the local gradient step scale.

Reasoning: The prior/broader statement mechanically implies the assigned final claim.

### Source inspections

- **Natural-scale strong concavity and sharp Hessian conditioning for quadratically regularized optimal transport** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-natural-scale-qot-dual-conditioning--6d748f1f11d7): Covering and strictly broader. Material read: Complete RESULT and metadata. Method: Full public record inspection. Evidence: Its spectral theorem states the same soft and stiff curvature orders and condition number, with additional neighborhood strong-concavity and PL results.
- **Geometry and Convergence of Quadratically Regularized Optimal Transport I** (https://arxiv.org/abs/2609.20400): Relevant source ingredients; not needed to overcome the decisive published-record coverage. Material read: Abstract/metadata; full text retrieval failed in this run. Method: Primary-source abstract inspection plus authorized-access attempt. Evidence: The assigned and broader records both cite its sharp support geometry as input.

Checked sources: Published record: Natural-scale strong concavity and sharp Hessian conditioning for quadratically regularized optimal transport; González-Sanz and Nutz, Geometry and Convergence of Quadratically Regularized Optimal Transport I, arXiv:2609.20400; González-Sanz, Nutz and Riveros Valdevenito, Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport; Resultary semantic search for QOT dual conditioning

Residual risks: The exact publication ordering of the two 2026-09-18 SCOPE records is not encoded by their public date, but the broader record is presently published and mathematically dominates this final claim. The companion QOT II working paper remains inaccessible.

## Scientific value — PASS

The sharp stiffness exponent and corresponding local iteration scale are mathematically useful. Scientific value survives even though the finding is rejected because the same theorem is already contained in a broader published result.

## Limitations

- The mathematics is correct in the stated smooth optimizer-local regime, but the final spectral theorem is already contained in a separately published broader result; the independent audit therefore rejects originality.

## Conclusion

The final claim is scientifically rejected because originality fails; correctness and scientific-value evidence are preserved.
