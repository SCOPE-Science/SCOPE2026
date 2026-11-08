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

The exact graph-theoretic proof is in `RESULT.md`, including the complete necessary-and-sufficient forcing criterion and the enumeration of its four disjoint classes.

Run `python3 verify.py` from this file's directory using Python 3.9 or newer. The verifier constructs every graph in the 50 profiles \(4\le a,b\le6\), \(0\le t\le\min\{a,b\}\), enumerates every initial black set, applies forcing to its closure, and separately tests domination. It requires the resulting full coefficient distribution to equal the displayed closed polynomial and that no zero forcing set fail domination. It also exhibits a small-part counterexample at \(a=3,b=4,t=2\).

Finite enumeration cannot prove a statement quantified over all orders. The unrestricted theorem rests on the combinatorial proof; independent mathematical assessment is not performed.
