---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproduction

Compile and run `verification/enumerate_codes.cpp` using `c++ -O3 -std=c++17 verification/enumerate_codes.cpp -o codes && ./codes` from the package root. Each comma-separated line reports alphabet size, subset size, number of identifying subsets and a first-witness bit mask. For the claimed alphabet sizes the observed first three fields were `(4,3,0)`, `(4,4,168)`, `(5,4,0)`, `(5,5,24)`, `(6,5,0)`, `(6,6,0)`, `(6,7,4320)`. The last empty layer for each alphabet size suffices to exclude all smaller sizes by monotonicity.

Run `python3 verification/orbit_check.py` from the package root. The 17 representatives for the claimed alphabet sizes have disjoint orbits for each fixed size, and their orbit unions reproduce the corresponding exhaustive totals. Run `python3 verification/crosscheck.py` with SciPy and NumPy installed for an independently formulated hitting-set MILP corroboration of the minimum sizes. The original package also checks and tabulates the three-symbol comparison case, outside the finding.

## Boundaries

The exhaustive argument covers the stated finite candidate layers for \(q=4,5,6\). The MILP and orbit verifier corroborate the minima and orbit data, respectively; neither replaces complete subset enumeration. No assertion is made for larger alphabets or orbits of the full graph automorphism group.
