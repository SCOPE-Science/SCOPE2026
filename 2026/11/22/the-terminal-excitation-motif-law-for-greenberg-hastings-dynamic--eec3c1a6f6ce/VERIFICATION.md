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

The executable file `verify_fan.py` uses only the Python 3 standard library. From the directory containing the delivered files, run:

```sh
python3 verify_fan.py
```

The resulting terminal output is provided verbatim in `verify_fan_output.txt`. The script checks the actual three-state synchronous fan update and compares each initial configuration's first-rest time to its independent initial-word motif count for every rim length from one to ten, a total of 265716 configurations. Every state is at rest within five updates in those finite tests. A separate seven-site local-window exhaustive check covers 13122 possible window/hub-history combinations, with no centrally excited site at time three. An independent suffix automaton computes exact word counts containing zero, one, or at least two patterns for lengths zero through 65, and the at-least-two coefficients agree with the claimed rational generating function's polynomial recurrence in every case.

These tests are finite corroboration. The mathematical reasons for the all-length assertion are the rim-exclusion lemma, the exact two-step motif equivalence, the legal overlap classification, and the marker/cluster generating-function identity in `RESULT.md`. An independent mathematical audit has not been performed.
