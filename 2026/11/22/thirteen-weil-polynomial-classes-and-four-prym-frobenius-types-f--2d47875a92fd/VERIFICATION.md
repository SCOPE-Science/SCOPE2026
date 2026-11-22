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

# Exact arithmetic verification

The standalone `verify.py` requires only Python 3 standard-library facilities and the adjacent `SPECTRUM.json`. It builds finite fields with polynomial coefficient representatives, checks that exactly 42 coefficient pairs meet the discriminant criterion, computes point counts of each genus-three curve over 7, 49 and 343 elements, and independently cross-checks the 49-element fourth-power counts by the subgroup criterion.

It then reconstructs the Weil numerator from the two base/degree-two counts, checks the thirteen-type histogram and individual parameter assignments, and verifies the four degree-four Prym factors. The degree-three counts are an independent check of the *proved* identity over odd-degree extensions, not a substitute for it. A successful execution reports `VERIFY_CYCLIC4_F7_OK: 42 smooth models; 13 Weil polynomials; 4 rational Prym types`.

All finite enumerations are complete for the specified finite fields. They are not an exhaustive survey of all prime powers, and the calculations do not establish historical priority or independent mathematical certification.
