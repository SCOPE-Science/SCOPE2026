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

Use Python 3 with no nonstandard dependencies. In the directory containing the extracted files, execute:

```text
python3 checker.py
```

Observed output:

```text
Cyclic one-dimensional checks passed for lengths 4..13.
4x4: 65536 states; entry populations [9, 65511, 16]; exact recurrent count 9.
4x5: 1048576 states; entry populations [15, 1048521, 40]; exact recurrent count 15.
All exact checks passed.
```

The test computes the original two-dimensional row and column integer fields for all \(2^{16}\) and \(2^{20}\) configurations respectively. On both boards it checks \(F^4(X)=F^2(X)\) for every \(X\), compares recurrence counts to \(1+C_H+C_W\), and witnesses a strictly two-update transient. It independently enumerates the length-4 through length-13 cyclic one-dimensional masks, checks \(T^3=T\), tests which masks are recurrent, and compares direct counts with both the transfer-matrix trace and Lucas closed form.

The checker only evaluates the equivalent zero-field predicate. Its equivalence to the original normalized rule throughout \(0\le\varepsilon<1/(9HW)\) is an exact integer inequality proved in RESULT.md, not a numerical test. Finite tests do not prove the all-length theorem. No independent scientific audit has been performed.
