# Mathematical assessment

## Correctness — PASS

The covariance is strictly positive definite at distinct sites, as follows from all-positive Fourier multipliers and Vandermonde independence. The exact inverse cofactor identity reduces the sign to a theta-function multiplicative ratio. Jacobi triple product then produces the explicit polynomial factorization shown in RESULT.md; the sign is strict outside a narrow negative-cosine interval, and its log derivative is strictly positive within it. This proves a unique critical angle for every real heat time. Poisson summation and the leading product factor prove the sharp endpoint limits. The `check.py` calculations passed 85 assertions, but finite experiments are not the infinite-parameter proof.

## Originality — PASS (historical priority provisional)

Borovitskiy et al., arXiv:2006.10160 (2020), explicitly develop this periodic Gaussian heat covariance. Their inspected full text does not provide the symmetric three-site precision sign transition. The Karlin–McGregor odd determinant positivity in Cunden–Mezzadri–O'Connell (2018) does not constrain the needed non-principal two-by-two cofactor. Huang–Li's circular Matérn CAR results involve different Fourier multipliers. published-finding corpus searches on conditional independence, theta multiplicative inequalities, 3-site precision and Gaussian circle thresholds found no same claim; closest results concern either intrinsic-distance Gaussian positivity, Gaussian quadrature, or Bergman three-point determinants. An unlocated theta inequality could imply this result, so priority should not be treated as independently verified.

## Mathematical value — PASS

Three samples are the minimal setting for a nontrivial conditional-dependence question. Determining a unique theta-kernel opening angle at which the outer sites become independent given the center, separating two strict sign phases, and proving both sharp heat-scale limits is a natural complete geometric classification, relevant to Gaussian graphical modeling and precision sparsity. It is neither a restatement of Fourier covariance construction nor a routine cofactor calculation without sign control.

## Closest literature and limitations

The same kernel is classical and explicitly given by arXiv:2006.10160, Example 3. The proof uses classical DLMF 20.5.3 and Poisson summation. The result covers only symmetric three-site configurations and gives no monotonicity in the heat parameter. An earlier specialist theta inequality may cover an equivalent formulation. All underlying independent historical-priority and independent mathematical audits remain open.

Self-review: passed. Independent audit: not yet performed.
