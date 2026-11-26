# Four rational hyperflexes on smooth plane quartics over the ternary field

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_3}\) be any geometrically smooth plane quartic. A rational hyperflex is a point \(P\in C(\mathbf F_3)\) whose tangent line has intersection divisor \(4P\) with \(C\). Then \(C\) has at most **four** rational hyperflex points. Equality is attained by exactly **2,340 scalar-normalized quartic equations** in fixed projective coordinates. They constitute three \(\operatorname{PGL}_3(\mathbf F_3)\)-orbits of sizes \(1872,234,234\), with stabilizer orders \(3,24,24\), respectively.

Representatives of these orbits, in the variable order \(X,Y,Z\), are:

\[
\begin{aligned}
F_A={}&X^3Y+2X^3Z+2X^2Y^2+X^2YZ+2XY^2Z+XZ^3+Y^4,\\
F_B={}&X^3Z+XZ^3+Y^4,\\
F_C={}&X^4+X^3Y+2X^3Z+XZ^3+Y^4.
\end{aligned}
\]

The three curves have \(5,4,4\) rational points, respectively. The four hyperflexes of \(F_A\) lie on \(Y=0\); those of \(F_B\) have no three collinear; those of \(F_C\) lie on \(X=Y\).

## Assumptions and scope
All coefficients and point coordinates are in \(\mathbf F_3\). Geometric smoothness means nonsingularity after extension to an algebraic closure, not merely at rational points. Two equations are projectively equivalent if one is a nonzero scalar multiple of the pullback of the other by a matrix in \(\operatorname{GL}_3(\mathbf F_3)\). A scalar-normalized coefficient vector has its first nonzero coefficient equal to one, using the monomial order \(X^iY^jZ^{4-i-j}\) with decreasing \(i\) then decreasing \(j\). Thus there are \((3^{15}-1)/2=7,174,453\) such equations.

## Proof
**Contact criterion.** For each of the 13 rational projective points \(P\), each of its four rational lines \(L\), a second vector \(Q\in L\setminus\{P\}\), and a transverse vector \(R\), expand \(F(uP+vQ+wR)\). A rational smooth point \(P\) is a hyperflex with tangent line \(L\) exactly when the coefficients of \(u^4,u^3v,u^2v^2,uv^3\) vanish and that of \(u^3w\) is nonzero. For a geometrically smooth quartic, the coefficient of \(v^4\) is then necessarily nonzero, as otherwise \(L\) would be a component. There are exactly 52 rational point-line flags, and each imposes four independent linear conditions on the 15 coefficients.

**Exhaustive lower bound.** For each flag, row-reduce its four linear forms over \(\mathbf F_3\), enumerate all \(3^{11}\) elements in the kernel, normalize nonzero scalar multiples, test the nonzero transverse coefficient, and count that flag once for each eligible equation. The exact count of equations with precisely the indicated numbers of contact flags is:

| Flags | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Equations | 1,657,656 | 288,522 | 143,780 | 87,750 | 7,020 | 2,496 | 468 | 13 |

There are no cases of 8 through 11. Independently evaluating all three partial derivatives at the 13 rational points shows that **every** equation with at least five such flags is singular at a rational point. The exact candidate totals are 9,997 for at least five flags, and 87,750 for exactly four. The latter contain 52,884 equations with no rational singularity. Euler's identity in characteristic three and degree four guarantees that a common zero of all partials is on the curve. Therefore no geometrically smooth quartic has five rational hyperflexes.

**Completeness at equality.** Apply the four projective substitutions exchanging \(X,Y\), exchanging \(Y,Z\), replacing \(X\) by \(X+Y\), and replacing \(X\) by \(2X\). They generate \(\operatorname{PGL}_3(\mathbf F_3)\), of order 5,616. Exact orbit closure partitions all 52,884 equations without a rational singularity and with four contact flags into 18 orbits. Gröbner bases of the homogeneous partial-derivative ideal on each of the three standard affine charts show that precisely the three representative indices **83262**, **78741**, and **78754** are geometrically smooth; all other orbit representatives have a nonempty geometric singular locus. The three surviving orbits have sizes \(1872,234,234\), proving the total of 2,340 and the classification.

**Explicit geometric smoothness.** For \(F_B\), the partials are \((Z^3,Y^3,X^3)\). For \(F_C\), the partials are \((X^3+Z^3,X^3+Y^3,2X^3)\). Both triples vanish only at the affine origin. For \(F_A\), \((F_A)_Z=2X(X+Y)^2\). If \(X=0\), the other two partials force \(Y=Z=0\). If \(X\ne0\), vanishing of \((F_A)_Z\) forces \(Y=-X\), where \((F_A)_Y=-X^3\ne0\). Thus all three representatives are geometrically smooth. The accompanying contact table verifies four distinct rational hyperflexes on each.

## Verification
The included source programs use only exact integer/finite-field operations; the orbit/smoothness review additionally uses Python, NumPy and SymPy. From the directory containing the packaged files, regenerate flag conditions with `python hyperflex_prep.py`, action matrices with `python hyperflex_orbit_prep.py`, compile `hyperflex_enum.cpp` and `hyperflex_orbits.cpp` with a C++17 compiler, execute the enumerator, execute `python hyperflex_filter.py`, execute `python independent_rational_smoothness.py`, execute the orbit program, then execute `python hyperflex_smooth.py`, `python hyperflex_reps.py`, and `python contact_table.py`. Machine-readable orbit members, rational candidate indices, contact witnesses, and execution summaries are included. The independent standard-library Jacobian screening reproduces the 52,884-candidate list exactly and confirms that all 9,997 cases with at least five flags are singular at a rational point. These are finite exhaustive computations, not extrapolations from random sampling.

## Relationship to prior work
Oyono and Ritzenthaler study hyperflexes, inflection phenomena, and characteristic-three exceptions for plane quartics (arXiv:1006.0873), including the exceptional Fermat quartic. Their geometric contact analysis does not state this particular sharp \(\mathbf F_3\)-rational hyperflex count or the three arithmetic projective orbits. Bergvall (arXiv:2106.13072, first publicly available 2021-06-24) determines arithmetic and cohomological invariants of plane quartics marked by bitangent configurations, but the marked-bitangent counts do not specify when two tangencies merge into a rational hyperflex or enumerate these three extremal orbits. Dolgachev and Martin classify automorphism groups in odd characteristic (DOI:10.1112/jlms.12905), including characteristic-three Fermat exceptional behavior, not this finite-field contact census. The result is not claimed to be independently validated or publication-priority certified.

## Limitations
The statement concerns rational contact points over exactly \(\mathbf F_3\); it does not bound geometric hyperflexes, which can be much more numerous, nor does it address arbitrary finite extensions or classify quartics with three or fewer rational hyperflexes. The comparison literature and searchable databases do not establish exhaustive publication novelty: unindexed characteristic-three computational classifications, unpublished databases or implied consequences of prior full tables remain possible. The finite certificates and reconstruction code are provided for reproduction, not external certification.

## References
1. R. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, arXiv:1006.0873.
2. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072 (initial posting 2021-06-24).
3. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, Journal of the London Mathematical Society (2024), DOI:10.1112/jlms.12905.
4. E. Costa, D. Harvey, and A. Sutherland, *Counting points on smooth plane quartics*, arXiv:2208.09890.
