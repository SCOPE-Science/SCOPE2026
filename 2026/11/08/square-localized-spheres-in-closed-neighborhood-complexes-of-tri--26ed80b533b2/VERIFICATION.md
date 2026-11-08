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
# Reproducible verification and limits

Run `python3 verify.py` using Python 3.10 or newer. The file has no external dependencies. Its deterministic output is in `verify_output.txt`.

The program enumerates every connected labeled simple graph on three through six vertices meeting the triangle-free and pairwise edge-disjoint-four-cycle hypotheses; for each it reconstructs all simplices from closed neighborhoods. It then checks that every proposed pair is a genuine elementary free-face collapse at its removal, checks that the exact remainder is the union of the graph and tetrahedral boundaries of all squares, and independently computes mod-two boundary ranks on the remainder. Counts: 3,195 qualifying connected graphs, including 1,323 with at least one four-cycle. It additionally checks 83 qualifying connected random graphs of orders seven through nine and two explicit noncactus two-square graphs. Output ends in `ALL_VERIFY_OK`.

The unrestricted claims for all finite graph orders, the integer homotopy splitting, integral torsion-freeness, natural homology representations and free fundamental group are established by the proof in `RESULT.md`; finite binary computations alone would not establish them. No independent external audit has been performed.
