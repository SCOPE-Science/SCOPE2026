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
The exact verifier `klein21_certificate.py` uses the integral rank-two algebra with relation \(\omega^2=-\omega-2\). It enumerates all 1330 three-line determinants; nonzero norms are powers of two, and pair-concurrence classes form 28 triples plus 21 quadruples. This proves the field-uniform concurrency statement once the elementary norm-unit argument in `RESULT.md` is applied.

The independent enumerator `klein21_finite.py` counts every rational point of \(\mathbb P^2\) over each of \(\mathbb F_7\), \(\mathbb F_9\), \(\mathbb F_{11}\) using both roots, and \(\mathbb F_{23}\). It records membership in zero, one, three or four of the 21 lines and checks that the complement counts equal \((q-9)(q-11)\). In particular, no point lies outside the divisor over the fields of orders nine and eleven. The exact output transcript is `verification_output.txt`; these computations and the accompanying proof do not constitute independent external validation.

Limitations: the direct field enumeration is finite and does not independently establish the theorem over infinitely many fields. That conclusion comes from the integral determinant and incidence argument. No claim is made in characteristic two or for nonisomorphic line models.
