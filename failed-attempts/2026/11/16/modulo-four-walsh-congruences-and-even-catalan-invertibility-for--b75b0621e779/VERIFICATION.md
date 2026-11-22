---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The identity (-1)^x=1−2x for Boolean edge indicators implies a product expansion mod4 retaining only the constant and linear terms. Munagi Theorem 2.1 already counts exactly C_d C_(n-d) noncrossing partitions containing each fixed d-adjacency. Thus W mod4 follows rigorously at every H; Deutsch–Sagan Theorem 2.1 gives ν2(C_k)=s2(k+1)−1. A product is odd iff both arc lengths have all-ones binary values, which gives critical chord set and parity split. For odd n critical set is empty; s2(n+1)=1 or 2 makes every W respectively odd or ≡2 mod4. For even n, n+2 sum-of-two-powers criterion and parity of critical edges yield exactly half the frequencies W≡2 mod4 if s2(n+2)<=2. Rank lower bounds and norm<=1/2 for even-Catalan odd n follow from nonzero integer W. Independently enumerated all NC partitions up to n=6, checked all fixed-pair marginals and every character up to n=5; finite tests corroborate but do not prove universal statements. These proofs respect unnormalized counting convolution.

## originality

FAIL

FAIL. The claimed universal mod4 Walsh theorem follows immediately by multiplying standard Boolean characters and dropping all quadratic terms mod4, once the exact pair co-block incidence counts in Munagi (2016) Theorem 2.1 are supplied. Deutsch–Sagan (2004) Theorem 2.1 supplies the exact Catalan 2-adic valuation and odd Catalan criterion. The remaining zero-free classes and half-frequency parity claims are elementary binary-sum consequences, not separate structural information or an independently new theorem. The source RESULT.md itself reconstructs precisely Munagi’s chord-count proof as if new and omits that primary antecedent. Matching these implications, rather than matching a paper title mentioning Walsh, defeats originality under the established corollary-coverage rule. This is not an access uncertainty or computational error.

## value

PASS

PASS as an intrinsically motivated statement about the first two-adic layer of an all-frequency transform for a natural Catalan incidence set; the infinite even-Catalan invertible family and half-rank lower bound would be useful if independently new. Its independent value does not overcome that the supplied result is a routine algebraic extraction of already-published stronger ingredients, so overall scientific rejection is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
