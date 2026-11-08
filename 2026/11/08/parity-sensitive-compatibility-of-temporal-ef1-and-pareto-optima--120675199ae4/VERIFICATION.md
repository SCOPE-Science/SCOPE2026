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

# Verification evidence

The included Python 3 program `verify.py` performs a direct independent Pareto test against **every** competing complete assignment and checks both directions of EF1 at each arrival prefix. It tested 192 parameter triples/quads across 45,120 directly evaluated assignments; 105 parameter cases admitted at least one valid allocation. A separate set of 189 larger parameter cases verifies the exact enumeration after identifying the absence-of-crossed-pairs Pareto condition. All tests passed with exact integer arithmetic and without external packages.

Run `python3 verify.py` in the same directory as this document. The code and claimed theorem are fully specified; experiments corroborate but do not substitute for the general proof. The ratio bound includes equality, and no checks were claimed for real-valued inputs outside the exact algebraic argument. Independent external verification has not been performed.
