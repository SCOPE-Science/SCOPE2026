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

Both programs are standard-library Python 3 scripts and terminate without any external data. Place `verify_direct.py`, `verify_formula.py`, and their accompanying captured JSON output files in one directory. Execute `python3 verify_direct.py` and `python3 verify_formula.py`; each writes a single deterministically sorted JSON object with `"status":"PASS"` on success. Their captured outputs are `verify_direct_output.json` and `verify_formula_output.json`.

`verify_direct.py` separately implements the graph adjacency, literal two-update synchronous dynamics, and phase-interval enumeration on ten small split graphs. It checks 3,178,320 bounded configurations and compares full mass histograms. The box \(0\le x_v<2d_v\) is mathematically exhaustive for initially primitive-two states because of the local phase constraints proved in the result. `verify_formula.py` constructs the full exact polynomial and independently evaluates the proposed sharp interval, reciprocal coefficients, endpoint formula, total count and evenness for 132 pairs. Its additional \(b=1\) computations check an algebraic boundary case but are not claimed as new results. All integer operations are exact.

The infinite-dimensional claims and parameter quantifiers are justified by the proof, not by testing. The checks neither certify publication priority nor constitute an independent audit. The full text of the historical Bitar–Goles paper could not be consulted.
