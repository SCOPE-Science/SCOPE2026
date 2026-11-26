---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The quotient and formulas check for every stated n. For M=z^3w^2 u_1^2 ... u_n^2 and T=xu_1, the invariant opens D(1-M), D(M) cover the quotient; upstairs x≠0 is D(1-M)∪D(T) and u_1≠0 is D(M)∪D(T). This justifies the use of the two gauges for the affine invariant quotient, including over other fields. At T=0, E,W',U_i are units and the derivatives with coefficients 2 and 3 cannot both vanish in any characteristic. B=EW' yields E=B^(-2)P^(-1), W'=B^3 P; the equation T=0 trivializes the normal line on a neighborhood of the whole divisor. The preceding term H^(k−1)(U) and following term H^k(U) vanish for k≥2, so the integral Thom–Gysin maps are isomorphisms, with projection and self-intersection giving zero positive-degree products. General position moves loops into the contractible open stratum. The algebraic Gysin map adds one Tate twist. Chow localization generates CH^1 by the divisor, whose primitive integral Gysin class shows infinite order, and kills higher codimensions. The scissor relation and disjoint rational points on the two integral-model strata give the remaining formulas. This is a symbolic proof check; the frozen finite-field verifier was inspected but not executed and does not test the Gysin or Chow assertions.

## originality

FAIL

A distinct indexed result covers the same family, both strata, the normal line, simple connectivity and the square-zero integral ring, and gives a stronger wedge-of-spheres conclusion. The remaining Chow, mixed Hodge and counting formulas are direct deductions from the already available algebraic charts and strata using standard functorial formulas. This is a statement-level coverage decision, not an assertion that one same-day record preceded or copied the other.

## value

FAIL

The geometry and topology of this natural family are worthwhile, but already covered by a distinct stronger description. The remaining list uses the identical charts and reduces to standard Gysin, Chow localization, scissor and point-count evaluations; no separate nonmechanical result remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
