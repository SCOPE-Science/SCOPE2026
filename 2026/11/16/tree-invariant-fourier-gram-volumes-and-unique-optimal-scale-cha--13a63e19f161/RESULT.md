# Tree-invariant Fourier Gram volumes and unique optimal scale chains for causal exponential contrasts

## Finding

For every integer \(K\ge1\), let \(0<r_0<r_1<\cdots<r_K\) and put
\[
 h_r(t)=r^{-1}e^{-t/r}\mathbf 1_{(0,\infty)}(t),\qquad
 W(a,b)=\|h_b-h_a\|_2^2=\frac{(b-a)^2}{2ab(a+b)}.
\]
Choose exactly \(K\) distinct unordered pairs \(E\) from the \(K+1\) scale indices. For each edge \(e=\{i,j\}\) select either orientation \(\psi_e=h_{r_j}-h_{r_i}\) and its unit-norm version \(\phi_e=\psi_e/\sqrt{W(r_i,r_j)}\). Write \(G_E=(\langle\psi_e,\psi_f\rangle)_{e,f\in E}\) and \(\widehat G_E=(\langle\phi_e,\phi_f\rangle)_{e,f\in E}\).

**Complete tree criterion and determinant.** Both Gram determinants vanish unless \(E\) is a spanning tree on the \(K+1\) vertices. If \(E\) is any spanning tree, then
\[
 \boxed{\det G_E =
 \frac{2\left(\sum_{j=0}^{K}r_j\right)
 \prod_{0\le i<j\le K}(r_j-r_i)^2}
 {\prod_{i,j=0}^{K}(r_i+r_j)}},
 \qquad
 \boxed{\det\widehat G_E=\frac{\det G_E}{\prod_{\{i,j\}\in E}W(r_i,r_j)}}.
\]
In particular, the unnormalized Gram volume is *independent of spanning-tree topology*, even on an arbitrarily irregular scale grid.

**Unique normalized determinant maximizer.** Among every choice of \(K\) scale-pair contrast channels, the unique maximizing edge set is the consecutive chain
\[
 \boxed{E_*=\big\{\{0,1\},\{1,2\},\ldots,\{K-1,K\}\big\}}.
\]
Changing orientations changes neither determinant nor uniqueness of the edge set. The maximal normalized determinant is obtained by inserting \(E_*\) into the displayed quotient. Every other tree has strictly smaller normalized Gram determinant and every non-tree has zero determinant.

**Sharp fixed-rank collision law.** Fix real \(t_0<\cdots<t_K\) and \(r>0\), and let \(r_j=r e^{L t_j}\) with \(L\downarrow0\). Then
\[
 \boxed{\det\widehat G_{E_*}\sim
 \frac{K+1}{2^{K^2}}
 \frac{\displaystyle\prod_{0\le i<j\le K}(t_j-t_i)^2}
 {\displaystyle\prod_{j=1}^{K}(t_j-t_{j-1})^2}
 L^{K(K-1)}.}
\]
In the equally log-spaced case \(t_j=j\), the constant simplifies to
\[
 \frac{K+1}{2^{K^2}}\prod_{d=1}^{K}(d!)^2.
\]
The collision exponent is exactly \(K(K-1)\), for every *fixed* number \(K\) of contrast channels. There is no joint increasing-rank assertion.

## Assumptions and scope

All inner products are those of the real or complex Hilbert space \(L^2((0,\infty),dt)\) with Lebesgue measure. The positive scales are strictly ordered but otherwise completely arbitrary. A selected channel is the difference of **two** causal unit-mass exponentials. A tree has all \(K+1\) vertices and \(K\) edges. The normalized determinant is the product of eigenvalues of the \(K\times K\) correlation Gram matrix, a natural determinant-based stability/volume criterion; it is not the spectral condition number. The near-collision asymptotic holds at fixed \(K,r,t_0,\ldots,t_K\), with a positive asymptotic constant. In particular, \(K=1\) has determinant exactly one. No frame claim is made for all of \(L^2(0,\infty)\) or for time-translated banks.

## Proof

