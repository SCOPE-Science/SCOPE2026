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

The lower block has eigenvalues 6,−6,−6 and the Schur complement is 2−t²/2<0. The known exact K3 lattice realization applies. For q=x²+txS+2S²−3T, q=0 first forces x,S even mod 2; two odd y_i would then give q≡2 mod 4. Thus all coordinates are even, proving anisotropy by descent. For roots d=2x+tS satisfies d²=(t²−8)S²+12T−4. S=0 yields the nonsquare residue 8 mod 12; |S|≥2 gives d²≥4t²−20>t² even at t=3; |S|=1 gives equality at |d|=t exactly for T=1. The six positive choices are e_i and th−e_i. In particular h is perpendicular to no root by this calculation (negative definiteness alone would not suffice). Move h to the ample chamber; the genus-two system is base point free, since the elliptic exception to Saint-Donat is ruled out by anisotropy. Ampleness precludes contracted curves. Riemann–Roch makes the positive roots effective; a divisor of square −2 has a negative component, necessarily a smooth rational curve by adjunction, whose degree already uses the entire divisor degree t. Two distinct curves cannot represent the same negative-square class. The finite double cover of the smooth plane is flat, has sextic branch by the canonical formula, and the local branch equation is smooth since the total space is. Invariant rational cohomology of the double-plane quotient is spanned in degree two by h, so the involution sends v to (v,h)h−v. The two distinct components over each image each map with degree one; the normalized branch section is a square in the function field after rational trivialization, giving even contact. Pairings and the quotient by ⟨e_i,th⟩ give exactly the stated intersections and cyclic index t. Direct Gram-matrix replay: python3 /workspace/independent_checks.py 4; bounded checks are only diagnostic.

## originality

PASS

The contribution is the exact polarized short-root spectrum and resulting six-curve arrangement for the known lattice. The original Gram matrix, anisotropy (including the same descent), root-pair separation, and lattice realization are already in Kikuta; standard degree-two projective-model theory is also background. None of the inspected statements resolves the new minimum and its equality set in this family.

## value

PASS

At fixed polarization square two, the least smooth rational degree gives concrete information about the effective cone that does not follow from mere existence of high-degree curves. In a uniform family the least degree is unbounded, with exactly six witnesses and a quantified failure of their span to be saturated. Three rational plane images with even normalized contact connect the lattice result to double-plane geometry without claiming that it determines the full splitting locus or excludes low-degree singular rational curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
