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

Run `python3 checker.py` with standard Python 3 and no third-party packages. It enumerates formal quartic zero-frequency tensors for gaps \(2,3,4,5,6,7,10,19\); checks the exact dyadic value \(45/14\); exactly checks two deficits on \(728\) signed integer-amplitude profiles; checks the two ternary witnesses; and independently integrates eight fourth-moment examples on a normalized circle grid. Its accepted output ends with `ALL_LACUNARY_FOURTH_MOMENT_CHECKS_OK`.

The proof of the stated universal bounds does not depend on finite-grid experiments. The needed identities are mathematically established by Fourier orthogonality and the two algebraic nonnegative deficit decompositions in `RESULT.md`. For gaps at least four, the modular signed-frequency argument proves exhaustive nonresonance for every admissible integer gap, not just the gaps enumerated by the checker. All calculations use the stated normalization.

Independent audit has not been performed. No external certification of the result or of its originality is claimed.
