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

The entire infinite-dimensional minimization is reduced analytically by the real-Hilbert-space parallelogram identity to maximizing \(C_a(\phi)=\cos\phi-a^2\cos(2\phi)\) over one circle. The substitution \(x=\cos\phi\) gives a strictly concave quadratic and directly establishes global optimality, the exact equality cases, the variance and the mean multiplicities. The unaligned arithmetic mean remains fixed under the exact best-alignment iteration because its alignment correlations for both inputs are \(\cos\phi\); arbitrarily close strict-descent competitors follow from \(C_a''(0)=4a^2-1>0\).

`verify_phase.py` is a self-contained Python 3 standard-library checker. Invoke `python3 verify_phase.py`. Expected successful output:

`VERIFY_OK exact_parameter_cases=8 harmonic_inner_products=48 scanned_phases=2888 suboptimal_descent_checks=12`

The rational formulas are checked exactly; floating-point checks only corroborate phase correlations and descent at selected values. The sampled phase grid is not a proof of the continuum maximum. The analytical proof, not the script, justifies the universal quantifiers over \(a>0\), all phases, and all mean candidates in \(L^2\). Historical-priority conclusions are limited to the listed inspections; no independent scientific audit has been performed.
