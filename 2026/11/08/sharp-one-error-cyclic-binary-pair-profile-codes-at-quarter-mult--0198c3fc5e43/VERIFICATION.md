---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The cyclic ordered pair histogram necessarily has p01=p10=t and p=(n-k-t,t,t,k-t); all t>=1, t<=k<=n-t are realized by explicit run words, plus two constant profiles. Replacing at most one observed pair label gives integer-histogram distance half L1, equal to max(|Δk|,|Δt|)+|Δt|. Disjoint radius-one corruption balls therefore require distance>=3. At length 4m the source partitions D_4m into m² four-point diameter-two cliques using first two transition rows and shifted D_4(m-1); each selected residue k-2t=0 mod4 is pairwise distance>=3 and meets each clique once. Add two constants to get A(4m)=m²+2. Embedding feasible profiles into longer lengths proves the floor/ceil general n bounds. Independently verified selected-code sizes and pairwise distances for m=1..9; analytical clique induction establishes all m.

## originality

PASS

PASS best-of-knowledge: published DNA substring-profile coding literature supplies count-vector metrics and general constructions, not the inspected exact 2-gram cyclic binary one-error optimum m²+2 with matching all-m cliques and residue code. Enumerating Markov types counts clean histograms, not disjoint radius-one corruption balls. Positional cyclic symbol-pair distance is a different channel from unordered adjacent-pair multiset label substitution. No stronger exact same-channel coverage found in Resultary search; residual possibility of equivalent lattice-code result remains.

## value

PASS

PASS: maximum message count for one arbitrary corrupted cyclic adjacent-pair multiset is a natural zero-error read-channel capacity. A sharp formula at all 4m and a provably optimal explicit code, plus leading n²/16, give exact finite-rate limits useful in short-read and profile-code design, beyond known asymptotic order or clean profile counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
