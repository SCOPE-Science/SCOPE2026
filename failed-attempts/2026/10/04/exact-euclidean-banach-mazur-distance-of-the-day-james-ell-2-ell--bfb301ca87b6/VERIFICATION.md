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

After the orthogonal change \(u=(x+y)/\sqrt2\), \(v=(x-y)/\sqrt2\), the norm satisfies \(N(u,v)^2=u^2+v^2\) when \(|u|\ge|v|\) and \(N(u,v)^2=2v^2\) when \(|v|\ge|u|\). Averaging any quadratic pullback under the coordinate-swap isometry reduces without loss to \(u^2+t v^2\). The two sector ratios have only endpoint extrema, giving the displayed piecewise distortion and unique minimum \(3/2\) at \(t=2\). The same coordinates also show directly that the norm is the Banaś--Frączek norm \(\max\{\sqrt2|v|,\sqrt{u^2+v^2}\}\) after swapping coordinates, providing an independent correctness check.

## originality

FAIL

A current published theorem for the full Banaś--Frączek family proves \(d_{BM}(X_\lambda,\ell_2^2)^2=C_{NJ}(X_\lambda)=2-\lambda^{-2}\) and gives the optimal ellipse. The present Day--James plane is linearly isometric to the \(\lambda=\sqrt2\) member: in the displayed \((u,v)\) coordinates its norm is exactly \(\max\{\sqrt2|v|,\sqrt{u^2+v^2}\}\). Setting \(\lambda=\sqrt2\) gives \(3/2\), and the published optimal ellipse becomes, up to scale, \(u^2+2v^2\). Thus the entire scientific claim is a direct special case of stronger current published coverage.

## value

FAIL

The exact distance is a natural quantity, but once the plane is recognized as the \(\lambda=\sqrt2\) Banaś--Frączek member, its distance, von Neumann--Jordan equality and optimal ellipse are immediate specializations of the broader published theorem. The separate record is therefore scientifically redundant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
