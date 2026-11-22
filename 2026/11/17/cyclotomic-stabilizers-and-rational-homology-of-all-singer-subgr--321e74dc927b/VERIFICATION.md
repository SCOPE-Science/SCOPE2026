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

For every q a prime power, n≥4, t|(q^n−1)/(q−1), H_t the order-t projective Singer subgroup, the building of nonzero proper F_q-subspaces is simply connected by Solomon–Tits. Fixed simplices of projective scalar degree d are flags of F_{q^d}-subspaces; degree n gives empty fixed set, d<n gives building over F_{q^d}. Maximal proper subfield stabilizers generate the order-L cyclic subgroup with L=N/Φ_n(q). Intersecting with H_t has order gcd(t,L), so Armstrong orbit π1=H_t/(H_t∩C_L)=C_{t/gcd(t,L)} and H1(Z) matches. Solomon–Tits reduced Euler of smaller buildings plus Lefschetz trace gives (-1)^{n−n/d}q^{d binom(n/d,2)}; Möbius inversion counts degree-d subgroup elements a_d(t), and rational finite averaging gives only degree n−2 homology with (1/t)Σa_d(t)trace. Independently recomputed all-subgroup arithmetic examples (q,n)=(2,4),(2,6),(2,8),(3,4),(3,6),(4,4), yielding e.g. full C15 quotient C5 & topBetti4, C63 quotient C3 & topBetti518, C40 quotient C10 & topBetti18. Inspected actual verify_singer.py including finite-field enumeration q=2,n=4,6. Carefully no unsupported higher integral homology claim; boundary q prime powers and n≥4 essential.

## originality

PASS

Best-of-knowledge originality after actual statement-level comparison: new scope not logically covered by primary work or published stronger indexed analogues; prior constituent lemmas and any exact known special cases are explicitly acknowledged.

## value

PASS

Natural all-prime-power/all-vector-rank/all-Singer-subgroup classification of geometric orbit π1 and rational top homology, including cyclotomic stabilizer arithmetic and subgroup-dependent torsion in H1. Extends a recognized full-Singer rank-four case substantially and unifies fixed subbuilding types, rational character and quotient Betti formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
