# Review of the first-step ellipsoidal minimax theorem

## Correctness — PASS

For every \(0<\delta<1\), the first normalization of Algorithm 1 in arXiv:2609.38561v2 reduces exactly to a unit step \(x_1=-g_0/\|g_0\|\). The prescribed linear objective, disk and fixed full-rank preconditioner satisfy the source's convexity, Lipschitz and active-subspace assumptions; projection is inactive. Pairing antipodal directions yields an explicit one-dimensional integral. Two verified antiderivatives give the stated arcsinh/arcsin closed form. A compact minimizer exists. Positive-term estimates trap all minimizing orientations at the \(1/\sqrt{\log(1/\delta)}\) scale, where a uniform expansion reduces the asymptotic minimum to the unique minimizer of \(t/2+1/t\). This reconstructs the exact constants and all quantifiers; it does not infer an asymptotic from finitely many trials. The separate standalone numerical calculation in `verify_progress.py` returned `CHECKS_OK 460` and was compared with the formula.

## Originality — PASS with residual historical risk

The primary Sholokhov--Rogozin paper (arXiv:2609.38561v2) defines the method, proves rank/conditioning-dependent bounds and considers experiments, but its main analysis and appendices do not state the exact worst-first-step expected-progress functional, the least-favorable orientation or the \(\sqrt{\delta\log(1/\delta)}\) minimax law. The original Ren--Luo POEM paper (arXiv:2502.05600) treats isotropic sampling. Vareilles (arXiv:2605.31536) computes ordinary moments of a related angular Gaussian distribution, not signed POEM-ES progress and its optimization over slope. Earlier Gaussian sign-correlation identities and broad derivative-free convergence bounds are not claimed as original. Mathematical implications and the explicit domain of each comparison are recorded in `AUDIT.json`. An unlocated prior sharp signed-angular minimax identity is a residual priority risk; absence from searches is not proof of absolute uniqueness.

## Mathematical value — PASS

The algorithm's parameter-free first move always has unit Euclidean norm on this natural linear benchmark. Its *expected* objective progress nevertheless has a nontrivial worst-direction sensitivity to geometric preconditioning; the direction causing maximal degradation is neither an eigenvector nor fixed as anisotropy grows. The exact constant and moving worst orientation answer an intrinsic algorithmic robustness question that is not supplied by the existing general convergence bound, and can calibrate anisotropic startup behavior against the isotropic benchmark \(2/\pi\). This is an exact natural minimax invariant, not merely a numerical observation. It is not evidence of poor end-to-end convergence and does not challenge previously proved conditioning-dependent bounds.

## Closest literature and limits

The closest article is *Parameter-Free Zeroth-Order Optimization with Ellipsoidal Sampling*, arXiv:2609.38561v2, Algorithm 1 and the main convergence analysis. Historical priority is qualified by the angular Gaussian and signed-projection literatures. The theorem concerns just the first noiseless update in two dimensions; alternative stepsizes, noisy sketches, rank-deficient covariance and subsequent averaging are outside scope.

Self-review: passed. Independent audit: not yet performed.
