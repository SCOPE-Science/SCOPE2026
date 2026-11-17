---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Orthogonal harmonic Bergman monomial basis indexed by Z gives T_(z^m) as a weighted bilateral shift. Degree-one products telescope except for -m<j<0, yielding gamma_(m,n)=n(m-n)/[(m+1)sqrt((n+1)(m-n+1))]. Images are distinct positive modes, so exact singular values, rank m-1 and square-zero follow. For any degree-d polynomial, linearity produces a reverse-triangular (d-1)x(d-1) crossing block with anti-diagonal proportional to a_d != 0, proving rank d-1 and nilpotence. Strict monotonicity in n(m-n) yields sharp norm; Riemann sum of sqrt(t(1-t)) gives beta-law and all moments including pi/8,1/6. Compared older weighted theorem with alpha=0 at degrees 2,3,8,31: all singular formulas equal within rounding. Inspected frozen verify.py; tests not a proof.

## originality

FAIL

FAIL: the already published November 1 weighted harmonic-Bergman semigroup-defect theorem covers every monomial degree N, including the exact unweighted singular multiset, rank N-1, nilpotence, sharp norm, beta limiting density and all Schatten moments by setting alpha=0 (a=1). Its unweighted special case explicitly records operator norm 1/2, S1/N=pi/8 and S2^2/N=1/6. The present additional general-polynomial rank formula is elementary reverse-triangular linearity from those monomial coefficient identities and does not rescue the claimed combined singular/beta-law novelty.

## value

PASS

The power-defect spectral problem and beta law are mathematically meaningful and the exact general analytic-polynomial rank is a sensible finite-dimensional invariant. Value of the subject matter survives even though its central monomial theorem has already been published; correctness/reproducibility do not restore originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
