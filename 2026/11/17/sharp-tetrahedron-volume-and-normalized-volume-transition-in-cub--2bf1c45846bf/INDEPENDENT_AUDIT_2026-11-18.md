# Independent mathematical audit

## correctness

PASS

For 1<h<3 the extreme vertices are the eight cube corners and six +/-h axis points. The determinant of any tetrahedron is multiaffine in its four points, so its absolute maximum reduces to 1001 vertex quadruples. Verified the actual standalone checker builds degree<=3 integer determinant polynomials and checks both signs of their gaps against five classwise envelopes in degree-3 Bernstein form on h=1+2s, s in [0,1]. Independently regenerated all 1001 determinants and EXACTLY 8008 nonnegative rational coefficients, with tight class counts 2,48,12,8,12 for 0..4 axial vertices. Comparing envelopes on (1,3) yields max{16,h²(h+3)}, with exactly two complementary cube maximizers and eight axis+opposite corner maximizers (ten at crossover r); independent pair comparison found no two maximal vertex tetrahedra sharing three vertices, and multiaffine convex combinations then exclude nonvertex optimizers. Cube volume 8, six pyramid extensions volume 8h on [1,2], and octahedron plus eight corner pyramids volume 4h² on [2,3], with 4h³/3 beyond; dividing determinant/6 gives five monotone branches, unique min 1/(3r). Boundary h=1,3 volumes match, but no equality-classification at those endpoints is asserted. This is an exact symbolic all-interval certificate combined with analytic vertex-reduction; not interpolation from numerical samples.

## originality

PASS

Best-of-knowledge PASS. An older published theorem gives largest tetrahedra for the polar-related intersection K_c=[-1,1]^3 cap cB_1^3; polarity relates support geometry but does not preserve largest contained tetrahedron volumes or their normalized ratio, so its exact three-phase profile does not imply this hull result. Akopyan–Glazyrin (2014) provide general maximal-simplex/Radon structural results but not the specific h-dependent 14-vertex hull phase diagram; Gritzmann–Klee–Larman (1995) concern general qualitative/computational complexity, and full exhaustive priority remains a risk.

## value

PASS

The cube–octahedron hull is a natural one-parameter transition including cube, rhombic dodecahedron and octahedron. Its exact largest-simplex occupancy and all equality types have a non-obvious algebraic switching point r<2 and unique worst ratio at a nonregular member, a motivated finite-dimensional extremal geometry result rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
