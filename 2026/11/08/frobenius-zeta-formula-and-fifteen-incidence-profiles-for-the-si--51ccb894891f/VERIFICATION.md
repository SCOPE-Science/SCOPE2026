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

# Verification record

The general point count is established by geometry and the Lefschetz trace formula, not by extrapolating a field enumeration. Geometric inputs are the sixteen \((-1)\)-curves, their triangle-free forty-edge intersection graph, and the faithful action of \(W(D_5)\) on the curve configuration. The displayed point count for every extension field follows by distinguishing individually rational curves from swapped conjugate pairs. Traces of signed edge permutations give the formal zeta factorization.

`verify_frobenius.py` uses only the Python standard library and enumerates exactly \(16\times120=1920\) group elements. It asserts the full fifteen-row frequency table, eighteen conjugacy classes, fourteen different counting polynomials, geometric graph preservation, and the signed-edge trace relationship for powers through ten. The expected successful output is `VERIFY_FROBENIUS_OK 1920 18 15 14`.

`verify_geometry.py` separately enumerates projective-plane points off a conic and ten secant lines through five rational conic points for primes \(5,7,11,13,17,19\). The count is \((p-5)^2\), consistent with the known split calculation. It additionally constructs three rational points and a degree-two closed point on the conic, with all ten secants represented over an exact quadratic extension for primes \(5,7,11,13\). It counts \(p^2-4p+5\), an independently checked nonsplit profile. The expected output is `VERIFY_BLOWUP_GEOMETRY_OK`.

Finite scripts verify a fixed group census and individual geometric examples; the scripts do not independently certify all varieties, the published literature's exhaustiveness, or every field-size realization of the Weyl group types. No independent mathematical audit is claimed.
