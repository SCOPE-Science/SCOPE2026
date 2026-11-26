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

The first two measurements have rank two, so the delay map embeds the phase circle. For every initial phase a finite initial orbit segment is a twofold net at any prescribed resolution. Uniform continuity of the map and its inverse on the embedded circle forces every delay-nearest phase to approach its base phase uniformly, including ties. The exact chord cancellation evaluates the relative test at the pair midpoint modulo pi, so the ratios converge uniformly to the corresponding phase function; the absolute test vanishes uniformly by equidistribution of the first two moments (sample standard deviation tends to 1/sqrt(2)). Writing the squared ratio as (b·v)^2/(v^T A v), the Gram determinant is 2 sin²(theta)+sin²(2 theta), and the numerator of b^T A^(-1)b is the sum of sin²(m theta) for m=1,2,3. These give the claimed E. For 0<R²<E the threshold quadratic form has trace 1-3R² and determinant R² det(A)(R²-E)<0; its two angular cones give the stated arctangent and its finite boundary is null for equidistribution. At and above the maximum the strictly greater relative test is impossible for every chord, not merely almost surely; the absolute test can still matter at small finite n. The derivative changes sign once at z=(sqrt(2)-1)/2. At this point 4cos²(theta)=2sqrt(2)-2 has a negative algebraic conjugate, whereas for a root of unity all conjugates of (2cos(theta))² are nonnegative. Thus the minimizers really are irrational rotations.

## originality

PASS

No inspected distinct prior result gives or implies the exact fixed-cosine, fixed-tolerance angular law and its sharp irrational-angle optimization. This is a bounded best-of-knowledge assessment, not a priority certificate.

## value

PASS

This is an exact calibration of a standard diagnostic on a canonical smoothly embedded signal: it quantifies how a positive false-neighbour fraction can persist despite injectivity, distinguishes a strictly positive limit from an eventual zero, and identifies the best worst-case relative threshold as the frequency varies. The fixed-observable benchmark fills a gap left by generic large-tolerance results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
