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

Induction on syntax gives the root undefinedness support: negation and the locally infectious box preserve it, disjunction unions it, J_2 erases it, and constants have empty support. Distinct supports are distinguished by setting just a letter in their symmetric difference to u at a chosen root. The depth signatures truncate recursively by truncating every type in the successor set. Hence the depth-d signature fixes the previous-depth signature at the root and all previous-depth successor types, which suffices to evaluate a boxed operand, including at a dead end. For the converse, all three atomic colors have Boolean tests. A characteristic formula conjoins the root color test with box of the disjunction of the required successor-type tests and diamond of each required test, where diamond is negation-box-negation on Boolean-valued formulas. Empty conjunction and disjunction work at dead ends. These tests give arbitrary Boolean decisions on realized types; multiplying by the weak-Kleene conjunction of p_i or not p_i over the chosen support exactly inserts the prescribed u values. Thus the sum counts term functions with no overcount. On a cycle the recursive singleton successor signatures read the entire prefix of length min(d+1,n), after which they just repeat previous colors; every such prefix occurs. The exponents, small counts, and strict growth for k>=1 before saturation follow, including the trivial n=1 cutoff. For k=0 the cycle gives two functions at all depths, although nonserial frames can have nontrivial uncolored types. As a separate finite check, direct evaluation of the characteristic tests on a root with two terminal successors, with one letter and depth one, distinguished all 21 types (14 classical at the root) across all 81 world/valuation pairs.

## originality

PASS

The Bochvar semantics and classical characteristic-formula method are antecedents. The supported distinct claim combines the indecomposable root undefinedness supports with a full, depth-preserving Boolean decision algebra on each support's classical locus; it also supplies the exact cycle census and its sharp stabilization. The closest available papers and catalogue analogues do not supply that result.

## value

PASS

This explains structurally how local infection and finite modal observations interact: exactly one support controls the third value while modal types are freely selectable on the rest. The fixed-frame formula applies even with branching or dead ends; the directed-cycle case gives a complete census and exact point at which added modal depth is useless. Both are natural invariants of formula-function algebras and provide useful checks on depth-bounded expressivity, rather than simply counts of small syntactic examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
