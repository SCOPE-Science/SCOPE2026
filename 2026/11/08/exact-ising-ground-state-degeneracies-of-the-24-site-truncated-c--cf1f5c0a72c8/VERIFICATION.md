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

# Reproducible verification

Compile `scan2.cpp` using `g++ -O3 -std=c++17 scan2.cpp -o scan2`; run `./scan2 > /tmp/hist.csv`; the result must be byte-identical to the included `hist2.csv` after normalizing only the output path. All \(2^{24}=16777216\) spin assignments are counted by Gray-code updates of their plus population, disagreeing internal bonds and disagreeing external bonds. The 539 output rows together sum to \(16777216\).

Separately run `python3 verify_degeneracies.py`, which must print `VERIFIED EXACT DEGENERACIES`. This script counts \(2^{12}\) cube-edge orientations and recursively enumerates local sets of one, two, or zero chosen ports under the opposite-edge exclusion condition. It does not import or read the C++ histogram or any external data.

The two methods agree on the five total ground degeneracies and all coexistence magnetization counts. Evaluating the exact energy formula on histogram bins at strictly positive \((J,K)=(1,1),(1,3),(3,1),(1,7)\), at the two critical fields and within the open regions, reproduces the same values. The general phase-boundary theorem is previously known; the independent complete enumeration supports the particular truncated-cube count theorem. No infinite-system or quantum-physics assertion is verified.
