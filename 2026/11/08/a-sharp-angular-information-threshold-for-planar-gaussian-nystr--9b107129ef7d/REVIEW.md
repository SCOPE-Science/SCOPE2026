# Scientific review

## Correctness

PASS. The residual is positive semidefinite and has rank one, and Cayley–Hamilton gives the exact scalar ratio (5). The pivotal angular integral (6) is evaluated from the elementary complete-circle integral and two linear constraints; no unevaluated probability limits are used. A two-by-two inverse identity then yields the exact determinant/traces expression. The exact orientation law, the derivative-sign classification ruling out finite interior anisotropy minima, the critical uncertainty angle and the joint asymptotic are proved for all stated parameters. The included rational, symbolic and numerical checks are supportive and were replayed; they are not an infinite proof.

## Originality

PASS, with specialist-precedence risk. Persson–Boullé–Kressner's correlated Gaussian Nyström analysis (arXiv:2404.00960, Sections 2.1–2.2) uses dimension/rank and oversampling assumptions and provides general *bounds* rather than this exact one-column planar expectation and sharp fixed-spectrum covariance orientation/uncertainty-minimax law. Persson–Kressner (arXiv:2209.11023, Sections 2–3) and Tropp–Yurtsever–Udell–Cevher (arXiv:1706.05736, Sections 2–4) analyze isotropic sketches or different matrix function estimators. Prior isotropic two-dimensional Gaussian projection formulae and general Gaussian-ratio integration are acknowledged; no novelty is assigned to those isolated facts. A published equivalent risk-law treatment under a different name cannot be excluded, and specialist human literature inspection is warranted.

## Value

PASS. Correlated Gaussian sketches are explicitly motivated by the cited operator-Nyström theory, and covariance design is a consequential choice when approximate spectral information is present. This theorem completely classifies the natural smallest nontrivial case, quantifies the tradeoff between informed alignment and worst-orientation robustness, and identifies the nontrivial \(\arctan((a/b)^{1/4})\) information threshold and the sharp \(r^{-1/4}\) local angular precision scale. The exact values are useful as correctness benchmarks for covariance-aware numerical implementations. No speed, high-dimensional performance or practical spectral-information assumption is silently claimed.

## Scope and risk

Only real two-by-two strictly positive-definite targets, positive-definite Gaussian sketch covariances and one sketch column are treated. The minimax comparison bounds the angular error of an estimated eigendirection, keeps the target eigenvalues fixed and optimizes only Gaussian covariance anisotropy with the major covariance axis aligned to that estimate; it is not over all numerical algorithms. The asymptotic result presumes fixed target eigenvalues. The proof is analytic; finite checks cannot certify novelty. Precedence risk remains for unindexed Gaussian quadratic-ratio and sketch-design literature.

Self-review: passed. Independent audit: not yet performed.
