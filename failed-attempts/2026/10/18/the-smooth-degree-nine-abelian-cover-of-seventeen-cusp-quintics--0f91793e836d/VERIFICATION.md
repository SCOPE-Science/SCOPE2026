---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The input is two weight-12 supports with intersection seven on a quintic with exactly 17 A2 points; the result is conditional, not a claim about all such quintics. Tan's weight restriction as stated by Borisov–Rito gives allowable nonzero weights 12 and 15. Two independent words give dimension at least two; Griesmer would require at least 12+4+2=18 positions for dimension three. The four projective column types then have multiplicities 5,5,r,7−r and each one is the zero type of exactly one projective word, so r must be 2 or 5. This gives the asserted supports and spectrum. The resolved quintic is simply connected: a smoothing and the resolution both fill the same truncated smooth locus with simply connected Milnor fibers or A2 plumbings, so van Kampen and Lefschetz for the smooth quintic give the claim. Mayer–Vietoris makes H1(U,Z) a quotient of the sum of link H1 groups, hence of exponent three; the preceding boundary map is the intersection map to the A2 discriminant groups. On each A2 factor the generator is represented by (2E'+E'')/3, and the local linking pairing identifies its annihilator condition with the mod-three intersection relation against 2E'+E''. Mod-three Poincaré duality gives precisely the stated cusp-code kernel. The dual therefore has dimension two, and the two support sets cover all cusps, so every inertia image has order three. The corresponding normal extension has three smooth universal local covers at each cusp. Cartier adjunction and quasi-étaleness give ample canonical class and K²=45; e(U)=55−3·17=4, hence e(Y)=9·4+3·17=87 and χ=11. Nontrivial characters factor through the four cyclic quotients and the trivial eigenspace is zero on the quintic. The use of q=0 for the weight-12 and weight-15 resolved triple quotients is supported by the inspected reports of Tan's classification, and Rito independently uses the cited theorem in the weight-15 case of his quintic. For a check on the normalization, a resolved triple quotient of weight w has K²=15 and e=3·4+w+9(17−w), hence χ=7 and 5 for weights 12 and 15; the respective reported genera 6 and 4 give q=0. The character argument then gives q(Y)=0 and pg(Y)=10. The full primary text of Tan's Chapter 4 was not retrieved; the irregularity assessment relies on those sources for the precise theorem scope, not on the code replay or on an asserted direct primary-text check.

## originality

FAIL

9f45f44ee9f7 uses the same precise hypotheses and states the full code spectrum, the connected smooth degree-nine simultaneous cover and the same invariant package, with a stronger canonical character result. 8102a764f4ed also gives all four intermediate cyclic covers and the full mod-three smooth-locus H1 computation (in the dual cohomology formulation). The integral formulation in the frozen record goes beyond what is explicitly printed in those findings, but only by the immediate quotient-of-link-groups exponent-three bound on a simply connected resolution; hence the stated integral abelianization and maximality are mechanically covered as well. No priority or provenance conclusion follows solely from catalogue dates.

## value

FAIL

A smooth canonical cover of this family and its invariants would be geometrically useful as a distinct result. The same cover and a stronger invariant package are already covered, and the only explicit extra formulation—the integral rather than mod-three abelianization—follows directly from the standard link-group exponent argument in this setting. There is no supported distinct increment in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
