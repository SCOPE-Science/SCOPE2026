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

For all n>=7 over C, generically the three initial observed Hankel values a=x1,b=x2,c=x6 give the recurrence-parameter curve F(s,t)=(2as+b)t^2+(as^3+3bs^2)t+bs^4-c=0. Its quadratic discriminant is a generic squarefree sextic, hence its smooth projective model is irreducible genus two. There are exactly three polar places of the function x_n: the two distinct branches P,Q over s=infinity and the simple t-pole R over s=-b/(2a). Their respective pole orders are n-6, n-1-1_{n=2 mod4}, floor((n-1)/2); at Q the period-four cancellation is shown via the recurrence polynomials f_n(-1/2) and their derivatives, with nonzero next coefficient for n>=10. The sum is 2n-7+floor((n-1)/2)-1_{n=2 mod4}. The recurrence chart is birational to the generic rank-two locus, so pole degree equals the generic number of completions without multiplicity. Specializations and finite tests corroborate but do not prove generic irreducibility or the all-index pole orders.

## originality

PASS

The full formula for the exact generic projection degree of {1,2,6,n} for every n>=7 survives prior comparisons. Reed–Tsakiris gives generic finiteness and a nonsharp upper bound, plus six exact special n values; its exact general formula concerns {i,i+1,i+2,n}. Other published exact Hankel degree laws examine distinct coordinate samples {1,2,4,n}, {1,2,5,n}, {1,3,5,n}, which do not imply this genus-two three-pole law. The six tabulated values are already known, not a novelty contribution.

## value

PASS

Exact field-extension degrees for sparse rank-two Hankel completions are natural algebraic-matroid invariants and determine the number of generic solutions. Filling the all-index gap of a specifically tabulated yet only bounded sixth-gap sampling pattern, together with genus-two and period-four pole structure, is a motivated nontrivial classification beyond textbook recurrence manipulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
