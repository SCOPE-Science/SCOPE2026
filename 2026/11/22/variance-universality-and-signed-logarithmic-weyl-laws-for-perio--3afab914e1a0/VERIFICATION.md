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

# Verification and limits

The supplied `verify.py` can be executed with Python 3 and NumPy. It exactly checks the rational residue-class formula against the original periodic Hilbert commutator for five patterns and their first five vectors in each residue block, totaling 1,750 matrix entries. It numerically confirms Hermiticity and exact positive–negative eigenvalue pairing for 15 finite cutoffs. The mathematical argument does not infer infinite-dimensional spectra from these tests.

Analytic checks: the Hilbert shift difference is a signed trace-norm convergent rank-one integral; the finite residue-block sum is trace class; the rank-two coefficient matrix has eigenvalues \(\pm\sigma\); a weighted \(\ell^1\) tail makes the diagonal-commutator perturbation trace class; Hilbert-section counting at nonzero fixed thresholds transfers under uniform trace-norm bounds. The cited Hilbert spectral theorem, Widom counting law, Weyl theorem, and Kato–Rosenblum theorem remain necessary external theoretical inputs.

There has been no independent audit or independent mathematical validation. The bibliography does not resolve all possible historical priority claims.
