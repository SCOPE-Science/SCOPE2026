---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For triangle indicators, covariance is nonzero only for edge-sharing triples, and after factoring \(\nu=p^3(1-p^3)\) the off-diagonal ratio is \(r=p^2/(1+p+p^2)\), giving \(C=\nu(I+rA_1)\) in the Johnson scheme \(J(n,3)\). Distance transitivity forces the inverse to have four distance coefficients. The four neighbor-count equations printed in the package were independently substituted into the claimed \(b_0,b_1,b_2,b_3\) and simplify identically to the inverse equations. Since \(0<r<1/3\), all denominator factors are positive; the separate \(n=6\) check makes \(Q>0\). The precision signs and partial-correlation signs therefore follow exactly.

## originality

FAIL

Once the elementary covariance calculation identifies \(C/\nu=I+rA_1\), the remaining inverse is a direct specialization of standard Bose–Mesner/Johnson-scheme theory. The Johnson scheme has explicit relation matrices and explicit eigenmatrices (Eberlein polynomials); an invertible element \(I+rA_1\) has inverse in the same Bose–Mesner algebra with coefficients obtained by the standard spectral idempotent formula. The displayed four coefficients are exactly that diameter-three specialization, and the sign classification is then elementary substitution of \(0<r<1/3\). The probabilistic wording and partial-correlation interpretation do not change that the final mathematical formulas are mechanically implied by established association-scheme machinery.

## value

FAIL

The random-graph interpretation is neat, but after the covariance is recognized as a scalar Johnson resolvent, the exact coefficients and alternating signs are a short specialization of standard association-scheme inversion. Under the stated value bar, this is a routine application of known algebra rather than an unknown non-implied invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
