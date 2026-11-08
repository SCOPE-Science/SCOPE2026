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

# Reproduction and limits

Execute `python check_tree_mahler.py` after installing the packages named in `requirements.txt`. The script uses exact integers for all claims of finite extremality. Every Prüfer sequence of lengths zero through five, over vertex sets of size two through seven, is visited once; the resulting 18,248 labeled trees are reduced to all 24 tree isomorphism classes across those six sizes. Two subset recurrences independently evaluate matching counts and linear extensions, and output the winner at each size. It checks the 11 exact seven-vertex entries and the strict difference between the spider and the path.

Four separate primal/polar hull calculations are performed in double precision by SciPy's Qhull interface, with a stated relative tolerance of one part in a million. They are numerical corroboration only. The general product formula is instead established by the published primal forest identity and a direct polar order-polytope derivation; this derivation is given in `RESULT.md`. The finite census is exhaustive only through seven vertices. No independent mathematical audit has been carried out.
