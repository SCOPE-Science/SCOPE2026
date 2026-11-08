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

# Exact finite verification

Run `python3 verify.py` beside the bundled `atlas.tsv`. Standard-library-only code reads the graph atlas source encoding; 1,253 atlas graphs have the expected order counts, and all 32,191 connected graph/three-terminal instances with at least two missing edges have coefficientwise-optimal interventions. The eight-vertex nine-edge example has 19 missing links; direct, independent breadth-first enumeration on 32 survivor subsets confirms the two winner vectors and unique interior switch. All comparisons are exact integers.

The code does not prove the external published atlas is complete up to seven vertices, nor independence of scientific validation, nor the absence of prior stronger published theorems. Results concern exactly the model in RESULT.md; an independent audit has not been performed.
