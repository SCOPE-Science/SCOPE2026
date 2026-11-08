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
The exact finite computation is `python3 verify.py`, with expected output recorded in `verify_output.txt`. It checks every prime \(p\equiv1\pmod3\) at most \(840\) using two different exact classifications of cubic cosets, then checks all \(27\) ternary words for every eligible prime \(307\le p\le840\). It separately certifies the unique missing \((0,0,0)\) word at \(283\) and exhibits witnesses at \(307\).

The infinite range \(p\ge841\) is proved symbolically by the finite-field character-sum inequality in `RESULT.md`; no finite test substitutes for it. There was no independent audit. The output includes Python's floating-point evaluation of the strictly positive lower bound at \(p=841\), but mathematical positivity there is the exact integer identity \(841-28\cdot29-27=2\), so there is no numerical tolerance dependency.
