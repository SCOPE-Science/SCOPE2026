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

Over an algebraically closed field of characteristic exactly five, the distinct finite branch points give independent square classes X-a_i by their odd valuations. Together with infinity this gives five tame index-two fibers of eight points each, and Riemann–Hurwitz gives genus five. H=dX/(product Y_i) and Y_i H are regular by the branch parameters t=Y_j and t=1/Y_1 and are independent by their distinct sign characters. The Hasse coefficients 1,3,3,1,0,2 follow, for example, by squaring (1+z)^3(1+z^5)^(-1/2) in characteristic five and using the square root with constant term one. The zero order-four derivative row and the nonzero determinant on rows 0,1,2,3,5 establish the generic sequence: after factoring the constants and the Y_i, the alternant is the Vandermonde times product u_i times sum u_i, with u_i=1/(X-a_i) and sum u_i=f'/f. This determinant times the canonical trivialization yields W = c f'(X)(dX)^16/f(X)^7, c nonzero, as a rational section of K^16. At a finite branch point, val(f)=2, f' is a unit and val(dX)=1, giving weight 2. At infinity the corresponding valuations of f,f',dX are -8,-6,-3, again giving 2. The leading terms of Y_i at infinity may differ by signs; only their unit orders are used. Away from the branch locus the zeros of f' have their original multiplicities in all sixteen points of each fiber. These disjoint contributions have degrees 80 and 48, exhausting 16*8=128. The derivative is a cubic, hence the support size is 40+16r for r=1,2,3 distinct roots. For the three given quartics the derivatives are 4X^3+1, X^2(4X+1), and 4X^3. They have the claimed patterns and no common root with their respective quartics: in the first case a common root would have X^3=1 and 2X+1=0, which is impossible; in the other cases substitute 0 and, where appropriate, 1. The statement concerns geometric Hasse-Wronskian support and uses the reduced ramification divisor, not the full pullback of the branch locus.

## originality

PASS

Pass for the complete characteristic-five Wronskian formula, generic nonclassical sequence, and three exhaustive geometric support sizes. The classical Humbert branch gap sequence and forty-point support are known; local branch semigroups do not determine the generic Hasse orders or the extra zeros away from the branch locus.

## value

PASS

The result gives the full intrinsic divisor for an entire smooth genus-five family in the exceptional small characteristic, not an example or a branch-point-only calculation. It isolates a generic order jump and identifies the moving part of the divisor with a cubic critical locus, explaining and realizing every possible support size. This supplies useful data for comparing canonical nonclassicality and ramification across the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
