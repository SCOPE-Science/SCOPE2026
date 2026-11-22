---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For c=a/(a+b), 1<=a<b coprime, the allowed transition after a one is governed by integer height H=aN0−bN1; zeros add a, ones subtract b. Legal zero states have a free zero (+a) and whenever h<b the legal block 10 (−(b−a)); lowering h>=b with a chosen one and finitely many forced ones reaches h<b. Since gcd(a,b−a)=1, any integer zero state connects to any other by blocks 10 followed by zeros, including reachable states from an initial zero. This gives a bridge from any finite language factor u to v via zero-state communication, proving topological transitivity. Construct ω=1 0^m 1^r 0 with am≡1 (mod b), am>b, r=(am−1)/b+1; its initial forced zero and final long 1-run respectively impose h<=b−1 and h>=b−1. Every occurrence therefore starts at exactly h=b−1 and all pairwise returns have zero discrepancy, hence lengths divisible by a+b, excluding mixing. Independent finite transition replay verified unique marker start for six coprime pairs; infinite statement rests on Bezout and height argument.

## originality

PASS

Reyes, arXiv:2611.10995v1, Definition 2.2, Theorem C and Question 7.1, treats all parameters for nonsoficity and absence of specification but identifies established transitivity only for the c=k/(k+1) family at or above 1/2; the 0<c<1/2 rational family in the claim is distinct. Becker–Baraviera 2023 introduced the same digit-density system but its abstract is insufficient to rule out all unpublished implications; recorded as priority risk. Same-day Resultary results for rational >=2/3 or >1/2 prove nontransitivity in disjoint parameter ranges, while the irrational-frequency transitivity theorem has disjoint parameter type. The new combined transitive/nonmixing classification is not subsumed by these.

## value

PASS

Transitivity and mixing are central dynamical invariants for a non-sofic family with a long-standing parameter classification question. All rational frequencies strictly below 1/2 and an explicit modular return obstruction constitute a natural infinite structural regime, not a finite example or name change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
