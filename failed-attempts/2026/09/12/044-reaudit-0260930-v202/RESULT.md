# Formality of the moment-angle manifold over J_{(3,2,1,1,1,1)}(octahedron)

## Context

Let K_0 be the boundary of the octahedron: the 6-vertex triangulation of S^2
with vertices {a_0,a_1,b_0,b_1,c_0,c_1} whose minimal nonfaces are the three
antipodal pairs {a_0,a_1}, {b_0,b_1}, {c_0,c_1}. The simplicial multiwedge
(J-construction of Buchstaber-Panov) with J = (3,2,1,1,1,1) is the iterated
simplicial wedge: wedging at a_0 twice and at a_1 once. The admitted target
asks for the Stanley-Reisner Tor algebra of the resulting complex K via
Hochster's formula, the Massey defining systems from full subcomplexes with
indeterminacy quotients, and the formality/non-formality verdict for the
associated moment-angle manifold Z_K, a case recorded as outside the
Limonchenko rational-formality tables for multiwedges.

## Definitions

- Simplicial wedge at a vertex v (minimal-nonface rule): each minimal nonface
  F containing v is replaced by (F \ {v}) union {n_1, n_2} (two new vertices);
  minimal nonfaces not containing v are kept. Iterating gives the multiwedge.
- K_A denotes the 4-vertex square cycle (boundary of a square, S^1); K_B
  denotes the boundary of the 4-simplex (S^3).
- Simplicial join K_A * K_B: faces are unions A union B with A in K_A,
  B in K_B; topologically S^1 * S^3 = S^5.
- Moment-angle complex Z_K = union over sigma in K of (D^2,S^1)^sigma.
  When K triangulates a sphere, Z_K is a closed smooth manifold.
  Join/product rule: Z_{K*L} = Z_K x Z_L.
- Rational cohomology H*(Z_K; Q) is isomorphic to
  Tor_{Q[v_1..v_m]}(Q[K], Q) with the Baskakov bigrading collapsed
  (Buchstaber-Panov/Hochster). The Koszul CDGA
  R(K) = (Lambda[u_i] tensor Q[K], d u_i = v_i) computes Massey products.
- formality (Sullivan): the minimal model is determined by the cohomology
  ring; a non-vanishing Massey product obstructs formality, while a
  zero-differential minimal model (e.g. a product of spheres) implies formality.

## Result

Let K = J_{(3,2,1,1,1,1)}(boundary of octahedron). Then:

1. K is a 9-vertex triangulation of S^5 with minimal nonfaces, up to
   relabelling, MNF(K) = {{0,1},{2,3},{4,5,6,7,8}}, f-vector
   (9,34,70,85,60,20), Euler characteristic 0, and every vertex link a
   homology 4-sphere.
2. K splits as the simplicial join K = K_A * K_B of the square 4-cycle with
   the 4-simplex boundary, verified by exact face-set equality (279 faces).
3. Hence the moment-angle manifold is
   Z_K = Z_{K_A} x Z_{K_B} = (S^3 x S^3) x S^9,
   a closed simply connected smooth 15-manifold (9 + 5 + 1 = 15).
4. The bigraded Tor groups are beta^{0,0} = 1; beta^{-1,4} = 2 (supports
   {0,1},{2,3}); beta^{-2,8} = 1 (support {0,1,2,3}); beta^{-1,10} = 1
   (support {4,...,8}); beta^{-2,14} = 2; beta^{-3,18} = 1 (full 9-set);
   total Tor dimension 8. Thus H*(Z_K; Q) has dimensions
   H^0 = Q, H^3 = Q^2, H^6 = Q, H^9 = Q, H^12 = Q^2, H^15 = Q,
   the exterior algebra Lambda(a_3, b_3, c_9).
5. Z_K is formal: its Sullivan minimal model is
   (Lambda(a_3, b_3, c_9), d = 0). It carries no non-vanishing triple or
   higher Massey product. Every triple of positive-degree classes with
   vanishing pairwise products was enumerated (205 defined triples); in each
   case the Massey cocycle is already zero at cochain level, hence a boundary,
   hence zero in the indeterminacy quotient.

