# Fixed-angle equiangular Kolmogorov widths and the number-partition threshold

## Finding
Fix an integer \(m\ge 2\), real numbers \(a_1,\ldots,a_m>0\), and \(\delta>0\). In a real Hilbert space containing the orthonormal vectors \(e_1,\ldots,e_m,u\), form the finite set
\[
E_{a,\delta}=\{0\}\cup\left\{v_j=\frac{e_j+\delta u}{a_j}:1\le j\le m\right\}.
\]
Write \(Q=\sum_{j=1}^m a_j^2\), \(\gamma=\delta^2/(1+m\delta^2)\), and the weighted sign discrepancy
\[
\Delta(a)=\min_{\varepsilon\in\{-1,1\}^m}\left|\sum_{j=1}^m\varepsilon_j a_j\right|.
\]
Then the exact real Kolmogorov width at the terminal nontrivial dimension is
\[
\boxed{d_{m-1}(E_{a,\delta})^2=\frac{1}{Q-\gamma\Delta(a)^2}.}
\]
Every minimizing \((m-1)\)-plane **inside the span of the nonzero points** has an explicit normal given below. At \(\delta=1\), every pair of distinct nonzero vertex directions has cosine \(1/2\), independent of the unequal radial scales. For positive integer inputs \(a_j\), deciding whether \(d_{m-1}(E_{a,1})^2\le1/Q\) is weakly NP-complete. This is a sharp restricted decision problem; it does not assert strong NP-hardness or a constant-factor hardness threshold.

## Assumptions and scope
The ambient scalar field is **real**. Width means
\[
d_n(E)=\inf_{\substack{L\text{ a linear subspace}\\\dim L\le n}}\ \max_{x\in E}\operatorname{dist}(x,L).
\]
Only the order \(n=m-1\) is addressed. No affine translation is allowed in the definition. The input set need not be centrally symmetric, but replacing it with its absolutely convex hull leaves this width unchanged because distance to a linear subspace is a seminorm. All \(a_j\) are strictly positive, with no ordering requirement. For the complexity conclusion, \(m\) and the positive integers \(a_j\) are the input in binary; the vectors have rational coordinates at the fixed coupling \(\delta=1\), and the threshold is the rational number \(1/Q\).

The Gram matrix \(G=(\langle v_i,v_j\rangle)_{i,j=1}^m\) is positive definite because the \(v_j\) are linearly independent. Their normalized pairwise inner products are
\[
\frac{\langle v_i,v_j\rangle}{\|v_i\|\|v_j\|}=\frac{\delta^2}{1+\delta^2},\quad i\ne j.
\]
In particular, \(\delta=1\) corresponds to a fixed acute angle of \(60^\circ\).

## Proof
**Reduction to a dual cube problem.** Let \(H=\operatorname{span}\{v_1,\ldots,v_m\}\), of dimension \(m\). Orthogonal projection of an arbitrary candidate \(L\) into \(H\) cannot increase its distances from points of \(E_{a,\delta}\); extending its image, if necessary, gives a candidate \((m-1)\)-plane contained in \(H\). Thus it suffices to consider \(L=H\cap w^\perp\) with \(w\in H\) and \(\|w\|=1\).

Let \(B:\mathbb R^m\to H\) be the injective synthesis map \(Bx=\sum_j x_jv_j\), and put \(G=B^*B\). The coordinate vector \(y=B^*w\) has \(\|w\|^2=y^{\mathsf T}G^{-1}y\), since \(w=BG^{-1}y\). Moreover, the worst distance to \(L\) is \(\|y\|_\infty\). Homogeneity therefore gives
\[
d_{m-1}(E_{a,\delta})^{-2}
=\max_{\|y\|_\infty\le1}y^{\mathsf T}G^{-1}y
=\max_{\varepsilon\in\{-1,1\}^m}\varepsilon^{\mathsf T}G^{-1}\varepsilon.
\]
The last equality holds because \(G^{-1}\) is strictly positive definite: in each coordinate, a strict convex quadratic cannot be maximized at an interior point of an interval. Hence every maximizer of the cube problem is a sign vector.

**Rank-one Gram inversion.** Let \(A=\operatorname{diag}(a_1,\ldots,a_m)\) and \(\mathbf 1\) be the all-ones vector. The Gram matrix and its inverse are
\[
G=A^{-1}(I+\delta^2\mathbf 1\mathbf 1^{\mathsf T})A^{-1},\qquad
G^{-1}=A(I-\gamma\mathbf 1\mathbf 1^{\mathsf T})A,
\quad\gamma=\frac{\delta^2}{1+m\delta^2}.
\]
Direct multiplication verifies the inverse. For each sign vector,
\[
\varepsilon^{\mathsf T}G^{-1}\varepsilon
=\sum_{j=1}^m a_j^2-\gamma\left(\sum_{j=1}^m\varepsilon_j a_j\right)^2.
\]
Maximizing amounts exactly to minimizing the squared sign discrepancy, establishing the boxed expression. The denominator is strictly positive, since \(G^{-1}\) is positive definite. No interchange of asymptotic or infinite-dimensional limits is involved.

