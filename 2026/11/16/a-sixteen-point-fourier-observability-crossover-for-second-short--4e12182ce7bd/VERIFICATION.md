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

The complete claim is a covariance spectrum for span-three chord starts on 2m labeled points, m>=4. Catalan deletion gives p=C_(m-2)/C_m and q=C_(m-4)/C_m; conflicting starts within circular distance 1..3 have joint probability zero. The circulant Fourier eigenvalues follow from summing this kernel. Explicit support points 0 and each e_i establish positive definite covariance. The cubic D3(c)=8c^3+4c^2-4c-1 and rational pi/cosine sign certificates at m=4..11 establish the mode switch, with a rational inequality m>=12. The polynomial bounds and decreasing q/p yield the sharp 21/5 m=4 ratio and the cosine critical point gives the limit (439+14 sqrt7)/243; no sample cutoff is used to infer the universal statement.

## originality

PASS

Exact second-shortest chord position-covariance and its sharp Fourier crossover do not follow from the located Catalan adjacent-edge enumeration/cyclic-sieving statements or published random-pairing incidence results. Catalan deletion and circulant Fourier diagonalization are classical tools, not asserted new. Best-of-knowledge PASS, with an unindexed broader structure-factor identity a residual risk.

## value

PASS

A position-resolved covariance and spectral condition number for the second-shortest local chord is a natural observability quantity for random Catalan matchings. The finite crossover at sixteen labeled points, uniqueness of the optimum conditioning at eight points, and interior highest-variance direction are non-obvious scale-specific conclusions beyond textbook Catalan edge counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
