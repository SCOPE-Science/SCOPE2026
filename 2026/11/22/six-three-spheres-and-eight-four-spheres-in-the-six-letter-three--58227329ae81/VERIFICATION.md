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

# Reproducibility and limits

The files `checker.py` and `morse_pairs.json` are a self-contained exact-arithmetic proof certificate. Run them together using `python checker.py`; no third-party Python packages are required.

The checker regenerates every three-cycle on six symbols, all distinct ordered subsequences, all incidences and all signs, and then checks the pairing certificate against the freshly built cells. It checks every cellular boundary-square identity, the uniqueness and unit incidence of all \(311\) pairs, a complete \(637\)-vertex topological sorting of the reversed Hasse graph, and the vanishing of all \(48\) Morse boundary entries from degree four to degree three.

Successful replay reports:

```
PASS: 40 three-cycles; f-vector (6,30,120,247,194,40)
PASS: full signed cellular boundary squares to zero
PASS: 311 distinct unit-incidence matches; 637-cell matching DAG acyclic
PASS: critical cells 1 in degree 0, 6 in degree 3, 8 in degree 4
PASS: all 48 signed integer Morse boundary coefficients are zero
CONCLUSION: X_6 is homotopy equivalent to 6 S^3 wedge 8 S^4
```

The last line invokes the mathematical discrete Morse and Hurewicz arguments in `RESULT.md`, not an additional automated test. The finite certificate is complete for this \(637\)-cell complex, not for other alphabet sizes. Independent mathematical review has not been performed.
