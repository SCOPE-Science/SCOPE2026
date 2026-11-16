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

# Reproducible finite verification

From this directory, execute `python3 corona_walsh_checker.py` using Python 3.9 or later with no third-party dependencies. Expected terminal output begins with `LEAF_CORONA_WALSH_EXACT_PASS` and reports `graphs= 75 graph_coefficients= 16932 signed_continuants= 131071`.

The checker constructs the independent-set indicator on the full binary group and calculates its Walsh transform with a fresh integer butterfly. For all 75 labelled graphs on at most four vertices, it compares each of 16,932 multipliers with a distinct residual-graph signed independence-sum implementation and checks sharpness of the vertex-cover gap. For path lengths one through eight, it independently tests every pendant-frequency fiber for the all-zero, all-nonzero or mixed-zero dichotomy, including the claimed uniform two-adic valuation where applicable. It exhaustively tests 131,071 sign sequences on path lengths zero through sixteen against the signed-continuant valuation and all-negative resonance statements.

No finite verification alone establishes the all-graph or all-length theorem. Those statements are supplied by the proof in RESULT.md. Neither a formal proof assistant nor an independent mathematical audit was used. The verification is reproducible from this package and requires no external data.
