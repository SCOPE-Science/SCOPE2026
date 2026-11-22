# Twelve vertices are sharp for loss of positivity in three-step Chebyshev inverses on trees

## Finding
Let \(T\) be any finite, connected, unweighted tree with at least two vertices. Write \(L_T\) for its combinatorial Laplacian, \(\Lambda=\lambda_{\max}(L_T)\), and \(A=\mu I+L_T\) with \(\mu>0\). Define the exact-endpoint third Chebyshev residual and corresponding quadratic approximate inverse by
\[
r_3(z)=\frac{T_3((\mu+\Lambda/2-z)/(\Lambda/2))}{T_3((\mu+\Lambda/2)/(\Lambda/2))},\qquad B=\frac{I-r_3(A)}{A},\qquad T_3(t)=4t^3-3t,
\]
where division by \(A\) means polynomial division followed by evaluation, not a numerical solve.

**Theorem.** Every tree with at most eleven vertices has \(B\) entrywise nonnegative for every \(\mu>0\). Indeed, all entries at tree distance at most two are strictly positive, and all entries at distance at least three vanish. Twelve vertices are the sharp smallest possible order of failure: the double star with two adjacent hubs each carrying five leaves has a strictly negative bridge entry whenever
\[
0<\mu<\mu_5=6-\frac32\sqrt{14}.
\]
For every integer \(m\ge1\), the symmetric double star with \(m\) leaves at each hub has an entrywise nonnegative \(B\) for every positive shift if \(m\le4\); if \(m\ge5\), its bridge entry is negative exactly for \(0<\mu<\mu_m\), zero at \(\mu=\mu_m\), and positive above it, where
\[
\mu_m=\frac{5m-1-3\sqrt{m^2+6m+1}}4.
\]
All other entries of its \(B\) are nonnegative for every shift, with strictly positive entries on the diagonal and at graph distance at most two apart from the specified bridge.

A stronger weighted-tree identity also holds. For an arbitrary connected positive-edge-weight tree, define weighted degrees \(d_i=\sum_j w_{ij}\). Then the sign of \(B_{ij}\) on each edge \(\{i,j\}\) is exactly the sign of \(\mu+3\Lambda/2-d_i-d_j\); the nonedge and diagonal assertions continue to hold. The twelve-vertex minimality claim is restricted to **unit edge weights**, not arbitrary positive weights.

## Assumptions and scope
The Chebyshev interval is the **exact** spectral interval \([\mu,\mu+\Lambda]\), with no extra margin. This is the inverse polynomial associated with three completed semi-iteration steps starting at zero. All assertions concern the *completed polynomial*, not positivity of its intermediate implementation stages. The graph is undirected, connected and loopless. All vertex and edge counts refer to the original tree, without isolated vertices. In the stated weighted extension, all weights are finite and strictly positive.

Let
\[
\Delta=\Lambda^2+16\Lambda\mu+16\mu^2,
\quad a_2=\frac{32}{(\Lambda+2\mu)\Delta},
\quad a_1=-\frac{48}{\Delta},
\quad a_0=\frac{6(\Lambda+4\mu)(3\Lambda+4\mu)}{(\Lambda+2\mu)\Delta}.
\]
Then \(B=a_0I+a_1A+a_2A^2\). The constants are strictly well-defined, and \(a_2>0\).

