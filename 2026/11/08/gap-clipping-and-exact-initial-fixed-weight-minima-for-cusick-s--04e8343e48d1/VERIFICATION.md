---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Carry conservation s_2(n+t)-s_2(n)=k-C identifies the nondecrease event as C<=k. If a carry enters an inter-one zero run, its first incoming carry already contributed at least one to C; after k zero digits any continuing carry would exceed the budget. Longer runs therefore cannot change retained probabilities, proving d_i -> min(d_i,k+1) for all k and finite bound t<2^(k^2). Exact two-state carry updates and geometric tail give common denominator 2^(k^2+k+1). Independently implemented Fraction recursion and an unrelated C++17 128-bit exhaustive canonical-gap enumerator; all 5,063,361 tuples k=1..8 reproduced every minimum and complete odd optimizer list (1;5;11,13;27;107;219;439,475;951), with no optimizer at a clipping boundary. This verifies all-weight lemma plus finite exact table, not any larger-k table.

## originality

PASS

Fixed-t carry recurrences and individual small values, and Cheng large-k sharp extremal asymptotics, are antecedents. A separate October 25 finite-gap shielding theorem treats ONLY widely separated set bits (gaps at least k), not arbitrary short-gap clipping or complete minimizer search. The universal short-gap-to-finite-search reduction and exact initial eight-weight optimal sets are not implied by any inspected full comparator.

## value

PASS

Cusick fixed-weight infima are a natural studied extremal invariant; uniform exact attainment/search cutoff for every weight changes an infinite optimization into a finite certified task, and the first eight complete extrema provide meaningful benchmarking and optimizer geometry, not arbitrary small numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
