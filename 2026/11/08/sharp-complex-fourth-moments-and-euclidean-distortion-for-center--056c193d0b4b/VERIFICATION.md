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

The analytical proof in `RESULT.md` covers every complex centered affine coefficient vector on every nondegenerate simplex of real dimension at least two. The standalone standard-library `verify.py` checks direct Dirichlet integration against the invariant formula using exact rational arithmetic, exact one-outlier upper witnesses in dimensions \(3\) through \(74\), the exact lower-deficit identity, and real triangle equalities. The roots-of-unity lower witnesses in dimensions \(3\) through \(59\) are additionally checked numerically; the exact attainment of the lower endpoint follows analytically from sums of roots of unity. Finite enumerations do not establish global inequalities or uniqueness: the global real zero-sum spectral lemma, phase inequality, and permutation symmetrization in the proof do.

To replay, run `python3 verify.py` with Python 3 from the directory containing the extracted scientific files. This code requires no external modules, network, files, or state. No independent audit has been performed.
