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

# Reproducible arithmetic verification

Run `python3 verify.py` with Python 3 and the standard library only. The code checks two complementary routes: (i) residue-field recurrences and all local polynomial roots, and (ii) the original rational recurrence in exact fractions, checked against the independent published square/gcd criterion. It does not download data or rely on floating-point tests for divisibility.

Actual test summary:

```
QUARTIC_OK primes_le_1000= 168 classes=2,5,1_9_13_17_mod20
VERIFY_OK primes= 168 stabilized_residues= 324753 joint_residues= 333461 exact_rational_tests= 720 strict_converse=yes
```

The stabilized full-period tests cover 22 values of \(h\), including \(h=442=2\cdot13\cdot17\), whose observed one-failure density is exactly \(51577/195364\). The general first-two joint period tests cover 12 values, including \(h=290=2\cdot5\cdot29\), with counts (neither, index 2 alone, index 3 alone, both) equal to \((52605,24399,5286,1810)\) among 84100 residue classes. The test also constructs an index-3 obstruction for each prime through 1000 in the forbidden classes.

Finite tests alone do **not** show that no later failure occurs or that the residue classification holds for every prime. Those unrestricted conclusions follow from the homogeneous two-step identity and the quadratic-residue proof in RESULT.md, conditional only on the explicitly cited published square/gcd criterion. This is self-review, not independent validation.
