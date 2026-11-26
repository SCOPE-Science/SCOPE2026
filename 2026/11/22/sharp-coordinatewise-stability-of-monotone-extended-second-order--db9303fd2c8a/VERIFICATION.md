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

At fixed output radius s, radial alignment minimizes the spatial squared distance and leaves ordinary nonincreasing isotonic least squares for (z,||w||₂), with a zero floor. The floor preserves optimality: untruncated residuals have zero block sums and satisfy the prefix KKT signs, and the new negative-block residual contribution lies in the nonpositivity polar with zero dot product against the truncated fit. For r=||w||₂>0, a free final singleton leaves w unchanged and a zero-floor final block gives spatial output zero. In a positive terminal pool with k scalar inputs the last KKT multiplier is r−t≥0, so c=t/r lies in [0,1]. Differentiation gives scalar row bound (k+√q)/(k+1) and spatial block c(I−nnᵀ)+nnᵀ/(k+1), plus k scalar entries n_i/(k+1) in row i. For a=|n_i|, B=∑_{j≠i}|n_j|, only |c−1/(k+1)|aB is nonlinear in the absolute row sum; convexity bounds it by the endpoints. At c=0 the row sum is a(k+a+B)/(k+1)≤(k+√q)/(k+1); at c=1 it is 1+k a(1−a+B)/(k+1), maximized for k=p with B=√(q−1)√(1−a²). Piecewise-affine isotonic regions give these derivatives almost everywhere away from w=0; Lipschitz regularity from the Euclidean projection and convolution of its weak derivative globalize the bound. For sharpness, strict inequalities isolate a size-two terminal pool with equal direction magnitudes; alternatively z_j=1−δ and r=1 give strictly active internal pool multipliers and a positive all-coordinate average tending to r as δ→0. Signs of the norming row realize the local quotients. For q=1 the unit row has a=1,B=0 so both endpoints give factor one, attained on the cone interior. For q≥2 the second derivative is strictly negative and the endpoint derivative signs are opposite. At q=6 the unique critical point is a=2/3, where g₆=4/3; 17/9 is larger than (1+√6)/2.

## originality

PASS

The p=1 formula and the PAVA structure are prior coverage, not novelty. The sharp comparison of shortest and longest terminal pools for p≥2, with its p-dependent spatial sensitivity, is a distinct extension on the available evidence.

## value

PASS

Monotone conic constraints combine ordering and a norm bound; entrywise input accuracy makes the sharp ℓ∞ modulus of their Euclidean projector relevant beyond Euclidean nonexpansiveness. The formula identifies which terminal pools control the exact error amplification, with a concrete nontrivial branch change relative to p=1. The value is the full parameter formula for these constraints, not the already-known Lorentz case or the isolated rational example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
