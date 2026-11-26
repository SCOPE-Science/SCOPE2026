# Independent mathematical audit

## correctness

PASS

After dephasing, four rows either give the four orthogonal characters of a plane or give columns (1,(-1)^x,(-1)^y,(-1)^z). In the latter case no three distinct cube vertices are collinear. For four distinct vertices, anchoring at one and removing the dephased first row and column extracts a factor of 8 times a binary 3-by-3 determinant. Mod-two independence makes it odd, and the Hadamard bound on the original sign matrix forces magnitude 8. For a projected affine plane, normals of weights one and two give coordinate/equality planes over the reals (six faces and six diagonal rectangles, rank three); the two parity cosets have determinant magnitude 16, as follows from the anchored columns 110, 101, 011. Of 70 projected four-sets this gives 56, 12 and 2 in the respective categories. Counting original four-sets by fiber occupations (4), (3,1)/(2,2), (2,1,1), (1,1,1,1) and weighting by P=N(N-1)(N-2)/24 and I=P(N-4) reproduces all formulas. I independently multiplied out the occupancy polynomials with denominator 2359296 and compared coefficients for each rank; all four identities held. D8=56I(N/8)^4 and D16=P(N/4)^4+2I(N/8)^4 simplify to the stated polynomials. These arguments include N=8 and empty occupancy classes. RESULT.md line 48's wording about faces is imprecise; the count is six faces plus six diagonal rectangles. The frozen checker.cpp was read, not executed; it checks the two finite orders by integer rank/determinant tests against occupancy formulas, not the symbolic polynomial identity. The replay of the independent coefficient check is to expand the occupancy expressions stated in the originality comparison below after substituting u=N/4, v=N/8, T=P(N-4), and multiply each polynomial by 2359296. No finite test is needed for the quantified proof.

## originality

FAIL

A distinct earlier indexed statement gives the identical all-d rank and absolute determinant distributions and the same projection-level classification. All of the headline polynomials are algebraic re-expressions of that statement. This is demonstrable equivalence to the earlier catalogue finding, not an attribution of human priority or a conclusion from search similarity alone.

## value

FAIL

A complete census is a natural interpolation/design invariant, but this submission adds only expanded forms of an already available exact count and repeats the classification and finite examples. There is no distinct gap, meaningful quantitative improvement, or independently useful new remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
