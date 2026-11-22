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

# Verification details

The finite certificate checks **all** 531441 labelled initial colorings on the explicit 12-vertex Chvátal graph. Run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`, and separately run `python verify.py` with NumPy installed. Each implementation constructs two successor functions using only the explicit graph edge list and the two stated local rules. The C++ implementation uses indegree peeling and reverse propagation on functional graphs; the Python implementation compares actual consecutive iterates and searches all entries 0–12 and periods 1–12. Both give zero disagreements in paired eventual least periods, the same attractor counts, and the sharp entry clocks 8 and 10. `JOINT_CENSUS.csv` includes all 165 nonempty entry-period pairs (CCA entry, CCA period, GHM entry, GHM period) with frequencies summing to 531441.

The finite proof does not establish anything about larger graph families or historical priority. No independent external mathematical check has been performed.
