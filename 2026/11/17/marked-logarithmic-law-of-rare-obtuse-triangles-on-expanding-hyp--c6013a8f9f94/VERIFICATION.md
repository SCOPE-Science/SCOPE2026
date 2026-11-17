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

# Verification of the conditional marked law

The exact region \(xy<q\), Jacobian \(q\log(1/q)\), and integral identity for \(J(q)\) have analytic derivations in RESULT.md. The density limit follows from Scheffé's lemma, not simulation. The side-length limit uses the hyperbolic half-chord relation and \(\log(1/q)/(2R)\to1\).

The included standalone standard-library `verify_marked.py` was run and returned `MARKED_HYPERBOLIC_CHECKS_OK`. Its checks cover direct three-angle-gap sampling at radii 1.5 and 3.5, normalization of the two-mark conditional density by midpoint quadrature, and numerical asymptotics for fixed logarithmic marks. An additional numerical script using quadrature and geometric cosine-law comparisons was run. Finite numerical tests do not establish a continuum total-variation limit.

No independent mathematical audit was performed. The historical-coverage comparison is a self-review, not definitive priority certification.
