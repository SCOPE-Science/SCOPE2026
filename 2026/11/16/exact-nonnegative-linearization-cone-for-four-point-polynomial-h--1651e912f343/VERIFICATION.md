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

The tridiagonal row-stochastic 4x4 recurrence J has positive irreducible off-diagonals, a simple real spectrum and orthogonal polynomials R_i normalized at one; coefficients g(m,n;k)=[R_m(J)]_{n,k}. All R1 multiplications are nonnegative, so only (2,2),(2,3),(3,3) must be checked. Independent symbolic SymPy reconstruction of R2(J),R3(J) verified the source 12 exact coefficient formulas and their row sums: only L/(1-x), H/(1-x), rH/[(1-x)(1-y)] and (1-r)K/(1-y) can be negative for 0<r<1. At r=1, K disappears, H=1-x-y and H>=0 forces L=1-x(1+y)>0. For every ratio r, H(r=1)>=0 forces x+y<=1 and limit K(r->1-) enforces y<=2/3; these two conditions force H,K>=0 and L>0 by the stated y(2-3y) bound. Independent exact rational witnesses verify L independence and a profile with negative third Newton coefficient. This is an all-real-parameter symbolic proof, not a finite parameter sampling claim.

## originality

PASS

Polzer 2026 establishes Newton log-concavity as a sufficient condition and asks explicitly for the all-ratios exact region; the displayed four-point inequalities and two-wall sharp region resolve a nontrivial low-dimensional instance outside that sufficiency cone. Szwarc 2003 supplies an abstract general matrix criterion but not its explicit four-node semialgebraic elimination; the published five-state symmetric endpoint has different size and ratio quantifiers.

## value

PASS

The exact four-point cone and all-ratio profile region give an explicit first nontrivial answer to a stated problem about necessary-and-sufficient property(P) conditions; independence of L and a negative-Newton but positive-profile witness demonstrate true enlargement beyond a known sufficient criterion. Exact small finite hypergroup classifications are natural and potentially reusable; no paper-sized generalization is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
