# Ten projective classes of smooth plane quartics with extremal nontrivial blocking sets over \(\mathbf F_3\)

## Finding

A set of rational points in a projective plane is **blocking** if it meets every rational line, and **nontrivially blocking** if it contains no entire rational line. Among geometrically smooth plane quartics \(C\subset\mathbf P^2_{\mathbf F_3}\) for which \(C(\mathbf F_3)\) is a nontrivially blocking set of minimum cardinality, the minimum is six. Precisely **51,948** distinct projective quartic equations, modulo nonzero scalar multiplication, have this property. They form exactly **ten** classes under \(\operatorname{PGL}_3(\mathbf F_3)\), nine of size **5,616** and one of size **1,404**. Their respective rational projective stabilizers have orders one and four.

The 13-point rational projective plane has exactly **234** nontrivial blocking six-sets, forming a single orbit under \(\operatorname{PGL}_3(\mathbf F_3)\). For each such set \(B\), exactly **222** smooth quartic projective equations have rational zero set **exactly** \(B\). This gives \(234\cdot222=51,948\), and the ten-orbit statement refines the count.

The exceptional class with stabilizer of order four has a representative
\[
X^3Y+X^2Z^2+XY^3+XYZ^2-XZ^3-Y^3Z+Y^2Z^2=0.
\]

## Assumptions and scope

The ground field is \(k=\mathbf F_3\); all coefficients and projective automorphisms are \(k\)-rational. A quartic is **geometrically smooth** when its projective base change to an algebraic closure is smooth. Curves are counted as fixed-coordinate homogeneous degree-four equations up to the two nonzero scalars in \(k\), and equivalence classes are for projective coordinate transformations over \(k\), not arbitrary abstract-curve isomorphisms. Rational-point sets are required to contain precisely six points; a blocking set of six points is called *extremal nontrivial* because no nontrivial blocking set of smaller size exists in \(\mathbf P^2(k)\).

Projective points are normalized by making their first nonzero coordinate one and sorted lexicographically. In this order the selected set has bitmask `311`, i.e. consists of
`(0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,1)`.
Polynomial coefficient strings use the exact lexicographic monomial order
\[
X^4,X^3Y,X^3Z,X^2Y^2,X^2YZ,X^2Z^2,XY^3,XY^2Z,XYZ^2,XZ^3,Y^4,Y^3Z,Y^2Z^2,YZ^3,Z^4.
\]
The ten verified projective representatives and their orbit sizes inside the stabilizer of this selected rational set appear in `verification/orbit_representatives.txt`.

## Proof

**1. The extremal rational configurations.** Enumerate the 13 normalized projective points and the 13 four-point rational lines. Iterate over every subset of at most six points, accepting only subsets meeting all lines and containing no full line. This exhaustive finite calculation finds no qualifying subsets with at most five points and precisely 234 qualifying six-subsets. Direct enumeration of all 5,616 elements of \(\operatorname{PGL}_3(k)\) shows that those 234 subsets form one orbit and that the indicated six-set has stabilizer order 24. The exact point, line, and matrix enumerators are given in `verification/orbits.py`; the independent incidence enumeration is also in `verification/groebner.py`.

**2. Quartics with the prescribed rational set.** Evaluate the 15 degree-four monomials at the six specified points. Their evaluation matrix has rank six, so its kernel has dimension nine. Its nonzero vectors number \(3^9-1=19,682\). The coefficient enumeration in `verification/enumerate.cpp` examines every one of these vectors, checking all 13 projective points. Exactly 1,134 nonzero vectors vanish **precisely** on the chosen six-set, corresponding to 567 projective equations after dividing by the two scalar representatives. A separately row-reduced kernel is constructed in `verification/groebner.py` and yields the same 567 equations.

