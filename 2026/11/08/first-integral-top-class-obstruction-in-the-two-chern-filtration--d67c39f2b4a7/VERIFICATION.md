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

# Reproduction

The files `CHECK.py` and `CERTIFICATE.json` are standalone and require Python 3 with no external modules. Run `python3 CHECK.py CERTIFICATE.json` from their directory. The checker builds every top intersection in every width \(1\leq\ell\leq16\) by integer Pieri moves and by an independently coded six-term alternant coefficient extraction. It then compares every complete integer array against `CERTIFICATE.json` and computes all greatest common divisors. Success prints `PIERI_AND_ALTERNANT_CHECKS_OK` and `FIRST_NONPRIMITIVE_WINDOW_EXACT`.

# Verification boundaries

The calculations are exhaustive over the finite parameter range and all allowed top monomials; they do not constitute a proof for any wider parameter. The finite proof depends on standard integral Pieri and Schubert integration identities stated in `RESULT.md`. Reproduction of code and stored outputs does not imply independent mathematical review.
