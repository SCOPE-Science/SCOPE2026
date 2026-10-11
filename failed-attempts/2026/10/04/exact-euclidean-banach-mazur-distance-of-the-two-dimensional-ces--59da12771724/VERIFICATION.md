---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Zuo's primary article gives the same linear normalization of the two-dimensional Cesàro \(p=2\) norm. In those coordinates the squared norm is \(u^2+v^2+(2/\sqrt5)|uv|\). The package lower bound correctly treats its unit ball as the intersection of two ellipses, and the positive-semidefinite containment inequalities force every inscribed ellipse used in a Banach--Mazur pair to have dilation at least \(\sqrt{1+1/\sqrt5}\); the concentric Euclidean pair attains it. The same value is independently recovered by the Lorentz-family identification below.

## originality

FAIL

The normalized Cesàro plane is an orthogonal re-expression of the current published \(q=2\) Lorentz family. Let \(a=1/\sqrt5\) and rotate by \(x=(u+v)/\sqrt2\), \(y=(u-v)/\sqrt2\). Then \(u^2+v^2+2a|uv|=x^2+y^2+a|x^2-y^2|\), which equals \((1+a)\max\{x^2,y^2\}+(1-a)\min\{x^2,y^2\}\). Thus, up to scalar, it is \(d^{(2)}(w,2)\) with weight ratio \(b=(1-a)/(1+a)\). The published family theorem gives \(d_{BM}^2=2/(1+b)=1+a=1+1/\sqrt5\). The assigned theorem is therefore a direct special case of stronger current coverage.

## value

FAIL

The Cesàro value is a natural affine invariant, but after the standard normalization and a 45-degree rotation it is simply one weight ratio in a currently published all-weight Lorentz theorem. The separate exact number is therefore a routine specialization rather than an independent mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