## Proof
**1. Exact polynomial and local edge criterion.** Expand \(T_3\) to obtain the coefficient identity just given. For any weighted graph with Laplacian \(L\), off-diagonal entries of \(A\) and \(A^2\) are
\[
A_{ij}=-w_{ij},\qquad (A^2)_{ij}=-(2\mu+d_i+d_j)w_{ij}+\sum_{k\ne i,j}w_{ik}w_{kj},\quad i\ne j.
\]
Consequently
\[
B_{ij}=a_2\left[w_{ij}\left(\mu+\frac32\Lambda-d_i-d_j\right)
+\sum_{k\ne i,j}w_{ik}w_{kj}\right].\tag{1}
\]
For a tree, adjacent vertices have no common neighbor, and a pair at distance two has exactly one common neighbor. Thus (1) gives the asserted edge sign, strict positivity at distance two, and zero beyond distance two. On the spectral interval, the modulus of the Chebyshev residual \(r_3(z)\) is at most \(1/T_3(1+2\mu/\Lambda)<1\). Hence \((1-r_3(z))/z>0\) on the positive spectrum of \(A\). Therefore \(B\) is positive definite and its diagonal entries are strictly positive. This conclusion does not require its off-diagonal entries to be nonnegative.

**2. A double-star spectral comparison.** Given an edge \(ij\) in a tree, put \(k=\deg(i)-1\), \(\ell=\deg(j)-1\), \(s=k+\ell\). The edge and all incident edges form a double star \(D_{k,\ell}\) with \(s+2=\deg(i)+\deg(j)\) vertices. Its Laplacian is a positive-semidefinite summand of the Laplacian of the full tree, after padding by zeros; thus
\[
\Lambda(T)\ge\Lambda(D_{k,\ell}).\tag{2}
\]
Direct elimination of the leaf coordinates in the double-star eigenvalue equation gives the cubic
\[
P_{k,\ell}(z)=z^3-(s+4)z^2+(k\ell+2s+5)z-(s+2),\tag{3}
\]
whose largest real root equals \(\Lambda(D_{k,\ell})\). This remains true when a hub has zero extra leaves, in which case the cubic contains redundant factors at eigenvalue one.

Set \(z_s=2(s+2)/3\). At fixed \(s\), the value \(P_{k,\ell}(z_s)\) increases with \(k\ell\); the maximum therefore occurs at the balanced pair. Writing \(s=2r\), or \(s=2r+1\), gives respectively
\[
P_{r,r}(z_s)=\frac{2(r+1)(2r^2-8r-1)}{27},\qquad
P_{r,r+1}(z_s)=\frac{(2r+3)(2r^2-6r-9)}{27}.\tag{4}
\]
Both expressions are strictly negative for all integers \(0\le r\le4\). Thus for every \(s\le9\), \(P_{k,\ell}(z_s)<0\). Since the monic cubic tends to positive infinity as \(z\to+\infty\), its largest real root is strictly greater than \(z_s\). From (2),
\[
\deg(i)+\deg(j)=s+2<\frac32\Lambda(D_{k,\ell})\le\frac32\Lambda(T).\tag{5}
\]
If the tree has at most eleven vertices, \(s+2\le |V(T)|\le11\), so \(s\le9\) and (5) applies to every edge. Formula (1) proves strict positivity on every edge for every \(\mu>0\). Together with step 1 this proves the universal statement.

**3. Sharpness, all symmetric double stars, and exact witness.** For \(D_{m,m}\), the largest Laplacian eigenvalue is
\[
\Lambda_m=\frac{m+3+\sqrt{m^2+6m+1}}2.
\]
(The other nontrivial roots are \(m+1\) and \((m+3-\sqrt{m^2+6m+1})/2\), with eigenvalue one contributed by leaf differences.) Both central degrees equal \(m+1\). Formula (1) shows that the central edge changes sign precisely when
\[
\mu=2(m+1)-\frac32\Lambda_m=\mu_m.
\]
The numerator of \(\mu_m\) is positive for integer \(m\ge1\) exactly if \(m\ge5\): squaring the positive-sided inequality \(5m-1>3\sqrt{m^2+6m+1}\) is equivalent to \(2m^2-8m-1>0\). An outer hub-to-leaf edge has degree sum \(m+2\), which is smaller than \(3\Lambda_m/2\), since \(\Lambda_m>m+2\). Hence it always gives positive \(B\) entries; other off-diagonal cases follow from step 1.

