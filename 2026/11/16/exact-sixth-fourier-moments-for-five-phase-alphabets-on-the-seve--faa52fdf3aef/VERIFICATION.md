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

Run `python3 checker.py` in the extracted artifact directory, using only Python 3 standard library. Success marker: `HEXAGON_SEVEN_L6_ALPHABETS_PASS`.

The checker constructs cubic Fourier coefficient fibers directly from 343 ordered triples and also builds the moment Laurent polynomial independently from unordered multinomial triples. It checks their agreement for all \(2274\) normalized exponent tuples over cyclotomic rings, and then checks the complete minimum, next-value, maximum and optimizer count tables. The exact five-phase comparison orders elements \(A+B(\sqrt5-1)/2\) by integer sign and squared-integer comparisons, so no numerical tolerance enters any claimed minimum. Expected normalized minimizer counts are \(3,6,3,6,3\), and the raw coefficient counts are \(24,162,192,750,648\). The all-one moment is \(5881\).

The analytic proof supplies Fourier orthogonality, the bijective three-coefficient phase gauge, and the no-aliasing transfer on rectangular grids of side lengths at least seven. The finite exhaustive certificate proves no statement about arbitrary coefficient phases, other alphabets, or other apertures. No separate external mathematical validation has been performed.
