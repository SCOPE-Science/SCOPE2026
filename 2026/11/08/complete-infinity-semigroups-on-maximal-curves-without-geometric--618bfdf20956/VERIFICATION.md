---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The program `verify_semigroup.py` is standalone and requires Python 3 with the standard library only. Run `python3 verify_semigroup.py` after extracting it from the finding package. An unmodified successful run prints individual exact cases and terminates with `VERIFY_OK`.

The program checks the residue-class minima of invariant affine monomials, using all \(0\le b<p\) and \(0\le a\le15D\). It enumerates every integer through the computed Frobenius number, determines gap counts and pseudo-Frobenius numbers, tests generator minimality and the sum-of-gaps weight identity. Cases are \((p,n)=(3,2),(3,3),(5,2),(5,3),(7,2),(11,2)\). Every enumeration is finite and explicitly bounded; it does not certify the all-parameter statements by itself.

The general proof relies on two exact structural facts: the Artin–Schreier coordinate ring is free over \(k[x]\) on \(1,y,\ldots,y^{p-1}\); the scalar-invariant monomials have \(x\)-exponent congruent to \(-2b\pmod{2(p-1)}\). Their pole orders at the single ramified infinite point occupy disjoint residue classes modulo \(p\), eliminating any possibility of cancellation and furnishing the whole Apéry set. The remaining genus, conductor, type and weight formulas are exact finite algebraic identities.

Independent expert validation and an exhaustive mathematical-literature priority search have not been undertaken. The computations do not determine semigroups at any other point or code-distance parameters.
