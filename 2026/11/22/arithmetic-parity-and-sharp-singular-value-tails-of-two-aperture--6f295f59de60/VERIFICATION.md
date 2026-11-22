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

# Verification of the two-aperture spectral coefficient

The proof in `RESULT.md` is analytic. It uses Fourier diagonalization, an elementary threshold-counting lemma, irrational rotation equidistribution, exact rational cosine sums, a one-dimensional integral at \(b=2a\), and monotone inversion of the counting law. Numerical tests are auxiliary and are not an infinite-dimensional proof.

## Reproduction

Run `python check.py` with the Python standard library. The checker completed **18,153** finite assertions. Tests compare exact Fourier-integral expressions to the factored multiplier for 150 frequencies in each of six admissible configurations; enumerate rational denominator cosine-sum identities and numerator permutation invariance; verify zero residues and strict rational-parity comparisons; and test six long frequency averages and three thresholds per configuration.

The printed reference values are:

- Rational half-circle shift, \(q=2\): \(0.405284734569\ldots\).
- Rational third-circle shift, \(q=3\): \(0.540379646092\ldots\).
- Dependent irrational shift \(b=2a\): \(0.494022401288\ldots\).
- Rationally independent shift: \(0.516024550931\ldots\).

## Mathematical scope of verification

The finite computations do not prove Weyl equidistribution, the continuity of limiting distributions, or the threshold-counting limit; these are established in the proof. The check does not cover all irrational displacements, arbitrary unequal apertures, phase-weighted apertures or the statistical reconstruction problem. The nonzero Fourier zero-set is already covered by a more general two-interval Fourier-zero theorem; the present spectral statement concerns the reordered singular-value tail and its arithmetic coefficient.
