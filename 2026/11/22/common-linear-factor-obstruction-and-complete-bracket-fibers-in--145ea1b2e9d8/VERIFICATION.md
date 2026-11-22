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
# Computational verification

Run `python3 verification/bracket_fibers.py` with Python 3 and NumPy installed. The script directly enumerates all 65,536 ordered pairs in the eight-dimensional algebra over the binary field and checks every one of its 64 possible derived-target fibers against the proved formula, including zero multiplicities. For the ternary field, it computes an independent rank-consistency count over all 6,561 first arguments for 20 specified targets, instead of enumerating all 43,046,721 ordered pairs. The recorded output is in `verification/bracket_fibers_output.txt`.

The tested finite fields do not constitute an exhaustive proof for all prime powers. The algebraic determinant and common-factor arguments in RESULT.md establish the universal theorem. No external independent audit has been performed.
