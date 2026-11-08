---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS for the narrowly stated feasibility equivalence. For s∈(0,1],r∈(0,1],p∈(0,1], the endpoints of Barsukow Eq (118) have positive denominators, and for p<s nonemptiness is equivalent to (s-p)/(1-s/6)≤1 and ≤(1+rs-p)/(1+s/6). The first is s≤6(1+p)/7; crossmultiplication of the second gives (1+r)s²+(7−6r−2p)s−6≤0. The positive quadratic root yields exactly the stated s_max and limiting p↓0 yields uniform s_star, with breakpoint r=1/6. For p≥s the same bounds hold automatically. This is a correct algebraic translation of the published interval; it is NOT a sharp CFL necessity for any solver.

## originality

FAIL

FAIL: Barsukow Theorem 4 Eq (118) publishes the identical interval, and its primary proof Eqs (130)-(133) publishes the TWO EXACT EQUIVALENT FEASIBILITY CONDITIONS, not merely the conservative 0.712 bound. Eq (131) reads s≤6(1+p)/7 after p=1/(R+1); Eq (133) is precisely 6+(6r−7+2p)s−(1+r)s²≥0 after r=a_min/a_max. The proposed s_max is simply the quadratic formula applied to that already displayed exact condition, while s_star and r=1/6 are immediate minimization of those published inequalities. This is decisive mathematical implication even though the prior paper does not print the final root/phase-diagram wording. Under implication-based novelty this entire final claim is covered. No repair claimed; original preserved.

## value

FAIL

FAIL under the meaningful mathematical-gap bar: practical clarification of a safe CFL number is useful as a presentation of Barsukow’s exact published conditions, but the proposed stand-alone mathematical result performs only substitution, a quadratic formula, and monotonicity of the already supplied feasible interval. It does not add a new stability/algorithm theorem, nonstandard lemma, or previously undetermined natural invariant beyond the explicit conditions in the original paper. The numerical gain over the author’s conservative corollary is real but mechanically extractable from equations (131),(133), so does not establish independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
