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
# Reproduction and limits

Run `python3 check_rank2.py` from this directory with Python 3.9 or newer. The program uses standard-library exact integer modular arithmetic, binary Walsh transforms, and a separate ternary character-count procedure. Its final output is `RANK_TWO_BALL_ALL_EXACT_CHECKS_PASS`.

The direct calculations cover all Fourier values on three binary matrix spaces, canonical Fourier representatives on one ternary matrix space, and a broad range of rank-shell arithmetic checks. In particular, the program verifies the binary square two-shell transition in the integer formulas, without exhaustively enumerating all binary matrices at large dimensions. Only the written argument proves the universal finite-field theorem. Independent audit has not been performed.
