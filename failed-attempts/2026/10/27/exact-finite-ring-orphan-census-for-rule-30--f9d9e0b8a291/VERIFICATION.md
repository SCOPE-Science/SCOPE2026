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

A length-n closed path in the pair graph imposes exactly cyclic consistency of overlapping pairs, even at n=1,2, so Boolean diagonal reachability detects existence, not number, of predecessors. Independently reproduced the exact finite certificate by using each output bit b as the backward function (u,v)→(b XOR (u OR v),u), rather than the uploaded Boolean matrix code. Replay: python3 /workspace/independent/rule30.py. It found 41 reachable functions, 11 with no fixed point, the six initial orphan counts 1,1,3,5,6,12, and zero recurrence errors for all 41 required shifts n=1..41; direct integer-rotation enumeration agreed for n=1..14. Integer word populations evolve under the 41-by-41 transfer, so Cayley–Hamilton for the shifted scalar error sequence forces every later error to vanish. The order-six annihilator factors as (t^3-1)(t^3-t^2-2), so matching six starts proves the cubic power sum plus period-three correction and the stated generating function. The real cubic root is unique and in (1,2); the product of its conjugate pair is 2/alpha, whose square-root modulus is below alpha by the cubic equation. Both constant inputs map to zero on the ring. On the bilateral shift any finite target window can be inverted from a pair on its right by left-permutivity, and compactness yields an unrestricted predecessor. Thus finite nonsurjectivity and bilateral surjectivity are consistent.

## originality

FAIL

Two distinct indexed records cover the same all-period indexed Rule-30 law, one by the same 41-state transformation method and one as the zero class of a full multiplicity law. This establishes equivalent and stronger catalogue coverage, not the order of discovery, historical priority, or dependence. The generating series and sharp exponential rate follow algebraically from the same exact recurrence; the finite table alone would not have justified this verdict.

## value

FAIL

The all-period same-period image would be a useful exact invariant in the absence of equivalent coverage. In the available catalogue it is known at all sizes and is contained in a strictly fuller invariant; the rational series and dominant-root rate are routine consequences of that same census. Neither the certificate nor repetition of small-ring counts supplies a separate valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
