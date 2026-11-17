---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Orthogonal Gaussian invariance puts the 3x3 symmetric A in a Ritz diagonal 2+1 block and the sketched 2x2 M in diagonal + q(t1,t2) form. The discriminant D<0 is an indefinite homogeneous quadratic in three independent standard normals because F^-1g has bivariate Cauchy density (2pi)^-1(1+||q||^2)^-3/2. The K quadratic has three vanishing principal 2x2 minors, negative determinant for dt1t2 !=0 and two positive/one negative eigenvalues; u+v=1. Conditioning on normal Z3, the Gaussian measure of the ellipse is dominated by a disk of area pi Z3^2 sqrt(uv)<=pi Z3^2/2, giving 1-sqrt(2/3). Strict rearrangement and the product determinant imply equality precisely |t1|=|t2|=beta-alpha with alpha<beta. Degenerate d=0 or t1t2=0 gives zero risk. The displayed SPD example has positive Schur complement 14/3; the result is only for fixed U, ambient 3 and two Gaussian rows.

## originality

PASS

Liu and Liu (2026) directly motivate the appearance of nonreal sketched symmetric Ritz pairs and real-Schur remedies; the inspected abstract/secondary detailed exposition does not state this special sharp probability or its equality cases. Resultary returned a sharp one-quarter theorem, but that has a fixed-length uniformly oriented cross-coupling model, whereas this is the exact inverse-Gaussian 2x2 ratio and is not a corollary of the one-quarter number. PASS with explicit inaccessible full-text risk.

## value

PASS

A sharp worst-case probability with equality classification quantifies a concrete failure mechanism of minimally sketched symmetric Rayleigh–Ritz. It is a natural exact small-dimensional quantitative bound, not merely a nonreal counterexample; it supplies a benchmark for real-Schur safeguards while making no large-dimensional promises.

The dated certificate retains the supplied scientific assessment, sources and limitations.
