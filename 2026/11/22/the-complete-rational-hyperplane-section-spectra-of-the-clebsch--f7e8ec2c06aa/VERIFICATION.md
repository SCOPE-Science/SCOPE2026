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

# Verification details

- Execute `python3 verification/clebsch_section_census.py` in an environment with Python 3 and its standard library only.
- The program must print `CLEBSCH_SECTION_CENSUS_OK`. It recomputes all surface points and hyperplanes, compares cubic and independent quadratic point generators, checks exact first and second incidence moments, and exhaustively enumerates every contained rational line.
- It checks that the maximizers are exactly the ten explicit planes obtained from coordinate pairs, verifies the evaluation code dimensions and full ordinary Hamming weights, and computes the complete \(S_5\) orbit partition.
- `data/clebsch_section_orbits.json` holds all 43 coefficient-normalized orbit representatives and their cardinalities and section sizes. These are auxiliary finite witnesses, not a substitute for rerunning the exact loops.
- Full finite computations at \(q=7\) and \(q=11\) do establish these finite classifications; they make no assertion about any other field or arithmetic model. The parent historical-priority comparison is literature-limited, and independent mathematical audit has not been performed.
