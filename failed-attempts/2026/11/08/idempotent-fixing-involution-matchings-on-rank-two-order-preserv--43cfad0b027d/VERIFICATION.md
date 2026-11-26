---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The Finding literally says 'of order two' for every n≥2. At n=2 the only rank-two transformation is the identity, so its sole permutation has order one. The weaker identity Θ²=id, explicitly used in the assumptions, is true for all n≥2. Composition cannot increase rank, and maps of a given rank two are mutually obtainable by precomposing with a monotone two-valued map with the desired cut and postcomposing with a monotone map taking the old image pair to the desired one; hence they are one J=D class. Direct evaluation on the two image values gives the inverse criterion a≤h<b and c≤k<d. In the non-idempotent branches the pair is exactly f_(x,y,z) and f_(z−1,x,y), x<y<z, and both satisfy the criterion. Reversing and re-indexing this pair with x'=n+1−z, y'=n+1−y, z'=n+1−x just interchanges its branch order; the fixed set is also invariant. The separated cuts count the idempotents by sum k(n−k)=binom(n+1,3). Thus the formulas, counts and commutation are all correct and the exact-order wording is the only correctness failure. The separately written checks/rank_reviews.py replayed direct compositions, equivariance and counts at n=2..7 and found one fixed point and no moved elements at n=2. The submitted verify.py and recorded output were read, not executed; their n=2 line itself reports zero transpositions. No finite run proves the general claim.

## originality

FAIL

Multiple earlier indexed reports already give the very same rank-two inverse pairing and counts, including odd sizes. Reversal commutation follows immediately by substituting the reflected sorted triple in that pairing; the n=2 case is the identity. This is direct mathematical coverage, not a decision based on a missing source or a similar title.

## value

FAIL

An explicit inverse pairing at rank two is a worthwhile object, but the earlier records already supply it in full. The only candidate remainder is re-indexing a known pair under reversal and checking the sole permutation of a singleton. That yields neither a new classification of equivariant matchings nor a distinct valuable invariant. Correcting the endpoint wording cannot rescue this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
