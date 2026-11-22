---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For complex traceless 2x2 T=H+iK, writing traceless Hermitian parts as Pauli vectors gives ||H cos(theta)+K sin(theta)||_op^2=a cos^2(theta)+b sin^2(theta)+2c sin(theta)cos(theta), with F^2=2(a+b) and |det T|^2=(a-b)^2+4c^2 by Cayley–Hamilton. This is (F^2/4)(1+rho cos(2theta-phi)), rho=2|det T|/F^2<=1, proving the exact Lp angular formula for all real p>=1. Evenness plus strict concavity of t^(p/2) for p<2 and strict convexity for p>2 proves strict monotonicity in rho (except p=2), with sharp normal (rho=1) and nilpotent (rho=0) endpoints. The p=4 identity omega^4=F^4/16+|det T|^2/8 was independently checked for noncommuting Pauli parts a=6,b=13,c=1 (moment=775/8, F^2=38, |det|^2=53). This finite exact test does not prove all p.

## originality

PASS

The reviewed primary Lp-Cartesian-radius paper gives universal comparisons with the ordinary numerical radius, not a trace-zero 2x2 invariant classification or the exchange of extremizers at p=2 for fixed Frobenius norm. Related rank-one and unitary L2 special cases cover only boundary observations; they do not imply the full varying-determinant p profile. Best-of-knowledge priority only.

## value

PASS

A complete two-parameter exact classification for a natural operator radius, including sharp normal/nilpotent equality cases, a universal critical p=2 reversal and perturbative determinant response. The one-parameter family of nonnormal matrices is not covered by universal bounds; precise extremal data is useful when analyzing sharp Cartesian radius inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
