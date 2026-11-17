---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: A five-element subset of F2^d has affine dimension only 3 or 4, giving the two local row types. Independently enumerated all C(8,5)=56 and C(16,5)=4368 quotient column sets with an exact integer Bareiss determinant, obtaining row-type tables (0:24,32:32) and (0:1360,16:2672,32:320,48:16). Verified 16 maximal 48-column sets equal exactly 16 translates of {0,3,5,9,14}. The projection to dual quotient has fibers Q/2^r and repeated columns force determinant0, proving all d≥4 count polynomials without extrapolation. Unit-normalization Q^(−5/2) and q=16 boundary respected.

## originality

PASS

PASS for all-dimensional five-point Sylvester Walsh minor distribution and affine maximizer lifting; historical d=4 table and max48 are explicitly excluded from originality.

## value

PASS

PASS: Full minor distribution and maximizing masks quantify exact singularity and D-optimality of natural five-sample Walsh frames across every Boolean dimension, a meaningful invariant beyond finite q16 table and trivial determinant maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
