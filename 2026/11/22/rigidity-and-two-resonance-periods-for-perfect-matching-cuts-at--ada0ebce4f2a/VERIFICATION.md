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

Since n>2k the graph is connected and cubic with three distinct neighbors at each vertex. For any cut with one crossing at each vertex, the outer transitions t determine each spoke difference d_i=1−t_(i−1)−t_i, and therefore both shores up to simultaneous complement. Conversely an even cyclic t with no consecutive ones reconstructs the shores, and the remaining exact test is one crossing at each inner vertex. The 2k+2-bit windows are precisely the span needed for the central test; their overlaps identify closed walks of length n with indexed cyclic words, including when a window wraps. I reproduced the cyclic core using the simplified inner crossing parity t_(j−1)+sum(t_(j+1),…,t_(j+k−2))+t_(j+k) modulo 2, and iteratively removed sources and sinks rather than using the supplied Tarjan code. Every surviving state had one predecessor and one successor. The replay produced (arc count, incident state count) (180,280), (720,1120), (2880,4480), (11520,17920), respectively, with cycle representatives 0; 0,01; 0; and 0,01,00101 and the same minimum states as the frozen table. Source/sink removal cannot delete any closed walk, so this is exhaustive. The alternating word yields two phases with even parity exactly when 4 divides n; the five-period word yields five phases with even parity exactly when 5 divides n and has one crossing spoke per period. The zero word gives the spoke cut. Different indexed words give different edge sets, not extra shore orientations. This proves the four all-order formulas; the recorded direct tests are corroborative, not the all-order argument.

## originality

PASS

The prior jump-3 theorem has exactly the jump-7 count formula, and earlier jump-specific theorems cover individual isomorphic instances. Those overlaps are real but do not supply the all-admissible-order classification at the four claimed jumps. The inspected general perfect-matching-cut sources address the same predicate but do not give that enumeration or its exact cyclic cores. No inspected exact source establishes an equivalent all-order census for these jumps.

## value

PASS

These are the consecutive next small jumps after the two prior classified families, testing whether their period-four and period-five resonances persist. The exact answer separates two rigid families, one with only the first resonance, and one with both. The proof gives the actual cut types, including spoke content, and applies to every admissible order; it is not a table of small graphs or a certificate of the obvious spoke cut alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
