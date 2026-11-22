# The parity–Picard conic-pencil support lattice of cubic surfaces

## Finding

Let \(S\) be any smooth cubic surface over an algebraically closed field of characteristic zero. Write \(\mathcal L\) for its set of \(27\) geometric lines and \(F=\mathbb Z^{\mathcal L}\) for the free abelian group of formal line symbols \(e_\ell\). Projection from any line \(\ell\) induces a conic-bundle pencil with exactly five reducible fibers; these consist of the ten other lines meeting \(\ell\). Set
\[
 c_\ell=\sum_{m\ne\ell,\;m\cdot\ell=1}e_m,\qquad L_{\mathrm{con}}=\sum_{\ell\in\mathcal L}\mathbb Zc_\ell.
\]
Let \(\pi:F\to\operatorname{Pic}(S)\) take a formal symbol to the corresponding divisor class. Then the complete integral membership test is
\[
\boxed{L_{\mathrm{con}}=\left\{v=\sum_\ell a_\ell e_\ell:\ \sum_\ell a_\ell\equiv0\pmod2,\ \pi(v)\in5\operatorname{Pic}(S)\right\}.}
\]
Equivalently,
\[
\boxed{\operatorname{coker}(F\longleftarrow\mathbb Z^{\mathcal L})\cong\mathbb Z/10\mathbb Z\oplus(\mathbb Z/5\mathbb Z)^6},
\]
where the displayed arrow has columns \(c_\ell\). Thus its integral Smith form is
\[
\boxed{\operatorname{diag}(1^{20},5^6,10)},\qquad [F:L_{\mathrm{con}}]=2\cdot5^7=156250.
\]
In particular, the least positive integer multiplying an individual line symbol into the support lattice is exactly \(10\), independent of the line or the cubic surface.

## Assumptions and scope

All statements concern **formal unsigned integer combinations** of the \(27\) lines, not torsion in \(\operatorname{Pic}(S)\) or an arithmetic Galois-descent assertion. Fix a blow-down of six disjoint lines to six general points of \(\mathbb P^2\). In the standard basis \(H,E_1,\ldots,E_6\) of \(\operatorname{Pic}(S)\), with intersection form \(H^2=1\), \(E_i^2=-1\), and all other basis pairings zero, the \(27\) line classes are
\[
E_i\quad(1\le i\le6),\qquad L_{ij}=H-E_i-E_j\quad(1\le i<j\le6),\qquad Q_i=2H-\sum_{j\ne i}E_j\quad(1\le i\le6).
\]
The anticanonical hyperplane class is \(h=-K_S=3H-\sum_iE_i\). The support vector \(c_\ell\) counts the **ten distinct components** of all five reducible fibers of the residual plane-section pencil, each exactly once. There are no coefficients from fiber multiplicities or from rational field extensions.

## Proof

**1. Conic geometry and the two congruences.** A plane through a fixed line \(\ell\) cuts out \(\ell\) and a residual conic of divisor class \(h-[\ell]\). The five singular residual conics split into two lines each. The twenty-seven-line intersection configuration has exactly ten lines meeting \(\ell\), paired by the five plane sections (the explicit class verification is reproduced by the accompanying exact checker). Consequently
\[
 \pi(c_\ell)=5(h-[\ell])\in5\operatorname{Pic}(S),\qquad \deg(c_\ell)=10\equiv0\pmod2.
\]
Thus \(L_{\mathrm{con}}\) is contained in the right-hand congruence lattice, say \(B\).

**2. The determinant fixes the index of the conic support image.** In the above line-label order, let \(A\) be the \(27\times27\) symmetric matrix with \(A_{\ell m}=1\) for distinct meeting lines and \(0\) otherwise. Its columns are the \(c_\ell\). The intersection counts for the \(27\) lines are: each line meets ten other lines; two distinct meeting lines have exactly one further line meeting both; and two distinct skew lines have exactly five common meeting lines. These follow by direct substitution of the \(27\) displayed Picard classes, without any choice of special cubic surface. Writing \(J\) for the all-ones matrix, these counts give
\[
 A\mathbf1=10\mathbf1,\qquad A^2=5I-4A+5J.
\]
Since \(A\) is symmetric, the orthogonal complement of \(\mathbf1\) has eigenvalues among the roots of \(t^2+4t-5=(t-1)(t+5)\). As \(\operatorname{tr}A=0\), they occur with multiplicities \(20\) and \(6\). Hence
\[
 \det A=10\cdot1^{20}\cdot(-5)^6=156250=2\cdot5^7,
\]
and \([F:L_{\mathrm{con}}]=156250\).

