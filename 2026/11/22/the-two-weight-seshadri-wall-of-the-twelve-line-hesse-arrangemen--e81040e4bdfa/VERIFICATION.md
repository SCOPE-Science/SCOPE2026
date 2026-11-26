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

Independently checked incidences in the given coordinates. For x+y+z=0 the three axis points are of type Q, and the two grid nodes correspond to the two orderings of ω and ω² after the leading 1. Diagonal multiplication by cube roots gives the other eight non-coordinate Hesse lines; each coordinate line has three Q and two N directly. The claimed original singular support accounts for 9·6+12=66 distinct intersecting line pairs, the total. Each new line, e.g. x=ω^i y, has one coordinate vertex and three grid nodes; a Q with one zero coordinate cannot qualify because either one side alone vanishes or the nonzero ratio is a negative cube root. Every node belongs to three new lines. For any irreducible curve other than the 21 lines, normalized multiplicities a=A/d,b=B/d satisfy 2a+b≤6 and b≤3 by summed Bézout, including all singular curves in any degree. The support-function bound for αa+βb is 3α if β≤α/2 and 3α/2+3β otherwise. These bounds lie strictly below the larger line denominator off β=3α/2. The lines have normalized multiplicity vectors (3,2) and (0,4), giving equality as claimed, with no exhaustiveness claim on the wall. The exceptional intersections of the Seshadri class are positive. Its square vanishes precisely when max(3α+2β,4β)^2=9α²+12β², by the factorizations 4β(3α−2β) and 4β²−9α² in the respective chambers. At that ratio it is F/12; intersecting with the two line types gives zero, their strict transforms have squares 1−5 and 1−4, and gcd(12,2,3)=1. The proof uses these exact calculations, not sampled weights.

## originality

PASS

The line coordinates and the equal-weight value are prior. Dumnicki et al. even supply a quartic net whose displayed reducible generators visibly contain the nine new lines. Credit those equations and the known dual arrangement: do not sell the lines themselves as new. The distinct result is identifying and combining the two sharp line-family constraints for the fixed 21-point support, deriving the full two-orbit envelope with strict off-wall classification and the isotropic wall. The earlier unweighted bound from smooth quartics alone does not give it.

## value

PASS

The deformation uses the two natural incidence strata of the exceptional twelve-line case in the unweighted theorem. It identifies when external rather than arrangement lines obstruct local positivity, shows they are the only obstructions off the wall, and locates a concrete nef isotropic class annihilating 21 negative curves. This is a useful weighted nef-cone slice, beyond computing the unweighted number by a second method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
