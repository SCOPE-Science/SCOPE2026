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

# Reproducibility

The result concerns all \(2^{20}=1048576\) subsets, without sampling. C++17 with an ordinary standard-library compiler is sufficient. No external graph package is required.

```
g++ -O3 -std=c++17 verify_bitsets.cpp -o verify_bitsets
./verify_bitsets replay.txt
cmp replay.txt min_masks.txt
g++ -O3 -std=c++17 verify_gray.cpp -o verify_gray
./verify_gray
python3 verify_orbits.py
```

Both executables print `8:720 10:960 12:720`. The first then prints `BITSET_EXHAUSTIVE_OK`; the second prints `GRAY_EXHAUSTIVE_OK`. The Python program prints `ORBIT_CERTIFICATE_OK orbits [240, 240, 240] selected-edge counts [4, 5, 6]`.

The two complete enumerators use independent graph presentations and signature-construction algorithms: the 2/3-subset inclusion graph with population counts, and the generalized Petersen \(GP(10,3)\) graph with Gray-code histogram updates. The first generates the exact explicit list of 720 size-eight masks, and the group-action verifier checks the list and all three orbits. Unreplayed graph families are not claimed. The files do not represent independent mathematical validation or external certification.
