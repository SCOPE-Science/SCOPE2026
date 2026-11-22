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

# Verification procedure and scope

Run `python3 verify.py` using Python 3 with only the standard library. The program enumerates all reflexive transitive relations on carriers of orders one, two and three, all binary accessibility relations, all upward-closed valuations of two atoms, and every pointed evaluation of the two sides of the announcement-necessity reduction. It compares the directly evaluated instance against the first-order criterion without deriving either side from the other.

The expected output begins with `VERIFY_OK` and includes `all_preorders=[(1, 1, 2, 2), (2, 4, 64, 56), (3, 29, 14848, 9571)]`, where each tuple is (carrier order, preorder count, frame count, valid frame count), and `chain_counts=[(2, 12, 1), (3, 224, 26), (4, 14592, 1215)]`, where each tuple is (chain order, valid relations, valid relations failing ordinary forward confluence).

Both explicit two-world examples are separately checked. The symbolic proof in `RESULT.md` proves the theorem on arbitrary cardinalities; the finite checker gives no independent certification of the unbounded claim. Independent audit has not been performed.
