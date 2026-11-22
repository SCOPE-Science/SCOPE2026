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

# Verification and scope

The theorem is verified analytically in the `RESULT.md` proof. The critical assertions are: (i) the support of a convex hull is the maximum of the supports; (ii) the two-max scalar expression has its minimum at one of two endpoints; (iii) the odd-polygon opposite supports satisfy a product inequality; (iv) the resulting two angular endpoint functions are decreasing; and (v) all equality cases are accounted for. The symbolic square–pentagon width uses the standard exact trigonometric identity for \(\cos(\pi/10)\).

`check.py` uses no external libraries. Run `python3 check.py` from the directory containing the extracted package. It checks the predicted normal directly against all square and polygon vertices, tests 4,000 pseudorandom directions per polygon order for \(3\le q\le30\), and checks the square–pentagon radical. This computation was executed successfully. The program does not establish uniqueness of minimizers or global inequalities over a continuum and is not a substitute for the proof.

The date attached to the motivating article is the original arXiv submission date (6 November 2026); no later revision has been used as the first public date. Only the family of unit-circumradius regular orthogonal polygon joins is claimed. Scientific priority is provisional and no independent audit has been performed.
