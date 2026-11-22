# A projective-plane zero-divisor spectrum for \(k[(C_2)^3]\)

## Finding
Let \(k=\mathbb F_q\), where \(q=2^e\) and \(e\ge1\), and let
\[
R=k[C_2\times C_2\times C_2]\cong k[x,y,z]/(x^2,y^2,z^2).
\]
The **ordinary simple zero-divisor graph** \(\Gamma(R)\) has a vertex for each nonzero zero divisor and an edge between distinct vertices precisely when their product is zero. Set
\[
m=q^2+q+1,\quad a=q-1,\quad b=q(q-1),\quad c=q^3(q-1),
\quad E=(a-1)+m(b-1)+mq(c-1).
\]
**Theorem.** The graph on \(q^7-1\) vertices admits the following complete projective-plane decomposition. There is a universal clique of order \(a\); an additional clique, partitioned into \(m\) blocks of order \(b\), whose blocks are indexed by the lines of \(\operatorname{PG}(2,q)\); and \(mq\) disjoint cliques of order \(c\), indexed by a projective point \(p\) and a scalar \(s\in k\). Each point-scalar clique is joined to the universal clique and exactly the \(q+1\) line blocks incident with \(p\), and is joined to no other point-scalar clique. All line blocks are mutually completely joined, and the universal clique is joined to every block.

Equivalently, the complete adjacency characteristic polynomial is
\[
\boxed{\begin{aligned}
\chi_{\Gamma(R)}(\lambda)={}&(\lambda+1)^E
(\lambda-c+1)^{m(q-1)}\\
&\cdot\bigl((\lambda+1)(\lambda-c+1)-bq^2c\bigr)^{m-1}
\det(\lambda I_3-T),
\end{aligned}}
\]
where
\[
T=\begin{pmatrix}
a-1&mb&mq c\\
a&mb-1&(q+1)q c\\
a&(q+1)b&c-1
\end{pmatrix}.
\]
**In particular, its ordinary adjacency matrix is nonsingular over \(\mathbb R\) for every \(q=2^e\).** Indeed,
\[
\det T=-q^9\bigl((q-1)^3-1\bigr)-2(q^7-2q^4+q^3+1)<0.
\]
This is a statement about the simple (loopless) adjacency matrix, not about a graph retaining the square-zero loops.

## Assumptions and scope
The coefficient field has characteristic two and order \(q=2^e\), \(e\ge1\). Write \(J=(x,y,z)\subset R\), and use the graded decomposition \(J=J_1\oplus J_2\oplus J_3\) with \(J_1=\langle x,y,z\rangle\), \(J_2=\langle xy,xz,yz\rangle\), and \(J_3=\langle xyz\rangle\). Every nonzero element of \(J\) is a zero divisor (indeed every such element has square zero), and every element outside \(J\) is a unit. Thus the graph has precisely \(q^7-1\) vertices. Projective points and projective lines are both indexed by one-dimensional subspaces of a three-dimensional vector space; point-line incidence means that the corresponding standard nondegenerate bilinear pairing vanishes. The parameter \(c\) is a block size, not a graph chromatic number.

