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

Run `c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` and `python3 verify_orbits.py` from the directory containing the files. Both tools were executed with their embedded source text and returned `PASS`. The first examines all 65,536 seeds. The second independently builds 384 cube symmetries, verifies the four minimal-seed orbits, checks the subcube-merging closure of all 2,517 seeds of size at most four, tests the geometric criteria, and evaluates each slow triple's thirteen possible fourth vertices. The external mathematical subcube-merging fact used by the second program is identified in the cited Riedl paper; the exhaustive first program does not require it.

The only verification channels represented here are ordinary computational reproduction and the documented self-review. No independent external audit or expert certification is claimed. The classification has no assertion beyond the finite four-cube setting.
