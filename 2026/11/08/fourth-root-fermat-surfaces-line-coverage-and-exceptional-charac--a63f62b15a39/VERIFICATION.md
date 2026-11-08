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

# Reproducibility and scope

Run `python verify_root_sums.py` and `python verify_point_incidence.py` with Python 3 and no third-party libraries. Both programs were executed successfully using the embedded versions and returned `VERIFY_ROOT_SUMS_OK` and `VERIFY_POINT_INCIDENCE_OK`, respectively.

`verify_root_sums.py` enumerates all four-tuples from the fourth roots of unity with zero adjoined across multiple prime characteristics; it confirms \(c_2,c_3,c_4\) and the short Gaussian-norm restriction. The second program enumerates projective points of the smooth Fermat surfaces over \(\mathbb F_9,\mathbb F_{13},\mathbb F_{17},\mathbb F_{25},\mathbb F_{29},\mathbb F_{37},\mathbb F_{49}\), checking whether the surface equation holds and how many of the explicit lines contain each point. It confirms \(N_1,N_2,N_d,N_0\), including the \(d=2\) stratum merger.

These are exact finite computations, not a proof covering infinitely many finite fields; that coverage follows from the Gaussian-norm and additive-character argument, explicit intersection pattern, and double-counting proof in `RESULT.md`. No external independent audit, priority certification, or validation has been performed.
