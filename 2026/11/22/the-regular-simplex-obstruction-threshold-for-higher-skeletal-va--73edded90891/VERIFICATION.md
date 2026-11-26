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

Using the vertex Gram matrix (diagonal n², off-diagonal −n), the centroid of m=n−k+1 selected vertices is perpendicular to every difference between them, so the squared affine-face distance is nk/(n−k+1)≥k. The j-dimensional edge Gram determinant gives volume [n(n+1)]^(j/2)√(j+1)/j!, including the convention at j=0. Face counts then give the frozen ratio. Its consecutive factor is √(n(n+1)/((j+1)(j+2))), >1 until the last equality. At j=0 the ratio is <1, whereas AM–GM on 1,…,n gives R(n,n)≥√(n+1)(n/(n+1))^(n/2)>1 for all n≥2. Thus the first qualifying index lies between 1 and n−1, with n=2 included. Independently, Stirling's formula at x=sn cancels both powers of log n and leaves −log s+s/2−(log 2π)/2 after the order-n term. At x=αn+t for bounded t this gives slope −log α>0 and the stated β; the digamma asymptotic gives strict local increase. Bracketing β by fixed displacements then checking the nearest integers, together with the exact discrete single crossing, gives ceil of the actual root, not of the asymptotic truncation. At k=n−j the simplex is admissible and violates the proposed universal inequality precisely when j<j_*(n); no universal lower bound on k_max is inferred. A separate bounded integer recurrence check compared the squared-ratio numerator and denominator, multiplying respectively by n(n+1) and (j+1)(j+2). For n=2,3,4,10,100,250,400 the thresholds were 1,1,2,3,33,82,131. The arithmetic/spot-check replay path skeletal_threshold_check.py was read, not rerun, and the finite evidence is not the proof of the infinite statement.

## originality

PASS

Credit the classical face totals, direct ratio calculation, and Zwierzyński's prior example. The supported distinct claim is the single crossing across all face dimensions, its two-term displacement, and the resulting quantitative obstruction to a universal initial codimension range. This does not answer the unrestricted range question.

## value

PASS

The useful result is not a new simplex volume formula. It gives a reproducible exclusion boundary for a specific published open higher-skeleton question: even a single centered admissible simplex rules out a linear portion of the candidate codimensions, with a precise finite-dimension crossing and an asymptotic constant displacement. The explicit bound is useful independent of whether other polytopes sharpen it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
