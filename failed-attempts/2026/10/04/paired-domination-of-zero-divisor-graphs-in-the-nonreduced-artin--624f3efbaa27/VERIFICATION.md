---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

An Artinian local factor has one maximal associated prime, so the product has k. The published Noetherian theorem gives a minimum total dominating set of k annihilator witnesses and its proof shows those witnesses pairwise multiply to zero, hence form a clique. The parity lower bound and perfect-matching upper bound follow; in odd rank the package's x_2+x_3 witness supplies the extra adjacent vertex. The proof is correct.

## originality

FAIL

Kiani–Maimani–Nikandish prove for a Noetherian ring with more than one relevant maximal associated prime that gamma_t is the number of maximal associated primes and explicitly choose annihilator witnesses x_i satisfying x_i x_j=0 for i not equal to j. Thus their minimum total dominating set is already a clique. In a product of k Artinian local rings, the maximal associated primes are precisely the k lifted maximal ideals. The claimed least-even-above-k paired value is therefore again the direct parity consequence of a published minimum total-dominating clique, with the odd-k extra vertex construction elementary. Originality fails by implication.

## value

FAIL

The nilpotent-thickness interpretation is pleasant, but the formula is a routine Artinian specialization of a published general total-domination clique theorem plus the even-cardinality requirement. It does not introduce an independently substantive invariant computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
