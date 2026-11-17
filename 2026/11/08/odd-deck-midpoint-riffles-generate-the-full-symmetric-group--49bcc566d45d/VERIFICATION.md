---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Actual rational midpoint-key ordering gives cuts 1 and n-1 as cycles of length (n+1)/2 with supports meeting at exactly one point. Their commutators produce mixed three-cycles, which generate A_n. The cycles are odd iff n=3 mod4; at n=1 mod4 the second cut has 4t-1 cross-packet inversions and therefore is odd. Independent exact Fraction-generated permutations and Schreier group orders: n=3,5,7,9 give two-cut orders 6,60,5040,181440 and three-cut orders 6,120,5040,362880. Identity cut has positive binomial mass, so finite-group random walk is irreducible, aperiodic and uniform stationary. No mixing time is proved.

## originality

PASS

Jiang's original binomial-cut deterministic midpoint model addresses even-n mixing and the accessible abstract does not claim odd-n irreducibility. Two-cycle group-generation results are foundational, not the model-specific identification of cuts and odd-deck subgroup. Equal-pile perfect shuffles and uniformly random conditional interleavings have different hypotheses. Full Jiang and 2017 primary texts were inaccessible, which is a concrete priority risk, not automatic scientific failure.

## value

PASS

Determining actual allowed positive-probability generator cuts and the full odd-deck permutation group fills a qualitative ergodicity gap in a concrete shuffle, despite not yielding a mixing bound; the two-cut parity split is exact and relevant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