## Proof
**1. Multiplication and strata.** Write an element of \(J\) uniquely as \(f=v+w+txyz\), with \(v\in J_1\), \(w\in J_2\), and \(t\in k\). Given \(g=v'+w'+t'xyz\),
\[
fg=vv'+vw'+wv'.
\]
Products involving \(J_3\), and all degree-four products, vanish. The identification of the squarefree graded multiplication with wedge multiplication gives \(vv'=0\) if and only if the two degree-one coefficient vectors are proportional. The degree-three coefficient of \(vw'\) is the bilinear pairing
\[
\langle v,w'\rangle=v_xw'_{yz}+v_yw'_{xz}+v_zw'_{xy}.
\]
No signs appear because the characteristic is two.

If \(v=0=w\), then \(f=txyz\ne0\) is adjacent to every other vertex. These \(a=q-1\) vertices form the universal clique. If \(v=0\), \(w\ne0\), then all such vertices lie in \(J^2\setminus J^3\) and annihilate each other. Normalize the first nonzero coordinate of \(w\) to one: its projective direction defines a line \(\ell\), and there are \(q-1\) scalar multiples and \(q\) choices of \(t\). Hence each of the \(m\) line blocks contains \(b=q(q-1)\) vertices.

Now assume \(v\ne0\). Normalize \(v=\alpha u\), with \(\alpha\in k^\times\) and the first nonzero coordinate of \(u\) equal to one. The projective class of \(u\) is a point \(p\). Define the scalar
\[
s(f)=\alpha^{-1}\langle u,w\rangle.
\]
For a fixed \((p,s)\), there are \(q-1\) choices of \(\alpha\), \(q^2\) choices of \(w\), and \(q\) choices of \(t\): thus exactly \(c=(q-1)q^3\) elements. If \(f=\alpha u+w+txyz\) and \(g=\beta u+w'+t'xyz\) have the same projective point, then \(fg=0\) precisely when
\[
\alpha\langle u,w'\rangle+\beta\langle u,w\rangle=0,
\]
which in characteristic two is exactly \(s(f)=s(g)\). For distinct projective points the degree-two product \(vv'\) is nonzero, so the corresponding vertices cannot be adjacent. Thus the \(mq\) point-scalar blocks are disjoint complete graphs.

Finally, an element of a line block labelled by \([w]\) annihilates an element in the point-scalar block labelled by \(([u],s)\) exactly when \(\langle u,w\rangle=0\), independently of \(s\). This is the point-line incidence relation in \(\operatorname{PG}(2,q)\). The universal clique meets every other block completely. This proves the entire graph description, with vertex count
\[
a+mb+mq c=q^7-1.
\]

**2. Spectral decomposition.** Consider the real adjacency operator. Vectors whose coordinates sum to zero *within* any one of the universal clique, each line block, or each point-scalar clique, and vanish outside that block, are eigenvectors with eigenvalue \(-1\). Their total dimension is
\[
E=(a-1)+m(b-1)+mq(c-1).
\]
After quotienting these internal differences, each block is represented by its constant coordinate. For each fixed projective point the \(q\) point-scalar blocks have identical neighbors outside themselves and no edges between them. Differences among their block constants are eigenvectors with eigenvalue \(c-1\); their total multiplicity is \(m(q-1)\).

The remaining block-constant space has dimension \(2m+1\): one universal coordinate, one for each line, and one aggregate coordinate for the \(q\) point-scalar blocks at each point. Let \(N\) be the \(m\)-by-\(m\) projective-plane line-point incidence matrix. The induced adjacency map in this coordinate system is
\[
\begin{pmatrix}
a-1 & b\mathbf1^\top & qc\mathbf1^\top\\
a\mathbf1 & b\mathbf1\mathbf1^\top-I_m & qcN\\
a\mathbf1 & bN^\top & (c-1)I_m
\end{pmatrix}.
\]
Every projective line has \(q+1\) points, and two distinct lines meet in exactly one point, giving
\[
NN^\top=qI_m+\mathbf1\mathbf1^\top.
\]
On the three-dimensional constant-on-all-lines-and-points subspace, the quotient is exactly \(T\). On the \(2(m-1)\)-dimensional orthogonal-complement subspace, the two diagonal blocks are \(-I\) and \((c-1)I\); multiplication of off-diagonal blocks is \(bq c NN^\top\), which is \(bq^2cI\) there. Consequently its characteristic polynomial is
\[
\bigl((\lambda+1)(\lambda-c+1)-bq^2c\bigr)^{m-1}.
\]
Together these invariant subspaces have dimension
\[
E+m(q-1)+2(m-1)+3=q^7-1,
\]
proving the asserted factorization without any missing eigenvalues.

**3. Nonsingularity.** At \(\lambda=0\) the quadratic factor is \(1-c-bq^2c<0\), while \(c-1>0\) and \(-1\ne0\). Direct expansion gives
\[
\det T=-q^9((q-1)^3-1)-2(q^7-2q^4+q^3+1).
\]
For \(q\ge2\), the first summand is nonpositive and the second is strictly negative because \(q^7\ge2q^4\). Therefore \(\det T\ne0\). None of the factors vanishes at zero, completing the proof.

## Verification
The included standard-library checker constructs multiplication independently in the seven-element squarefree monomial basis using finite-field arithmetic. It verifies the predicted projective incidence identities at \(q=2,4,8\), all 8,001 unordered pairs of distinct nonzero radical elements at \(q=2\), and 25,000 and 10,000 seeded pair tests at \(q=4\) and \(q=8\), respectively. It also enumerates all vertex-block populations at \(q=2,4\), evaluates the displayed determinant identity at \(q=2,4,8\), and (when NumPy is installed) compares all 127 eigenvalues of the direct \(q=2\) adjacency matrix with the factorization. These checks passed; the proof above, not the finite checks, establishes the theorem for every \(2\)-power field order.

## Relationship to prior work
Aliniaeifard and Li (2014) develop the ordinary zero-divisor graph of finite group rings, proving diameter/girth and recognition results; their Section 3 uses annihilator classes to recognize rank and order of finite abelian groups. Their full accessible paper does not state a projective-plane block decomposition, an adjacency characteristic polynomial, or nonsingularity for this elementary-abelian group algebra. The rank/exponent recognition statement for modular abelian group algebras published in 2026 likewise concerns minimum degree rather than the full spectrum. The known characteristic-uniform square-zero graph for \(k[x,y]/(x^3,y^3)\) has a different algebra (dimension nine rather than eight), and describes only a square-zero induced graph in that setting. The squarefree-radical zero-product-determination theorem treats universal bilinear-map factorization, not the incidence relation or adjacency spectrum here.

Mönius (2020) develops general spectral methods for finite commutative zero-divisor graphs and explicit spectra for direct products of finite residue-class rings. Its spectral formulas do not give this non-chain local squarefree group algebra. A later published semisimple-ring spectral treatment similarly does not apply to this nonsemisimple local ring. These comparisons concern implication and hypotheses, not merely title matches.

## Limitations
The theorem is specific to three independent order-two group generators and characteristic two; no universal formula for \(k[(C_2)^r]\) with arbitrary \(r\) is claimed. It concerns the ordinary real adjacency spectrum of the simple zero-divisor graph, not its loop-retaining variant, Laplacian, or automorphism group. Computational checks are finite corroboration, not an infinite proof. Literary searches and accessible primary-source comparisons reduce, but cannot eliminate, the risk of an implicit historical antecedent. Independent validation has not been performed.

## References
1. F. Aliniaeifard and Y. Li, *Zero-Divisor Graphs for Group Rings*, Communications in Algebra **42** (2014), 4790–4800. First public online date 2014-05-23. https://doi.org/10.1080/00927872.2013.827689
2. D. F. Anderson and P. S. Livingston, *The zero-divisor graph of a commutative ring*, Journal of Algebra **217** (1999), 434–447. https://doi.org/10.1006/jabr.1998.7840
3. K. Mönius, *Eigenvalues of zero-divisor graphs of finite commutative rings*, Journal of Algebraic Combinatorics **54** (2021), 787–802, online 2020-11-17. https://doi.org/10.1007/s10801-020-00989-6
4. K. D. Masalkar, A. Khairnar, A. Lande and A. Patil, *Spectra of the zero-divisor graph of finite rings*, arXiv:2106.15977 (2021). https://arxiv.org/abs/2106.15977
5. *A characteristic-uniform square-zero annihilation graph for the bivariate cubic truncation*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-characteristic-uniform-square-zero-annihilation-graph-for-the--c6e7cc1901a7/RESULT.md
6. *The exponent of an abelian p-group from its modular zero-divisor graph*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/9/21/SCOPE-abelian-p-group-exponent-modular-zero-divisor-graph--b4dbafcd5467/RESULT.md
7. *Zero-product rigidity of squarefree radicals and exact defect of their unitizations*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-zero-product-rigidity-of-squarefree-radicals-and-exact-defect-of--95178287ccd5/RESULT.md
