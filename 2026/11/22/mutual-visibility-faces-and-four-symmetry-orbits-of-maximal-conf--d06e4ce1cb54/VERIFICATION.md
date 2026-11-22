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

The standalone `verify.py` uses only the Python 3 standard library and no network or external input. Run `python3 verify.py`. The same exact source was executed successfully with all assertions enabled. Expected terminal markers: `FANO_GEODESIC_CRITERION_OK`, `FACES [1, 14, 91, 322, 651, 728, 392, 58] TOTAL 2257`, `FACETS {6: 70, 7: 58}`, `AUTOMORPHISMS 336`, `VERIFY_OK`.

The program first builds the 14-vertex Fano incidence graph and all breadth-first-search distances, enumerates all shortest-path internal-vertex masks, and compares this graph-level definition against a separately implemented incidence-geometric predicate for every one of the \(16384\) vertex subsets. It counts every admissible size, tests every unselected single-bit extension for maximality, builds all 168 point collineations from seven-factorial candidate permutations, constructs a valid polarity to obtain 336 automorphisms, and verifies all four maximal-set orbits.

No statistical sampling or extrapolation is involved. The result concerns this single specified 14-vertex graph; the certificate does not imply analogous formulas for other projective planes. These are finite integer calculations and program-level assertions, not an independent mathematical audit. The proof explaining why the certificate tests the correct mathematical definition appears in `RESULT.md`.
