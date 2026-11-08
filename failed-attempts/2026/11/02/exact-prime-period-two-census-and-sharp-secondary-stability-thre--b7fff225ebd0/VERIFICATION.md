---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Read RESULT.md and verify.py at frozen Git blob identities. For T_h(x)=x-hx/(1+x^2), h>0, algebraic factorization of the numerator of T_h^2(x)-x into -h*x*(2(1+x^2)-h)*((1+x^2)^2-h*x^2) with positive real denominator exhausts period dividing 2. Symmetric ±sqrt(h/2-1) exists exactly h>2, asymmetric reciprocal radii exist exactly h>4, coalesce at h=4. Differentiation gives multipliers (3-8/h)^2 and 9-2h, hence 2<h<4 and 4<h<5 attraction and neutral boundaries h=4,5. Source exact polynomial verifier inspected; symbolic factorization and positive denominator checked. No claims about longer orbits or nonlinear boundary stability.

## originality

FAIL

FAIL: the exact advertised asymmetric coordinates, two mirror-image cycles, multiplier 9-2h and h=5 sharp stability threshold are explicitly established by Alexander Itin, arXiv:2610.27321v2 (dated 2026-10-28), Proposition 8 and its complete proof in Appendix A, for the same momentum-free map b=0 and A=h. The assigned paper's comparison with v1 (2026-10-19) overlooked this older revision; all central advertised novelties are covered. No disclaimer or routine re-derivation can turn the original unchanged result into an original theorem. This is scientific rejection on O, not a literature access block.

## value

PASS

Complete exact period-two phase and multiplier classification is a natural relevant dynamical fact with the secondary stability threshold, beyond a vacuous formula, even though this instance is already published and thus fails originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
