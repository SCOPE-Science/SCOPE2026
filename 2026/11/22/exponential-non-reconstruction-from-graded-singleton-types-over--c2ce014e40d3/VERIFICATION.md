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

# Reproduction and scope

Run `python3 verify_ultrametric_types.py`; standard Python 3 is the only dependency. Its exact exhaustive verification generates all unlabelled nested partition hierarchies of each size up to eight. For every one of the 220 hierarchies through size seven it enumerates all admissible ternary one-point distance vectors via the ultrametric triangle conditions and compares the resulting two-statistic type count against the independent ball-tree prediction. It then groups all hierarchies through size eight by that polynomial, verifying the signature-collision census, including the previously known five-point pair. It evaluates one numerical instance of the closed lower bound. The stored `verify_output.txt` records the actual run and ends in `VERIFY_OK`.

The proof of the universal fiber bound rests on a choice of distinct partitions of the common radius-two ball size and a pigeonhole over at most \(p(n)\) possible global radius-one size partitions. It separately proves the elementary partition-number upper bound. Exhaustive checks through eight points do not certify any larger cardinality; the symbolic argument does.

The quoted source date is the documented first arXiv submission date. The scientific originality conclusion remains subject to external literature review, particularly combinatorial studies of prescribed multilevel tree-size profiles. No independent audit or external certification is asserted.
