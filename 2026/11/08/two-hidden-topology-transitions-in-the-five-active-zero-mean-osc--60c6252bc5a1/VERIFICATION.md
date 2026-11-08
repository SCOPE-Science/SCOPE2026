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

The exact-integer checker `verify.py` uses certified rational intervals for square roots and enumerates the short subsets in all three open chambers. Expected output: `VERIFY_OK exact_sign_checks 43 threshold_certificates 4 generic_topology_chambers 3`.

Analytic checks of the proof: the two wall functions have strictly opposing derivative signs; the other potentially changing pair and triple inequalities retain fixed signs; the five-link homology formula yields the specified Betti numbers. The verification depends on the source's rotating-state reduction and the published general polygon-space homology theorem. It does not verify the Floquet stability of any oscillator state. There has been no independent audit.
