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

The log ratio of my to z cancels the matched basal gain, giving v'=c3 v(1-v)(Delta-G(v)). G has endpoints 1 and e3/a3 and derivative m(e3-a3)/D(v)^2. The strict root conditions, monotone flow to the attractor or the endpoints on the stated sides, and the neutral case follow, including endpoint equality when there is no interior root. Positive states exist for all finite positive times: x is bounded above by logistic comparison and bounded away from zero on finite intervals by x'/x>=1-x-c; the positive consumers have bounded per-capita rates. At a positive equilibrium A=B=C=0, so w=Ec/L-a is positive precisely for L<Ec/a and then x>1-c; the inverse gives positive y,z. In the neutral case L is strictly decreasing, and the inequality cuts out an open interval if nonempty. The Jacobian splits off the real composition eigenvalue; the other block has trace -x-wc(E-a)/(a+w)^2<0 and determinant xwcE/(a+w)^2>0. This includes E=a and proves local stability, the saddle alternative, or local transverse attraction along the neutral curve, as appropriate. No Hopf crossing is possible in this positive-equilibrium family. The rational witnesses agree by substitution. The scope is relative composition, not global absolute abundance convergence; normal attraction is local along the interior curve, not uniform up to its endpoints. RESULT.md §§1–4, VERIFICATION.md and checker.py were inspected without executing the supplied script.

## originality

PASS

Chan–Wu already gives the model, coordinates and general transformed equations; cancellation is an immediate specialization and is not independently original. The supported distinction is the combined global weighted-composition basin classification and exact viability, stability and normal-attraction trichotomy for the matched family, including the positive-equilibrium no-Hopf conclusion. The closest inspected sources do not state or supply this classification as a theorem under encompassing hypotheses.

## value

PASS

Matching the competing basal gains is a mechanism-based restriction rather than a random numerical slice. The value is not the substitution: the result separates a global relative-composition prediction from the viability and full local stability of coexistence, and identifies the exact neutral threshold where a continuum replaces isolated equilibria. The stable transverse block also answers whether the broader model's Hopf mechanism can operate at coexistence under those restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