**1. Cauchy structure and graph rank.** Elementary integration gives
\[
 \langle h_{r_i},h_{r_j}\rangle=\frac1{r_i+r_j}.
\]
Let \(C=(1/(r_i+r_j))_{0\le i,j\le K}\). This symmetric Cauchy matrix is positive definite: for arbitrary complex coefficients, the corresponding quadratic form is the squared \(L^2\) norm of a linear combination of the pairwise distinct exponential functions, which are linearly independent by successive decay-rate comparison. Let \(B_E\) be the \(K\times(K+1)\) edge-vertex oriented incidence matrix, with one negative and one positive entry per row. Then \(G_E=B_E C B_E^{\mathsf T}\). As \(C\) is positive definite, \(\operatorname{rank}G_E=\operatorname{rank}B_E\). The row rank is \(K\) precisely when the \(K\)-edge graph is connected, hence a spanning tree; otherwise the determinant is zero.

**2. Tree-invariance and exact Cauchy determinant.** For a spanning tree, its oriented edge vectors are an integral basis of the root lattice \(\{x\in\mathbb Z^{K+1}:\sum_jx_j=0\}\), because paths from any fixed root express every elementary difference integrally and uniquely. Consequently the edge-incidence matrices of any two trees are related by a square integer unimodular transformation, of determinant \(\pm1\), and their Gram determinants coincide. It suffices to evaluate the incidence Gram of one tree.

Let \(\mathbf1\) denote the all-ones column vector of length \(K+1\). The standard codimension-one Gram identity
\[
 \det(B_E C B_E^{\mathsf T})=\det(C)\,\mathbf1^{\mathsf T}C^{-1}\mathbf1
\]
holds for an incidence basis: using Cauchy--Binet on a square factorization of \(C\), the cofactors of \(B_E\) are \((-1)^j\) times a common sign, because deleting any vertex column of a tree incidence matrix gives determinant of modulus one. Equivalently, augment the tree basis by one coordinate vector to a unimodular square matrix and take its Schur complement. The identity has no extra factor of \(K+1\): at \(C=I\) it reads \(K+1=K+1\).

The classical Cauchy determinant identity yields
\[
 \det(C)=\frac{\prod_{0\le i<j\le K}(r_j-r_i)^2}
 {\prod_{i,j=0}^{K}(r_i+r_j)}.
\]
To compute the remaining scalar without inverting the matrix explicitly, put \(x=C^{-1}\mathbf1\) and
\[
 R(z)=\sum_{j=0}^{K}\frac{x_j}{z+r_j}.
\]
The equations \(Cx=\mathbf1\) give \(R(r_i)=1\) for every \(i\). The two rational functions \(1-R(z)\) and \(\prod_{j=0}^K(z-r_j)/(z+r_j)\) have the same poles and zeros and both tend to one at infinity; hence they coincide. Comparing coefficients of \(1/z\) in
\[
 R(z)=1-\prod_{j=0}^{K}\frac{z-r_j}{z+r_j}
 =\frac{2\sum_{j=0}^{K}r_j}{z}+O(z^{-2})
\]
gives \(\mathbf1^{\mathsf T}C^{-1}\mathbf1=2\sum_jr_j\), proving the first boxed formula.

**3. Exact unique optimal tree.** The channel energy is
\[
 W(a,b)=\frac1{2a}+\frac1{2b}-\frac2{a+b},\qquad 0<a<b.
\]
Its partial derivatives are
\[
 \partial_aW=-\frac1{2a^2}+\frac2{(a+b)^2}<0,
 \qquad
 \partial_bW=-\frac1{2b^2}+\frac2{(a+b)^2}>0.
\]
For each cut \(\{0,\ldots,j\}\mid\{j+1,\ldots,K\}\), the unique minimum-energy crossing edge is \(\{j,j+1\}\): moving its left endpoint left or its right endpoint right strictly increases \(W\). The same statement holds after applying \(\log\), since \(W>0\). By the spanning-tree cut-exchange principle, every minimum spanning tree for the edge costs \(\log W(r_i,r_j)\) must contain the unique minimum crossing edge of each cut. All \(K\) adjacent edges therefore belong to the tree, leaving exactly \(E_*\). Since the unnormalized determinant is positive and common to all trees and
\[
 \log\det\widehat G_E=\log\det G_E-\sum_{e\in E}\log W_e,
\]
this unique minimum spanning tree is the unique normalized determinant maximizer, with all non-trees strictly worse because their determinant vanishes.

