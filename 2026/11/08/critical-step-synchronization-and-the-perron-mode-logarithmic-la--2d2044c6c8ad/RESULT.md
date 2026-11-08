# Critical-step synchronization and the Perron-mode logarithmic law on trees

## Finding

Let \(G\) be any finite, connected, unweighted tree with \(m+1\geq 3\) vertices. Orient each edge from one bipartition class to the other, let \(B\) be its vertex-edge incidence matrix and \(K=B^{T}B\), and put \(L=\lambda_{\max}(K)\). Then the discrete sine-coupled edge-phase map
\[
F_h(z)=z+hK\sin z\pmod{2\pi},\qquad z\in\mathbb T^{m},
\]
has the following properties at the *critical step* \(h_{*}=2/L\).

1. **Global convergence at the descent endpoint.** Every orbit converges to one of the \(2^m\) phase configurations in \(\{0,\pi\}^m\), and the all-antiphase configuration \(p=\pi\mathbf1\) attracts Lebesgue-almost every orbit. This remains true although \(F_{h_*}\) need not be invertible and its derivative at \(p\) has a multiplier \(-1\).
2. **Sharp stability threshold.** The fixed point \(p\) is Lyapunov asymptotically stable at \(h=h_*\) and is linearly unstable for every \(h>h_*\). Thus the closed critical endpoint cannot be discarded from its stability range.
3. **Graph-dependent critical law.** Let \(u\) be the positive unit Perron eigenvector of \(K\), with \(Ku=Lu\), and set
\[
 A=I-\frac{2K}{L},\quad Q=I-uu^T,\quad c=\frac13\sum_i u_i^4,\quad
 w=-\left.(I+A)\right|_{u^\perp}^{-1}Q\frac{K(u^{\circ3})}{3L},
\]
\[
 d=\sum_i u_i^3w_i-\frac1{60}\sum_i u_i^6,\qquad
 b=\frac{2d+3c^2}{2c}.
\]
Here powers with a circle are taken componentwise and the restricted inverse acts on the invariant space \(u^\perp\). For every orbit tending to \(p\) except its codimension-one strong-stable set, choose the small real lift \(y_n=z_n-p\) for sufficiently large \(n\), and put \(a_n=u^Ty_n\). Then \(a_n\neq0\) eventually, and a finite orbit-dependent constant \(H\) exists with
\[
 \boxed{a_n^{-2}=2cn+b\log n+H+o(1).}
\]
In particular, \(\sqrt n\,|a_n|\to(2c)^{-1/2}\). For the path on four vertices (three edges), this becomes the **explicit, genuinely multidimensional** formula
\[
 \boxed{a_n^{-2}=\frac n4+\frac{17-\sqrt2}{96}\log n+H+o(1)},
 \qquad u=\left(\frac12,\frac1{\sqrt2},\frac12\right)^T.
\]
The exceptional strong-stable set has zero Lebesgue measure in the basin of \(p\); its trajectories approach \(p\) exponentially. Consequently the displayed law holds for almost every initial phase.

## Assumptions and scope

The graph has at least three vertices, unit symmetric edge weights, reciprocal sine interaction and the specified bipartite orientation. Its \(m\) edge coordinates give a complete quotient by common phase because the graph is a tree. The matrix \(K\) is symmetric positive definite, has diagonal entries \(2\), and its off-diagonal entries are \(1\) on incident edge pairs and \(0\) otherwise. Thus it is irreducible and nonnegative, with a simple largest eigenvalue \(L>0\) and a strictly positive unit eigenvector \(u\). All conclusions concern exact, unperturbed deterministic iterations on the \(m\)-torus; the reciprocal-square law excludes the strong-stable exceptional set.

## Proof

