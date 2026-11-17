---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Reconstructed complete proof at pinned source: intersection with a Fano line has three prescribed simple rational roots, fourth residual root rational by degree four, so exact F4 locus forces one of those three to be double; smooth tangent uniqueness yields a perfect point-line incidence matching. Independently generated all 7!=5040 bijections, found exactly 24 incidence matchings, built 14 constraints on 15 monomials for each and checked rank14 in all 24 using separate mod2 elimination. Each one-dimensional nullspace over F2 extends to the same line over F4, establishing equation descent. One representative has exact F4 rational locus B in packaged 21-point finite-field checker; independently checked all three polynomial affine Jacobian ideals with SymPy Groebner mod2 give the unit ideal, proving geometric smoothness over algebraic closure. PGL3(F2) order168 acts transitively on matchings; PGL3(F4) order60480 divided by 168 yields 360 subplanes and 24*360=8640 normalized curves in one orbit, stabilizer7; genus3. No degree below four: conics have five points, cubic smooth elliptic F4 group would have seven rational points and a flex, but F7 has only five distinct zero-sum triples versus seven Fano lines. Distinguish finite F4 nonsingularity enumeration from geometric Jacobian ideal proof.

## originality

PASS

A published 2026-10-26 theorem already gives the 24 smooth binary plane-filling quartics and order-seven stabilizer, but assumes F2 coefficients. The submitted extra rigidity asks whether a smooth quartic with F4 coefficients can have exactly the F2 Baer seven-point locus: forcing seven tangent matchings, rank14 constraints over F2, and one-dimensional extension-of-scalars kernel excludes new F4 forms. Thus it is NOT simply a re-count of the earlier 24 and yields the all-F4 count 8640 plus matching bijection. Literature and Resultary searches located no implication eliminating F4-only forms. Due incomplete blocking-curve primary text, the originality decision is best-of-knowledge with explicit priority risk.

## value

PASS

The precise effect of changing the coefficient field while demanding an exact small subplane rational-point locus is a natural descent/rigidity phenomenon in finite algebraic geometry. The forced-tangent perfect matching supplies structural mechanism, complete F4 classification and orbit count, not merely repetition of known binary quartic count; this fact is useful for rational-point blocking classifications and finite curve enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