**4. Sharp collision constant and exponent.** With \(r_j=r e^{Lt_j}\), uniformly for the finitely many indices,
\[
 r_j-r_i=rL(t_j-t_i)(1+O(L)),\quad
 \sum_{j=0}^K r_j=r(K+1)(1+O(L)),\quad
 r_i+r_j=2r(1+O(L)),
\]
and for each chain edge,
\[
 W(r_{j-1},r_j)=\frac{L^2(t_j-t_{j-1})^2}{4r}(1+O(L)).
\]
Inserting these expansions into the exact determinant quotient yields exponent \(K(K+1)-2K=K(K-1)\), with the displayed constant \((K+1)2^{-K^2}\) after cancellation of all \(r\)-powers. For \(t_j=j\), count the factors \(j-i\) by their separations to obtain \(\prod_{i<j}(j-i)^2=\prod_{d=1}^K(d!)^2\). The factors are strictly positive, so the exponent and coefficient are sharp.

## Verification

Run `python CHECK.py` with the adjacent standalone file in a Python 3 environment. It uses exact rational arithmetic to reconstruct finite Cauchy and contrast Gram matrices independently, and compares the analytical determinant against direct elimination on non-geometric scale grids. A complete Prüfer-code enumeration of all trees through six vertices tests the unique maximizing chain and the common unnormalized determinant. The separate symbolic asymptotic coefficient calculation checks the collision constant for several ranks. These are exact **finite** checks; the universal rank, uniqueness and asymptotic claims are proved in the preceding four steps.

## Relationship to prior work

J. E. Pedersen, T. Lindeberg and P. Gerstoft, *Frame bounds and bandwidth tiling for time-causal bandpass wavelets* (arXiv:2609.17201, first public September 15, 2026), develop causal difference-of-exponentials wavelets, spectral channel bounds, and interchannel Gram conditioning. Their constructions motivate choosing contrasts between lowpass scales, but the inspected sections do not provide the present non-geometric scale-pair tree selection theorem, tree-invariant finite Gram determinant, or rank-dependent collision law.

The previously published work *Sharp dense-scale conditioning of causal exponential-difference dilates* (November 2026; see references) evaluates an infinite Toeplitz Gram symbol for uniformly geometrically spaced normalized adjacent channels and an exponentially small infinite-sequence Riesz bound. It does not imply the finite, arbitrary-scale **tree** determinant and unique all-edge-set D-optimal design: its statement fixes a geometric chain and studies a different limit. The present finite-rank collision exponent is polynomial, so the distinct asymptotic regimes must not be conflated.

The Cauchy determinant and graph-incidence lattice basis are classical ingredients, not independently claimed discoveries. Their combination with normalization and strict cut monotonicity gives the exact arbitrary-scale design and its sharp collision law.

## Limitations

The theorem optimizes the determinant (Gram volume), not individual spectral endpoints, coherence, additive noise amplification, or a frame condition number. It does not analyze implementation delay, discrete recursion, time translation, or infinitely many channels. For a fixed number of channels the collision law is polynomial; taking the channel count to infinity as scales collide can change the conditioning regime. Older specialized experimental-design or totally positive kernel work might contain an equivalent tree-invariance statement, a residual originality risk requiring independent literature audit.

## References

1. J. E. Pedersen, T. Lindeberg and P. Gerstoft, *Frame bounds and bandwidth tiling for time-causal bandpass wavelets*, arXiv:2609.17201 (first public September 15, 2026), https://arxiv.org/abs/2609.17201.
2. *Sharp dense-scale conditioning of causal exponential-difference dilates*, published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dense-scale-conditioning-of-causal-exponential-difference--665865eb3d5b.
3. The classical symmetric Cauchy determinant identity and incidence-matrix characterization of spanning trees are used as explicit algebraic inputs, with the needed specializations proved above.
