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
# Verification

The universal proof is in `RESULT.md`, not in a finite search. Analytic checks explicitly cover singular input coefficients, output-nonzero normalization, both endpoint atoms, the weighted arithmetic boundary, symmetric and nonsymmetric measures, and strict positivity of interior inputs.

Run `python check.py` with Python 3 and NumPy. It prints `PASS: 20012 supplementary assertions; proof is independent of finite tests`, after tests of five finite-atom normalized representing measures, random separable Bell probabilities, direct numerical partial-transpose diagonalization, exact boundary witnesses and a rational test case.

The exact rational test uses endpoint masses \(c=1/7\), \(d=2/7\) and interior harmonic mass \(4/7\) at \(t=2/5\). The extremal unnormalized output has Bell coefficients \((1/2,1/14,1/7,0)\), whose normalization gives negativity \(1/5\). This agrees with the formula.

Finite experiments cannot certify all representing measures or all input states. The proof provides those quantifiers, while originality remains subject to older equivalent formulations. No external independent audit has been performed.
