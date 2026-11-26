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

The relative inverse image of the rank≤1 cone under the surjective six-dimensional evaluation bundle map is irreducible of projective fiber dimension 32; adding p gives dimension 34. A zero evaluation is excluded on the smooth-branch open because its two base-derivative conics in the fiber meet. Simultaneous evaluation at two distinct points is independently surjective, so the ordered two-point incidence has dimension 33. Properness of the incidence projection and this bound give a divisor with a unique split fiber generically. Nonemptiness follows from the primary example and can also be checked by Bertini: fix p and a square ℓ² there; the linear system with evaluations proportional to ℓ² is base-point-free off the fiber. In the chart at p, assign the two first derivatives independently, with restrictions to ℓ=0 equal to the squares of two independent coordinates, so the generic branch is also smooth along its base line. The fiber w²=ℓ² has precisely the two graphs that are planes, meeting along that line. Differentiation in the total space gives the stated normal-bundle sequence (a sign change in the vertical column for the other graph is harmless). Smoothness gives no common zero of the restricted binary quadrics, which even implies their independence for every such fiber: a dependent pair would have a common root. The global section map has rank 5, so its kernel vanishes and its cokernel has dimension 1; higher line-bundle cohomology vanishes. This proves the reduced isolated Hilbert points. The 2×2 kernel block of the symmetric matrix gives the degree-two determinant term; the displayed witness yields −t(s+t). In fact a base-point-free binary pencil meets the discriminant conic transversely: a pencil tangent at a square would share its double root. The claimed ordinary node is therefore correct with the stated generality. The normal Chern ratio is (1+H)/(1+2H), giving c₂=2. Restriction to the plane and projection degree give the stated pairing. Removing the orthogonal <2> summand leaves a rank-three block of determinant −8 with an entry 1 and a 2×2 minor −1, so its Smith invariants are (1,1,8); the total invariants are (1,1,2,8). This is a sublattice, not an asserted saturation. The submitted symbolic checker was inspected, not executed.

## originality

PASS

Existing papers exhibit split-plane fibers, including exactly the cited smooth nodal example, and compute the ambient rank-three pairing. These are not new. No inspected source covers the generic uniqueness of the split fiber in the full smooth parameter divisor together with the embedded plane rigidity and its rank-four cycle pairing. The general symmetric determinantal picture is a relevant standard tool and explains the expected incidence and node, but it does not itself calculate the embedded deformations or self-intersection of these planes.

## value

PASS

This is a natural degeneration of a marked Verra quadric fibration, not an arbitrary extra plane imposed in a numerical example. It identifies the generic parameter locus and computes the scheme-level deformation behavior and exact intersection pairings of its distinguished planes. These are concrete data one can use to compare families and additional algebraic classes. The value is in the full geometric calculation, not in renaming the known example or claiming a full saturated lattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
