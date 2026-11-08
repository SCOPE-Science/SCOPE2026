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

Reproduce using `python3 verify.py` with standard Python 3; no downloaded datasets or external libraries are needed. The script verifies all \(8\) possible states, the exactly-four-step reachability, the incoming-transition count and all \(128\) residue/state factor cases for each length \(1\) through \(16\). Each stated palindrome-and-multiplicity list and all long-factor starting positions are checked against their exact definitions. Direct prefix and high-index diagnostics are also performed.

Observed output:

`VERIFY_OK exact_cases=2048 primitive_state_power=4 direct_windows=2097152 long_position_checks=80000`

The argument extending the finite certificate to every index is in RESULT.md: the exact binary-block formula and the primitive-substitution uniform-frequency theorem. The diagnostics do not establish infinitude on their own. Independent audit has not been performed.
