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

The eigenvalues are -1 and ±√b with b>0; det DF_b=b cos z ensures a local diffeomorphism, and the other two directions contract. The normalized left eigenfunctional is ℓ(X)=(z-bx)/(1-b) for the right eigenvector (1,-1,1). Standard finite-smoothness center and strong-stable theory applies (C^7 suffices); oddness can be preserved by an equivariant local graph construction, or used to force the even Taylor coefficients to vanish by uniqueness of the finite center jet. An independent elimination uses the exact projected return ℓ(F_b(X))=-ℓ(X)+(z-sin z)/(1-b). Writing x(u)=u+A u³+B u⁵ on the normalized graph forces z(u)=u+bA u³+bB u⁵. With f(u)=-u+a u³+d u⁵, the identities x(f(u))=y(u) and y(f(u))=sin z(u) give (1-b)A=2a-1/6 and (1-b)B=2d-3a²+6aA-bA/2+1/120. The projection gives a=1/[6(1-b)] and d=(bA/2-1/120)/(1-b). Exact truncation reproduces the entire given cubic and quintic jet, and at b=1/2 the two scalar clock coefficients are 2/3 and 39/20. Along a nonzero sufficiently small center orbit, f reverses sign and shrinks magnitude since a>0. For v=u^(-2), its increment is 2a+(3a²+2d)/v+O(v^(-2)); thus v grows linearly, then v=2an+O(log n), and the differences 1/v_n-1/(2an) are summable. This yields a finite remainder constant, not merely O(1). The stable foliation gives exponential tracking; its origin leaf is the strong-stable manifold. Reduction and tracking give local asymptotic stability. An exponentially small perturbation of a nonzero shadow amplitude of order n^(-1/2) changes its reciprocal square by O(n^(3/2)θ^n)=o(1), so the actual ℓ amplitude has the same clock and is eventually nonzero. On the center graph z-u=O(u³), yielding the claimed physical z comparison after tracking. No inference about the global basin or b=0. The supplied symbolic script was inspected, not run.

## originality

PASS

The map family and general neutral parabolic summation are not new. The inspected critical fixed-point, period-two and related flip results do not cover the fifth-order coefficient and whole local strong-stable versus algebraic stratification for this parameter slice. Earliest exact-parent full text was not recovered independently; this limits the priority assessment, not the correctness argument.

## value

PASS

At a natural loss of strict spectral stability, distinguishing attraction from instability and algebraic relaxation from a codimension-one exponential exception is a meaningful local question. The model-specific logarithm and finite remainder improve on the leading critical power law and hold for the actual observable of all nearby off-leaf states, not only formal center orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
