# Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance

## Finding
Let \(G=(V,E)\) be any finite simple graph and let \(A\) be any finite abelian group of order \(q\ge 2\), endowed with a symmetric perfect bicharacter \(b:A\times A\to\mathbb C\). Index a square matrix by the assignments \(x\in A^V\) whose nonzero support is an independent set of \(G\), with entries
\[
H_G(x,y)=\prod_{v\in V}b(x_v,y_v).
\]
This matrix is always invertible. Define \(I_J(t)=\sum_{S\subseteq V(J),\ S\text{ independent}}t^{|S|}\), including the empty set, and let \(U=\operatorname{supp}(x)\cup\operatorname{supp}(y)\). The inverse has the following exact entries:
\[
(H_G^{-1})(x,y)=
\begin{cases}
0,&U\text{ is not independent};\\
q^{-|U|}\overline{H_G(x,y)}\,I_{G-N[U]}\!\left(-\frac{q-1}{q}\right),&U\text{ is independent}.
\end{cases}
\]
Here \(N[U]\) is the union of \(U\) and its graph neighbors, and the empty graph has independence polynomial \(1\). For \(q\ge3\), **every entry whose union support is independent is nonzero**. Thus the inverse's zero pattern is completely determined by the graph exclusion constraint.

For the binary alphabet \(q=2\) and the path graph \(P_n\), let the graph induced on \(V\setminus N[U]\) have path-component lengths \(m_1,\ldots,m_s\). Besides nonindependent unions, an inverse entry vanishes **if and only if** some \(m_j\equiv2\pmod4\). In particular, its entry indexed twice by the all-zero assignment vanishes exactly when \(n\equiv2\pmod4\). This is a genuine binary arithmetic resonance absent for every larger alphabet.

