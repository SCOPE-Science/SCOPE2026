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
The independent standard-library `verify.py` enumerates all \(18564\) candidate six-facet bases by exact rational elimination, verifies 31 actual vertices with denominators one or two, and compares the exact four-variable lattice count against the formula at \(0\le m\le19\). The all-bound proof uses rational Ehrhart theory: degree six and quasiperiod at most two are guaranteed by the certified rational vertex denominators, and seven counts in each parity class determine the two polynomials. Run `python3 verify.py` in this directory; expected last line `VERIFY_OK`. Computations are finite exact certificates, and no independent mathematical audit is claimed.
