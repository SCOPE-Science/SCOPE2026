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
# Verification

Run `python verification/check_600cell.py` with `verification/SPECTRUM.csv` present. The checker uses exact arithmetic in the quadratic integer ring and no nonstandard Python libraries. It verifies the 120-vertex normalization, every one of 273,819 anchored tetrahedral Gram determinants, an independent Cauchy--Binet calculation for every one, all 164 rows of the frequency table, the two largest values and all 600 maximum four-cliques, their edges and face incidences. Output from the completed local replay:

`600CELL_TETRA_EXACT_PASS vertices=120 anchored_triples=273819 levels=164 total_subsets=8214570 maxima=600 golden_K4=600 max_det=(160,256) next_det=(160,240) all_Cauchy_Binet=PASS`

The analytical reduction from arbitrary contained tetrahedra to vertex-supported ones is established in the proof. Finite exact enumeration is sufficient to determine this finite vertex-set spectrum, not a numerical extrapolation.
