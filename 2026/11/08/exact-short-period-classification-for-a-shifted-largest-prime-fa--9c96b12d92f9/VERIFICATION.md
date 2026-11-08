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

The proof covers all \(k\ge1\) and all starting integers \(n\ge2\). Its exhaustive short-cycle case split is symbolic; a composite maps immediately to a prime, and every block of consecutive prime states increases by the same positive shift. Conditions on multipliers in the four-cycle parameterization are exact largest-prime-factor tests, with both multipliers required to exceed one.

Run `python3 verify.py` from the folder containing the script. The accompanying `verification_output.txt` is the recorded stdout from this checker. The program compares independently observed trajectories and candidate-generating arithmetic formulas for \(1\le k\le160\), including the boundary shifts \(k=1,2\), with a specified finite set of starting primes. This is a regression of the proof, **not** a finite proof of completeness for all parameters or all start values. No external certificate, independent audit, or formal proof-assistant validation has been performed.
