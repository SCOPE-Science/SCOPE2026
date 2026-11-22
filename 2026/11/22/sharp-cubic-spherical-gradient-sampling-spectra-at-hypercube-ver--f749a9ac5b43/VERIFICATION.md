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

# Reproducibility of cubic spherical-gradient sampling identities

The complete proof for every integer \(d\ge3\) appears in `RESULT.md`. It relies on the finite-dimensional signed-permutation decomposition, the exact spherical even-monomial moment formula, and exact vertex signs. It does **not** infer a uniform theorem from a finite test.

## Standalone checker

With Python 3 installed, execute `python3 check_cubic_gradient.py` in the extracted artifact directory. No third-party dependencies, network calls, numeric tolerances, external test data or random seeds are required.

The checker builds each independent cubic harmonic basis element and its Cartesian derivatives. It obtains normalized sphere moments from double factorials and signed-cube moments from even-exponent parity, then forms each spherical Gram entry and each sampled-tangent-gradient Gram entry exactly as `fractions.Fraction`. It checks the three eigenvalue identities, all cross-block identities, the dimension counts, the trace identity and the condition-number formulas for dimensions \(3\) through \(7\). This is a full pairwise check of the entire finite matrices for each tested dimension, not a sample of rows.

Observed output: PASS for dimensions \(3,4,5,6,7\); harmonic dimensions \(7,16,30,50,77\) respectively. The \(d=3\) kernel has dimension one; cases \(d=4,5,6,7\) are full rank. The all-dimensional ordering including the crossover at \(d=9\) follows from the displayed exact rational eigenvalue ratios, rather than any extrapolated numerical trend.

## Limits

No external expert audit or independent mathematical validation is claimed. The checker cannot rule out an undiscovered priority precedent, and its finite tests do not prove untested dimensions. All needed input formulas and code are embedded in this package.
