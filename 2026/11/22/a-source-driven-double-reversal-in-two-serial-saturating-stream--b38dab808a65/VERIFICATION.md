---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Both maps satisfy T_i(0)=0, strict increase and 0<T_i(y)<y for y>0. Independent composition and coefficient expansion recover P_r/Q_r and its positive denominator. The source-free polynomial is positive for x>0. Strict concavity in r between 0 and 2/5 proves positivity below 2/5, and the exact factorization at 2/5 gives just a double tie at x=2, not a reversal. Above 2/5 up to 12/25, Descartes' two sign variations and the signs at 0, 2 and infinity give exactly two simple roots straddling 2. From 12/25 (where the degree drops) through r<2 there is one sign variation among the nonzero coefficients and opposite signs at zero and infinity, hence one simple positive root. At or above 2 every positive-power coefficient is negative and the constant is nonpositive; the boundary zero at x=0 when r=2 is not in the domain. The sign orders therefore agree with the claimed minimizers. Setting r=2/5+t² and x=2+tz, the polynomial divided by t² extends at zero with leading equation 96z²−7200=0; the two simple z-roots give x=2±5√3 t+O(t²). As r increases to 12/25, the smaller root tends to the limiting cubic's unique positive root below 2. The larger cannot have a bounded subsequence, since it stays above 2 and the limiting cubic has no root there or at 2. The equation divided by x³ then gives (12/25−r)x→264/625. The frozen checker was inspected, not run. The model represents an order-independent fixed concentration addition at constant flow, not continuous distributed loading or dilution.

## originality

PASS

The source-free preference for this pair is already covered. The closest distinct same-day result with lateral input uses a continuous distributed source and does not cover the inserted fixed translation. The exact two-switch window and sharp birth and escape laws are supported as distinct for the stated discrete pair in the inspected material, not as a new general result on saturating kinetics or an empirical prediction.

## value

PASS

The concrete example puts an exact boundary on the scope of a natural source-free ordering law. A single physically interpretable addition changes the number of optimal-order switches, so a rule designed for source-free serial removal can fail in a qualitatively new way. Proving both reversals and the complete source-strength diagram, including the mechanism by which the roots are created and one escapes, is more useful than a sign plot or isolated parameter tuple. The value is as an exact model counterexample, not as evidence for field deployment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
