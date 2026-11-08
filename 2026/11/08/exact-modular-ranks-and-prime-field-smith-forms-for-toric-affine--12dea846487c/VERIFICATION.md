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

# Verification of arithmetic line tomography

The supporting checker is `toric_radon_checker.py`. From the extracted package, run:

```bash
python toric_radon_checker.py
```

Expected final output is `TORIC_RADON_SMITH_AND_JACOBI_PASS 7_fields=checked`.

The checker reconstructs the incidence matrices over \(\mathbb F_q\) for \(q\in\{3,4,5,7,8,9,11\}\), performs exact modular rank elimination and tests the complete complex singular spectrum. It uses exact integer matrix arithmetic for the polynomial reconstruction relation over \(q\in\{3,4,5,7\}\), and independent exact Smith-form calculations for prime fields \(p\in\{3,5,7\}\). The numerical singular-value comparisons employ standard floating point and do not certify exact algebraic identities. The defining-characteristic rank and prime-field Smith formula for all parameters are established by symbolic character sums, Lucas's theorem, and invariant-factor counting in `RESULT.md`.

The checker depends on Python 3, NumPy and SymPy. Its input is constructed in the code, with no unavailable datasets or downloads. This is computational corroboration and self-review only; independent mathematical validation has not been performed.
