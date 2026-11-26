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

In the exact coefficient norm the basis action sends e_1 to e_0 and e_n to w_n e_{m(n-1)} for n>=2, with distinct targets. Thus the two Gram operators are diagonal and the commutator diagonal is -1 at zero, and w_k^2 minus the unique incoming square w_{k/m+1}^2 when m divides k. Exponential decay beats every polynomial for fixed h, also for every positive Schatten exponent. The finite trace sum telescopes with incoming indices 1 through floor(N/m)+1; the limit is zero. Nonmultiples are positive; on multiples the outgoing/incoming weight-square ratio tends to zero for fixed h. For h tending to zero, h^2 times the outgoing and incoming squares converge away from x=0 to A(x) and C(x)=A(x/m), respectively, uniformly on compact scaled intervals. The exact factors (1-1/n)^s are uniformly bounded for n>=2, so scaled weights near zero are O(x^2+h^2), with exponential tails bounded by a polynomial times exp(-x/m). This proves the local law on the m separate residue classes, and exponential domination extends it to |y|^p for every fixed p>0 and to a supremum limit. The only positive zero of A-C solves exp(2x(1-1/m))=m^2; max(A)=max(C)=m^s exp(-2), attained asymptotically by the outgoing-only branch. The limiting signed integral is zero since integral C=m integral A. Twice the negative mass gives the stated trace coefficient by integrating x^2 exp(-a*x) above the zero. For p=2 the combined integral is 2 integral A^2 minus (2/m) integral AC; the x^4 gamma integrals give exactly the stated coefficient. Small exceptional indices do not affect any limit.

## originality

PASS

Exact same-operator action on the Dirichlet slice and a closely related signed self-commutator boundary calculation are already available. The distinct result is the local two-branch law for the derivative-weighted degree map and the resulting positive-degree zero and sharp coefficients; neither an assertion of a new general method nor novelty for the Dirichlet monomial action is supported.

## value

PASS

The canonical Gram imbalance of an established monomial derivative-composition operator has an exact signed scaling law resolved by degree. It shows specifically where incoming and outgoing energies change order and yields reusable trace, Hilbert–Schmidt, and general Schatten calibrations. These are distinct from an unsigned edge or a norm bound, with no arbitrary parameter slice beyond the natural fixed monomial family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
