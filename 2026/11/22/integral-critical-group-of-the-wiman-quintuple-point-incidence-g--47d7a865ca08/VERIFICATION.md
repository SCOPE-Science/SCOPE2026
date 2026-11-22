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

# Exact reproducibility

Run `python3 wiman_quintuple_critical_verify.py` with Python 3.8 or later; no external packages are required. Expected first line: `WIMAN_QUINTUPLE_LEVI_CRITICAL_GROUP_OK`.

The script constructs \(A_6\) as all \(360\) even permutations on six letters, enumerates its \(45\) involutions and \(36\) cyclic subgroups of order five, and compares two independent normalizer tests for every one of the \(1620\) possible incidences. It checks degrees, Gram-matrix entries, connectedness, an annihilating polynomial and traces, then processes the reduced graph Laplacian at two different sinks using exact modular Smith elimination.

A unit pivot over \(\mathbb Z/p^E\mathbb Z\) permits invertible row and column clearing. When no unit remains, every residual entry is divisible by \(p\); division records one valuation level. The precision chosen is \(E=v_p(\tau)+1\), so no nonzero invariant factor can disappear through modular truncation. The resulting prime-local exponent sums match the tree number obtained independently from the Gram spectrum.

This check covers the exact finite group and integer matrices. The identification with the Wiman configuration additionally relies on the quoted classical reflection arrangement and stabilizer descriptions, as explained in `RESULT.md`. No independent audit is claimed.
