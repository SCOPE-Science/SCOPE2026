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

# Verification notes

Run `python3 verify.py` from the directory containing the delivered standalone file. It requires Python 3 standard library only. The executed output was `PASS finite checks 67738 ; all cyclic-order checks 3..8 and all ordered digraphs 3..6`.

The verifier enumerates all rank assignments to simple cycles of lengths 3 through 8 and checks that precisely \(2r\) of the \(r!\) assignments contain an increasing shortcut. It then enumerates every simple forward-arc subset on \(n=3,4,5,6\), compares direct alternate-path reachability against witness existence, and verifies by exact rational arithmetic the binomial witness expectation under independent half-probability arcs.

This check does not inspect every size, does not prove Poisson convergence, and does not establish independence of the limiting Poisson marks. Those conclusions use the explicit cycle factorial-moment and truncation argument in `RESULT.md`. No independent mathematical audit has occurred.
