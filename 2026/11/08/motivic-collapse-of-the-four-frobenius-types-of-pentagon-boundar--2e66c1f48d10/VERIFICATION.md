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

The split blowup of four rational points admits the split pentagon pair, whose constant stabilizer is D5 in the split S5 automorphism group. Continuous twists of this pair by the procyclic finite-field Galois group realize all four D5 conjugacy classes over every finite field. In the ambient S5 the two rotation types are both 5-cycles and the reflection has type (2,2,1). Boitrel's perfect-field models give the three proper classes L^2+5L+1, L^2+1+L E5, and L^2+L+1+2L E2, respectively. In the rotation model, blowing up a degree-five point on a split smooth conic adds L E5; contracting its strict transform P^1 to a rational point subtracts L. The conic has degree-five points (there are q^5-q geometric points of exact degree five), and no three are collinear. For the reflection model, choose one degree-two closed point on each of two distinct rational lines. Each line supplies q^2-q nonrational F_(q^2)-points, including at q=2. Any collinear triple would contain a conjugate pair and lie on its rational spanning line, which cannot contain a nonrational point of the other line. For the divisor, normalization has class (L+1)[V] over the finite étale component scheme V since the descended genus-zero curves are split over their finite fields of definition. Removing the branch flags B and restoring the nodes E yields [D]=(L+1)[V]-[B]+[E]. For a reflection V and E each have class 1+2E2 and B has class 5E2: its unique fixed node interchanges the two branches, so there is no fixed flag, even in characteristic two. For identity and rotation the divisor classes are 5L and L E5. Subtracting gives L^2+1 for identity and both rotations, and L^2-1+E2 for a reflection, without localization or division. Counting over extensions sends E2 to 0 or 2 according to parity, proving the counts and zeta function; the degree-one count distinguishes the two classes. For the cohomology, the normalization sequence identifies H^1(D) with the one-dimensional cycle orientation representation. The restriction H^2(Y) to H^2(D) is the intersection pairing in the boundary basis and is invertible; H^0 restricts isomorphically by connectedness. Compact-support localization leaves precisely H_c^2=H^1(D) and H_c^4=Q_l(-2) for l different from the characteristic. Independent finite replay enumerated the 252 five-element subsets of the four E_i and six H-E_i-E_j using the blowup intersection form, retaining those whose induced graph has degree two at every vertex. This gave 12 pentagons, every class-matrix determinant of absolute value one and every sum equal to (3,-1,-1,-1,-1) in the H,E_i basis. The uploaded scripts were inspected, not executed; the finite enumeration checks the lattice step, not the field-uniform geometric identities.

## originality

PASS

Qualified best-of-knowledge pass for the exact comparison in the unlocalized Grothendieck ring across all four marked finite-field Frobenius types, especially the equality of both order-five twists with the split complement. The orientation character, lattice basis, classification of forms, and proper-surface constructions are antecedents. The split and quadratic affine models already imply their own scissors formulas in their applicable settings, not just point counts. The positive assessment rests on the simultaneous boundary calculation and rotational comparison, not on those known parts in isolation.

## value

PASS

These complements are a natural arithmetic family of pentagon-boundary log K3 surfaces. The exact class is useful for motivic calculations where a cohomological trace or even every extension count is not a substitute for a scissors relation. The result settles the precise comparison: the split pair and both distinct order-five twists agree before localization, while the reflection is separated already by the base-field count. The complete finite-field comparison, uniform through characteristic two, gives independent value beyond recovering the known split and quadratic models or the proper-surface trace table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
