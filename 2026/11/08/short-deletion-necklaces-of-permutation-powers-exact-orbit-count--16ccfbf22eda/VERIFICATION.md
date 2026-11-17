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

For a circular repeated permutation P^k, q distinct labelled letters, t<=q deletions, every cyclic output V specifies gaps g_i by congruence g_i ≡ index(v_{i+1})−index(v_i)−1 (mod q) with sum t. For t<q each gap is uniquely determined by its residue and source placements differ only by whole-period shifts. For t=q exactly a single q-long deleted interval can have ambiguous 0/q gap, and all q phase-orbits of those intervals give [P^(k−1)] while every other output retains unique orbit preimage. Burnside on the cyclic k-period action yields (1/k)sum_{d|gcd(k,t)}phi(d)C(qk/d,t/d) minus q−1 only for t=q. Independent direct necklace canonicalization of all tested q=2..5,k=2..4,t<=q and orbit mask code inspection agree; universal classification follows gap uniqueness, not finite extrapolation.

## originality

PASS

PASS qualified: Previous full published embedding-multiplicity spectrum for cyclic permutation powers counts rooted linear target positional embeddings and a weak-descent histogram, whereas the current theorem quotients circular deletion outputs by rotation and pinpoints the first q-to-1 phase-wrap collision. Standard Burnside enumeration alone counts mask orbits, not the precise collision quotient.

## value

PASS

Exact first non-injectivity threshold and explicit orbit correction for deletion descendants of a natural periodic source is a meaningful coding/enumerative combinatorics invariant. The full collision-fiber classification matters for circular deletion channels, even though the theorem stops at t=q and uses standard Burnside and modular gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
