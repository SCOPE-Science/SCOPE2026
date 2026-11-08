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
# Reproducible finite checks

Using standard Python 3, execute `python3 verify_graph.py` and `python3 verify_formula.py` in the same directory. The first program constructs the exact channel balls, then compares all ordered source pairs through length 9 and verifies the degree law against each vertex. The second program uses a separate composition-counter routine to reproduce every degree polynomial coefficient through length 18 and independently enumerates derivatives. Both programs were executed successfully on the packaged source before delivery and again from extracted package paths.

The all-length theorem relies on the combinatorial proof in RESULT.md, not on extrapolation from any finite list of checks. The only cited external work is scientific literature; no external mathematical certification has been performed.
