---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

In the Fock normalization used in RESULT.md, the single-disk spectrum is ∫_0^R t^n e^-t/n! dt, with gap Re^-R. Coherent overlap equals s=e^-pi*d²/2. The opposite-disk coherent leakage q≤R exp(-pi(d-r_R)²) controls squared coupling to the orthogonal complement, and trace cross-bounds isolate excited states. Compression on the two coherent vectors has (ell+q±2ell s)/(1±s); Schur complement gives O(q) perturbation, q=o(s), so the stated asymptotics and spectral gap follow for every fixed R>0. Parity fixes approximate eigenvectors. Finite Galerkin quadrature is only numerical corroboration.

## originality

FAIL

November 1, 2026 Resultary theorem already proves exactly the two top Fock localization eigenvalue splitting and sharp leading constant under the unitary coordinate rescaling zprime=sqrt(pi)z, s=R, dprime=sqrt(pi)d. The submitted smaller secondary error and parity-mode restatement do not change its already established central claim.

## value

FAIL

Gaussian localization top-pair tunneling is a meaningful problem, but the exact doublet coefficient and separated-mode result were already proved in the November 1 theorem. The new subordinate exponent in the error is neither claimed optimal nor motivated by a new inverse, stability, or uniformity question. As submitted the finding is a covered theorem with an incidental estimate improvement, not a separately valuable original result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