**Equality subspaces.** For a minimizing sign vector \(\varepsilon\), put \(W=Q-\gamma\Delta(a)^2>0\) and
\[
w_\varepsilon=\frac{BG^{-1}\varepsilon}{\sqrt W},\qquad
L_\varepsilon=H\cap w_\varepsilon^\perp.
\]
Then \(\|w_\varepsilon\|=1\), and \(\langle v_j,w_\varepsilon\rangle=\varepsilon_j/\sqrt W\) for all \(j\), so \(L_\varepsilon\) has maximal error \(1/\sqrt W\). Conversely, the coordinate image of a normal for any optimal \((m-1)\)-plane in \(H\), scaled to have sup-norm one, maximizes the strictly convex cube quadratic, hence is a discrepancy-minimizing sign vector. The choices \(\varepsilon\) and \(-\varepsilon\) yield the same plane. This classification is only stated for planes contained in \(H\); no classification of all possible ambient minimizers is needed.

**Fixed-angle complexity boundary.** Choose \(\delta=1\), so \(\gamma=1/(m+1)\). The formula implies
\[
d_{m-1}(E_{a,1})^2\ge\frac1Q,
\qquad
 d_{m-1}(E_{a,1})^2=\frac1Q
\iff \exists\varepsilon\in\{-1,1\}^m:\sum_j\varepsilon_j a_j=0.
\]
The right side is exactly the usual positive-integer PARTITION decision question. Mapping an instance to the rational coordinates \((e_j+u)/a_j\) and the rational threshold \(1/Q\) requires polynomial binary length and polynomial computation, so the restricted width-threshold decision problem is NP-hard. It lies in NP because a balanced sign vector is a polynomial-length exact certificate. The standard subset-sum dynamic program computes \(\Delta(a)\) in time polynomial in \(m\) and \(\sum_j a_j\), making this particular hardness weak rather than strong. Thus the restricted threshold decision problem is weakly NP-complete.

For equal radial scales \(a_j=a>0\), \(\Delta(a)=0\) when \(m\) is even and \(\Delta(a)=a\) when \(m\) is odd. In the orthogonal limit \(\delta=0\), the width instead always equals \(Q^{-1/2}\). This contrast singles out a precise effect of common-axis correlation.

## Verification
The accompanying standalone Python program `CHECK.py` uses only exact rational arithmetic. It tests Gram-inverse identities, the sign-cube quadratic, positivity, and constructed optimal normals on eight explicitly specified instances with \(2\le m\le9\) and rational couplings, checking **2,932 assertions**. Run from this directory with `python CHECK.py`. Successful output is `EQUIANGULAR_TERMINAL_WIDTH_RATIONAL_OK 2932`. Finite rational checks do not prove the theorem for arbitrary real inputs; the preceding matrix identities and convexity argument constitute the proof. The complexity statement relies on the standard NP-completeness of PARTITION and its standard pseudo-polynomial dynamic program.

## Relationship to prior work
Sinai (2026, arXiv:2611.19378v1), particularly Proposition 4.4 and its cited Sofman theorem, treats widths of **orthogonal coordinate spikes** and motivates the finite-codimension comparison. The present calculation changes the Gram matrix to a coupled rank-one form, for which a weighted sign-discrepancy optimization persists and can encode PARTITION. Sofman (1969) analyzes coordinate-aligned octahedra; the fixed-angle correlated construction is not a case of his stated orthogonal-axis formula.

Varadarajan, Venkatesh, Ye and Zhang (2006) discuss hardness of **unrestricted point-set outer radii**, mainly for affine flats and broad input families. Those results establish an important general hardness context, but by themselves do not provide a fixed acute-angle, one-point-per-direction construction or its exact width threshold. The algebraic inverse-Gram/cube reduction is elementary linear algebra; the assessed addition is the exact restricted equiangular discrepancy formula and its structural computational consequence, not the reduction alone.

## Limitations
The result is finite-dimensional, real, and terminal-codimension only; it does not extend automatically to complex subspaces or to arbitrary widths \(d_n\). The complexity conclusion is weak NP-completeness of a specifically parameterized exact-threshold decision, **not** strong NP-completeness, no polynomial-time approximation inapproximability, and no claimed application to a particular global attractor. More general historical treatments of matrix widths may implicitly subsume the inverse-Gram step, and a comprehensive historical uniqueness claim is not made.

## References
1. Arthur Sinai, *Lower bounds for the Kolmogorov widths of global attractors of dissipative systems*, arXiv:2611.19378v1, first public version 14 November 2026, Proposition 4.4. https://arxiv.org/abs/2611.19378
2. L. B. Sofman, *Diameters of octahedra*, Mathematical Notes **5** (1969), 258–262, DOI:10.1007/BF01410793. https://doi.org/10.1007/BF01410793
3. Kasturi Varadarajan, S. Venkatesh, Yinyu Ye, Jiawei Zhang, *Approximating the Radii of Point Sets*, 2006 preprint; preliminary versions in 2002 and 2003. https://optimization-online.org/wp-content/uploads/2006/08/1447.pdf
4. Allan Pinkus, *Matrices and n-Widths*, Linear Algebra and its Applications **27** (1979), 245–278, DOI:10.1016/0024-3795(79)90046-6. https://doi.org/10.1016/0024-3795(79)90046-6
