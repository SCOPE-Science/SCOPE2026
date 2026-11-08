# One projective orbit of smooth quartics attaining both blocking minima over \(\mathbb F_5\)

## Finding
Let \(k=\mathbb F_5\). A geometrically smooth plane quartic is called *minimum blocking* when its set of \(k\)-rational points meets every rational projective line and contains the minimum possible number of points for a nontrivial blocking set. By Blokhuis's bound, this minimum is nine. Among homogeneous quartic equations over \(k\), identified up to multiplication by \(k^\times\), **exactly 372,000** define minimum-blocking smooth curves. They form **one orbit under \(\operatorname{PGL}_3(k)\)**; the projective stabilizer of each is trivial. Every such curve has precisely nine rational points and geometric genus three.

One representative, with all coefficients interpreted modulo five, is
\[
3X^3Y+4X^3Z+4X^2YZ+2XY^3+3XY^2Z+XZ^3+4Y^3Z+YZ^3=0.
\]
The nine rational points are the standard projective triangle
\[
\Delta=\{[0:1:-s^2],[1:-s^2:0],[-s^2:0:1]:s\in\mathbb F_5\}.
\]
These curves simultaneously attain the lower bound on the number of points in a nontrivial blocking set and the minimum degree of a geometrically smooth nontrivially blocking plane curve over \(\mathbb F_5\). The degree-three obstruction is already known; the new contribution is the complete nine-point quartic classification and its single-orbit rigidity.

## Assumptions and scope
All lines, rational points, coefficients, and projective transformations are defined over \(\mathbb F_5\), except when testing geometric smoothness over its algebraic closure. There are 31 rational projective points and 31 rational lines, with six points on each line. A blocking set meets every line; it is nontrivial if it contains none of the six-point lines. Equations differing by a nonzero scalar define the same plane curve. An orbit under \(\operatorname{PGL}_3(\mathbb F_5)\) means an orbit of embedded plane quartics, not an abstract isomorphism class of genus-three curves.

## Proof
**1. The nine-point blocking sets.** The prime-field lower bound of Blokhuis gives \(|B|\ge 3(5+1)/2=9\) for every nontrivial blocking set. Enumerate the 31 normalized projective points and their 31 line-incidence masks. The file `verify_nine_point_blockers.cpp` traverses **every** \(\binom{31}{9}=20,160,075\) nine-subset via Gosper's exact next-combination algorithm, checks that it meets all 31 lines, and separately rejects any subset containing a complete line. It obtains 86,800 blocking nine-sets, of which 71,300 are trivial and **15,500 are nontrivial**. This is an exhaustive finite enumeration, not a random sample.

The displayed set \(\Delta\) has nine elements, meets every line, and contains no full line. Its exactly three four-secants are the three coordinate sides. Any projectivity preserving \(\Delta\) must permute these sides and therefore has a monomial matrix. The side-point ratios are \(\{1,-1\}\) away from the vertices, so its diagonal entries must agree up to independent signs, modulo common scalar. The stabilizer has order \(6\cdot4=24\). Conversely all 24 signed monomial projectivities preserve \(\Delta\). Since \(|\operatorname{PGL}_3(\mathbb F_5)|=372,000\), its orbit contains \(372,000/24=15,500\) distinct nine-point sets, exhausting the preceding incidence census.

**2. Quartics over one triangle.** The space of ternary quartic forms has dimension 15. Evaluation at the nine points of \(\Delta\) has rank nine, so the vanishing space is six-dimensional. Its projective space has \((5^6-1)/4=3,906\) nonzero scalar classes. The file `verify_triangle_quartics.py` constructs a modular row-reduced nullspace basis, enumerates precisely these 3,906 classes, and evaluates each at all 31 rational points. The exact point-count histogram is
\[
\begin{array}{c|rrrrrrrrrrrr}
\#C(\mathbb F_5)&9&10&11&12&13&14&15&16&17&18&19&21\\\hline
\#\text{forms}&24&240&564&560&750&564&665&228&180&40&82&9.
\end{array}
\]
In particular, **24** projective quartic forms have rational zero set exactly \(\Delta\). The same code applies all 24 signed monomial transformations to one of these forms, normalizes its nonzero scalar, and finds exactly the complete set of 24. Hence the stabilizer of any one quartic inside the triangle stabilizer is trivial.

