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
# Verification record

The proof is given in `RESULT.md` and applies for every integer alphabet size at least two and every positive block length; the finite computations below only check reproducibility of its consequences.

Run `python3 verify/direct_deletion_graph.py` with Python 3. It directly constructs all admissible source words and exactly-one-deletion descendant sets, exhausts all unordered pairs, then checks both total and first/last-difference span counts in 24 small parameter cases.

Run `python3 verify/interval_construction.py` with Python 3. This program constructs edge candidates from single-position changes and canonical shift intervals instead of from deletion descendants; it verifies predicted totals and confirms the alternating structure of all doubly represented larger intervals.

Each program was executed directly from the packaged project before the review and exited normally. Tested ranges: q=2, n=1..8; q=3, n=1..7 in the direct checker and n=1..6 in the interval checker; q=4, n=1..5; q=5, n=1..4. The unrestricted theorem is *not* certified by these finite tests. No external audit or independent validation has been performed.
