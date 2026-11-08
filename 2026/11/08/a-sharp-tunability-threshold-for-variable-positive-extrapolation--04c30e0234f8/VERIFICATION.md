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

# Reproducibility and verification

Run `python3 verify.py` from the extracted package directory. Python 3 standard library suffices and no network, datasets, or compiled dependencies are needed. The script was actually executed and returned `PASS: 8737 exact and numerical diagnostic groups` and `PASS: separation determinants 1/200 -3/125`.

Its exact rational checks confirm the strict separation of the new and previous comparison matrices and the negative-feedback determinant identity on a rational parameter grid. Floating-point checks test the equality cases for planar skew resolvents, the monotonicity of the comparison coefficient over a grid, and random planar positive-plus-skew operators and couplings. The finite samples cannot prove the infinite-dimensional or all-operator theorem. The universal conclusions instead follow from the explicit firm-resolvent inequality, Schur/M-matrix identity, common weighted norm construction and scalar counterexample in `RESULT.md`.

Critical boundary and scope checks: \(\theta=0\) and \(\theta=1\) are included; \(L=0\) allows any positive steps; \(\mu_A\mu_B=L\) gives eigenvalue one for the scalar obstruction; \(\mu_A\mu_B<L\) gives an eigenvalue above one. The public proof gives no fixed-step necessity condition outside the scalar obstruction, no optimized rate or stochastic guarantee. Independent mathematical review and independent audit have not been performed.
