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

# Reproducible verification

Run `python3 verify_quartic.py` in a directory containing this file and `verify_quartic.py`. Only the Python standard library is required. The script performs exact integer and rational arithmetic; it does not use floating-point root finding to decide norm equality.

The checks cover all parity nodes for dimensions from four through 301, compare the combinatorial Walsh sum with the quartic polynomial, compare the exact projection-norm differences with the weighted sign-change identity, and compare zero differences with the exact arithmetic test. Next, the two Pell seed orbits are enumerated up to \(N\le10^{100}\) and both candidate squared roots are checked using integer square roots. Only the plateau at \(n=7\) survives this finite check.

The proof of the increment formula and the \(O(\log X)\) candidate bound is analytical and does not depend on finite enumeration. The finite test does not rule out further plateaus above the cutoff. Independent mathematical audit has not been performed.
