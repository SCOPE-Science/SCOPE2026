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

# Reproducible mathematical checks

Run `python verify.py` in the directory containing this file and `verify.py` using Python 3 with no packages. The script constructs all 877 restricted-growth strings of length seven, rejects 52 with equal short codewords, and tests all 825 remaining cases by a suffix-cancellation implementation of the Sardinas–Patterson algorithm. It verifies the two stated structural families exactly, counts 10 ambiguous equality types, checks each explicit length-five witness, and independently checks every literal codebook for alphabet sizes 2–5. Expected end marker: `VERIFY_OK`.

The restricted-growth enumeration is complete for every possible alphabet size because unique decipherability and the structural prediction depend only on equality of symbols at seven positions. Full alphabet enumeration for 2–5 is auxiliary. The result is not a theorem about any other three-word length profile; no independent mathematical validation is asserted.
