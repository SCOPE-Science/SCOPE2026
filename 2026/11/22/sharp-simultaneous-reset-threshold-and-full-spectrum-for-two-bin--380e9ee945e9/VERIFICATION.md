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

# Verification of the simultaneous-reset spectrum

The exhaustive domain consists of all \(3^6=729\) component transition tables, yielding \(729^2=531441\) ordered pairs, of which exactly \(549^2=301401\) have both components synchronizing. The two standalone sources use different proof-oriented calculations:

- `check_words.py` directly evaluates each starting state under all length-one through length-six binary words, tests product reset by bitset intersection, independently verifies individual synchronizability using a reachability closure of nonempty subsets, and counts extremal symmetry orbits.
- `census.cpp` independently constructs all nonempty subset transition maps and performs a breadth-first shortest-path search in their Cartesian product, computing all component and product reset thresholds.

Run:

```sh
python3 check_words.py
g++ -O3 -std=c++17 census.cpp -o census
./census
```

The expected text outputs are included as `check_words.out` and `census.out`. The full product spectrum is \(13041,154008,87552,37872,7488,1440\) at exact reset lengths one through six. The Python checker asserts all six totals, total pair coverage, absence of longer synchronized-product thresholds, individual reachability consistency, eleven symmetry orbits, and the explicit six-letter witness. Every asserted finite statement is decidable from the listed source files. The mathematical coverage justification and a hand-checkable witness are included in `RESULT.md`.

Limits: finite exhaustive verification proves the stated finite classification, not a bound for different component state sizes, alphabets, or more factors. No other independent review is claimed.
