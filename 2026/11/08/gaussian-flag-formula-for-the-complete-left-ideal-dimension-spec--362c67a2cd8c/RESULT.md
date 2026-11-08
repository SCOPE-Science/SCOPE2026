# Gaussian flag formula for the complete left-ideal dimension spectrum of triangular matrix algebras

## Finding
For every integer \(n\ge1\) and every finite field \(\mathbb F_q\), write \(T_n(\mathbb F_q)\) for the algebra of upper-triangular \(n\times n\) matrices. Let \(\mathcal Z_{n,q}(T)=\sum_I T^{\dim I}\), summing over its distinct left ideals, each considered as a vector subspace of the fixed labeled algebra. Put \(d_{n+1}=0\). Then
\[
\boxed{\mathcal Z_{n,q}(T)=\sum_{\substack{0\le d_n\le\cdots\le d_1\\d_i\le n-i+1}}\left(\prod_{i=1}^{n}{n-i+1-d_{i+1}\brack d_i-d_{i+1}}_q\right)T^{\sum_i d_i}.}
\]
The Gaussian symbol \({a\brack b}_q=\prod_{j=0}^{b-1}(q^{a-j}-1)/(q^{b-j}-1)\), with \({a\brack0}_q=1\), counts \(b\)-dimensional subspaces of \(\mathbb F_q^a\). Thus the formula determines the number of left ideals of **every** possible dimension, in all dimensions and characteristics. The first cases are
\[
\mathcal Z_{2,q}(T)=1+(q+1)T+2T^2+T^3,
\]
\[
\mathcal Z_{3,q}(T)=1+(q^2+q+1)T+(q^2+2q+2)T^2+(q^2+2q+3)T^3+(2q+3)T^4+3T^5+T^6.
\]
Over \(\mathbb F_2\) these totals are respectively \(7\) and \(40\), compared with \(62\) left ideals in \(T_3(\mathbb F_3)\).

There is a geometric refinement: for every admissible dimension vector \(\mathbf d=(d_1,\ldots,d_n)\), its reduced parameter stratum is an iterated Grassmann bundle, geometrically smooth and irreducible, of dimension
\[
\boxed{\delta(\mathbf d)=\sum_{i=1}^{n}(d_i-d_{i+1})(n-i+1-d_i).}
\]
If the total count is treated as a polynomial in a **formal** variable \(q\), then
\[
\boxed{\mathcal Z_{n,0}(1)=\frac{1}{n+2}\binom{2n+2}{n+1}.}
\]
This is a Catalan degeneration of a field-dependent **one-sided** ideal enumerator; it is not evaluation at a finite field of cardinality zero.

## Assumptions and scope
A left ideal is an \(\mathbb F_q\)-linear subspace \(I\subseteq T_n(\mathbb F_q)\) closed under left multiplication by every upper-triangular matrix. It need not be a right or two-sided ideal. The exponent in the rank polynomial is the \(\mathbb F_q\)-vector-space dimension of \(I\), not the matrix rank of an element. In the geometric assertion, keep \(\mathbf d\) fixed and allow the ground field to vary; the stratum is a locally closed reduced variety parametrizing all flags of that dimension vector.

## Proof
**1. Row decomposition.** Write \(e_{ij}\) for matrix units, with \(i\le j\), and define \(F_i=\langle e_i,\ldots,e_n\rangle\subseteq k^n\), the possible support of matrix row \(i\). For a left ideal \(I\), \(e_{ii}I\subseteq I\), so \(I\) is the direct sum of its row spaces \(U_i\subseteq F_i\). For \(i<j\), \(e_{ij}\) sends any row \(j\) to row \(i\) without changing its coordinates, hence \(U_j\subseteq U_i\). Conversely, if \(U_1\supseteq\cdots\supseteq U_n\) and \(U_i\subseteq F_i\), left multiplication by every \(e_{ij}\) preserves the collection of allowable rows, hence the corresponding subspace is a left ideal. The two constructions invert each other, for arbitrary ground fields.

**2. Count by dimension vector.** Put \(d_i=\dim U_i\) and \(d_{n+1}=0\). The necessary and sufficient bounds are \(0\le d_n\le\cdots\le d_1\) and \(d_i\le n-i+1\). Starting at \(i=n\) and choosing upward, once \(U_{i+1}\) is fixed inside \(F_i\), the choices for \(U_i\supseteq U_{i+1}\) correspond to \((d_i-d_{i+1})\)-planes in the quotient \(F_i/U_{i+1}\), of dimension \(n-i+1-d_{i+1}\). This gives precisely \({n-i+1-d_{i+1}\brack d_i-d_{i+1}}_q\) choices. Multiply these independent successive fiber counts and sum over \(\mathbf d\). Direct-sum rows give \(\dim I=\sum_i d_i\), proving the polynomial.

