# Independent mathematical audit

## correctness

PASS

The harmonic addition theorem for degree0..2 under probability surface measure gives the exact rational twelve-point row Gram kernel K_ij=(1+3t+5P2(t))/12 with t=(2vi+vj)dot(2vk+vl)/11. Evaluation of the nine monomials/harmonics yields a rank-nine integer 12x9 matrix M; the displayed independent 12x3 Gale matrix N has rank3 and N^T M=0. A nine-site restriction is nonsingular iff the erased three-row submatrix N_T is nonsingular. Independent SymPy exact arithmetic enumerated all 220 deletions, obtaining 128 nonsingular and 92 singular; each nonsingular N_T determinant has magnitude1, and one exact Gram determinant is 52428800000/34522712143931. The S4 action partitions deletions into 13 orbits; using exact rational Gram matrices, all eight directed-triangle masks have every leading principal minor of K_S-0.07 I positive, while each of the 120 other nonsingular masks has det(K_S-0.07I)<0. The sharp optimal spectrum has characteristic polynomial (5324z³-12353z²+7904z-1280)(161051z³-356708z²+194480z-12800)²/138090848575724, with isolated smallest root between .076 and .077. All computations were independently reconstructed from the pinned integer coordinates and compared to source verification; the finite enumeration exhausts the fixed grid by the symmetry proof.

## originality

PASS

Quadratic spherical harmonic sampling and spherical designs are established; this result gives the exact fixed-truncated-tetrahedron nine-node E-optimal erasure characterization, not generic sampling theory. The cuboctahedral result shares the rank split 128/92 but has a different geometry and does not entail the truncated tetrahedron kernel or eight sharp E-optimal masks.

## value

PASS

Nine is the information-theoretic minimum number of real degree-0-through-2 spherical harmonic coefficients; choosing nine among the natural twelve vertices while maximizing the smallest singular value is a motivated optimal stable recovery problem. The eight exact winning erasure masks and strictly separated lower frame bound give a complete natural finite classification; the equal determinants of all invertible masks additionally show determinant/D-optimality does not distinguish the much sharper E-optimal layouts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
