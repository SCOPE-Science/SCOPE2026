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

The positive inverse of sI+fL times A is strictly positive. The positive radial eigenvector therefore certifies the full Perron root. In the coordinates (hub, representative leaf), the radial kernel has common diagonal mf and off-diagonals m(s+f), s+mf, times ξf/((1+f)s(s+(m+1)f)), giving the stated formula. The decreasing variable r=sqrt(m(s+f)/(s+mf)) maps positive f onto (1,sqrt(m)); the derivative with respect to r has the sign of s−S_m(r). All three terms of (log S_m)' are positive, so S_m runs from s_c to infinity and equality s=s_c gives strict increase at every finite f. The endpoint limits and m=1 specialization follow directly. Positivity of K makes the derivative of the left-Perron linear functional strictly negative off zero even at equality on the forward-invariant cube. Above threshold, the positive right Perron vector times a small scalar is a strict subsolution; monotone iteration under the all-ones supersolution gives a positive equilibrium. For the witness, r=2 gives f=5 and Λ=1/9. A separate exact bracket check uses the sign of 1/10−Λ(f), equal to the sign of f³−42f²+57f+20: the positive quantity 18f²+74f+40 is compared to 4f sqrt((20+f)(20+16f)), and the difference of squares factors as 4(17f+20) times that cubic. The signs at 1, 7/4, 40, 42 are respectively the signs of 36, −225/64, −900, 2414; bisection matches both stated roots.

## originality

PASS

The exact kernel and its general Perron criterion are prior. Within the sources checked, the all-star mortality boundary, global uniqueness of the interior optimum above it, and verified two-sided invasion window go beyond those model statements and the related spectral catalogue entries.

## value

PASS

The mortality threshold distinguishes two globally different responses to exploration under a published birth law, not just a sign in one perturbative regime. An exact witness puts the deterministic invasion criterion strictly between the limiting and maximum capacities, showing that low and high mobility can both be subcritical with all other parameters fixed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
