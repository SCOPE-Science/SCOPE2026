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

# Reproducibility

Run `python3 verify.py` using Python 3.10 or later and no third-party packages. The expected terminal status is `VERIFY_OK direct_spectra 23 coefficient_shape_profiles 3750 boundary_inequalities 4420`.

The script separately enumerates assignments of below/incomparable/above relations, enforcing all transitivity constraints, for every positive \(a,k\) with \(ak\le9\). It independently constructs the generating polynomial by bounded-uniform convolution for \(1\le a\le150\), \(1\le k\le25\), and checks every internal log-concavity inequality against the exact classification. It also tests the sufficient binomial inequality on a grid of 4,420 cases. All arithmetic is integer-exact.

These computations are finite corroboration, not proof of the infinitely quantified classification. The proof in `RESULT.md` establishes the extension bijection, interior grade inequalities, convolution-tail log-concavity and a symbolic induction for the only possible boundary defect. External mathematical audit is not part of these checks.
