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

Under k=m-4 Braun's sphere-wedge theorem supplies simple connectivity. A pairwise-intersecting chord family is a star or a three-chord triangle. A nontrivial rotation preserves a singleton chord only at order two, a triangle only at order three, and no star with at least two chords. The order-two antipodal and order-three equally spaced witnesses are stable. For a reflection i↦t-i, at most six choices of i fail t-2i≠0,±1, so there is a fixed chord. Armstrong gives the cyclic quotient by the subgroup of order gcd(d,6); two reflections generate every reflection-containing subgroup, so its quotient is simply connected. The star-union face poset retracts by closing each nonsingleton star to the full star at its common label. The image is the barycentrically subdivided stable-chord graph, with reversed inclusion order. The boundary of a remaining triangle is sent equivariantly and homeomorphically to the six half-edges on its polygon-label triple; attaching these disks gives the stable-label two-skeleton as an equivariant homotopy model. After subdivision, disk and boundary quotients are CW pairs, so passage to each quotient also gives a two-dimensional model. Integral H_2 is free, higher homology vanishes, and rational chains after subdivision are coinvariants, so averaging the covering H_2 character gives the rank. The signed traces can also be counted on the small model: for instance an even reflection at m=2h has chain traces 2, 2-h, -2(h-2), giving H_2 trace 3-h. Independent replay python3 -B /workspace/checks/kneser.py verified all character cases over m=8..20 on that small model; contracted orbit spanning trees and performed relator substitutions tracking every remaining generator. The smaller cyclic CW models (6,17,12) and (8,26,20) in degrees 0,1,2 give final relations u^4 and (trivial,u^-3), respectively. The dihedral models give a point and a point with one trivially attached two-cell. These independently prove the stated four types. The original flag method is also sound: deleting different ranks in a flag gives distinct rank signatures, so incidence-one free faces lie in one coface only; single-occurrence relator elimination preserves the CW homotopy type by removing a generator with its solving 2-cell, not merely preserving the group. Duplicate degree-three relations attach a sphere after the first relation.

## originality

PASS

The supported additions are the stable-complex subgroup calculation including torsion, and the exact stable quotient types in the first two cases. Credit the prior nonequivariant type, dihedral character and star reduction, Armstrong's theorem, and the identical isotropy mechanism for unrestricted two-subset complexes. The strongest distinct catalog records have a different rational invariant, matching the unrestricted model exactly rather than the stable one.

## value

PASS

A natural invariant of Schrijver graph symmetries is computed for every acting subgroup, including integral torsion invisible to the prior rational trace calculation. Rotation quotients can have arbitrarily large prime-order fundamental groups even though the source and reflection quotients are simply connected. The exact models at the first two stable widths exhibit this via actual degree-four and degree-three attaching maps and distinguish the reflected quotients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
