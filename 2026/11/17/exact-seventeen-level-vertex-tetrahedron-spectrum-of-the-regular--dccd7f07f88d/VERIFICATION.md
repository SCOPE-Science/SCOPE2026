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

The result is reproducible using the accompanying `verify.py` and `SPECTRUM.csv`. Execute `python3 verify.py` in their common directory. It independently enumerates all 10,626 unordered vertex quadruples using exact integer determinants; re-enumerates the 265 orbits under the 48 signed-coordinate symmetries; verifies the two maximal and one runner-up orbit signatures using squared edge lengths; checks every row and representative in `SPECTRUM.csv`; and independently enumerates the same quadruples in the four-dimensional permutation representation using exact Gram determinants and integer square roots.

Expected output: `TRUNCATED_OCTAHEDRON_TETRAHEDRAL_SPECTRUM_PASS quadruples=10626 levels=17 octahedral_orbits=265 max_orbits=6+24 second_orbit=24`.

The computation is exhaustive over a known finite set, not probabilistic sampling. The correctness of code and of the elementary geometric identification of the vertex set are subject to normal independent mathematical scrutiny. The previous maximum-volume theorem is acknowledged rather than recertified here; the new result concerns the complete distribution and its distinct maximal and runner-up configurations.