**3. Geometric smoothness.** The representative in the Finding section is one of these 24 forms. Let \(f_X,f_Y,f_Z\) be its dehomogenizations in the three standard affine charts. For each chart, exact Gröbner-basis reduction over \(\mathbb F_5\) gives the unit ideal
\[
(f_X,\partial_1 f_X,\partial_2 f_X)=(1),\quad
(f_Y,\partial_1 f_Y,\partial_2 f_Y)=(1),\quad
(f_Z,\partial_1 f_Z,\partial_2 f_Z)=(1).
\]
Therefore there are no singular points even over the algebraic closure. Geometric smoothness is preserved under every projectivity, so all 24 members of the triangle orbit are geometrically smooth. A geometrically smooth plane quartic has genus \((4-1)(4-2)/2=3\).

**4. Exhaustion and orbit count.** Any smooth quartic whose rational points are a minimum nontrivial blocking set has exactly nine rational points; its point set is projectively equivalent to \(\Delta\) by step 1. Under this transformation the quartic is among the 24 forms of step 2 and hence among the 24 smooth forms of step 3. Distinct nine-point sets cannot describe the same quartic in this locus. Consequently the total number of scalar-normalized equations is \(15,500\cdot24=372,000\), one full projective orbit; because the group itself has this order, each curve has trivial projective stabilizer.

## Verification
Compile and run `verify_nine_point_blockers.cpp` with a standard C++17 compiler, for example `c++ -O2 -std=c++17 verify_nine_point_blockers.cpp -o nine_blockers && ./nine_blockers`. Its deterministic completion line is `NINE_POINT_BLOCKING_CENSUS_PASS 20160075 86800 15500 71300 9`.

Run `python3 verify_triangle_quartics.py` with Python 3 and SymPy. Its deterministic completion line begins `TRIANGLE_QUARTIC_REPLAY_PASS 31 31 9 6 3906 24 24`, followed by the representative and complete rational-point histogram. The script also confirms directly that the distinct smooth blocking quartic displayed in the motivating paper has eleven rational points, not nine. The geometric-smoothness conclusion relies on the exact three-chart Gröbner reductions, not on testing finitely many extension-field points.

## Relationship to prior work
Asgarli, Ghioca, and Yip (arXiv:2208.13299, 2022) establish the minimum-degree obstruction for irreducible cubic blocking curves and construct smooth blocking quartics for \(q=5\) in their Theorem 1.8. Their particular quartic has eleven \(\mathbb F_5\)-rational points by direct evaluation. Their Remark 5.3 explicitly discusses the challenge of obtaining smooth curves through the projective triangle when \(q\equiv1\pmod4\); neither their existence result nor that remark classifies the nine-point quartics or their projective stabilizers. Their published existence result is fully acknowledged rather than claimed again.

Coolsaet, Botteldoorn, and Fack (2022) give a computer classification of minimal blocking **point sets** in small Desarguesian projective planes. Such an incidence classification does not classify smooth quartic equations through the points, determine smoothness of their complete linear systems, or yield the one-orbit conclusion. Asgarli, Ghioca, and Yip (arXiv:2211.08523) study counting and asymptotic densities of blocking curves, including formulas for arbitrary-degree counting, without a smooth minimum-nine-point quartic classification at \(q=5\).

## Limitations
This is a theorem about projective plane quartic models over \(\mathbb F_5\), not all genus-three curves up to abstract isomorphism, and not smooth quartics whose blocking point set has more than nine rational points. It does not determine zeta functions, Jacobian endomorphism rings, or geometric automorphism groups over the algebraic closure. The finite classification depends on executing the complete, inspectable incidence and linear-algebra enumeration; the unit-ideal computations supply the necessary algebraic-closure smoothness test. An inaccessible or unindexed historical quartic census could affect originality, and no independent external audit has been performed.

## References
- S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first submitted 2022-08-28), Sections 3, 5, 7, especially Theorem 1.8 and Remark 5.3. https://arxiv.org/html/2208.13299v2
- K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Des. 30 (2022), 561–580, doi:10.1002/jcd.21842 (first published 2022-03-31).
- S. Asgarli, D. Ghioca, C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523 (first submitted 2022-11-15), Sections 1, 2, 7. https://arxiv.org/html/2211.08523v2
