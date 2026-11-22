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

# Exact computational verification

Use `python verify.py` with `spectrum_n7.tsv` in the same directory (Python 3.9+; standard library only). The program terminates with `PASS` after 2,429 exact integer comparisons/assertions.

It independently enumerates all involutions by fixing/pairing the least unused label and all standard Young tableaux by successive addable cells, comparing complete descent-set histograms through order ten. A Walsh--Hadamard transform is checked against direct character sums through order seven. It checks the complete order-seven frequency table (64 integer entries), the four exceptional even zeros at masks `43,45,53,63`, the rank of 28, least surviving multiplier magnitude 8, linear independence of the exceptional frequencies, and the projection-kernel numerator histogram with absolute sum 144 and norm 9/4. It checks that the remaining orders through eight have norm-one Fourier projections.

The finite exhaustive claim follows from the completeness of the explicitly implemented recursions. The group-averaging proof that the Fourier projection globally minimizes endpoint norms is mathematical and recorded in `RESULT.md`; it is not inferred from finite numerical experiments. No independent external audit has been performed.
