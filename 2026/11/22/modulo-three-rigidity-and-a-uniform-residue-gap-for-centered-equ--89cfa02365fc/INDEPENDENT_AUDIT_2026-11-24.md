# Independent mathematical audit

## correctness

PASS

The centroid and equal sides give each squared vertex norm s²/3. Each coordinate row is in the hexagon with vertices the six permutations of (1,−1,0); strict convexity gives row energy ≤2 with exactly those equality cases. Equal column energies at saturation force d/3 zeros per column; counting the zero-position blocks and two signs per row, then dividing by six, gives the claimed labelled-cube count and orbit. For a row (a,−b,−c), a=b+c with 0≤c≤b, rounding to (1,−1,0) costs at most the row deficit e by the convex endpoint test in b. The absolute squared-entry errors sum to e+2c²≤2e since e≥2c(1−c) and c≤1/2. For rounded integer energies totaling 2d, balancing minimizes the sum of absolute deviations from (2d−δ)/3. In residue 1 for δ<2 the minimum is (4+δ)/3, and in residue 2 for δ<1 it is (4−δ)/3; the complementary δ ranges are automatic. In residue 0 a nonbalanced triple has at least one energy ≤2m−1, hence total deviation ≥δ+2(1−δ/3), impossible if δ<6/5. The balanced rounding thus attains saturation in the same cube with cost ≤δ. Direct squaring of the three blocks gives column energies 8−4√3, 2, and 8−4√2 in dimensions 2, 3, and 4 respectively. Stacking adds the energies and preserves centering and equal column norms, proving the construction bounds and asymptotic.

## originality

PASS

With centroid fixed to the cube center and vertices allowed anywhere in the cube, the sharp saturation and enumeration together with the dimension-uniform residue gaps and labelled stability are materially distinct from the unconstrained maximum and from the inspected cube-section and simplex-embedding results. The shared coordinatewise approach and residue-three organization with Ionin are credited. No distinct catalogue claim or accessible prior result was verified to cover this centered statement.

## value

PASS

The prescribed centroid defines a natural constrained counterpart to the known inscribed equilateral-triangle problem. The work goes beyond a cap or three-dimensional example: it gives every saturation shape, a dimension-independent quantitative obstruction in the other residues, and a stability statement converting a near optimizer into a labelled saturation configuration. The finite block constructions make the remaining asymptotic gap genuinely bounded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
