---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The integral of two unit-normalized real exponential kernels is 2 sqrt(lambda mu)/(lambda+mu), i.e. sech of half the logarithmic-rate difference. Fourier transforming the resulting absolutely summable block Gram diagonals and applying Poisson summation gives diagonal F and conjugate off-diagonal entries G, with the conjugation dependent on Fourier convention; the eigenvalues are F±|G|. The half-line quadratic form is a compression of the Laurent form. Finite wave packets supported on consecutive nonnegative indices have diagonal overlap factors (1-|k|/N)_+, so at a chosen symbol eigenvector their Rayleigh quotients tend to the corresponding eigenvalue by absolute summability. Thus the extrema are sharp even on the half-line. Triangle inequality gives the upper extremum at zero, and positivity of all aliases with distinct adjacent phases gives a strictly positive lower minimum for 0<s<h. For fixed h, |G/F| squared is the characteristic function of the difference of independent copies of the alias frequency. Its moments are uniformly bounded on the compact frequency interval and its square root near one has uniform second-order term minus half the variance and remainder O_h(s^4). The minimum preserves that error; multiplying by F gives exactly the stated 4 pi^3/h^3 times the weighted index variance. For h down to zero, let a=2 pi^2/h and y=theta/(2 pi). At y=0 the two nearest side aliases give 4 exp(-a) to leading order. For 0<=y<=1/4 the central alias dominates uniformly and retaining its pairs with the two side aliases bounds the weighted variance below by (4-o(1))exp(-a)cosh(ay); for 1/4<=y<=1/2 the nearest pair alone gives order at least exp(-3a/4). This controls the actual minimum. For large h the direct Fourier coefficients and derivatives have tails O(exp(-h/2)), K''(0)=-1/4, and the s-odd first derivative of the off-diagonal series at zero is imaginary, so the modulus expansion gives 1/8+O(exp(-h/2)) uniformly. Endpoints s=0,h are excluded, the constants are squared and only the closed span is relevant. Replay: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 /workspace/reproductions/1.py verifies finite Gram convergence and samples the collision coefficient at multiple frequencies. The frozen script's high-precision check is at theta=0, despite its theta-min comment; neither diagnostic certifies the continuous minimum or either asymptotic regime.

## originality

PASS

Best-of-knowledge pass for arbitrary-offset half-line Laplace two-stream sharp bounds together with the explicit collision stiffness and its two mesh limits. The balanced half-period single-chain specialization is directly covered and expressly not claimed as new. The closest two-coset frame results are genuinely analogous but do not identify these Gram symbols or constants.

## value

PASS

Two interlaced decay scales form a natural stable sampling model with a genuine near-dependence when the scales collide. Optimal squared bounds separate mere existence of a Riesz sequence from quantitative stability. In particular the h^(-3) times exponentially small dense-grid prefactor, contrasted with the nonzero sparse-grid limit, supplies information not available from pointwise independence or a lower bound at one frequency. This does not purport to classify the minimizing frequency at all offsets or the joint h,s limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