**3. The congruence lattice has exactly the same index.** The line classes generate \(\operatorname{Pic}(S)\) integrally: the \(E_i\) occur as line classes, and \(H=L_{12}+E_1+E_2\). Hence \(\pi\) is surjective onto the free rank-seven Picard lattice. Consider
\[
 \Psi:F\longrightarrow\mathbb Z/2\mathbb Z\oplus\operatorname{Pic}(S)/5\operatorname{Pic}(S),\quad v\longmapsto\bigl(\sum_m a_m\bmod2,\pi(v)\bmod5\bigr).
\]
The Picard component is surjective. Moreover \(5e_\ell\) maps to \((1,0)\), proving that parity is independently surjective, too. Thus \(\Psi\) is surjective, \(B=\ker\Psi\), and \([F:B]=2\cdot5^7=156250\). Since \(L_{\mathrm{con}}\subseteq B\) and their indices agree, they are equal. The first isomorphism theorem gives
\[
 F/L_{\mathrm{con}}\cong\mathbb Z/2\mathbb Z\oplus(\mathbb Z/5\mathbb Z)^7\cong\mathbb Z/10\mathbb Z\oplus(\mathbb Z/5\mathbb Z)^6.
\]
The corresponding invariant factors are twenty units, six fives and one ten, as claimed.

**4. Sharp individual-line obstruction.** A line class \([\ell]\in\operatorname{Pic}(S)\) is primitive, since it has anticanonical degree \(h\cdot\ell=1\). If \(ne_\ell\in L_{\mathrm{con}}\), the two congruences force \(n\) even and \(5\mid n\); conversely \(10e_\ell\) satisfies both and therefore lies in the lattice. The exact order is \(10\).

## Verification

Execute `python3 verify_conic_support.py` with Python 3 and the standard library. The verifier rebuilds the \(27\) Picard classes, reconstructs every meeting relation and all five disjoint reducible-fiber pairs for each center line, verifies each support class equals \(5(h-[\ell])\), and checks all common-neighbor counts and the quadratic matrix identity. Exact fraction-free Bareiss elimination gives \(\det A=156250\). Independent modular elimination checks that the Picard map has rank seven modulo five and the support matrix rank twenty modulo five. The verifier prints `VERIFY_OK` followed by the key values.

An independent exact computer-algebra cross-check using SymPy computed the same determinant and Smith diagonal \(1^{20},5^6,10\); that external computation is not needed to reproduce the proof, which uses only integer identities and index comparison. Both procedures compute a finite \(27\times27\) universal incidence matrix; the extension from this matrix to *every* smooth cubic surface follows from the classical six-point blow-up classification, not a finite sampling argument.

## Relationship to prior work

The geometry of the \(27\) lines, their pairwise intersection graph, and the five singular fibers of the conic pencil through a marked line are classical. Casalaina-Martin, Grushevsky and Hulek (arXiv:2312.15369, Remark 3.2) explicitly use the five-fiber conic bundle in studying moduli of cubic surfaces with a line; their results concern moduli and nef/effective cones, not this integral support lattice. Published graph data for the *complement* of the Schläfli graph supply the intersection graph's eigenvalues, but rational spectra alone do not determine a Smith form or the intrinsic Picard-congruence image.

A published integral tritangent presentation concerns a \(27\)-by-\(45\) incidence map generated by three-line tritangent supports, while published double-six results concern a \(27\)-by-\(36\) twelve-line support map; their distinct source modules and congruences do not directly determine this \(27\)-by-\(27\) ten-line conic-support image. Özçelebi (2012, §6.3) studies *non-collinearity* generalized-quadrangle graphs, including the complementary Schläfli relation; it is not the meeting-line support map analyzed here. The new assertion assessed here is the exact two-condition integral membership criterion and its sharp tenfold obstruction, not the classical graph spectrum or conic geometry.

## Limitations

The result proves an integral statement over algebraically closed fields of characteristic zero. It does not assert a new cubic-surface classification, a finite-field descent theorem, or torsion in the surface's Picard group. The calculation is universal because the abstract \(27\)-line incidence configuration is universal; it is not moduli-sensitive. The published graph spectrum and the elementary index argument make the numerical Smith diagonal accessible, and equivalent historical work in integral association schemes or generalized-quadrangle incidence may exist; historical priority is therefore a residual risk. Independent mathematical validation has not been performed.

## References

1. S. Casalaina-Martin, S. Grushevsky and K. Hulek, *The birational geometry of moduli of cubic surfaces and cubic surfaces with a line*, arXiv:2312.15369v1 (first posted 2023-12-23); updated version arXiv:2312.15369v2, Remark 3.2. https://arxiv.org/abs/2312.15369 and https://arxiv.org/html/2312.15369v2.
2. *Complement of Schläfli graph*, DistanceRegular.org (last updated 2018-08-14), graph parameters, spectrum, and adjacency resources. https://www.math.mun.ca/distanceregular/graphs/complement-schlafli.html.
3. Ç. Güven Özçelebi, *Buildings and Kneser Graphs*, Ph.D. thesis, Eindhoven University of Technology (2012), §6.3 on Smith forms for non-collinearity graphs, DOI:10.6100/IR721532. https://research.tue.nl/files/3689733/721532.pdf.
4. A.-S. Elsenhans and J. Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra*, arXiv:1006.1474 (2010), classical tritangent and Steiner geometry. https://arxiv.org/abs/1006.1474.
