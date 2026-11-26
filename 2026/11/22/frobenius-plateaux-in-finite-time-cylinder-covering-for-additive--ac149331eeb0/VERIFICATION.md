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

For t≥1 each homogeneous or inhomogeneous recurrence extends from t consecutive symbols in both directions because the constant and leading coefficients of (1−S)^t are units. In particular F^t is surjective and the homogeneous solution space has dimension t. The binomial coordinates ((S−1)^j x)_0, 0≤j<t, form a unit triangular transform of the free initial coordinates, so restriction rows are represented by (1+y)^e modulo y^t. Independently reduce the row-space generators before truncation: the first block spans y^j for j<L, and the second spans (1+y^N)y^j for j<R, by triangularity and Frobenius. Subtract matching rows for j<h and retain the first block plus the unmatched second rows when R>L. The resulting basis has pairwise distinct lowest degrees 0,…,H−1 and N,…,N+h−1; modulo y^t only the rows of lowest degree below t survive and they stay independent. Counting them proves the formula, including t=0, t=N, and H=N. Write W=(ker F^t)|_E. If W is full, all preimage fibers meet any cylinder. If W is proper, for any prescribed v choose x with x|_E outside v+W and set z=F^t x; the fiber over z misses that cylinder. Thus the exact full-image threshold holds for every fixed pattern, not just for a quantifier over all patterns collectively. The time plateau has N−H steps of no rank increase. N is the separation of the two starting positions, not the number N−L of unobserved sites. The frozen finite checker was inspected; the all-parameter conclusion here follows from the rank proof, not from the finite evidence.

## originality

PASS

The distinct claim is the sharp rank and filling profile for two prime-power-separated contiguous blocks with both lengths at least two, on the bilateral system. Standard recurrence, polynomial and strong-transitivity tools, and the reported singleton special case, receive no novelty credit. The inspected results do not already determine this profile; see the limits on historical and archive access below.

## value

PASS

A precise delay for observing two contiguous pieces is a natural quantitative strengthening of strong transitivity: it quantifies the compatibility of spatial constraints with every output, not simply eventual covering. With fixed block widths their joint degrees of freedom can remain flat for arbitrarily many iterates by increasing the prime-power separation, then become independent at the exact reported time. The result describes all times and all block lengths in that geometry, with a clean mechanism explaining the delay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
