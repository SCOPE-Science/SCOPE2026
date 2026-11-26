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

Tame full ramification at four points gives genus 4. At infinity the orders of x,y,dx are -5,-3,-6; at a finite branch point the orders of y,dx are 1,4. The four independent forms in RESULT.md are thus regular and span. Inverse Frobenius sends the denominator characters 3→4→2→1; the last image is zero because f has degree 3 and contributes no degree 6 term. In the 4→2 step, the leading coefficient of f² is 1. In the 3→4 step the two coefficients A and B have no common zero on the smooth base. Hence the constant rank is 2. On composing, (B^(1/7))^(1/7) multiplies V^(1/7), producing B V^7 inside the 49th root, not B V. The scalar of C² factors as three distinct linear and three distinct irreducible quadratic factors (each discriminant 5), with neither 0 nor 1 a root. The displayed j-fiber identities are exact. Nonidentity anharmonic stabilizers fix either a harmonic parameter (2,-1,1/2, j=6 here) or a root of t²-t+1 (j=0), so the fibers at 6 and 4 are respectively single orbits of sizes 3 and 6. The stable rank is zero and the kernel dimension is two. The distinguished exponent at infinity is 2; the ramification index is 5 there as at the other branch points.

## originality

PASS

Credit the known family, Cartier machinery, and generic invariants. The supported distinction is the complete characteristic-seven Cartier-power jump locus in branch coordinates: an explicitly factored nine-root divisor with exactly the two j-fibers 4 and 6. No inspected source establishes this classification or a stronger statement fixing these parameters.

## value

PASS

The rank of the second Cartier power separates fibers even though both p-rank and a-number stay fixed. In a natural special genus-four family, the exact reduced jump divisor and its two marked branch configurations make the rank condition directly usable without recomputing a semilinear operator at each parameter. This is not a claim to classify Newton polygons or arbitrary isomorphisms of the curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