**Strict endpoint descent and global convergence.** Write \(V(z)=\sum_{i=1}^m\cos z_i\) and \(s=\sin z\), so the lifted update is \(\Delta=hKs\). For every real \(t\) and every nonzero real \(\delta\),
\[
 \cos(t+\delta)-\cos t<-\delta\sin t+\frac12\delta^2.
\]
Indeed the difference between the right-hand side and left-hand side is the integral of \((1-r)\delta^2[1+\cos(t+r\delta)]\) over \(0\leq r\leq1\), which is strictly positive. Since \(K\) is positive definite, \(s\neq0\) implies \(\Delta\neq0\). Summing the coordinate inequalities gives
\[
 V(F_hz)-V(z)<-h\,s^TKs+\frac{h^2}2s^TK^2s
 \leq\left(-h+\frac{h^2L}{2}\right)s^TKs.
\]
At \(h=h_*\) the right side vanishes, so \(V\) decreases **strictly** at every noncritical point. The finitely many critical points are exactly \(\{0,\pi\}^m\). Compactness and strictness show that the distance of every orbit to this finite set tends to zero: otherwise the decrease per visit to a compact subset away from the critical set would be bounded below. Moreover its steps tend to zero because \(\sin z_n\to0\). An orbit cannot consequently keep switching between separated critical neighborhoods; it converges to one fixed configuration. A noncritical fixed point is impossible because it would contradict strict descent.

**The sink and the null exceptional basins.** The point \(p=\pi\mathbf1\) is the unique global minimum of \(V\). Strict potential descent implies its Lyapunov stability, and global convergence proves attraction for starts in a sufficiently small strict sublevel neighborhood. Its derivative \(DF_{h_*}(p)=I-2K/L\) has one simple multiplier \(-1\) and all remaining multipliers strictly inside the unit disk. For every other critical point \(q\), write \(D_q=\operatorname{diag}(\cos q_i)\). The matrix \(KD_q\) is similar to the symmetric \(K^{1/2}D_qK^{1/2}\), which is congruent to \(D_q\), and hence has a positive eigenvalue because \(q\neq p\). The corresponding multiplier of \(I+(2/L)KD_q\) exceeds one. Every negative eigenvalue of \(KD_q\) exceeds \(-L\): equality would force all diagonal signs in \(D_q\) to be negative by equality in the Perron eigenvector triangle inequality for the irreducible nonnegative matrix \(K\), implying \(q=p\). Thus all other multipliers have modulus strictly below one, so each \(q\neq p\) is a hyperbolic saddle or source (in the endomorphism sense, allowing zero stable multipliers). The local stable-set theorem for smooth endomorphisms places the nearby forward-stable set in a smooth submanifold of codimension at least one. This version does not require invertibility in contracting directions: split the derivative into its contracting and expanding invariant blocks, solve the expanding coordinate backward by its invertible expanding block, and apply the contraction/graph-transform argument to forward orbits confined to a small neighborhood.

The determinant \(\det DF_{h_*}(z)\) is real analytic and not identically zero: at \(z=(\pi/2,\ldots,\pi/2)\) it equals \(1\). Its zero set is Lebesgue-null, and the inverse image of any null set under this analytic map is null by local inverse branches away from that set. Taking countably many preimages of the finitely many local stable submanifolds proves that the basins of all \(q\neq p\) are null. As every orbit converges to a critical point, \(p\) attracts almost every orbit. Finally, for \(h>2/L\), the derivative at \(p\) has multiplier \(1-hL<-1\), so \(p\) is unstable.

