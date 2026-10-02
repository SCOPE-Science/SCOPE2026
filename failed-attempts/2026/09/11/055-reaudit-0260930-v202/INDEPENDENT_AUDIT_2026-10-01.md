# Independent mathematical audit — 2026-10-01

## Slater-dual mod-18 product with mod-3-sensitive gaps is false at n=3; mod-5 family fails at n=0 with full dissection log to O(q^80)

**Disposition:** failed.

The low-degree counterexample is correct and apparently not already stated in the inspected modulus-18 literature, but it fails the scientific-value bar because it is only a cheap rejection of a narrowly specified candidate.

## Correctness

**PASS** — The disproof is hand-checkable. Under the stated gap rule, the single partition [3] gives C(3)=1, whereas the product with allowed residue parts 2, 7 and 12 modulo 18 has coefficient zero at q^3. Both series have constant term one, so no positive q-shift repairs the identity. Likewise [4] is the only admissible partition of 4, so C(4)=1 and the proposed C(5n+4) congruence fails at n=0. The committed finite expansion is corroborative rather than necessary.

## Originality

**PASS** — Searches of the primary modulus-18 Rogers-Ramanujan literature and Resultary did not locate this exact candidate gap rule/product or the same minimal counterexample; the known modulus-18 identity families are different statements.

## Scientific value

**FAIL** — The final mathematical content is a tiny-instance rejection of one narrowly specified candidate: n=3 kills the product and n=0 kills the congruence. No structural correction, classification, or independently motivated boundary survives. Under the audit value bar this is a cheap negative check rather than a worthwhile gap.

## Sources checked

- McLaughlin and Sills, Ramanujan-Slater type identities related to the moduli 18 and 24, J. Math. Anal. Appl. 344 (2008).
- McLaughlin-Sills-Zimmer Rogers-Ramanujan-Slater survey/database search.
- Resultary semantic search for the exact modulus-18 gap/product candidate.
- Audited package RESULT.md, artifacts/verify.py and artifacts/verify_results.json.

## Residual risks

- No corrected product or structural classification is established.
