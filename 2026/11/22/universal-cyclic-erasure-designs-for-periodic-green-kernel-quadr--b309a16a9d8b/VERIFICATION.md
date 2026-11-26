---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The Fourier zero mode gives Var(J)=2s/κ and the full covariance is the inverse of (−∂²+κ²)/(2κs). The conditional energy is its restriction to the functions vanishing at the delivered sites; continuity of point evaluation for this H¹ energy form permits the restriction, which splits on the Dirichlet arcs. Solving the constant-forcing Dirichlet equation and integrating gives f, including the unit arc at one survivor. With no survivor use the zero mode instead. For ≥2 survivors, each ordered consecutive pair is counted once by its start and positive index jump; cyclic shift invariance of the fixed index law makes its probability q_k for every start. Since f″(ℓ)=2s tanh(κℓ/2) sech²(κℓ/2)>0, equality in Jensen for each supported jump means all of its running sums agree, equivalently g_(i+k)=g_i. The generated subgroup proves the exact gcd criterion, including the empty-support constant risk and the nonuniform four-site family. For Bernoulli delivery, q_k=p²(1−p)^(k−1), so q_1>0, and at fixed p<1 the empty/singleton terms vanish after n² scaling. The gap cost has leading cubic coefficient sκ/6 and a uniform cubic bound on [0,1]; the geometrically weighted cubic sum evaluates to (p²−6p+6)/p² after multiplication by p². This gives the stated ratio, including 13 at p=1/2; p=1 follows directly.

## originality

PASS

Partial coverage is substantial for the Green kernel, conditioning, erasure-averaged scalar posterior variance, and interval optimization problems. The supported distinct result is the full optimizer classification for arbitrary cyclically invariant delivery laws on a circle, together with the sharp fixed-p many-site erasure factor. No equivalent or dominating statement for these was identified in the inspected evidence.

## value

PASS

Uniform spacing alone would not distinguish laws with the same one-site reliabilities. The gcd rule explains precisely which correlated erasures create flat optimal directions and when the design is rigid, without independence. The exact 13-fold limit at one-half reliability is a useful design benchmark and separates optimal placement from the large cost of failures under that placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
