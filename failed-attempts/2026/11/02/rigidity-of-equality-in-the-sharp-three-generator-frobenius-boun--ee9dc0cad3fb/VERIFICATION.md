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

For X={0,a,b} modulo c and k=ceil(c/2), if kX has stabilizer of order h, Kneser gives at least 2k+1 elements for h=1 or at least (k+1)h for h>1, since X generates the group. Hence kX is the whole group. Equality in the cited bound makes the maximum Apéry representative kb−1. A representative using at most k copies has size at most kb; kb is in a different residue, so the total deficit is exactly one. As b≥2, all k slots are used and exactly one b is replaced by a=b−1. If a≥2 and c=a+t<2a, k≥t+1 and the proposed Frobenius number is the representable value ta+(k−t−1)(a+1). If c≥2a+1, the bound exceeds the two-generator Frobenius number: this holds at 2a+1 and 2a+2 and the bound increases by a−1 under c↦c+2. At c=2a the generator c is redundant and equality holds. With a=1 the necessary b=2 and the convention F=−1 give precisely even c≥4. Both families are nonminimal generating triples.

## originality

FAIL

The distinct indexed record --dae7625c4d38 states and proves the identical iff classification for the identical bound and hypotheses, including the unit-generator convention. It is not a mere title match or the same source file: its elimination argument differs, but its main Apéry-deficit step is also substantially the same. Its displayed catalogue date does not establish priority or how the records came to overlap. The fail is for demonstrable equivalent coverage, not a claim of historical priority.

## value

PASS

As a mathematical question, the equality classification is natural: a general sharp bound has examples, but classifying every equality case shows that a genuinely three-generator numerical semigroup cannot be extremal. This is more than an exact table or a substitution. The classification has intrinsic structural value, but this record adds no new such result beyond the equivalent match.

The dated certificate retains the supplied scientific assessment, sources and limitations.
