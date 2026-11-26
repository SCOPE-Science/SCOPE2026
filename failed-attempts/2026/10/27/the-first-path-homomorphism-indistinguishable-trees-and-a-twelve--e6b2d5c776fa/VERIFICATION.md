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

PASS

The forward walk recursion counts all path homomorphisms, including W_0=n. Cayley–Hamilton on the block diagonal of the two adjacency matrices makes the first 2n entries conclusive at equal order. An independently written rooted-multiset generator covers every rooted tree by its multiset of child trees and deduplicates free trees by the least rooted code over all possible roots. Replay with python3 /workspace/audit_evidence/walktrees.py gave no collisions at orders 1–11 and 550 profiles for 551 order-12 trees, with exactly the displayed pair in the repeated class. The independent computation checked the pair's first 12 entries, matching polynomial and rational generating function. The complement determinant lemma expresses the complement polynomial in terms of the adjacency polynomial and the signed walk resolvent; conversely the two polynomials recover that resolvent. The only repeated profile in the range has a common adjacency polynomial, so the equivalence with generalized spectra follows. This is an exact finite computational check, not formal verification.

## originality

FAIL

The earlier October 26 Resultary branching-probe record explicitly gives the same unrooted walk-profile threshold and unique order-12 pair. The earlier September 8 generalized-spectrum census and that direct walk census together imply the equivalence of partitions through order 12: the generalized-spectrum partition refines the walk partition and the two have the same sizes at every order in range. The witness itself is the earlier generalized-cospectral pair. The frozen work reproduces these results but does not establish a distinct finding.

## value

FAIL

The first collision for a natural weak invariant would be a meaningful finite boundary if unknown. Here the census and witness are already established, and equality of the two partitions follows directly from prior counts and the standard refinement. The submitted replay offers corroboration but no additional mathematical fact or new useful boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
