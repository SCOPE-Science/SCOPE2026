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

The self-contained `verify.py` was executed with Python 3 and returned `VERIFY_OK graphs=42 profiles=757296`. It directly constructs every graph \(G_{n,t}\) with \(2\le n\le8\) and \(0\le t\le n\), exhaustively checks every assignment of the two distinct actions, and compares individually calculated best-response inequalities against the derived family classification. It separately tests the exact counting formulas and the predicted cut-size histograms for each network. This includes all parity and minimum-size boundaries; no random sample was substituted for exhaustive testing in this finite range.

The finite checks do not certify cases beyond \(n=8\); those are established by the general algebraic proof in `RESULT.md`. The game assumes homogeneous unit edge payoffs, no profitable unilateral deviations, and preservation of indifferent equilibria. Priority beyond the inspected sources is not independently certified. Independent audit has not been performed.
