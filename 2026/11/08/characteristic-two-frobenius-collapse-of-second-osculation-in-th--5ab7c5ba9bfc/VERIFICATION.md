---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Local torus coordinates reduce the sections to f_i=t_i, g_i=t_i², h_ij=t_i²t_j. Hasse jets satisfy h_ij−g_i−f_j=−1+2u_i u_j modulo degree3; yields 2n+binom(n,2) rank unless char2, then 2n+1. Translation preserves cubic polynomial independence; image of quadratic second fundamental map spanned by pure squares, so Frobenius function-field degree 2^(n−1). Independently built binomial-coefficient Hasse matrices n=2,3,4 giving char2 ranks 5,7,9 and odd ranks 5,9,14; n=2 rank and defect coincide in both characteristics; rank divergence starts at n=3.

## originality

PASS

The n=2 projection is the classical Togliatti six-section model and is partially described in earlier characteristic-two boundary work, but no inspected theorem covers all n and Frobenius degree 2^(n−1). The char-zero Perkinson Hasse-jet general framework can be applied but does not state modular rank formula. Best-of-knowledge PASS with possible implicit general toric jet coverage.

## value

PASS

All-dimensional osculating defects in positive characteristic and a purely inseparable second fundamental map are structurally meaningful modular invariants, not merely an n=2 table or routine numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
