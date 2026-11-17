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
# Exact-rational verification

Run `python verify_star_median.py` with Python 3 and standard library only, from the directory containing this file. The program computes medians of rational inputs by sorting, measures the exact weighted edge variation of the two outputs, and checks both the stated sharp upper estimates and true attaining pairs. It exhaustively enumerates every center-ordering for up to six leaves under three positive weight profiles per size. It also checks 180 explicit weighted attaining pairs through 30 leaves and 5,100 arbitrary exact-rational two-input pairs.

The universal mathematical claim does **not** depend on exhaustiveness beyond six leaves. The analytical proof in RESULT.md handles all integer star orders and positive real edge weights. Finite checks independently catch parity errors, tie conventions, normalization errors, sign and endpoint mistakes, and unexpected failures in small star orders. No external formal certification or independent audit is asserted.
