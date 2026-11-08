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

The proof is a direct analytic derivation, and no external certification is claimed. Run `python verify_short_chord.py` with Python 3, NumPy and SciPy installed. The recorded output from executing the exact standalone program was:

`SHORT_CHORD_VERIFY_OK ellipses=3 analytic_pairing=2049 smooth_counterexample=5001`

The program independently evaluates the exact offset measure of short chords for three ellipses at four thresholds each, compares unordered antipodal radii recovered by the quadratic to their known analytic values at 2,049 normal directions, evaluates the smooth first-Fourier compatibility integrals by adaptive quadrature, and checks pointwise squared bump profiles and inverse-curvature sums at 5,001 angles. The latter are finite checks of an identity already proved by disjoint compact supports. The numerical experiment cannot prove real-analytic rigidity or the all-angle smooth obstruction; those follow from the written argument.

A full historical originality certification and an independent mathematical audit have not been performed. The old full-covariogram theorems concern stronger observations than the two functions in this theorem.
