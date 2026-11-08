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

# Finite certificate verification

The included `certificate.json` is interpreted by `verify_certificate.py`, which reconstructs all 96 GC-balanced words, 44 permitted two-word reverse-complement orbits, the exact 344-edge conflict graph, a fourteen-clique rational upper-bound certificate, the explicit fourteen-word witness, all twenty maxima, and their four symmetry classes. The upper bound is the mathematical inequality described in `RESULT.md`, not merely a computation log.

Run:

```
python3 verify_certificate.py
c++ -O2 -std=c++17 independent_census.cpp -o census
./census
```

The C++ program independently derives shadow sets from base-four encodings and exhaustively counts compatible orbit selections of sizes seven and eight. Its output is `DIRECT_CENSUS_OK`. Both source programs and the exact finite data are present and require no remote services, third-party Python libraries or precomputed executable.

**Limits.** These checks verify a finite exact classification of four-letter DNA codes. They do not prove general statements at other lengths or independently establish historical priority. Independent scientific audit has not been performed.
