# Independent mathematical audit

## correctness

PASS

I regenerated the full census with `python /workspace/replay/cubics.py 200 <frozen-dir>/orbits.csv`. The twenty degree-three monomials give 2^20-1 nonzero masks. Swaps of neighboring coordinates and a single shear generate GL_4(F2): conjugation supplies all elementary shears, and Gaussian elimination requires no nontrivial scalings. Thus the independent orbit traversal covers PGL_4(F2) with no scalar quotient. It found 141 orbits on 1,048,575 forms and matched every orbit minimum and weight in the frozen CSV, which it used only for comparison. Geometric smoothness was checked by affine-chart unit-ideal tests over F2; a proper ideal stays proper after field extension and has an algebraic-closure zero, and the Euler identity in characteristic two ensures a common zero of the four homogeneous partials lies on the cubic. I independently tested tritangent sections by exact linear divisibility, not by generating the frozen list's products: a candidate linear form divides a section precisely when elimination of its pivot annihilates the restricted polynomial. If a nonzero cubic has three distinct geometric linear factors, Frobenius permutes them in a triple, a fixed line and a pair, or three fixed lines, so the relevant field is respectively F8, F4, or F2. Testing for three distinct divisors over these fields proves both directions and yielded 106 section masks. Applying the tests to all 15 rational planes and exact zero restriction to all 35 rational lines per smooth orbit gave 36 smooth orbits, 322560 smooth equations, and all 15 table rows with both multiplicities as printed. The explicit masks 66880 and 67195 gave (weight, line count, tritangent count)=(28,15,15) and (840,0,9). The first attains the total number of available planes; the second really permits conjugate components. The computation does not extend beyond F2.

## originality

PASS

Pass for the complete equation- and projective-orbit-weighted joint distribution over F2, not for the classification of smooth forms, the rational-line counts alone, or the generic fixed-count table indexed by Weyl conjugacy class. Parts of the result overlap existing data: a smooth cubic with fifteen rational lines already forces every plane to be tritangent by counting the 45 incidences of those lines with rational planes. The full weighted distribution, including multiplicities for the classes with few or no rational lines, was not found or mechanically obtained from the available prior tables.

## value

PASS

The smallest base field gives a natural exact census in which fixed plane sections bear directly on arithmetic descent of tritangents, not simply on whether their line components are rational. Equation counts and class counts answer different frequency questions because of automorphisms. A complete cross-tabulation is useful for checking small-field classification and Frobenius computations; the 840 equations with no rational lines but nine rational tritangents give a sharp concrete illustration of why the joint observable is needed. The value is not the re-enumeration of known forms or the generic Weyl-class data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
