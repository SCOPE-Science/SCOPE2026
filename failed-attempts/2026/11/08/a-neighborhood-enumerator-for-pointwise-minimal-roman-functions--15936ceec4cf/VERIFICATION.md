---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Roman domination is monotone under pointwise label increases, so local one-coordinate decreases suffice for minimality. Fixing X as the core vertices labeled 2 forces (2,0) at X, (0,1) on the external neighborhood N(X)\X, and independently (0,2) or (1,1) on each vertex outside N[X]; local zero-defender checks prove both necessity and sufficiency. The resulting weight is 2n-|N(X)\X|=n+|X|+|V\N[X]| and multiplicity 2^{|V\N[X]|} for every finite simple H. Counting independent subsets of a bipartite neighborhood double corresponds to choosing X and an arbitrary subset of V\N[X]. Minimum exponent n+gamma(H) follows because X union unexposed is dominating; maximum coefficient is product over components (2^{|Q|}+1) by zero boundary. Four-case bipartite-base specialization follows from the same sum. Independent direct brute enumeration for H=K2 gives 2 z^3+5 z^4. This is a universal structural proof, not an extrapolation from checks.

## originality

FAIL

Earlier Resultary works on 2026-10-18 and 2026-11-02 give the identical entire weight polynomial for all one-leaf coronas and the same local state classification. The current bipartite independent-set rephrasing, minimum-weight consequence, top coefficient and complete-bipartite specialization follow directly from that already known formula; no substantive independent surviving new theorem is present.

## value

PASS

A complete coefficient-by-coefficient classification for pointwise-minimal Roman functions on all one-leaf coronas is a motivated structural counting theorem with connections to domination numbers and independent-set enumeration. It would be valuable as a mathematical fact, even though it is already published, so novelty failure is assessed separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
