# Complete adjacency spectrum and nonsingularity of Heisenberg Brandt commuting graphs

## Finding
For every prime power \(q\) and every integer \(n\ge3\), the zero-deleted commuting graph of the Brandt inverse semigroup over the finite Heisenberg group \(\operatorname{UT}_3(\mathbb F_q)\) has a completely explicit factored adjacency characteristic polynomial. Unlike the aperiodic matrix-unit graph, the adjacency matrix is nonsingular in **every** matrix index and characteristic.

Write \(m=q^3\), \(z=q\), \(t=q+1\), \(s=q(q-1)\), and \(d=(n-1)(n-2)\). Define the numerical \(3\)-by-\(3\) matrices
\[
Q=\begin{pmatrix}
nz-1&nts&md\\nz&s-1+(n-1)ts&md\\(n-2)z&(n-2)ts&m-1+md
\end{pmatrix},\quad
R=\begin{pmatrix}
-1&0&-2m(n-2)\\0&s-1-ts&-2m(n-2)\\-z&-ts&m-1-m(n-2)
\end{pmatrix}.
\]
Then, with \(X\) an indeterminate, the full adjacency characteristic polynomial is
\[
\begin{aligned}
\chi_{n,q}(X)={}&(X+1)^{n(n-1)(m-1)+n(z-1+t(s-1))}(X-s+1)^{n(t-1)}\\
&\times(X-m+1)^{n(n-3)/2}(X+m+1)^{(n-1)(n-2)/2}\\
&\times(X-m(n-1)+1)^{n-1}\det(XI_3-R)^{n-1}\det(XI_3-Q).
\end{aligned}
\]
This is a polynomial of degree \(n^2m\). Distinct listed factors may share roots: all multiplicities are those of the polynomial, not a claim that the seven displayed factor types have disjoint spectra.

## Assumptions and scope
Let \(\mathbb F_q\) be any finite field, including characteristic two. The group \(H=\operatorname{UT}_3(\mathbb F_q)\) consists of triples \((a,b,c)\) with multiplication
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
\]
Its elements commute exactly when \(ab'=a'b\). The Brandt inverse semigroup is
\[
B_n(H)=\{0\}\cup\{(i,g,j):1\le i,j\le n,\ g\in H\},
\]
with \((i,g,j)(k,h,\ell)=(i,gh,\ell)\) when \(j=k\), and zero otherwise. Its center is \(\{0\}\) for \(n\ge3\). The commuting graph has all \(n^2q^3\) nonzero elements as vertices, joining distinct elements when their products commute. This is not the commuting graph on only noncentral group elements: center elements of \(H\) are included in each diagonal cell.

## Proof
**1. Product test and label decomposition.** Distinct index cells \((i,j)\ne(k,\ell)\) are completely joined exactly when \(j\ne k\) and \(\ell\ne i\). If both index pairs are diagonal and equal, the group labels commute precisely when their first two coordinates are collinear. For each off-diagonal index pair, any two labels have both products zero and are adjacent. Hence every off-diagonal cell induces \(K_m\); every diagonal cell induces
\[
K_z\vee\left(\bigsqcup_{a=1}^{t}K_s\right),
\]
since the \(q^2-1\) nonzero vectors in \(\mathbb F_q^2\) split into \(q+1\) projective directions, each carrying \(q(q-1)\) labels including the central coordinate.

The sum-zero subspace of labels on an off-diagonal cell is an adjacency eigenspace of eigenvalue \(-1\), of dimension \(m-1\); its interactions with all other cells vanish. Within a diagonal cell the center-difference subspace (dimension \(z-1\)) and differences inside each noncentral clique (total dimension \(t(s-1)\)) likewise have eigenvalue \(-1\). Contrasts between the \(t\) equal noncentral cliques (dimension \(t-1\)) have eigenvalue \(s-1\). The only remaining label subspaces are the two coordinates recording uniform values on center and noncenter at each diagonal cell, and one uniform value at each off-diagonal cell.

**2. Index equivariance.** On the remaining \(n^2+n\)-dimensional space, let \(a_i\) be a value constant on central labels of \((i,i)\), \(b_i\) its noncentral constant, and \(u_{ij}\) the constant on the off-diagonal cell \((i,j)\), \(i\ne j\). The adjacency map sends
\[
\begin{aligned}
a_i'&=(z-1)a_i+ts b_i+\sum_{k\ne i}(za_k+ts b_k)
 +m\sum_{\substack{k\ne\ell\\k\ne i,\ell\ne i}}u_{k\ell},\\
b_i'&=z a_i+(s-1)b_i+\sum_{k\ne i}(za_k+ts b_k)
 +m\sum_{\substack{k\ne\ell\\k\ne i,\ell\ne i}}u_{k\ell},\\
u_{ij}'&=(m-1)u_{ij}+\sum_{\substack{k\ne\ell\\\ell\ne i,k\ne j\\(k,\ell)\ne(i,j)}}m u_{k\ell}
 +\sum_{k\notin\{i,j\}}(za_k+ts b_k).
\end{aligned}
\]
The restriction on the third line includes the off-diagonal cell itself in its allowed incidence set; the displayed separate \((m-1)u_{ij}\) term accounts for its within-cell neighbors, whereas the sum explicitly excludes the cell. The first two sums contain exactly \((n-1)(n-2)\) off-diagonal cells.

