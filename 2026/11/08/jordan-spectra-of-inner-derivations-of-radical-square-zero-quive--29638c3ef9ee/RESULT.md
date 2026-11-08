# Jordan spectra of inner derivations of radical-square-zero quiver algebras

## Finding

Let \(Q\) be a finite loopless quiver with vertex set \(V\), distinct arrow set \(E\), \(|V|=n\ge1\), and \(|E|=m\ge0\). Parallel arrows and arrows in opposite directions are allowed. Over any field \(k\), let \(A=kQ/J^2\), with \(J\) the arrow ideal. An element has unique coordinates
\[
 x=\sum_{v\in V}d_v e_v+\sum_{a\in E}w_a a.
\]
Write \(\operatorname{ad}_x(y)=xy-yx\). For an arrow \(a\) with source \(u\) and target \(v\), put \(\lambda_a=d_u-d_v\), and let
\[
 E_0=\{a\in E:\lambda_a=0\},\quad E_\ne=E\setminus E_0,\quad
 F=\{a\in E_0:w_a\ne0\}.
\]
For an edge subset \(F\), let \(\kappa(F)\) denote the number of components of the spanning undirected multigraph \((V,F)\), including isolated vertices. Set \(\rho=n-\kappa(F)\), \(h=|E_\ne|\), and \(h_\alpha=|\{a\in E:\lambda_a=\alpha\}|\) for nonzero \(\alpha\in k\).

**Complete Jordan form.** Every \(\operatorname{ad}_x\) has split Jordan form
\[
 \boxed{\operatorname{ad}_x\sim J_2(0)^{\oplus\rho}
 \oplus J_1(0)^{\oplus(n+|E_0|-2\rho)}
 \oplus\bigoplus_{\alpha\in k^\times}J_1(\alpha)^{\oplus h_\alpha}.}
\]
In particular, no Jordan block has size more than two, and every nonzero eigenvalue is semisimple. Its rank is exactly \(h+\rho\). This structural statement holds over any field.

For \(k=\mathbb F_q\), define the **joint Jordan-profile polynomial**
\[
 \mathcal J_{Q,q}(s,t)=\sum_{x\in A}s^{b_2(x)}t^{h(x)},
\]
where \(b_2(x)\) counts size-two zero Jordan blocks and \(h(x)\) is the total algebraic multiplicity of nonzero eigenvalues. Its coefficients are *labeled element counts*, not counts of distinct derivations or conjugacy classes. For a coloring \(d:V\to\mathbb F_q\), write \(E_0(d)=\{a=uv:d_u=d_v\}\), \(h(d)=m-|E_0(d)|\). Then
\[
 \boxed{\mathcal J_{Q,q}(s,t)=
 \sum_{d:V\to\mathbb F_q}(qt)^{h(d)}
 \sum_{F\subseteq E_0(d)}(q-1)^{|F|}s^{n-\kappa(F)}.}
\tag{1}
\]
The complete multiplicities of individual nonzero eigenvalues are also available by retaining the vector \((h_\alpha(d))_{\alpha\ne0}\) as a monomial label before this sum.

There is a second **cycle-matroid expression** involving only edge subsets:
\[
 \boxed{\mathcal J_{Q,q}(s,t)=\sum_{F\subseteq E}\sum_{H\subseteq E\setminus F}
 (q-1)^{|F|}s^{n-\kappa(F)}
 (qt)^{m-|F|-|H|}(1-qt)^{|H|}q^{\kappa(F\cup H)}.}
\tag{2}
\]
Consequently the joint \((b_2,h)\) distribution is orientation-independent and determined by the cycle-matroid rank function together with \(n\). The rank enumerator is \(\mathcal J_{Q,q}(z,z)\).

**Forest universality and characterization.** If the underlying multigraph is a forest with \(c\) connected components (isolated vertices permitted, so \(m=n-c\)), then
\[
 \boxed{\mathcal J_{Q,q}(s,t)=q^c\bigl(1+(q-1)s+q(q-1)t\bigr)^m,}\tag{3}
\]
\[
 \boxed{\sum_{x\in A}z^{\operatorname{rank}(\operatorname{ad}_x)}
 =q^c\bigl(1+(q^2-1)z\bigr)^m.}\tag{4}
\]
Thus for uniformly random \(x\), the rank is binomial with \(m\) trials and success probability \(1-q^{-2}\), independent of the shape and orientation of the forest. Conversely, for any loopless multigraph, the coefficient of \(s^m t^0\) in \(\mathcal J_{Q,q}\) is nonzero **if and only if** the graph is a forest; in that case it equals \(q^c(q-1)^m\). Equivalently, there exists an inner derivation that is square-zero and has rank \(m\) precisely for forests.