**Critical center mode and fifth-order invariant-graph calculation.** Near \(p\) write \(y=z-p\). Because the map is odd about \(p\),
\[
 y'=Ay+\frac{K(y^{\circ3})}{3L}-\frac{K(y^{\circ5})}{60L}+O(\|y\|^7).
\]
The one-dimensional simple center eigenspace is \(\mathbb Ru\), with eigenvalue \(-1\); the invariant complementary space is exponentially stable. Smooth center-manifold and strong-stable-foliation theory for maps gives an odd invariant center graph \(y=au+a^3w+O(a^5)\), with \(u^Tw=0\). Equating the transverse cubic terms gives
\[
 -(I+A)w=QK(u^{\circ3})/(3L),
\]
which is uniquely solvable on \(u^\perp\) since its eigenvalues for \(A\) lie strictly between \(-1\) and \(1\). Projecting the third- and fifth-degree terms onto \(u\) yields the center recurrence
\[
 a'=-a+ca^3+da^5+O(a^7)
\]
with exactly the coefficients specified above. The positive constant \(c\) gives local attraction on the center. For any nonzero center orbit put \(W_n=a_n^{-2}\). Direct inversion yields
\[
 W_{n+1}-W_n=2c+\frac{2d+3c^2}{W_n}+O(W_n^{-2}).
\]
First \(W_n/(2cn)\to1\); then subtracting \(2cn+b\log n\) leaves increments \(O((\log n)/n^2)\), which are absolutely summable, giving a finite constant \(H\). Each trajectory converging to \(p\) exponentially shadows a center-manifold trajectory; the unique strong-stable fiber shadowing the zero center trajectory is codimension one, and outside it the exponentially small shadowing error does not affect the reciprocal-square expansion. Analytic null-preimage reasoning makes this exception globally null.

**Exact four-vertex-path specialization.** In edge coordinates
\[
 K=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix},\quad
 L=2+\sqrt2,\quad u=\left(\frac12,\frac1{\sqrt2},\frac12\right)^T.
\]
Exact substitution into the displayed invariant-graph formulas gives \(c=1/8\), \(d=-(1+\sqrt2)/768\), and \(b=(17-\sqrt2)/96\), proving the example. The fully specified symbolic calculations are reproducible using `verify.py`.

## Verification

Run `python verify.py` with Python 3, SymPy and NumPy. It exactly reconstructs the spectral eigendata, checks the cubic and fifth-order center-graph invariance equations for the two-, three-, and four-vertex paths, and verifies all displayed rational/surd coefficients. It also iterates the nontrivial four-vertex-path example in double precision and checks stabilization of the predicted logarithmically corrected reciprocal quantity at several times. The analytic cosine inequality, compactness argument, stable-set geometry and infinite-time asymptotic law are proved above, not inferred from finite computation.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (2026), arXiv:2610.10993, formulate this discrete graph-phase system, prove strict potential descent and critical-point convergence for \(0<h<2/L\), and obtain diffeomorphism/Morse–Smale and almost-global statements on a smaller interval. Their strict-descent estimate has zero coefficient at \(h=2/L\); their theorem does not establish the endpoint attraction or the graph-dependent inverse-square and logarithmic law here. Earlier work by the same authors on three clocks treats small-step synchronization, not the largest-Laplacian-eigenmode flip at its global-descent endpoint. Schaeffer and McCalla (2019), arXiv:1908.01753, establish generic saddle avoidance for ordinary gradient descent under nondegeneracy assumptions with step size **strictly below** \(2/L\), rather than this endpoint global classification and fifth-order dynamics. The familiar scalar flip law is a one-edge special case, not the multidimensional four-vertex result.

## Limitations

The theorem needs an unweighted tree and standard sine interaction. It does not assert Morse–Smale dynamics at a noninvertible step, does not classify arbitrary cyclic graphs or unequal edge weights, and does not give a uniform numerical convergence time for all initial phases. The center-manifold asymptotic applies after entering a local neighborhood and excludes the codimension-one strong-stable set; the global convergence theorem itself has no such exclusion. A historical literature search is not a proof of priority; earlier unlocated endpoint treatments remain a residual risk.

## References

1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks* (first public version October 7, 2026), arXiv:2610.10993, https://arxiv.org/abs/2610.10993.
2. H. Schaeffer, S. G. McCalla, *Extending the step-size restriction for gradient descent to avoid strict saddle points* (2019), arXiv:1908.01753, https://arxiv.org/abs/1908.01753.
3. J. Buescu, E. D'Aniello, H. M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks* (2025), arXiv:2502.15371, https://arxiv.org/abs/2502.15371.
