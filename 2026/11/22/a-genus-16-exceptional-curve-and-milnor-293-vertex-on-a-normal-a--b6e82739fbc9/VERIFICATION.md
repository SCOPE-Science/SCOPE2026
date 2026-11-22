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

# Reproducibility
Run `python verify.py` with ordinary Python 3. The checker tests the nine-line incidence structure over \(\mathbb F_{13}\), the explicit transverse conic, the eighteen totally ramified points, genus and self-intersection arithmetic, both Euler calculations, and the Milnor number subtraction. Its output should consist of five lines beginning with `PASS:`.

# What is and is not checked by code
The geometric assertions rely on a proof using the normal cyclic triple cover, explicit blowup centers and contraction morphism, Riemann--Hurwitz, intersection theory, and topology of isolated hypersurface smoothings. Computation over one finite field witnesses the nonempty generality open; it does not prove all complex-parameter assertions or replace the geometric arguments. The genus-\(16\) exceptional curve is not deduced from finite enumeration. No independent audit has been performed.
