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

## Reproduction
Compile and run `verification/enumerate_codes.cpp` using `c++ -O3 -std=c++17 verification/enumerate_codes.cpp -o codes && ./codes` from the package root. Each comma-separated line reports alphabet size, subset size, number of identifying subsets and a first-witness bit mask. The observed first three fields, in order, were `(3,2,0)`, `(3,3,0)`, `(3,4,9)`, `(4,3,0)`, `(4,4,168)`, `(5,4,0)`, `(5,5,24)`, `(6,5,0)`, `(6,6,0)`, `(6,7,4320)`.

Run `python verification/orbit_check.py` from the package root. All \(20\) relabeling-orbit representatives were checked, and their orbit unions reproduced the exhaustive totals. Run `python verification/crosscheck.py` with SciPy and NumPy installed for a second, independently formulated hitting-set MILP confirmation of all four minimum sizes; all four solved to proven optimality.

## Boundaries
The exhaustive argument covers exactly the tested finite vertex and code-set universes. The MILP and the orbit verifier are independent corroborations, not substitutes for complete subset enumeration. No assertion is made for larger alphabets. Independent mathematical audit has not been performed.