Under simultaneous permutation of index labels, the constant sector \(a_i=a,b_i=b,u_{ij}=u\) has matrix \(Q\) in that order. For the standard sector, choose vectors \(a_i,b_i,r_i,c_i\) of coordinate sum zero, with \(u_{ij}=r_i+c_j\). Its action is
\[
\begin{aligned}
a_i'&=-a_i-m(n-2)(r_i+c_i),\\
b_i'&=(s-1-ts)b_i-m(n-2)(r_i+c_i),\\
r_i'&=-za_i-ts b_i+(m-1)r_i-m(n-2)c_i,\\
c_i'&=-za_i-ts b_i-m(n-2)r_i+(m-1)c_i.
\end{aligned}
\]
The antisymmetric coordinate \(r_i-c_i\) therefore has eigenvalue \(m(n-1)-1\) (multiplicity \(n-1\)); the symmetric coordinate \(r_i=c_i\) has matrix \(R\) (multiplicity \(n-1\)).

The off-diagonal symmetric matrices with zero row sums and zero diagonal form an invariant eigenspace with eigenvalue \(m-1\) and dimension \(n(n-3)/2\). The off-diagonal skew-symmetric matrices with zero row sums have eigenvalue \(-m-1\) and dimension \((n-1)(n-2)/2\). Direct row-sum elimination shows these pieces, the constant sector, and the standard sector span the reduced space, since
\[
3+4(n-1)+\frac{n(n-3)}2+\frac{(n-1)(n-2)}2=n^2+n.
\]
The decomposition is direct over characteristic-zero spectral vector spaces; no modular-representation assumption is used. Multiplying the characteristic polynomials of these invariant blocks and the earlier label-difference blocks proves the displayed factorization.

**3. Universal nonsingularity.** Put \(h=n-2\ge1\) and define
\[
A_q=2q^4-q^3+q^2-1,\quad B_q=3q^4-q^3+q^2-q-1,\quad C_q=q^3-q^2+1.
\]
All three are strictly positive for integer \(q\ge2\). Exact determinant expansion of the displayed \(3\)-by-\(3\) matrices gives
\[
\begin{aligned}
\det Q&=-(q-1)(q^2+q+1)A_q-hq^3B_q-h^2q^3A_q<0,\\
\det R&=(q-1)(q^2+q+1)C_q+hq^3A_q>0.
\end{aligned}
\]
The explicit other eigenvalues are \(-1\), \(s-1=q(q-1)-1\), \(m-1\), \(-m-1\), and \(m(n-1)-1\), all nonzero for \(q\ge2,n\ge3\). Therefore zero is never an adjacency eigenvalue.

## Verification
Run `python verify_heis.py` with Python, NumPy and SymPy. The checker builds each Brandt graph directly from the group multiplication commutation test, not from the asserted block matrices, computes its real symmetric adjacency eigenvalues, and compares them with the predicted polynomial roots in five cases: \((n,q)=(3,2),(4,2),(5,2),(3,3),(4,3)\). It also evaluates both symbolic determinant factorizations. The maximum absolute spectral discrepancy is less than \(5\times10^{-13}\). The finite checks are **not** a substitute for the arbitrary-\(q\), arbitrary-\(n\) proof in the preceding section.

## Relationship to prior work
Berezovski–Gutik–Pavlyk (2010) gives the general Brandt-extension structure. Kumar–Dalal–Pandey (2020) analyzes the commuting graph when the local group is **trivial**; its results address graph parameters and automorphism groups, not the present nonabelian family. The aperiodic matrix-unit adjacency spectrum is a known distinct special case; its eigenvalue-zero phenomenon for larger matrix indices does not transfer to the present nonsingular family. Rather et al. (2022) treat commuting graphs of finite groups, rather than the semigroup graph combining diagonal group commuting relations with off-diagonal Brandt incidences. The complete graph of the local group alone does not determine these mixed-sector eigenvalues without the additional index decomposition.

## Limitations
The result concerns \(\operatorname{UT}_3(\mathbb F_q)\), not all nonabelian local groups or arbitrary Rees sandwich matrices. It gives a characteristic polynomial with cubic factors, not a complete radical expression for every individual root. No historical-uniqueness or external proof certificate is claimed; overlap with unindexed semigroup-spectrum literature remains possible. Finite numerical checks are supporting evidence only.

## References
- T. Berezovski, O. Gutik, K. Pavlyk, *Brandt Extensions and Primitive Topological Inverse Semigroups*, first published 2010-03-07, DOI: 10.1155/2010/671401, https://doi.org/10.1155/2010/671401.
- J. Kumar, S. Dalal, P. Pandey, *On the Commuting Graphs of Brandt Semigroups*, arXiv:2010.05000 (first 2020-10-10), https://arxiv.org/abs/2010.05000.
- B. A. Rather et al., *A-alpha Matrix of Commuting Graphs of Non-Abelian Groups*, published 2022-06-20, DOI: 10.3934/math.2022845, https://doi.org/10.3934/math.2022845.