## Assumptions and scope

The algebra is unital and associative. Its multiplication is specified by orthogonal primitive vertex idempotents, with \(e_u a=a\) when \(u\) is the source, \(a e_v=a\) when \(v\) is the target, and all arrow-arrow products zero. Arrows are distinct even when their endpoints coincide as an unordered pair, and loop arrows are excluded. Formulae (1)--(4) apply for every finite field, including characteristic two. Jordan forms are of \(k\)-linear endomorphisms of the vector space \(A\), not the adjoint representation of the derivation Lie algebra. The polynomial \(\mathcal J\) counts all \(q^{n+m}\) algebra elements, including those inducing identical inner derivations. All powers in the polynomial expressions are ordinary nonnegative integer exponents.

## Proof

**1. Block matrix of the commutator operator.** Let \(D=\bigoplus_{v\in V}ke_v\) and \(J=\bigoplus_{a\in E}ka\), so \(A=D\oplus J\). The multiplication table gives
\[
 \operatorname{ad}_x(e_v)=\sum_{a:\operatorname{target}(a)=v}w_a a
 -\sum_{a:\operatorname{source}(a)=v}w_a a,
 \qquad\operatorname{ad}_x(a)=\lambda_a a.
\]
Split \(J=J_\ne\oplus J_0\) according to whether \(\lambda_a\ne0\). In bases of arrows and vertices, the matrix has the block shape
\[
 \begin{pmatrix}0&0&0\\ C_\ne&D_\ne&0\\ C_0&0&0\end{pmatrix},
\]
where \(D_\ne\) is the invertible diagonal matrix with entries \(\lambda_a\), and each row of \(C_0\) has entries \(-w_a\) at the source and \(+w_a\) at the target (signs depend on the chosen commutator convention and do not affect rank). Replace each vertex basis vector by itself plus a suitable vector in \(J_\ne\), eliminating \(C_\ne\) using \(D_\ne^{-1}\). The resulting matrix is similar to \(D_\ne\) direct-summed with \(\left(\begin{smallmatrix}0&0\\C_0&0\end{smallmatrix}\right)\). The first block is semisimple; the second has square zero.

**2. Incidence rank and Jordan form.** The rows of \(C_0\) indexed by zero weights vanish. Every remaining row is a nonzero scalar multiple of the ordinary oriented incidence row of an edge in \(F\). The incidence kernel consists exactly of functions constant on connected components of \((V,F)\), in any characteristic, including characteristic two. Hence \(\operatorname{rank}C_0=n-\kappa(F)=\rho\). A square-zero matrix of rank \(\rho\) acting on a space of dimension \(n+|E_0|\) has \(\rho\) Jordan blocks of size two and \(n+|E_0|-2\rho\) blocks of size one. Adding the nonzero-eigenvalue arrows proves the asserted Jordan decomposition and rank.

**3. Exact finite-field state sum.** Fix a diagonal vector \(d\). On each edge in \(E_\ne(d)\), the weight \(w_a\) is arbitrary (\(q\) possibilities), while the arrow contributes one nonzero semisimple eigenvalue. This gives \((qt)^{h(d)}\). On each edge in \(E_0(d)\), specify whether \(w_a\) is zero (one possibility) or nonzero (\(q-1\) possibilities); their nonzero support is a unique subset \(F\subseteq E_0(d)\). Step 2 shows that its zero Jordan block count is \(n-\kappa(F)\), giving (1). The construction is a disjoint, exhaustive partition of the \(q^{n+m}\) labeled elements.

**4. Edge-state expansion.** Reorder the sum in (1), choosing \(F\subseteq E\) first, restricting to colorings constant along every edge in \(F\). For each edge outside \(F\), the factor \((qt)^{{\mathbf{1}}_{d_u\ne d_v}}\) equals \(qt+(1-qt){\mathbf{1}}_{d_u=d_v}\). Expand the product by choosing the set \(H\subseteq E\setminus F\) on which the equality indicators are selected. Colorings constant along \(F\cup H\) number exactly \(q^{\kappa(F\cup H)}\). The remaining factors and the incidence exponent give (2). All exponents \(n-\kappa(\cdot)\) are cycle-matroid ranks; no orientation survives.

