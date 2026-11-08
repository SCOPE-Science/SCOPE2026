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
# Finite-state verification

Run `python3 verify_beta_graph.py` with Python 3 and no third-party dependencies. All binary16 numbers from encoding `0x0000` to `0x3bff` are enumerated (15,360 states). Each successor is computed with integer arithmetic after an explicit IEEE binary16 encoding and nearest-even round-to-nearest routine, and every state is assigned exactly one primitive cycle and its transient length. Every periodic edge, basin label, and distance-to-cycle recurrence is checked.

The exact manifest is:

- Post-remainder rounded map: `{1: 468, 3: 28, 8: 2480, 18: 187, 164: 12197}`; maximum transient `144`.
- Rounded-product map: `{1: 5705, 3: 26, 4: 3138, 24: 2013, 41: 4478}`; maximum transient `155`.
- Differing successor encodings: `512`.
- Independent NumPy binary16 evaluation: `0` differences versus the exact-integer successor algorithm, for each map, over all 15,360 inputs.

Both census totals equal 15,360. The verifier prints `BETA_HALF_EXACT_CENSUS_OK; states=15360; differing_successors=512` on success. Its successor-array digest is reported in `RESULT.md` and printed at run time, allowing independent replay without external databases. This exhaustively proves only the finite-domain proposition. Additional implementation platforms, stochastic rounding, arbitrary binary precision, and publication priority have not been independently verified.
