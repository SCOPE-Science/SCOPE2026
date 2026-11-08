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

# Reproducible mathematical checks

Run `python check.py` from the supplied directory after installing `requirements.txt`. The program uses exact `Fraction` arithmetic for all coefficient, determinant, Descartes and Sturm calculations. It enumerates nonisomorphic trees of order 2 through 11 and checks all 20,398 vertex pairs; its per-order counts are 1, 3, 12, 30, 90, 231, 644, 1692, 4770 and 12925. All trees of orders at most 10 yield at most one positive-root Descartes variation after the open-interval rational substitution. At order 11, exactly 30 comparison polynomials have two or more potential variations; rational Sturm counts isolate exactly three labelled witness pairs from one isomorphism orbit.

The exact polynomial linear-system identity \((I-\alpha AD^{-1})N=H\mathbf1\) is checked on each enumerated tree and is not inferred from floating-point PageRank calculations. For the witness, the script checks its edge set, factored numerator, exact determinant and exact sign evaluations. A separate symbolic direct rational inversion at damping values \(1/2,2/3,9/10,19/20\) gave score differences \(-157/404184,1/109450,342483/5651385080,-259875103/9226580460240\), agreeing independently with the displayed closed formula.

The finite exhaustive census relies on NetworkX's `nonisomorphic_trees` generator for completeness; no independent scientific audit has been carried out. The numerical approximations of the two roots aid interpretation only: the infinite-precision proof uses exact signs and Descartes/Sturm bounds.
