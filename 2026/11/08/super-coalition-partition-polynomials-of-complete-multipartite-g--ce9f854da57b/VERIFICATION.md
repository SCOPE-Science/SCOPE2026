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

# Reproducibility
Run `python3 verify.py` with Python 3 and standard library only. The program builds all edges of a labelled complete multipartite graph; for each vertex subset it independently checks the exact neighborhood-based super domination definition, and for each unordered set partition it independently checks every coalition-pair condition. The directly counted polynomial is compared to the closed formulas for all connected part-size profiles of orders seven and eight and three additional nine-vertex profiles. It also checks an excluded six-vertex boundary profile and a separate eight-vertex example. Expected final line: `VERIFY_OK 38`.

The finite program is not an infinite proof. The proof in RESULT.md supplies the unrestricted parameter argument. Historical priority is not independently certified.