**3. Geometry.** The same choices over an arbitrary field form successive relative Grassmannians: at stage \(i\), the tautological quotient bundle has rank \(n-i+1-d_{i+1}\), and the new subspace has relative rank \(d_i-d_{i+1}\). Each Grassmannian has smooth geometrically irreducible fibers and relative dimension \((d_i-d_{i+1})(n-i+1-d_i)\). Iteration proves the asserted geometry and dimension sum for a fixed \(\mathbf d\). This is a statement about the reduced strata, not the defining equation schemes of arbitrary ideals.

**4. Catalan formal specialization.** Each Gaussian coefficient is a polynomial with constant term \(1\). Therefore \(\mathcal Z_{n,0}(1)\) is the number of nondecreasing sequences \(0\le b_1\le\cdots\le b_n\) with \(b_j\le j\), obtained by reversing \(d_1,\ldots,d_n\). Such sequences are in bijection with Dyck paths of semilength \(n+1\): the successive heights of up-steps are encoded by these bounded nondecreasing integers (equivalently, reverse and complement the standard area sequence). The standard reflection-principle count is \(C_{n+1}=\binom{2n+2}{n+1}-\binom{2n+2}{n+2}=\binom{2n+2}{n+1}/(n+2)\). This establishes the **formal polynomial** specialization and no claim about a zero-element field.

## Verification
A standalone Python program in `verify.py` independently enumerates every vector subspace of the underlying algebra \(T_n(\mathbb F_q)\) in reduced-row-echelon normal form and tests closure under left multiplication by all matrix units. These direct tests agree with the separate Gaussian dimension-vector recursion at \((n,q)=(2,2),(2,3),(3,2)\). Larger Gaussian recursion checks at \((3,3),(4,2),(4,3),(5,2)\) give totals \(62,362,942,5134\). The arithmetic and direct exhaustive checks are finite corroboration; the proof covers all prime powers and every \(n\).

## Relationship to prior work
Shapiro (1975) counts **two-sided** ideals in upper-triangular matrix rings through ordinary Catalan numbers; left ideals are field-dependent and cannot be classified by the support order ideals alone. Standard triangular-module theory, for example Lam (1999), supplies the row-idempotent decomposition used here. Fei (2011, arXiv:1111.6452v1) develops general Hall-algebra and quiver-Grassmannian methods for polynomial point counts of subrepresentations. The present claim is the explicit **all-dimensional vector-space-dimension enumerator for left ideals of the regular triangular algebra**, its relative-Grassmannian stratum dimensions and its formal Catalan specialization. A general counting framework does not by itself state these specific coefficients, but broader quiver-Hall formulas could imply them following specialization and simplification. No claim is made that Gaussian-binomial coefficients, triangular row decompositions, or the Catalan bijection are newly discovered.

## Limitations
This is a complete count of **left** ideals, not simultaneous classification of right and two-sided ideals, products of ideals, or isomorphism classes under the algebra automorphism group. Its geometric statement concerns the reduced fixed-dimension-vector stratum and not components or nilpotents in a global ideal scheme. The novelty comparison has residual risks: existing specialized Hall-polynomial tables or older triangular-algebra ideal zeta functions may already give a mathematically equivalent formula. Independent mathematical and historical-priority audits have not been performed.

## References
1. L. W. Shapiro, *Upper Triangular Rings, Ideals, and Catalan Numbers*, American Mathematical Monthly **82** (1975), 634–637, doi:10.2307/2319698 (two-sided ideal count).
2. T. Y. Lam, *Lectures on Modules and Rings*, Springer GTM 189 (1999), discussion of triangular rings and idempotent row decomposition.
3. J. Fei, *Counting Using Hall Algebras I. Quivers*, arXiv:1111.6452v1 (first posted 2011-11-28), https://arxiv.org/abs/1111.6452, especially the treatment of quiver Grassmannian point counts.
4. R. A. Ferraz, C. Polcino Milies and E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289v1 (2017), for comparison with the full, not triangular, matrix algebra.
