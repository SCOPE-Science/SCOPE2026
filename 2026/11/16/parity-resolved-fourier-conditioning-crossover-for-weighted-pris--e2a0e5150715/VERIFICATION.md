---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Perfect matchings of the n-prism with rungs correspond to cyclic monomer-dimer coverings, plus two extra zero-rung horizontal configurations for even n, giving Z=alpha^n+beta^n+2*[n even]. Differentiation and pinned-rung path factorizations yield the exact two-point probabilities. A geometric Fourier sum over the two transfer roots gives Lambda_j=p_n 4cos²(pi j/n)/(lambda²+4cos²), j !=0, while Lambda_0=lambda p_n prime>0 by variance. The only nonconstant zero occurs at even n, j=n/2. Extremal retained cos² values are cos²(pi/n) and sin²(pi/n) even or sin²(pi/(2n)) odd; their ratio and both c/n limits follow directly. Independent full prism-matching enumeration n=3..8 at lambda=.8 checked probabilities and all nonzero Fourier eigenvalues numerically to 1e-9.

## originality

PASS

Two-dimensional torus dimer transfer-matrix results provide general methods and correlations, not the finite circular ladder with rung fugacity lambda and all-n exact rung covariance. The published uniform-prism full-edge covariance result handles a distinct fixed lambda=1 specialization; that instance is explicitly not claimed new. The activity-dependent n^-1 critical crossover, sharp parity-specific mean-zero conditioning and soft-mode profiles remain distinct on the inspected literature.

## value

PASS

The finite-size dimer observability question has a natural Fourier covariance and a real deterministic parity blind mode; its exact activity threshold scaling and conditioning crossover give a reusable quantitative boundary, not a mere model-renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
