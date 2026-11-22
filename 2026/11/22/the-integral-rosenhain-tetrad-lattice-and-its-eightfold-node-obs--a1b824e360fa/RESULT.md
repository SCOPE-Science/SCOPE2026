# The integral Rosenhain-tetrad lattice and its eightfold node obstruction

## Finding

Let \(C\) be a smooth genus-two curve over an algebraically closed field \(k\) with \(\operatorname{char}(k)\ne 2\), and let \(X\) be its singular Jacobian Kummer quartic. Its sixteen nodes are naturally labeled by the affine symplectic space \(V=\operatorname{Jac}(C)[2]\cong\mathbb F_2^4\). A **Rosenhain tetrad** is the four-node subset belonging to an affine translate of a nonisotropic two-dimensional linear subspace of \(V\) for the Weil pairing. There are eighty such tetrads.

For each tetrad \(R\), form its node-incidence vector \(e_R=\sum_{x\in R}e_x\) in the free lattice \(\mathbb Z^V\). Write \(L_R=\sum_R\mathbb Z e_R\). Choose binary coordinates \(x=(x_0,x_1,x_2,x_3)\) in which the symplectic form and one quadratic refinement are
\[
B(x,y)=\sum_{i\ne j}x_i y_j\pmod 2,\qquad q(x)=\sum_{0\le i<j\le3}x_i x_j\pmod2.
\]
For an arbitrary integral node-weight vector \(w=(w_x)_{x\in V}\), put \(S(w)=\sum_xw_x\), \(Q(w)=\sum_xq(x)w_x\), and \(m_i(w)=\sum_xx_iw_x\). Then the **complete integral membership criterion** is
\[
\boxed{L_R=\{w\in\mathbb Z^V:S(w)-4Q(w)\equiv0\pmod8,\quad m_i(w)\equiv0\pmod2\ (0\le i\le3)\}.}
\]
In particular,
\[
\mathbb Z^{16}/L_R\cong\mathbb Z/8\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^4,
\qquad [\mathbb Z^{16}:L_R]=128.
\]
The \(16\)-by-\(80\) incidence matrix has rank sixteen and Smith invariant factors \(1^{11},2^4,8\). The class of **each individual node** has exact order eight in this quotient: \(8e_x\in L_R\) but \(4e_x\notin L_R\) for every \(x\in V\).

## Assumptions and scope

The characteristic hypothesis makes the two-torsion reduced and gives the standard sixteen ordinary nodes. The node weights are **formal integer coefficients**: this is a theorem about the incidence image in \(\mathbb Z^{16}\), not an identification of that quotient with the Picard group, a Néron--Severi lattice or the Chow group of a surface. The choice of an affine symplectic labeling changes only the presentation, not the intrinsic sublattice. In any field extension over which the sixteen nodes become labeled, the same geometric statement holds. No arithmetic Frobenius reconstruction is claimed.

## Proof

**1. Geometry and completeness of the eighty generators.** Keum, Section 2, and Dolgachev, Section 5, identify Rosenhain tetrads with affine nonisotropic two-planes in the symplectic four-space \(V\). There are \((15\cdot14)/6=35\) two-dimensional linear subspaces: each has six ordered bases. For each nonzero \(u\), the space \(u^\perp\) contains exactly six vectors distinct from \(0,u\); hence the number of isotropic two-planes is \((15\cdot6)/6=15\). The other twenty have \(B(u,v)=1\), and each has four distinct affine translates, giving exactly eighty distinct Rosenhain tetrads. All are included in the certificate.

**2. Four parity conditions and a coupled eightfold condition.** If \(R=a+\langle u,v\rangle\), the sum over its four points of every affine-linear binary function is zero modulo two. Thus \(m_i(e_R)=0\pmod2\). Since \(q\) has polarization \(B\), its second finite difference on the plane is
\[
\sum_{z\in R}q(z)\equiv B(u,v)=1\pmod2.
\]
Therefore \(S(e_R)=4\) and \(S(e_R)-4Q(e_R)\equiv0\pmod8\). The span \(L_R\) lies in the proposed congruence kernel \(K\).

**3. The proposed kernel has index \(128\).** Define
\[
\Phi:\mathbb Z^V\longrightarrow\mathbb Z/8\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^4,\qquad
w\longmapsto\bigl(S(w)-4Q(w),m_0(w),m_1(w),m_2(w),m_3(w)\bigr).
\]
The basis vector \(e_0\) maps to \((1,0,0,0,0)\). For each coordinate vector \(b_i\) of \(V\), the difference \(e_{b_i}-e_0\) maps to \((0,\mathbf e_i)\) because \(q(b_i)=0\). These five images generate the target. Thus \(\Phi\) is onto and \([\mathbb Z^V:K]=8\cdot2^4=128\).

