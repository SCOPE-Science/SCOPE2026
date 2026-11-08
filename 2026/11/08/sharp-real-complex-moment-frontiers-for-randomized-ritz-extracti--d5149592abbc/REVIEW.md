# Scientific review: sharp real–complex Ritz error moment frontiers

## Correctness — PASS

The conclusion is a small-angle asymptotic distribution for the **selected near-zero** generalized Ritz eigenpair of the explicit Hermitian matrix \(A=\operatorname{diag}(-1,0,1)\), with real or circular complex Gaussian testing. The exact determinant formula supplies a simple zero root and its analytic continuation, the two differentiated null-vector equations supply the eigenvalue and vector slopes, and conditioning on independent Gaussian columns gives exact real/complex ratio laws. The geometric angle identity and exact Rayleigh quotient then give both further limiting laws. Their power-law tails prove the stated moment cutoffs, while Fatou's lemma transfers nonintegrability into divergence of normalized finite-angle moments. The supplied standalone checker passed all its algebraic/numerical and distributional sanity checks. The analytic proof, not the finite simulations, establishes the conclusion.

## Originality — PASS (qualified)

The closest primary work is N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1, specifically Example 1, Algorithm 1, Lemma 3, Theorems 2–3 and Section 5.3. That work already provides this interior Hermitian trial-plane construction, the high-probability convergence theorem, and an empirical observation of a sharp probability-loss factor. Its inspected results do **not** give the two field-dependent exact selected-eigenpair marginal laws, the analytic Pareto-inflation distribution, or the resulting rigorous no-uniform-moment-rate conclusion. Pillai (2016) already establishes real Gaussian quotient/Cauchy facts, and Gu (2020) develops complex Gaussian quotient distributions; the present result does not claim either distribution on its own as new. The new content is the precise mapping of these ratios through a selected generalized eigenpair to eigenvector and refined-value errors, including their sharp real–complex moment cutoffs. published-finding corpus semantic searches for the same eigenproblem, Gaussian-ratio equivalences and moment-obstruction statements returned related but noncovering records, notably `2026/9/21/SCOPE-spectral-filter-rayleigh-residual-distortion--7f8adc00c4c0` (deterministic normal-matrix filtering) and `2026/9/17/SCOPE-projected-eigenpair-certification-false-positive--dc23fa36a6e4` (deterministic stopping certificates). Similarity-search absence does not prove priority.

Historical priority is not certified: a broader older Gaussian Petrov–Galerkin perturbation theorem, or a later version of Shao's preprint (a version dated October 26, 2026 was publicly listed but its full text was not retrievable in this inspection), could cover some conclusions. No claim of independence, expert validation or publication has been made.

## Mathematical value — PASS

The method repairs a genuine deterministic interior-eigenvector extraction pathology and supplies high-probability accuracy, but a solver designer may instead measure expected absolute or squared error. The theorem proves a precise obstruction to upgrading these high-probability rates to uniform moment rates and quantifies how real versus complex Gaussian testing changes the critical integrability exponent. The exact Pareto-2 inflation law and the refined-eigenvalue tail are not arbitrary invariants: they answer whether RMS performance can be inferred for the basic algorithm on its own canonical stress test. No convergence claim is made for outer iterations, larger randomized test spaces or oversampled variants.

## Scientific limits

The result is only for the explicit two-dimensional plane in a three-dimensional Hermitian interior eigenproblem. Its error distributions concern small-angle limits; finite-angle distributions and uniform moments *below* threshold are not determined. This is a self-review only, and a later inaccessible source version remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
