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

# Reproducibility and scope

From the directory containing `verify.py`, run `python3 verify.py`. The program constructs the subset transition graph independently of the proof, performs breadth-first search from the full state set, and **counts all distinct shortest label strings** reaching any singleton by dynamic path counting. It tests all \(66\) pairs with \(2\le n\le12\) and \(1\le r<n\), including nonsynchronizing cases. It then replays the explicit candidate on all coprime pairs with \(2\le n\le50\) and verifies the final state \(r\).

The mathematical proof for arbitrary parameters is in `RESULT.md`. Finite exhaustive subset searches do not prove uniqueness for infinitely many parameter pairs. The optimal length and a shortest example were already published by Martyugin (2009), so the checked new point is the complete singleton optimizer set. The literature comparison is qualified by the possibility of a different formulation of uniqueness not indexed by the inspected sources. Independent audit remains unperformed.
