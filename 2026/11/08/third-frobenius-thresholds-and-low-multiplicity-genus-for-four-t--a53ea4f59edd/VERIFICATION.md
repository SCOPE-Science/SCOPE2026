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

# Verification
The file `verify.py` implements unbounded-knapsack coefficient extraction independently of the partition-coordinate proof. It checks, for each tested coprime pair \((a,d)\), every integer in \([0,\max_t M_t+2a]\), including exact membership in the at-least-three-representations region, its extremal complement, and the total number of exceptions. The scope of these finite tests is specified in the executable itself.

Reproduce with `python3 verify.py`. The proof of the infinite result is the argument in `RESULT.md`, not the finite tests. No independent audit or external formal certification has been undertaken.
