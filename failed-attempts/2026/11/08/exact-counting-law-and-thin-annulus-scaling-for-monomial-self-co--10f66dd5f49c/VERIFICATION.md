---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: In the Laurent basis, multiplication by z^k is a bilateral k-step weighted shift with weights squared (1+r^(2(n+k)))/(1+r^(2n)). Subtracting backward squared weights gives (1-r^(2k))²/((1+r^(2n))(1+r^(2(k-n)))), equal to L_a/(cosh a+cosh(b(2n-k))). The count is precisely the number of integers in an open interval of length A_a(t)/b, with discrepancy <=1. Layer cake gives the uniform |Tr(D^p)-kW_p(a)|<=c_a^p, including p<1, and direct integration/telescoping gives W1,W2 and all stated limits. Even/odd peaks follow by minimizing |2n-k|. Independent rational diagonal identities and bounded real counting checks passed; analytic bounds prove all parameters.

## originality

FAIL

FAIL: the 2 Nov 2026 all-mass annular Hardy selfcommutator theorem gives the complete spectrum for coordinate multiplication z on every weighted annulus. Decompose the k-th power multiplier into k reducing residue spaces n=j+kℓ, j=0,...,k-1; each is exactly its model at inner radius r^k and boundary mass beta=r^(2j). The prior eigenvalue formula thus yields the submitted complete k-power eigenvalues without new spectral analysis. The counting ±1, layer-cake moments, and scaling are direct one-dimensional lattice-count/Riemann-sum consequences of that known full spectrum.

## value

FAIL

FAIL: although annulus scaling is a natural parameter question, the particular full result is a routine aggregation of the earlier all-boundary-mass exact diagonal spectra under a standard residue-class decomposition plus interval counting and layer cake. No separately motivated new invariant survives the mathematical reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
