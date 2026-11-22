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

# Reproducible finite verification

The two standalone Python 3 standard-library scripts and the JSON table are packaged alongside this file. Extract them together and run:

```
python3 verify_weyl_chambers.py
python3 verify_orbit_union.py
```

The first program constructs all 27 line classes in the integer blow-up lattice, verifies the six E6 simple reflections act on those classes, computes the group order 51840, partitions it into precisely 25 conjugacy classes, enumerates all pairwise-skew subsets (2764), and compares every computed table row and Weyl class size with `e6_spectra.json`. The exact success marker is `W_E6_CHAMBER_CYCLE_TABLE_VERIFIED_OK`.

The second independently counts supports fixed under every positive power of every representative by enumerating unions of cycles of line orbits compatible with disjointness. It confirms each count agrees with the candidate cycle profile and that the Burnside total is 414720=8*51840. Its success marker is `W_E6_ORBIT_UNION_INDEPENDENT_CHECK_OK`.

These computations exhaust finite permutations and finite supports, rather than using statistical samples. The conclusion for any finite-field smooth cubic surface uses classical geometric classification of exceptional curves and the nef-Zariski support correspondence; these geometric premises are proved or cited in `RESULT.md`. An earlier published equivalent arithmetic table could have escaped indexing and is a remaining historical-priority risk. Independent external validation is not part of this package.
