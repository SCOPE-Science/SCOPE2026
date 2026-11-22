---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For GP(10,2), a separate bitmask independent-set recursion reconstructed face cardinalities (1,20,160,660,1510,1912,1240,320,5) and exact augmented mod-2 boundary ranks (1,19,141,519,991,921,315,5). Mod-2 homology is four in degree five and zero elsewhere, and Euler forces four rational degree-5 classes. The oriented-face Hopf-Lefschetz trace over 120 exact graph automorphisms gives the full character ε(g)(number of fixed cubes-1), the tensor of the antipodal sign and five-cube permutation augmentation. The prior published complete 120-element character gives a separately inspected independent exact proof; the source verifier performs direct cycle-orbit and simplex traces. Invariant averaging yields full, rotation and antipode rank zero, cube-stabilizer rank one; rational quotients have ring Q[x]/(x^2), |x|=5, for the latter. Integral lattice and quotient torsion are not claimed.

## originality

FAIL

The 2026-10-18 published theorem on exactly Ind(GP(10,2)) gives the identical A5×C2 rational H5-module as sign-twisted 4-dimensional five-cube augmentation, the complete character ε(g)(fix5(g)-1), absolute irreducibility and antipodal action −I. A second 2026-11-01 published independent full theorem again states this exact module. The current additional rational quotient cohomology ranks follow immediately by finite-group invariant averaging: A5, G and C2 have zero invariants; stabilizer of one cube has two orbits on five cubes, so augmentation invariants have dimension one, and inversion kills it. No distinct new equivariant result survives.

## value

FAIL

The natural dodecahedral homology representation is intrinsically valuable, but it has already been computed and published in exactly this form. The quotient statements are routine applications of Maschke invariants and orbit-counting to that known module; they add no independently motivated unknown precise invariant or new structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