At \(m=5\), the tree has twelve vertices, \(\Lambda_5=4+\sqrt{14}\), and \(\mu_5=6-3\sqrt{14}/2>1/4\). For the exact rational shift \(\mu=1/4\), one obtains
\[
B_{\mathrm{hub},\mathrm{hub}}=\frac{5888\sqrt{14}-22032}{193}<0,
\]
because \(\mu=1/4<\mu_5\), equivalently \(6\sqrt{14}<23\), as certified by \(504<529\). The explicit witness and step 2 show that twelve is minimal. \(\square\)

## Verification
Run `python verify.py` with SymPy. The script derives the polynomial coefficients directly from the defining Chebyshev polynomial, checks the exact balanced-double-star cubic evaluations (4), checks the symmetric-double-star eigenvalue and threshold identities, and reconstructs the full twelve-by-twelve rational-plus-radical matrix for the exact witness. Optional NetworkX and NumPy enumeration independently checks the edge inequality on every one of the 435 nonisomorphic trees of orders two through eleven. The enumerations are **not** used as proof of any universal or all-shift statement.

## Relationship to prior work
Chebyshev semi-iteration and its fixed residual polynomials are classical. The 2008 Wathen–Rees technical report explains the linear preconditioning use of fixed Chebyshev polynomials; the 2011 Meng–Saunders–Mahoney preprint applies semi-iteration in randomized numerical linear algebra. These sources concern convergence and implementation, not a smallest-tree sign-obstruction theorem.

A directly related published result, *Condition three is the sharp positivity frontier for the degree-three Chebyshev semi-iterate*, gives the same quadratic-polynomial identity and an unrestricted Stieltjes-matrix condition-number criterion with a three-dimensional counterexample. Here that algebra is explicitly reused, **not** claimed as new. Its counterexample is neither a connected shifted graph Laplacian nor an unweighted tree, and its uniform condition-number threshold does not imply the sharp eleven-to-twelve-vertex classification, the tree edge-degree spectral comparison, or the symmetric double-star threshold. The new contribution is precisely that graph-specific global classification and its proof via double-star domination and an extremal cubic sign test.

## Limitations
The minimal twelve-vertex threshold is for connected **unweighted trees** and the exact degree-three Chebyshev polynomial. Arbitrarily weighted trees, general graphs, inaccurate spectral enclosures, higher polynomial degrees, and intermediate iterate positivity have no analogous minimum claimed here. The polynomial may be symmetric positive definite even when it is not entrywise nonnegative. Literature searches and inspection of the closest related public results did not prove publication priority; an equivalent theorem in unindexed numerical linear algebra remains possible. The optional graph census corroborates, but does not replace, the symbolic proof.

## References
1. G. H. Golub and R. S. Varga, *Chebyshev Semi-Iterative Methods, Successive Overrelaxation Iterative Methods, and Second Order Richardson Iterative Methods*, Numerische Mathematik 3 (1961), Parts I and II.
2. A. J. Wathen and T. Rees, *Chebyshev Semi-iteration in Preconditioning*, Oxford Numerical Analysis Report NA-08/14 (October 2008), https://www.cs.ox.ac.uk/files/1540/NA-08-14.pdf.
3. X. Meng, M. A. Saunders, and M. W. Mahoney, *LSRN: A Parallel Iterative Solver for Strongly Over- or Under-Determined Systems*, first arXiv posting 2011-09-27, https://arxiv.org/abs/1109.5981.
4. *Condition three is the sharp positivity frontier for the degree-three Chebyshev semi-iterate*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-condition-three-is-the-sharp-positivity-frontier-for-the-degree--6e9af63df14e.
5. L. Yu. Kolotilina and A. Yu. Yeremin, *Factorized Sparse Approximate Inverse Preconditionings I. Theory*, SIAM J. Matrix Anal. Appl. 14 (1993), 45–58, https://doi.org/10.1137/0614004.
