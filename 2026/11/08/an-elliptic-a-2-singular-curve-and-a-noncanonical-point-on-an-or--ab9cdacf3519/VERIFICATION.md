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

# Exact reproducibility checks

Run `python certificate.py` using Python 3 with SymPy. The program checks the seven invariant monomials of the quartic, the exhaustive fixed-eigenspace partitions for the 26 nonidentity elements, four tangent-weight triples, the three order-nine residual representations after pseudo-reflection quotients, Reid–Tai minima, index arithmetic, the topological Euler and anticanonical-volume identities, and the exact Gröbner unit-ideal smoothness witness for the plane quartic at parameters \(a=1,b=0\).

A successful replay prints `CERTIFICATE_OK`. Exact finite calculations verify only the encoded identities, not the geometric results requiring fixed-point smoothness, local analytic linearization, the quotient canonical formula, or Riemann–Hurwitz. Those arguments are supplied in RESULT.md. The witness proves nonemptiness of the smooth-parameter locus; the theorem itself assumes smoothness for arbitrary parameters.

Independent audit: not performed.
