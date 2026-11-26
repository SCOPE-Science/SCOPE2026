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

Solving the killed backward Laplace equation with value 1 at each endpoint, the inward-coordinate flux at the interface from layer i is proportional to √(D_i r)[csch(x_i)−φ coth(x_i)], with x_i equal to the layer length times √(r/D_i). Matching the two fluxes with opposite signs gives the stated transform. Independent reset renewal yields M_r=(1/φ−1)/r. For a direct coefficient check let A=a²P and C=b²Q, and μ_j denote the j-th power moment of A,C under weights bQ/H,aP/H respectively. After canceling the 1/√r factors the reset mean is [weighted x_i tanh(x_i/2)]/[r weighted x_i csch(x_i)]. Its coefficients through r² are μ₁/2, (2μ₁²−μ₂)/24, and (10μ₁³−12μ₁μ₂+3μ₃)/720, by convergent Taylor expansions. Here μ₁=abPQ(a+b)/H and μ₂/μ₁²=(a²+b²+ab(z+1/z))/(a+b)². This verifies the stated c₁ and its reciprocal-root frontier, with vanishing first derivative at the endpoints of the delaying interval. For equal widths μ₁=2t₀, μ₂=(8+w)t₀², and at w=0, A+C=8t₀, AC=8t₀², μ₃=48t₀³. Hence the normalized linear coefficient in s=rt₀ is −w/24 and the critical quadratic coefficient is 2/45. Near both contrast roots w is an analytic local coordinate; critical curvature 4/45 in s gives a locally unique stationary minimum for w>0. Substitution gives s=15w/32+O(w²) and normalized improvement 5w²/512+O(w³).

## originality

PASS

Best of checked evidence for the explicit geometry/contrast criterion at a perfectly transmitting interface, the equal-width curvature and the sharp local onset. General reset renewal, CV>1 and transmission techniques are covered background. The homogeneous-interval calculation and the closest layered and resetting records do not cover the explicit heterogeneous frontier and its higher-order boundary behavior.

## value

PASS

A restart decision at a material interface is not determined by interval symmetry or the mean alone. The exact frontier gives a design boundary across all width and material ratios. Even at the midpoint where homogeneous weak restart delays escape, sufficient contrast reverses the effect; on the threshold, where the general CV rule cannot decide the sign, the result quantifies both the positive curvature and emergence of a locally beneficial reset rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
