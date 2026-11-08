# Scientific review: exact planar funNyström log-trace law

## Correctness — PASS

The matrix in the claim is strictly positive diagonal, and the sketch is real isotropic Gaussian with one column. Its Nyström approximation is rank one almost surely, with a single eigenvalue \((a^2+b^2T)/(a+bT)\), where \(T\) is a squared Cauchy ratio. The excess error is a strictly increasing fractional-logarithmic transform of \(T\), so the support and exact CDF follow by inversion, including endpoint behavior. The angular mean-value identity proves the closed-form expectation; the direct comparator's rank-one residual and reciprocal-quadratic angular integral prove its expectation and distribution. Coupling all spike sizes with fixed Gaussian coordinates proves almost-sure limits; direct expansion establishes the different leading mean scale. The checker reproduced from `verify.py` passed 6,020 exact and numerical assertions, but these are not substituted for the analytic proof.

## Originality — PASS, qualified

The motivating 2022 work of Persson–Kressner defines the function-after-Nyström algorithm and presents matrix-function approximation, probability bounds, and experiments. Its Theorem 3.9 concerns oversampled sketches and does not give the exact unoversampled planar CDF or the nonuniform-integrability contrast. The 2016 Saibaba–Alexanderian–Ipsen log-determinant paper uses a different compressed-subspace estimator and probabilistic bounds. General rank-one trace-residual expectation formulas already cover the *direct* Nyström comparator, which is not advanced as a novel result. The compared new content is the explicit function-after-Nyström distribution, its exact mean, and its joint sharp high-spike mean/quantile law. Searches for equivalent funNyström, planar Cauchy-ratio and Gaussian sketch formulations did not locate a stronger dominating statement. This is evidence-based noncoverage in inspected material, not proof of global priority. An older specialized matrix-function sketch calculation remains a residual risk.

## Value — PASS

The source algorithm is explicitly intended to compute matrix functions and traces without expensive direct matrix-function products. Its smallest unoversampled Gaussian instance is not captured by the published expectation theorem's oversampling hypotheses. This exact benchmark quantifies the full error distribution and shows why high-probability, median and expected-error behavior can be radically different: a typical \(a^{-1}\) excess coexists with an \(a^{-1/2}\) mean excess, while the direct comparator has a diverging mean despite convergence in distribution. These precise scales test the sharpness of sketching guarantees and risk metrics. This is a meaningful natural low-rank matrix-function diagnostic, not a claim about large matrices or production workloads.

## Closest literature and residual scope

Persson–Kressner (arXiv:2209.11023, Sections 2–5) supply the algorithm, motivation and existing larger-sketch bounds. Saibaba–Alexanderian–Ipsen (arXiv:1605.04893, Sections 2–4) give related spectral-gap bounds for a different log-determinant estimator. Gittens–Mahoney (2016) concern general Nyström low-rank error bounds. Classical Cauchy distributions, Gaussian rotational invariance and logarithmic trigonometric averages are used without novelty claims. The result covers only exact two-dimensional one-probe Gaussian function-after-Nyström error, with a direct-Nyström comparator; equivalent prior special-case analyses remain possible.

Self-review: passed. Independent audit: not yet performed.
