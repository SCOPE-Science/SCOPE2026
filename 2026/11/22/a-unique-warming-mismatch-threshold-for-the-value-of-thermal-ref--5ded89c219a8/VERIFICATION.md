---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

After shifting by the homogeneous eigenvalue, let G=R exp(-x^2/2), p=exp(-a^2/2), h=1-p cosh(ax). For x<=a/2 both heterogeneous diagonals before movement are at most the homogeneous one, with one strict, so irreducible Perron comparison is strict. For x>=x2 the mean equals or exceeds the homogeneous gross rate and the nonzero contrast raises the eigenvalue strictly above that mean for finite positive movement. On the intervening interval the shifted matrix has trace -2(Gh+m)<0. Its determinant is G^2(1-2p cosh(ax)+p^2)+2mGh, so the top eigenvalue has the opposite sign and crosses at the exact M_a(x). Differentiating M_a=G[(1-p^2)/(2h)-1] shows M_a'/G=x+(1-p^2)[ap sinh(ax)-xh]/(2h^2)>0: ap sinh(ax)/x increases from 1-p^2 at x=a/2, while h decreases from (1-p^2)/2 there. The derivative in m of the determinant is positive; the negative trace at equality makes the crossing transversal. The lower endpoint derivative Ra exp(-a^2/8) and the upper simple pole from -h'(x2)=a sqrt(1-p^2) reproduce the stated inverse expansions. The loss cancels exactly. Read checker.py and its notes without executing them. Independent 55-digit root computation on the shifted determinant at a=R=1, m=0.1 gives 0.5964895360394114 with negative trace, and x2=1.085038501948388. Only fixed finite positive movement, symmetric Gaussian growth, equal patch sizes and low-density linear dynamics are proved.

## originality

PASS

The distinct supported result is the global single crossing in mean mismatch against the homogeneous-mean control, with its migration monotonicity and sharp endpoint scales. Ordinary Perron comparison, the two-by-two eigenvalue formula and decreasing growth with mixing at fixed local rates are not novel. Related ecological simulations and nonlinear equilibrium classifications do not support credit for those methods, nor do their inspected results establish this Gaussian sign boundary.

## value

PASS

The theorem gives a usable three-region sign diagram under a precise homogenization control, not just the diagonalization of an example. It separates near-optimum harm from far-mismatch benefit and quantifies how increasing movement shifts the boundary and at what rates the two limiting boundaries are approached. This is an analytical benchmark for spatial thermal comparisons, not a calibrated field prescription; relative benefit does not imply either growth exponent is positive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
