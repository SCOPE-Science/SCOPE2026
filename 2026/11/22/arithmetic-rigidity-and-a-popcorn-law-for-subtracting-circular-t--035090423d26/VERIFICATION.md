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

# Verification record

The proof is analytic and self-contained beyond standard Fourier positive-type, Vandermonde invertibility, continuous circle characters, and trigonometric polynomial density. It is located in `RESULT.md`; this record only documents supplementary computations.

Run `python checks/check_tent.py` with Python 3, NumPy, SymPy, and mpmath installed. The checker directly evaluates the exact rational Fourier coefficient formula for all primitive radius fractions sampled with denominators \(5\le Q\le33\), tests sharp-frequency negativity just above the calculated thresholds, constructs four explicit rational-grid null vectors, verifies the odd-denominator exact closed form through denominator 69, and checks a ten-thousand-frequency irrational example plus a finite generic nonresonant probe. An exact SymPy simplification verifies the five-fold algebraic identity. The observed output was:

```
PASS: 84177 supplementary checks; rational, irrational, exact and finite-grid cases.
order-two irrational threshold: 0.207106781186547524
rational q=5 threshold: 3/4 - sqrt(5)/4
```

Critical infinite checks are **proved in the mathematics rather than certified by the finite script**. In particular, a finite scan cannot rule out untested frequencies for an irrational width, verify density of admissible widths, establish the all-sample positive-type equivalence, or prove absence of exotic character homomorphisms. The checker is supplementary and subject to numerical rounding, although the defining exact rational and algebraic formulas are derived symbolically in the proof.

The complete mathematical scope is \(0<b<a\le\pi\), \(\lambda\ge0\), exact angular circle distances, and arbitrarily large finite Gram matrices. Neither general smooth tapers nor finite-grid-only admissibility is addressed. The bibliographic originality comparison is provisional until independent expert review; no independent mathematical audit has been performed.
