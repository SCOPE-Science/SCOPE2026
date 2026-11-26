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

The repaired claim in repairs/5/RESULT.md concerns f with at least one directed chain of length ≥2 and includes the ambient identity. A word in f and f⁻¹ acts by signed displacement on each chain wherever defined, and by the same exponent modulo each cycle length on cycles. Exponent zero is idempotent, an exponent of absolute value ≥2 strictly loses rank on a genuine chain, and exponents ±1 with full generator rank force f or f⁻¹. Each generator of the same embedded inverse submonoid has the same rank and the ambient identity is not a generator here. Hence the normalizer acts on this two-element fiber with kernel C_{S_n}(f). Centralizing permutations preserve directed components, with independent phase translations on cycles and position-preserving chain matches, yielding the stated kernel. The displayed reflection squares to 1 and conjugates f to the distinct generator f⁻¹, including the endpoints and undefined positions on chains. Negating cyclic phases negates each translation; reflection independent of component index commutes with index permutations of both types. This proves the split action globally, also with no cycles, trivial rotation factors, or singleton chains. Independent replay `python /workspace/branches/independent_math.py normalizer` checked generating-fiber and stabilizer sizes by finite enumeration through n=5 and evaluated the involution, rotation inversion and index-permutation action for a mixed example with repeated cycles and chains. The examples are not the universal proof.

## originality

PASS

This is a fresh decision on the narrowed repair, not an originality pass for all the frozen claims. The source's assertion that the available generator-fiber and element-conjugacy results do not supply orbit sizes is incorrect: conjugation realizes each generator image, and the fibers all have the same size, so exact sizes follow with the component-centralizer order. Also credit the established single-cycle multiplier splitting. The repair removes the numerical classification and no-chain-arrows splitting from the affected Finding and isolates the genuine-chain involutory section and its simultaneous-inversion action. The inspected exact antecedents give the order or the regular cyclic case, but not this section and action for partial bijections with chain arrows.

## value

PASS

The surviving statement determines the actual stabilizer group and how its complement acts on independent cycle symmetries, not merely how many conjugates exist. In the genuine-chain case, reversing one chain alone does not realize a generator image; a single global reversal realizes the entire quotient and controls the cyclic rotation factors at the same time. This is a natural structural invariant for these embedded objects, not a new presentation of a known census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
