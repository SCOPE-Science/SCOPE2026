# P8-to-X9 corank-one inclusion lifts: primitive Seifert-compatible embedding with explicit Nikulin gluing

## Context

Arnold strange duality relates the unimodal singularities P8 and X9 by Dolgachev-Gabrielov number exchange: Dolgachev triples (3,3,3) versus (2,4,4). A recognized program from Pinkham through Dolgachev-Nikulin to Ebeling-Takahashi asks whether this numerical coincidence lifts to explicit lattice maps between the associated Milnor-lattice quotients, usable in Torelli and mirror-symmetry arguments. The admitted target instance fixes Q_P8 (rank 6, E6-type, discriminant 3) and Q_X9 (rank 7, E7-type, discriminant 2) with the distinguished Dolgachev-exchange E6-to-E7 vertex-deletion inclusion j of corank one, and asks whether j extends to a primitive isometric embedding preserving published Seifert-form divisibility, versus no such extension by an explicit Nikulin isotropic-subgroup plus Seifert obstruction. The admitted claim asserted non-extendability: no primitive corank-one Seifert-compatible lift and no isotropic gluing lift with compatible rank-1 complement.

## Definitions

Use positive-definite Cartan Grams G6 (E6) and G7 (E7): 2 on the diagonal, -1 on Dynkin edges, with E6 vertices {0,...,5} and edges 0-1-2-3-4 plus branch 2-5, and E7 vertices {0,...,6} with edges 0-1-2-3-4-5 plus branch 2-6. Then det G6 = 3 and det G7 = 2. The distinguished inclusion deletes the long-arm end vertex 5 of E7, i.e. sigma = (0,1,2,3,4,6); deleting any other single vertex does not yield an E6 diagram, so sigma is forced. Let J be the 7x6 (0,1)-matrix with J[sigma(j),j] = 1. Seifert normalization is L + L^T = -G with det L = +/-1 (unimodular Gabrielov shape); divisibility is div_L(x) = gcd of entries of x*L (0 for x = 0). Overall sign (+/-G) is immaterial to isometry, primitivity, gluing-index, and discriminant-form statements. A lattice map is primitive if its image is a direct summand (torsion-free cokernel).

## Result

The admitted non-extendability claim is FALSE. The distinguished inclusion j itself, realized as the coordinate inclusion Phi = J, IS a primitive isometric embedding Q_P8 -> Q_X9 of corank one extending j, with explicit rank-1 complement, isotropic Nikulin gluing, and exact Seifert compatibility with divisibility preserved on all vectors:

1. Isometry: J^T G7 J = G6, corank 7-6 = 1.
2. Primitivity: coordinate projection R (R[j,sigma(j)] = 1) satisfies R J = I_6, so J is a split monomorphism with coker(J) ~= Z torsion-free.
3. Rank-1 complement and gluing: S^perp = Z*w with w = (2,4,6,5,4,3,3), primitive, orthogonal to the image, <w,w> = 6; glue index [T : S + Z w] = |w_5| = 3 with 3*6 = 2*3^2; overlattice generator u = (1,2,2,2,2,1,1) in T with 3u = s + w for s = (1,2,0,1,2,0,0) in S; T even ((u,u) = 2); discriminant classes [s/3], [w/3] have order 3 with q_S + q_K = 4/3 + 2/3 = 2 in 2Z, an isotropic gluing subgroup.
4. Seifert compatibility: with canonical Dynkin-order data LS, LT (diagonal -1, strict-upper part from -G), det LS = +1, det LT = -1, LS + LS^T = -G6, LT + LT^T = -G7, and J^T LT J = LS exactly; every distinguished basis vector has divisibility 1 on both sides; by unimodularity every primitive vector has divisibility exactly 1 on both sides, so div_T(Phi x) = 1 = div_S(x) for all primitive x; exhaustive box [-2,2]^6 (15,624 nonzero vectors, 14,896 primitive) confirms div_T(Phi x) = div_S(x) throughout.

Hence every clause of the admitted obstruction (no primitive extension, no isotropic lift, Seifert-divisibility failure) is directly refuted.

## Proof / Evidence

All assertions are exact integer / Fraction arithmetic with stdlib only, no floating point. `python3 output/artifacts/verify_target.py` prints VERIFY_OK and checks: Bareiss determinants 3 and 2; J^T G7 J = G6; R J = I_6; Gw orthogonality on sigma slots, gcd(w) = 1, norm 6, glue index 3, relation 3*6 = 2*3^2; s in image, 3u = s + w, T even; s/3 in S^* nonzero of order 3, (s,s)_S/9 + 6/9 = (u,u) with sum in 2Z; Seifert identities and J-compatibility; divisibility 1 = 1 on bases plus the unimodularity-implies-divisibility-1 lemma. `verify_divisibility_census.py` prints CENSUS_OK after checking all 15,624 nonzero vectors. The Seifert divisibility condition is vacuous given primitivity for any unimodular datum, so it cannot obstruct.

## Limitations

Disproves only the literal admitted non-existence claim for the distinguished P8-X9 inclusion; does not classify all Seifert-compatible extensions or decide other dual pairs (other unimodal/quadrangle pairs need their own gluing computations). Uses the canonical Dynkin-order unimodular Gabrielov Seifert datum (L + L^T = -G); non-unimodular conventions untested but outside the published normalization referenced by the claim. Sign convention is immaterial.

## Reproducibility

Conventions: branch vertex at index 2 in both diagrams; sigma = (0,1,2,3,4,6). Run `python3 output/artifacts/verify_target.py` (expect VERIFY_OK) and `python3 output/artifacts/verify_divisibility_census.py` (expect CENSUS_OK) with any Python 3 stdlib, no external packages. Scripts use Bareiss determinants, explicit matrix multiplication, Fraction discriminant forms, and gcd divisibility.

## References

- Arnold strange duality; Dolgachev-Gabrielov exchange; Ebeling-Takahashi and Kobayashi duality theorems (numerical/mirror context, no instance gluing decision).
- V. V. Nikulin, integral symmetric bilinear forms and primitive embeddings / overlattice correspondence via isotropic subgroups of discriminant groups (general criteria applied here).
- Gabrielov diagrams and Seifert forms of unimodal singularities; Milnor lattices of elliptic hypersurface singularities (E6/E7 quotient inputs, det 3 / 2).
- Standard E6/E7 Cartan matrices and Dynkin vertex-deletion E6 = E7 minus long-arm end vertex.