**5. Forest factorization.** Choose one diagonal color per connected component, giving \(q^c\) choices. Root every tree and assign child colors moving along each edge. An edge has exactly three disjoint types: equal endpoint colors with weight zero (factor \(1\)); equal colors with nonzero weight (factor \((q-1)s\)); or distinct endpoint colors and arbitrary weight (factor \(q(q-1)t\)). In a forest, the nonzero equal-color edges are independent in the graphic matroid, so each adds one size-two Jordan block. Independence of edge choices gives (3); setting \(s=t=z\) gives (4). Dividing its coefficients by \(q^{n+m}=q^{c+2m}\) gives the claimed binomial law.

**6. Exact forest characterization.** For any multigraph, \(\rho\le n-c\), where \(c\) is the number of components of the full graph. If a cycle exists, then \(m>n-c\), so no element can have \(b_2=m\). If the graph is a forest, the coefficient of \(s^mt^0\) in (3) equals \(q^c(q-1)^m>0\). Such elements have only zero eigenvalues and their inner derivations square to zero by Step 1. Conversely, a square-zero inner derivation with rank \(m\) has \(b_2=m\), proving the equivalence.

## Verification

Run `python3 check_adjoint.py` to enumerate every algebra element for small loopless quivers over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\). It constructs the original algebra multiplication table, forms each full adjoint matrix, and independently computes its rank. It also computes \(\operatorname{rank}\bigl(M\prod_{\alpha\ne0}(M-\alpha I)\bigr)\) to isolate the number of size-two zero Jordan blocks. These values are compared with the graph-component formula and with a separately evaluated color/subset enumeration; forest multinomial coefficients are checked independently. The test cases include a three-vertex cycle, a four-vertex cycle, parallel arrows, paths, stars, and an edgeless graph. The complete actual output is in `check_output.txt`.

Run `python3 check_tutte.py` to test the independent double-subset formula (2) at seven pairs of integer evaluation points for four graphs. Its complete actual output is in `check_tutte_output.txt`. Both scripts use only the Python standard library. The finite tests validate small cases; the proof above establishes the infinite families and arbitrary prime-power fields.

## Relationship to prior work

Strametz's 2001 preprint develops the Lie algebra of outer derivations of monomial algebras and identifies the inner-derivation subspace via Hochschild coboundaries. Sanchez-Flores's 2007 preprint describes the Gerstenhaber Lie module structure of radical-square-zero monomial algebras. Guo and Li's 2010 work develops bases and incidence matrices for derivations of path algebras, including inner derivations. Those results motivate the present operator-level question. The result here concerns the **Jordan canonical forms of individual inner derivations and their finite-field population**, not the Lie brackets among derivations or the dimensions of Hochschild cohomology.

Prior work on commutator fibers and commuting probabilities of radical-square-zero quiver algebras determines the single specialization \(q^{-(n+m)}\mathcal J_{Q,q}(q^{-1},q^{-1})\) but does not state this complete two-variable Jordan distribution or the forest-universal binomial law. The component-rank identity uses the classical graph incidence-matrix theorem, and the expansion (2) is a Fortuin--Kasteleyn-style edge-subset expansion; neither classical ingredient is asserted to be original. No claim is made that the three-state graph polynomial is a previously unknown graph polynomial under all transformations.

## Limitations

Loop arrows and relations beyond radical square zero are not covered. The joint polynomial records the number of size-two zero Jordan blocks and the **total** nonzero eigenspace multiplicity, not the separate count of every eigenvalue, although the direct coloring formula allows that refinement. The counts are of labeled algebra elements, not distinct inner derivations, automorphism orbits, or conjugacy classes. The two-variable polynomial may be expressible as a specialization of existing multivariate Tutte/Potts polynomials; that equivalence is not ruled out. The original-observation status of the complete Jordan-type classification is subject to independent historical review. Exhaustive tests over small prime fields are corroboration, not a proof over arbitrary fields.

## References

1. C. Strametz, *The Lie algebra structure on the first Hochschild cohomology group of a monomial algebra*, arXiv:math/0111060, first public version 6 November 2001, https://arxiv.org/abs/math/0111060.
2. S. Sanchez-Flores, *The Lie module structure on the Hochschild cohomology groups of monomial algebras with radical square zero*, arXiv:0711.2810, first public version 18 November 2007, https://arxiv.org/abs/0711.2810.
3. L. Guo and F. Li, *Structure of Hochschild cohomology of path algebras and differential formulation of Euler's polyhedron formula*, arXiv:1010.1980, first public version 11 October 2010, https://arxiv.org/abs/1010.1980.
4. Classical incidence-matrix rank formula: the rank of the oriented incidence matrix of a finite loopless graph over any field is the number of vertices minus the number of connected components.
