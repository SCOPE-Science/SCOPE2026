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

Closure means choosing whole reverse-complement orbits. Testing every ordered overlap within an orbit and between compatible orbits gives a bijection between admissible literal codebooks and cliques, with codebook cardinality equal to the sum of orbit sizes. Positive weights imply every maximizer is inclusion-maximal. The independently written integer enumeration retained all ties and returned M=(2,1,0,1,0,2,0,5,2,14,10,42), T=(1,2,1,2,1,2,1,2,4,6,96,1134) for n=1,...,12. The empty clique counts once when there are no eligible orbits, and n=1 has no proper nonempty overlap. All 1134 length-12 optima have 16 pairs; weight 42 then forces 10 fixed words. Separately, direct checks of the displayed length-12 witness found 42 distinct binary words, closure, 10 fixed words, and zero prohibited matches in 19404 ordered prefix/suffix comparisons.

## originality

PASS

To the extent supported by inspected evidence, the distinct result is the exact weighted capacity and labeled equality-case census through length 12, including the length-12 composition. Nonempty feasibility and asymptotic rate are credited to the known strand-closed binary result, and ordinary non-overlap bounds and constructions are background. No inspected result supplies the claimed joint census by specialization.

## value

PASS

Short block lengths matter for synchronization under explicit two-orientation closure. The census gives exact achievable cardinality where asymptotic rate does not help, a concrete drop from 14 to 10 when length goes from 10 to 11, and an equality-case constraint shared by all 1134 optima at length 12. These are useful benchmarks for constructions and for explaining the role of fixed versus paired words, not just another witness to known existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
