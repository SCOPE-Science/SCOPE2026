---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The only possible terminal uncovered set in G=K_{2m} minus a perfect matching has 0 or 2 vertices. With k untouched forbidden pairs and s singles the D=binom(2k+s,2)-k admissible edges partition into binom(s,2),2ks,2k(k-1) transition classes; exact recurrence is correct. One tagged pair survives with limit m^2 p_m→3/4 using survival telescoping and two-tag suppression, hence m Pr(R_m=2)→3/4 and m E R_m→3/2. Independent labeled-state and reduced recurrence calculations matched m=2..7 including 0,1/5,8/65,1231/11375. Infinite limit follows from inequalities, not finite experiments.

## originality

FAIL

The exact same graph, process, terminal law, identical reduced-state recurrence, first values and limit were established in an already published same-day cocktail-party result; a second published same-day theorem gives stronger finite and asymptotic error bounds, and another general theorem covers arbitrary degree-two forbidden graphs. No unsupported within-day chronology is asserted; mathematical implication is decisive.

## value

FAIL

Sharp 3/4 rare-jam coefficient on an almost-complete graph is intrinsically natural, but two separate published complete theorems already give precisely the same recurrence and coefficient, one with O(m^−1/3) rate and another with O(log m/m²) rate, while a uniform degree-two-forbidden-graph theorem subsumes the asymptotic. No original independent valuable claim remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
