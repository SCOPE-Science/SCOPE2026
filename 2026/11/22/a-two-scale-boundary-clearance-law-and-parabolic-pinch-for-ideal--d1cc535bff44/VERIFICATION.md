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

The hyperboloid signed distance to the lines x=±c, y=±s gives the stated minimum after division by sqrt(1-x^2-y^2); these lines intersect the disk in the complete ideal sides. The Klein area density and total area 2π give the normalization. For an independent localization check, in the first quadrant let α=c-x, β=s-y and τ=min(α/s,β/c). The squared disk factor is α(2c-α)+β(2s-β), increasing separately on the allowed coordinate intervals. It is at least 4csτ-τ² with equality on α=sτ, β=cτ. Thus sinh(clearance)≤sqrt(τ/(4cs-τ)), increasing up to τ=s/c. This recovers the maximizing centers and radius, and the same bound tends uniformly to zero at the moving ideal corners when c is near the square. At a fixed right maximizer, the first-order inequalities for the displacements X,y give X≤U h+O(h²+X²+y²) and |y|≤2cs h+[c(2c²-1)/(s(4c²-1))]X+O(h²+X²+y²), with positive X coefficient in the latter. They imply |X|+|y|=O(h) by absorption after localization. The triangle has area s³(4c²-1)³/[c³(2c²-1)], and multiplying by the local area factor [1-x_*²]^(-3/2), two lobes, and 1/(2π) gives the fixed nonsquare coefficient. The square gives |x|,|y|=O(h) and the stated unit-half-width square. In the drifting shape, δ=sqrt(h) and the exact inequalities imply |x|=O(δ+x²+y²), |y|=O(δ²+x²+y²); first absorb in the sum, then apply its O(δ) bound to the second to get the anisotropic localization. The vertical-side first-order constraint is |u|≤2sqrt(2)λ, and the horizontal-side second-order constraint is |v|≤1+u²/(2sqrt(2))-2sqrt(2)λ². On bounded transformed supports, the constraint boundaries have measure zero and the area density converges uniformly; after removing the coordinate Jacobian and constant area normalization, dominated convergence and division by the limiting area give TV, not just weak convergence. Integrating twice the positive height yields the given area, the pinch at λ=2^(-3/4), and the 1/λ large-λ asymptotic. This is not a uniform two-parameter result. I inspected VERIFICATION.md and the SciPy quadrature artifact; integration of the Klein density there is a finite diagnostic and the argument here does not rely on its local integration windows or a script execution.

## originality

PASS

The distinct contribution is the nonsquare upper tail and anisotropic near-square spatial law with its explicit area profile and pinch. The inradius and maximizing centers are existing coverage, as is the scalar square coefficient under the separately indexed complete regular-polygon law. The square is a benchmark, not a distinct originality finding. The same-day catalogue dates are not evidence of priority in either direction.

## value

PASS

The divergent fixed-nonsquare coefficient poses a concrete nonuniformity question when the two maximizing disks merge. The crossover scale resolves it with an explicit probability constant and the full conditional spatial law. Its pinch and nonanalytic area turn a symmetry-breaking statement about maximizers into a quantitative statement about neighborhoods of near-maximizers. The square probability alone is not the basis for this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
