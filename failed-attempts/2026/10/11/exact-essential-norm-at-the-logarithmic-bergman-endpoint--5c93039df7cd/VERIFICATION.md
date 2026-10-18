---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Monomial orthogonality and two derivatives of beta product give exact v_n=((1+H_{n+1})²+H_{n+1}^{(2)})/(n+1), with v_n~(log n)²/n. Conjugated B matrix is HS-equivalent to upper-triangular D_{mn}=1/(sqrt(mn)log n) for n>=m>=3: verify diagonal relative error O(1/log n+1/m+m/n), square summable, and off triangle O(n/(m³log²n)). Schur test with u_n=(n log n)^(−1/2) gives essential norm <=2; escaping blocks n between exp R and exp(Re^L) force norm >=2, L→∞. Source artifacts/verify.py was read and elementary beta coefficients independently checked; proof is analytic, not finite-matrix extrapolation.

## originality

FAIL

A stronger published Copson-model theorem already computes the same critical Hilbert matrix essential norm 2 for asymptotically identical coefficient weights and proves an additional Fredholm spectrum. Compact diagonal equivalence transfers its exact essential-norm value to the original integral-norm spaces. Strong prior mathematical coverage beats nonmatching notation.

## value

FAIL

No independently surviving essential-norm constant remains after the stronger Copson theorem and standard compact diagonal reduction; the submitted HS estimates reestablish its norm-2 consequence without a new structural invariant. Numerical verification or extra estimates cannot rescue a fully covered original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
