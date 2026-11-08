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

Run `python3 verify.py` from this directory with Python 3.10 or later. The checker enumerates genuinely minimal eventual onset/period controllers over binary and ternary output alphabets and bases 2, 3, 4, 5, and 7. It independently constructs output-residual equivalence classes, compares valuations of nonnegative integers computed directly by divisibility with automaton outputs, and uses breadth-first search to find the shortest path with conflicting incoming digit labels. Observed result: `VERIFY_OK configurations=4094 digit_evaluations=237440`.

The finite test establishes neither correctness for unbounded parameters nor global novelty. These are addressed by the general state-minimization and path proof and by targeted comparison, respectively. No independent scientific audit has been performed.
