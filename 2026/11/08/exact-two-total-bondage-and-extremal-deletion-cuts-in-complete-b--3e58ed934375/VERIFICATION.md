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
# Verification and boundaries

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses no third-party packages and directly constructs each surviving bipartite adjacency relation. Its acceptance predicate enumerates all vertex subsets of cardinality two or three and checks open-neighborhood total coverage, separately rejecting isolated vertices. It does not assume the structural classification when testing an edge cut.

Exhaustive edge-subset tests cover \((a,b)=(2,2),\dots,(2,6)\), \((3,3),\dots,(3,8)\), and \((4,4),(4,5),(4,6)\); they verify that no smaller cut exists and count every optimal deletion subset. Additional small pair-cover checks and explicit construction tests strengthen cross-checking. These computations are finite corroboration, not proofs for unbounded graph orders. The unrestricted result is established by the missing-neighbor pair-cover lemma, two explicit construction families, and the equality-case intersection classification in `RESULT.md`.

The independent mathematical audit has not been performed. Historical priority is provisional because a relevant journal article's full text was not available; the complete lawful arXiv preprint was inspected.