**3. Exact test of smoothness over the algebraic closure.** Let \(F\) be any ternary quartic and \(J=(F_X,F_Y,F_Z)\). The characteristic is three, so Euler's identity reads \(F=XF_X+YF_Y+ZF_Z\). Thus a nonzero geometric common zero of the cubic partials is automatically a singular point of the projective curve. The three partials have no common nonzero geometric zero **if and only if** their degree-seven multiples by all degree-four monomials span the 36-dimensional space of ternary degree-seven forms. Indeed, absence of a projective common zero makes their ideal an ideal of height three and hence a regular sequence of three cubics in the Cohen–Macaulay ring \(\bar k[X,Y,Z]\); its quotient has Hilbert series \((1+t+t^2)^3\) and vanishes in degrees at least seven. Conversely, a projective zero would annihilate every degree-seven element of the ideal, making full rank impossible. These are exact criteria, with no bounded-extension sampling.

The modular-rank computation returns rank 36 for precisely **444** of the 1,134 prescribed-point coefficient vectors, i.e. 222 distinct projective equations. An independently coded Gröbner-basis computation eliminates all three projective affine charts for the 567 normalized quartics, finding exactly **222** geometrically smooth equations. The sets of normalized smooth coefficient vectors from both methods coincide exactly.

**4. Projective orbit decomposition.** For each of the 24 matrices stabilizing the selected rational six-set, substitute the three transformed linear forms into each normalized quartic, then normalize its first nonzero coefficient to one. Applying these 24 transformations to the complete set of 222 smooth quartics partitions it into exactly ten orbits: nine of length 24 and one of length six. Since all 234 six-sets form one orbit under the full group of order 5,616, the ten full curve-orbit sizes are nine copies of \(234\cdot24=5,616\) and one copy of \(234\cdot6=1,404\). Their stabilizer orders follow by the orbit–stabilizer theorem. The equality \(9\cdot5,616+1,404=51,948\) completes the classification.

## Verification

Run the standalone commands in `VERIFICATION.md` from the package root. `verification/enumerate.cpp` performs a nine-dimensional coefficient enumeration and exact finite-field row rank; `verification/groebner.py` constructs a different kernel and runs Gröbner elimination; `verification/orbits.py` enumerates the entire rational projective group and exact representative orbits. The generated output and reference lists are supplied in the `verification` directory. Independent normalization of the smooth lists gives an identical 222-element set. Every computation is over integers reduced exactly modulo three.

## Relationship to prior work

Asgarli–Ghioca–Yip (2022; arXiv:2208.13299) introduce algebraic curves with blocking rational point sets and establish degree-dependent obstructions and constructions, including a quartic nonblocking result over sufficiently large fields; their work does not give the small-field smooth-quartic six-point classification above. Their subsequent arithmetic-statistics paper (arXiv:2211.08523, first public 2022) determines exact limiting blocking densities over \(\mathbf F_3\) for degrees at least five; the authors explicitly impose that threshold in Example 7.2, whereas the present theorem concerns geometric smoothness and degree four and resolves projective orbits. Lercier–Ritzenthaler–Rovetta–Sijsling (arXiv:1403.0562) give a broad smooth-plane-quartic parametrization and computational class studies, but their displayed finite-field class tables concern larger characteristics and do not specify the incidence property here. The finite-geometric blocking-set classification of Coolsaet–Botteldoorn–Fack concerns rational point configurations, not which smooth quartic equations realize them. Each distinction concerns implications and hypotheses, rather than merely differing titles.

## Limitations

The classification concerns only extremal **nontrivial** six-point rational blocking sets over the field with three elements. It does not count all blocking quartics with larger rational sets, give a characteristic-uniform classification, or establish publication priority against unpublished or unindexed computational catalogues. The finite counts are computer-assisted but exhaustive by proved finite search domains; the geometric smoothness criterion is exact over the algebraic closure. Independent external audit has not been performed.

## References

1. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first posted 2022-08-28); Designs, Codes and Cryptography 91 (2023), 3643–3669.
2. S. Asgarli, D. Ghioca and C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523 (first posted 2022-11-15); Journal of Combinatorial Theory A 204 (2024), article 105871, especially Example 7.2.
3. R. Lercier, C. Ritzenthaler, F. Rovetta and J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562 (2014).
4. J. Coolsaet, J. Botteldoorn and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs (2022), DOI 10.1002/jcd.21842.
