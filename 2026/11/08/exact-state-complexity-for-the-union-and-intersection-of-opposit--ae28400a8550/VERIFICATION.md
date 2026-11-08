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

## Standalone replay

Use Python 3 standard library and run `python3 checker.py` from this directory. The program constructs and minimizes both complete product automata, verifies explicit state counts for every \(1\le a,b\le18\), enumerates all binary words up to length 11 for \(1\le a,b\le4\), and checks the differentiating suffix families for \(1\le a,b\le9\).

Expected replay line: `PASS: 324 parameter pairs, 65520 bounded direct-word checks, 221616 state/probe iterations`.

The core mathematical evidence is the explicit reachability partition and four probe-family residual equivalence tests in RESULT.md. The checker is deliberately finite; it is not an infinite proof, and independent mathematical review has not been performed.
