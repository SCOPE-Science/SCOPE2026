---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The explicit semidirect product G=F16^+⋊D10 has V=O2(G) characteristic, and G′=V⋊C5 characteristic because ζ−1 is invertible. Thus identity, V\{0}, G′\V, involutions outside G′ and order-4 elements outside G′ are five invariant disjoint sets. Their cardinalities are 1,15,64,5·4=20 and 5·12=60: each reflection coset has 4 fixed translations because Frobenius x↦x⁴ has fixed field F4. Kato’s established theorem says the specified exceptional group has exactly five automorphism orbits. Since these five sets are nonempty and invariant, each is automatically an orbit; no separate 20160-GL4 enumeration is necessary for completeness. Independent F16 fixed-space and partition counts reproduce 1,15,64,20,60. The claim is mathematically correct.

## originality

FAIL

FAIL: Julia Kato’s published characterization identifies precisely this C2^4⋊D10 group as having five automorphism orbits. Given that proven count, the candidate’s five elementary characteristic-subgroup/order strata force the entire orbit partition and sizes immediately. Therefore the alleged orbit classification is a direct corollary of a stronger prior result combined with routine element counts; absence of the numerical tuple from an abstract or exact-match search is not novelty.

## value

FAIL

FAIL. Although the orbit-size tuple is a well-defined invariant of an interesting group, the five-orbit theorem already identifies the entire partition once combined with the most elementary characteristic-group and fixed-field cardinality calculations. The purported new value is merely a numerical unpacking of a known stronger classification and does not present a mathematically substantive structural refinement or nontrivial open boundary. Exact arithmetic and reproducible enumeration alone do not establish scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