The determinant has the all-graph exact magnitude
\[
\big|\det H_G\big|=q^{\frac q2 I_G'(q-1)}.
\]

## Assumptions and scope
The graph is finite, simple, and undirected, and the vertex set may be empty. A bicharacter is perfect when the map \(a\mapsto b(a,\cdot)\) identifies \(A\) with its character group, and symmetric when \(b(a,c)=b(c,a)\). Such bicharacters exist for every finite abelian group via cyclic decompositions. The support of an assignment consists of vertices with nonidentity coordinates; both row and column indices range over all assignments with independent support. The Fourier matrix is unnormalized. For \(q=2\), the bicharacter is uniquely \(b(a,c)=(-1)^{ac}\); for the path formula, the path has consecutive edges and no isolated extra vertices.

## Proof
**1. One-coordinate Schur factorization.** Order the elements of \(A\) with the identity first, and let \(B\) be the \((q-1)\)-square submatrix of \(b\) on the nonidentity elements. Write \(J\) for the all-ones matrix of the same size and \(K=B-J\). The single-coordinate character matrix factors as
\[
W=Z_1\begin{pmatrix}1&0\\0&K\end{pmatrix}Z_1^{\mathsf T},\qquad
Z_1=\begin{pmatrix}1&0\\\mathbf1&I_{q-1}\end{pmatrix}.
\]
Character orthogonality implies \(B\overline B=qI-J\) and \(J\overline B=-J\), where symmetry makes ordinary multiplication the appropriate matrix product. Hence \(K\overline B=qI\): in particular \(K^{-1}=q^{-1}\overline B\). The full character matrix \(W\) has singular values \(\sqrt q\); since \(\det Z_1=1\), this also yields \(|\det K|=q^{q/2}\).

**2. Restriction to independent supports.** Let \(\mathcal D\) be the assignment index set, ordered by restriction of nonzero coordinates. Define \(Z(x,z)=1\) when \(z\) is a restriction of \(x\), and zero otherwise. Since \(\mathcal D\) is closed under restrictions, \(Z\) is unitriangular and has inverse
\[
Z^{-1}(x,z)=\mathbf1_{z\preceq x}(-1)^{|\operatorname{supp}(x)\setminus\operatorname{supp}(z)|}.
\]
Tensoring the first factorization and restricting to \(\mathcal D\) gives
\[
H_G=Z\,D\,Z^{\mathsf T},\quad
D=\bigoplus_{S\subseteq V,\ S\text{ independent}}K^{\otimes |S|},
\]
where the empty tensor block is \(1\). Every block is invertible, proving the all-graph assertion. The tensor determinant identity yields
\[
|\det H_G|=\prod_{S\text{ independent}}q^{\frac q2|S|(q-1)^{|S|-1}}
=q^{\frac q2 I_G'(q-1)}.
\]
The empty-support term contributes exponent zero.

**3. Inverse entry formula.** Substitute the explicit Möbius inverse of \(Z\) and \(K^{-1}=q^{-1}\overline B\) into \(H_G^{-1}=Z^{-\mathsf T}D^{-1}Z^{-1}\). A common support block must contain the union \(U\); if \(U\) is not independent, none is available. When it is independent, each coordinate in \(U\) contributes \(q^{-1}\overline{b(x_v,y_v)}\), whether both original coordinates are nonzero or just one is: in the latter case the extra Möbius sign cancels the nontrivial character sum \(\sum_{a\ne0}\overline{b(a,c)}=-1\). For every additional coordinate, where both original assignments vanish, the summed contribution is
\[
q^{-1}\sum_{a\ne0}\sum_{c\ne0}\overline{b(a,c)}=-\frac{q-1}{q}.
\]
The extra coordinates range exactly over independent subsets of \(G-N[U]\). Summing these products proves the displayed inverse formula.

**4. Complete nonbinary and binary path zero classification.** The polynomial \(I_J(t)\) is monic only in special cases, but always has **integer coefficients and constant coefficient \(1\)**. The reduced rational number \(-(q-1)/q\) cannot be a root for \(q\ge3\), by the rational-root theorem: the numerator \(q-1>1\) would have to divide the constant coefficient \(1\). Therefore the only zeros for these alphabets are forced by the union-support condition.

For a path \(P_m\), set \(F_m(t)=I_{P_m}(t)\), with \(F_0(t)=1\), \(F_1(t)=1+t\), and, by conditioning on its last vertex, \(F_m(t)=F_{m-1}(t)+tF_{m-2}(t)\). At \(t=-1/2\) the characteristic roots are \((1\pm i)/2\). Solving the recurrence with these initial values gives
\[
F_m(-1/2)=2^{-m/2}\sin\!\left(\frac{(m+2)\pi}{4}\right).
\]
This vanishes exactly when \(m\equiv2\pmod4\). The graph \(P_n-N[U]\) is a disjoint union of paths and independence polynomials multiply under disjoint union. The claimed criterion, including the all-zero boundary case, follows.

## Verification
Run `python3 path_fourier_checker.py` with the standard Python library. The checker independently builds each principal Fourier matrix and the proposed inverse, multiplies them **in exact cyclotomic arithmetic** and verifies the identity. It checks binary paths with lengths \(2\) through \(8\), ternary paths with lengths \(2\) through \(5\), and cyclic-quaternary paths with lengths \(2\) through \(4\). The two-sided identity follows from symmetry of both matrices. The checker also computes binary determinants by exact integer elimination for path lengths \(2\) through \(6\). The output terminates with `PATH_INDEPENDENCE_FOURIER_CHECKS_PASS`. These fourteen finite instances are corroboration, not a proof for all graphs and groups; the proof is the algebraic argument above.

## Relationship to prior work
Independence polynomials and their deletion recurrences are classical (Levit--Mandrescu, arXiv:1007.0880). Finite-group character duality and poset partition methods are developed by Gluesing-Luerssen (arXiv:1304.1207). Knill's face-indexed simplicial counting matrix (arXiv:1907.09092) has a zeta-type Green function but a **different kernel** \(2^{|x\cap y|}-1\), without the empty face, rather than the Walsh kernel \((-1)^{|x\cap y|}\) considered here. Earlier Fourier Hamming-ball interpolation formulas treat the cardinality-cutoff downset, not arbitrary graph-exclusion complexes; their proof technique provides a relevant motivation but not the present all-graph independence-polynomial formula or the binary mod-four path classification. Delvaux--Van Barel study rank-deficient Fourier-Kronecker submatrices (2007), chiefly via rank-one block tilings; accessible abstract-level evidence does not resolve full-text priority, and is not used to claim exhaustive novelty.

## Limitations
No quantitative spectral condition-number bound is claimed for general graphs. The exact path residue criterion is restricted to binary alphabets. A graph's binary inverse may exhibit cancellations beyond the path case and is characterized here through its independence polynomial, not by a complete graph-isomorphism classification. Independent validation and historical-priority assessment remain unperformed; a wider prior theorem on Fourier matrices restricted to simplicial downsets might subsume the general factorization.

## References
- V. E. Levit and E. Mandrescu, *On the independence polynomial of an antiregular graph*, arXiv:1007.0880, first public 2010-07-06. Relevant definitions and deletion identity, Introduction and Proposition 1.1.
- H. Gluesing-Luerssen, *Fourier-Reflexive Partitions and MacWilliams Identities for Additive Codes*, arXiv:1304.1207v1, 2013-04-03. Finite-group duality and poset partition context.
- O. Knill, *The counting matrix of a simplicial complex*, arXiv:1907.09092v1, 2019-07-22. Theorem 1 and inverse-star formula for a different face-indexed matrix.
- S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra Appl. 426 (2007), 349–367, DOI:10.1016/j.laa.2007.05.009. Abstract inspected; full text not accessible in this examination.
