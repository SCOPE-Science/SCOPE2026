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

The four nonzero Möbius terms give z^t(1-z^{t(p-1)})(1-H(z^t)), where H has q positive unit coefficients at exponents q-1+j(p-1). The constant term of the last two factors is 1, establishing origin multiplicity t; the middle factor contributes only unit-modulus roots. For H(z)=1, monotonicity of H(r) gives the unique positive radius and the lower bound. Equality forces every phase to be 1, and the first two consecutive exponents force exactly the gcd subgroup; zH'(z) is then a strictly positive sum. The nonzero t-th-root map is unramified, giving tg simple boundary roots. The raw radii vary with t, as the explicit t-th-root formula specifies; the squarefree kernel determines the parent moduli, not identical radii for all powers. For the fixed-p estimate, u=-(q-1)log rho lies between log(q)/p and log(q). The exact geometric series gives e^{-u}=(1-e^{-(p-1)u/(q-1)})/(1-e^{-q(p-1)u/(q-1)}), so e^{-u}=O_p(log q/q), and the denominator differs from 1 by at most that order. Therefore u+log u=log((q-1)/(p-1))+O_p(log q/q); the inverse is 1-Lipschitz there, and expanding 1-e^{-u/(q-1)} yields the stated error. The supplied scripts were inspected, not executed; a separate bounded reproduction (branches/e1d2767d-76b8-468d-ad0f-7b8ebcddc875/independent_check.py) checked 24 sparse identities, six phase cases, five radial/derivative cases and nine numerical Lambert-W samples, not the all-size claim.

## originality

PASS

The supported distinct content is the necklace-specific innermost zero description as a package with a quantified radius asymptotic, not the triangle-equality mechanism, squarefree substitution, or generic Lambert-W inversion. No covering statement was found in the available evidence; historical priority is not certified.

## value

PASS

The first nonzero complex-root circle is a canonical invariant of the necklace count polynomial. Its exact complex equality set and fixed-small-prime rate near the unit circle distinguish it from unit-circle factor testing and integer alphabet estimates. The combination gives a reusable radius equation and an asymptotic with relative location and error, not just a finite root plot or a reformulation of standard power substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