**4. Exact finite maximal-minor certificate.** Order the sixteen nodes by their binary labels \(0,1,\ldots,15\), with bit \(i\) representing \(x_i\). Order the eighty tetrads lexicographically by their sorted four-element node tuples. The following sixteen tetrads, identified by zero-based positions in that order, have an incidence determinant **\(+128\)** (rows are tetrads and columns are nodes):

```text
index   sorted node labels
  0     0,1,2,3
  3     0,1,14,15
  7     0,3,5,6
 12     0,5,9,12
 13     0,5,11,14
 24     1,3,9,11
 26     1,4,8,13
 35     1,7,11,13
 42     2,5,9,14
 44     2,5,11,12
 49     3,4,8,15
 60     4,5,10,11
 68     5,7,8,10
 69     5,7,13,15
 70     6,7,8,9
 72     8,9,10,11
```

The exact fraction-free Bareiss determinant evaluation and full enumeration are implemented in `verify_rosenhain.py`; the complete independent list of eighty ordered tetrads is `rosenhain_80.csv`. Because these sixteen incidence vectors lie in \(L_R\), their determinant shows \([\mathbb Z^{16}:L_R]\le128\). Combined with \(L_R\subseteq K\), whose index is \(128\), this proves \(L_R=K\), without assuming that any incomplete enumeration proves a universal statement.

**5. Quotient and sharp obstruction.** The surjective map \(\Phi\) identifies the quotient with its explicit finite target, producing Smith factors \(1^{11},2^4,8\). Every \(e_x\) has an odd first coordinate under \(\Phi\), so its quotient order is eight; this is also true for \(x=0\). Coordinate transformations preserve the statement, because the incidence definition of \(L_R\) is intrinsic. Adding linear terms to \(q\) or translating node labels leaves the kernel conditions equivalent once the four parity moments and the total-sum condition are imposed.

## Verification

Run `python3 verify_rosenhain.py` using the Python standard library. It enumerates the twenty nonisotropic directions and eighty affine tetrads, checks each quadratic and linear moment, evaluates the displayed exact \(16\)-by-\(16\) determinant by fraction-free integer elimination, and matches all eighty entries of `rosenhain_80.csv`. Separately, integer Smith-form computation on the same \(80\)-by-\(16\) matrix gives diagonal \(1^{11},2^4,8\), consistent with the theoretical quotient. The proof of the bound and equality does not depend on a floating-point experiment or on historical computation logs.

## Relationship to prior work

Keum (1997, Section 2) and Dolgachev (arXiv:2302.13101, Section 5) establish the eighty Rosenhain tetrads and their nonisotropic affine-plane geometry. Neither supplies the integral node-incidence congruence kernel, its exact quotient or the order-eight node obstruction. The published *Integral Göpel-tetrad lattice of a Kummer quartic* addresses the **different sixty isotropic** tetrads and gives a formal-node quotient \(\mathbb Z/4\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^5\), also of index \(128\). Although these complementary incidence problems have the same total index, their quotient exponents are different (four versus eight); the Göpel theorem does not imply the Rosenhain classification. Cullinane's 2013 description of Rosenhain and Göpel tetrads in the binary projective setting supplies combinatorial context, but not the stated integral quotient.

## Limitations

This result concerns a universal finite incidence lattice, not the lattice of divisor classes or its intersection pairing on the Kummer resolution. It does not classify configurations in characteristic two, where the ordinary sixteen-node quartic picture changes. It also does not assert a higher-genus or higher-dimensional analogue. Searches found no exact previous statement of this integral Rosenhain lattice; this is not proof of historical uniqueness, and a hidden coding-theoretic Smith table remains a priority risk. Independent mathematical validation has not been performed.

## References

1. I. V. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, arXiv:2302.13101 (first public 2023-02-25), Section 5. https://arxiv.org/abs/2302.13101
2. J. H. Keum, *Automorphisms of Jacobian Kummer surfaces*, Compositio Mathematica **107** (1997), 269--288, Sections 1--3, https://doi.org/10.1023/A:1000148907120
3. S. H. Cullinane, *Rosenhain and Göpel Tetrads in PG(3,2)* (2013), https://m759.github.io/35/hudson.html
4. *The integral Göpel-tetrad lattice of a Kummer quartic* (2026), published research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-g-pel-tetrad-lattice-of-a-kummer-quartic--2fe9c0537bec
