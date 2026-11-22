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

# Reproduction and verification

Run `python3 verify.py` with Python 3.10 or later and no third-party packages. The executable directly enumerates all nonnegative contingency tables for the listed small sizes, calculates row, column, and joint modal deletion counts, and compares the entire attained set with the proposed integer interval. It separately solves integer feasible-circulation instances for random alphabet/size/error parameters and checks random independent determinant fibres.

Observed output from the supplied script:

```
VERIFY_OK exhaustive_tables=339613 constructed_instances=3373 multi_fiber_tests=9984
```

The checked exhaustive families were \((b,c,n_{\max})=(1,1,12),(1,3,10),(3,1,10),(2,2,18),(2,3,14),(3,3,10),(3,4,8),(4,4,6)\). Construction tests used alphabet sizes from two through seven and selected total sizes through forty, with seeded random choices of admissible errors and cell maxima. The multi-fibre check used a fixed random seed and at most seven determinant fibres. These are finite cross-checks, not an unbounded computational proof. The proof is the modal-fibre reduction and integral-circulation argument in RESULT.md.

No independent mathematical or historical-priority audit has been performed.
