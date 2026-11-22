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

The all-length claim is established by the four-event algebra in `RESULT.md`: the involution \(\Theta_\delta\) preserves the exact rate of each allowed particle hop and each autonomous obstacle birth/death, and sends bond \(i\) to bond \(-i-1\). Irreducibility of each finite sector then gives complementary stationary laws. These arguments do not assume the observed current curve is parabolic.

Reproduce the independent finite diagnostic with `python check_duality.py` using only the Python standard library. Its exact-rational checks cover rings of lengths 2 through 7, all particle and obstacle configurations, both source and arrival obstacle placements, and three sets of strictly positive autonomous obstacle rates with zero, partial and absent hindrance.

Observed diagnostic: PASS; 87,360 involution/sector checks, 131,040 generator-row comparisons, and 1,055,832 labelled event comparisons. This finite verification does not establish any assertion for untested ring lengths; the symbolic event matching in the proof does.

Scientific boundaries: no assertion for occupancy-dependent obstacle binding, open systems with reservoirs, spatially nonuniform obstacle clocks, or arbitrary nondual starting conditions. The proof does not supply an explicit stationary distribution and does not constitute independent scientific validation.
