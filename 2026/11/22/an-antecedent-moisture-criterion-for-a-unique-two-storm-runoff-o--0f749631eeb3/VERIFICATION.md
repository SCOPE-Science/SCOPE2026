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

The analytic proof uses the exact impulse-and-decay recurrence, positivity and 1-Lipschitz continuity of the positive-part map, and a complete three-case split. In the straddling case, it proves a unique sign crossing at retention \(q=s/(s+B)\); it does not infer uniqueness from a plotted or numerically scanned curve.

Run `python3 verify.py` with Python 3 standard library only. The executable uses `fractions.Fraction`, checks 46,683 rational parameter cases across three normalized capacities and all three structural regimes, and verifies the sample values \(\Delta(1/2)=1/5\), \(\Delta(9/10)=-1/100\), and \(\Delta(8/9)=0\). It also changes the larger storm at fixed initial storage and smaller storm, confirming the predicted invariant threshold in four exact instances. Numerical sampling is supplementary and does not establish an infinite theorem.

Verified parameter coverage is limited to rational grids. The exact proof covers all specified positive real parameters and every nonnegative integrable proportional-loss profile with positive finite integral. The theorem does not cover nonlinear loss or field-calibrated hydrology. Originality comparisons are based on the stated and materially inspected sources; independent priority validation is not supplied.
