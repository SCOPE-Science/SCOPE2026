---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof boundaries

Run `python3 verify.py`. The verifier constructs \(\mathbb F_{p^2}\) as \(\mathbb F_p[\theta]/(\theta^2-D)\), with nonsquare \(D\), then enumerates **all** affine pairs and adds the unique infinity point for every permitted \(\lambda\) for each \(p=5,7,11\). It verifies every non-Hermitian count and the Hermitian comparison, rather than sampling points.

Exact expected outputs: for \(p=5\), \(66\) non-Hermitian versus \(126\) Hermitian; for \(p=7\), \(176\) versus \(344\); for \(p=11\), \(672\) versus \(1332\). The program's finite enumeration does **not** certify all prime powers. The proof in RESULT.md establishes that universal quantifier by reducing to a nondegenerate ternary quadratic form over an arbitrary finite field of odd order.

The short-orbit identification additionally invokes Borges--Korchmáros--Speziali Proposition 4.26; the brute-force program does not reconstruct the geometric automorphism group. No independent audit has been performed.
