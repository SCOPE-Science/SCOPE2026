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

Differentiating in the moving cylindrical frame gives ||X′||²=V=4(R+c)²+9 and X′·X″=−12(R+c)sin(3t); the Gram determinant gives the stated N. Independently expanded (N_c V−3NV_c)/8 and substituted R=1+z, c=(y−1)/(y+1), clearing (1+y)^5 using exact integer polynomial convolution. All six g_j rows agree; direct Horner evaluations at the four proposed R brackets give (−8028,32508), (−162022,38160), (−684562,401217), (−125222,1563705). The positive first two rows and exactly one positive zero of each other row, in increasing order, give one sign change in y when g5<0 and none when g5≥0, ignoring zero coefficients. Thus any interior root is unique and simple. F_R(−1)>0, while F_R(1) is the stated positive quadratic factor times the cubic. Passing to curvature preserves strict extrema because square root is strictly increasing. Each interior cosine root has six preimages, each endpoint three. At R=13/4 the inner endpoint gives K=0, K_c>0 and hence a positive multiple of |t−t0| to leading order; no other curvature zero occurs since the radial cross component is 18 sin(3t)(c−R). At the vertex threshold, g5=0 and F_c(1)=−g4/2<0, so the cosine expansion gives a fourth-order decrease at positive curvature. The cubic crosses simply, so F_R's parameter derivative is positive there; the implicit root satisfies c=1−Pδ+O(δ²) and inverse cosine gives the two branches. Independent bisection and differentiation give R*=10.1012691095328, reciprocal 0.09899746152256, splitting coefficient 0.1707184632790. The supplied checker was inspected, not run; global coverage is from the sign proof.

## originality

PASS

Oberti–Ricca study exactly this geometry, including the exact inflection value and a qualitative observation that two curvature peaks develop, which are prior. Their sampled profiles include λ=0.1, close to the reviewed threshold, but do not give the cubic vertex onset, exclude further extrema at all ratios, or supply quantitative splitting. The nearest inspected same-geometry catalogue records instead treat integrated curvature or regular torsion zeros. The sign proof and local scale resolve an exact gap rather than reasserting the known peak observation or inflection theorem.

## value

PASS

The circular trefoil is a canonical embedding, and pointwise extrema describe its bending geometry independently of knot type or integrated curvature. The result replaces sampled peak profiles with a complete all-ratio count, distinguishes inflection from onset of new extrema, and gives a quantitative merger law. The global exclusion of additional branches is substantive, not a routine local differentiation or a single numerical parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