## Proof and evidence

Wedge rule validation: the minimal-nonface edge-replacement rule was validated
on the tetrahedron boundary (wedge gives S^3) and the pentagon (wedge gives
S^2) before application to the octahedron; iterated wedging at a_0 twice and
a_1 once yields the stated 9-vertex complex with homology S^5. An earlier
incorrect face-closure wedge implementation producing a non-spherical complex
was detected via Euler-characteristic and link checks and discarded; only the
validated construction is used.

Join decomposition: the minimal nonfaces split across disjoint vertex sets
{0,1,2,3} and {4,5,6,7,8}, suggesting K = K_A * K_B. This was verified by
exact comparison of the two face sets (279 faces each, equal). The
polyhedral-product join rule then gives Z_K = S^3 x S^3 x S^9.

Tor computation: Hochster's formula over all 2^9 = 512 full subcomplexes gives
the bigraded Betti table above (script tor_true.py, exact rational homology).
The cup product follows the Hochster disjoint/overlapping-support rule:
disjoint supports ({0,1},{2,3},{4,...,8}) multiply to the classes in H^6,
H^12, H^15, while overlapping supports give zero (odd-degree generators square
to zero over Q), yielding the exterior algebra on degrees 3, 3, 9.

Massey vanishing: cocycle representatives in the Koszul CDGA are
a = [u_0 v_1], b = [u_2 v_3], c = [u_4 v_5 v_6 v_7 v_8] (degrees 3, 3, 9).
All products of positive classes not listed vanish for degree reasons or
graded commutativity. The exhaustive Koszul-CDGA check over all triples of
cohomology basis classes with pairwise-vanishing products (205 defined, 205
with primitives solved, 0 essential; script massey_true.py, exact Fraction
arithmetic) shows every Massey cocycle x*c +/- a*y is zero/boundary, hence
trivial in the indeterminacy quotient. Higher Masseys vanish because the
minimal model has zero differential (product of spheres).

## Limitations

Computations are over Q (rational homotopy and rational formality); integral
cohomology torsion is not addressed. Diffeomorphism rigidity beyond the
standard join/product rule and the simplex-boundary sphere theorem was not
separately reproved. Higher Massey vanishing is deduced from the
zero-differential minimal model of a product of spheres together with the
exhaustive triple-Massey computation, not from an independent infinite-order
search.

## Reproducibility

Verification-critical scripts copied to output/artifacts: homology_lib.py
(exact rational simplicial homology, validated on S^1, S^2, T^2, RP^2, balls),
wedge_correct.py (wedge validation plus the true K), tor_true.py (Hochster
bigraded Betti table), massey_true.py (205 defining systems with indeterminacy
quotients). Re-run with PYTHONPATH=output/artifacts: python3 wedge_correct.py,
python3 tor_true.py, python3 massey_true.py.

## References

- V. M. Buchstaber and T. E. Panov, Toric Topology (moment-angle complexes,
  Stanley-Reisner rings, J-construction/multiwedge, join-product rule,
  Hochster cohomology decomposition).
- I. Yu. Limonchenko, On Higher Massey Products and Rational Formality for
  Moment-Angle Manifolds over Multiwedges, Proc. Steklov Inst. Math. 305
  (2019) (multiwedge Massey/formality program and tables).
- J. Grbic and A. Linton, Non-trivial higher Massey products in moment-angle
  complexes, Adv. Math. (2021), arXiv:1911.07083 (join/star-deletion/
  stretching constructions of non-trivial Massey products; nearest prior).
- G. Denham et al., Moment-angle complexes, monomial ideals and Massey
  products (triple Massey classification); A. Linton, thesis (2019)
  (systematic Massey constructions); P. Beben and J. Grbic, LS-category of
  moment-angle manifolds (2021) (Massey vanishing conditions).
