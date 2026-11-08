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

# Verification and reproducibility

The two packaged programs operate only with exact arithmetic, standard C++17/Python3 and no external data. Run them in one directory as follows:

```sh
c++ -O2 -std=c++17 verify_f4_cubic_census.cpp -o cubic_census
./cubic_census candidate_masks.txt
python3 verify_f4_cubic_geometry.py candidate_masks.txt
```

The first enumerates 349525 normalized cubics, determines all rational zeros and gradients, all tangents and blocking tests. Its retained input point-set masks are generated locally, not supplied from elsewhere. Its output includes `rat-smooth 248928 rat-sing 100597 tangent 6328 blocking 6328 both 6328` and `F4_CUBIC_TANGENT_BLOCKING_CENSUS_PASS 349525 6328 280 6048`. The second independently enumerates line incidences, 1008 nonsingular conics, the resulting 6048 exterior line-conic products, 280 nine-point unitals and all 60480 projectivities, with `F4_CUBIC_INDEPENDENT_GEOMETRY_PASS 60480 1008 6048 280 6048`.

The C++ exhaustive mask count establishes both directions of the equivalence, and the Python geometric enumeration proves two complete projective orbits and stabilizer values. These are finite exhaustive computations only. Neither code execution nor self-review constitutes an independent outside mathematical audit; that audit remains not performed.
