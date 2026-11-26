# Six-residue finite-size oscillations for signed-prism Schur norms

## Finding

For every integer \(m\ge3\), let \(P_m=C_m\square K_2\) be the undirected prism graph, with \(2m\) vertices. Its adjacency matrix is \(A_m\), and \(J\) is the all-ones matrix of the same size. Form the real sign matrix \(M_m=J-2A_m\), so entries on graph edges are \(-1\) and all other entries are \(+1\). Define its (real or complex) spectral-operator Schur-multiplier norm by
\[
 s_m=\sup_{B\ne0}\frac{\|M_m\circ B\|_{\mathrm{op}}}{\|B\|_{\mathrm{op}}}.
\]
The supremum may be taken either over real matrices or over complex matrices, with the same result. Put \(n=m/\gcd(m,2)\), \(q=\lfloor n/3\rfloor\). Then
\[
\boxed{\displaystyle s_m=3-\frac6m-\frac{2(2q+1)}n+\frac4n\frac{\sin((2q+1)\pi/(2n))}{\sin(\pi/(2n))}.}
\]
In particular, with \(L=5/3+4\sqrt3/\pi\),
\[
\boxed{\displaystyle s_m=L-\frac6m+\frac{C_{m\bmod6}}{m^2}+O(m^{-3}),}
\]
where the six residue coefficients are
\[
 C_0=-\frac{4\pi\sqrt3}{3},\quad C_1=C_5=\frac{\pi\sqrt3}{9},\quad C_2=C_4=\frac{4\pi\sqrt3}{9},\quad C_3=-\frac{\pi\sqrt3}{3}.
\]
Consequently, the norms are **not eventually monotone**: \(s_{6k}<s_{6k-1}\) for all sufficiently large positive integers \(k\). Already \(s_5=(9+2\sqrt5)/5> s_6=8/3\). These assertions hold uniformly over the choice of labeling of \(P_m\).

## Assumptions and scope

The cycle \(C_m\) is simple and has unit edges; for \(m=3\) it is a triangle. Graph indices are \((i,a)\) with \(i\in\mathbb Z/m\mathbb Z\) and \(a\in\{0,1\}\). Adjacent pairs satisfy either \(a=b\) and \(i-j\equiv\pm1\pmod m\), or \(a\ne b\) and \(i=j\). The spectral operator norm is that induced by the Euclidean norm on \(\mathbb R^{2m}\) or the Hermitian norm on \(\mathbb C^{2m}\); \(\circ\) is entrywise multiplication. The asymptotic error is absolute as \(m\to\infty\) through all integers. No monotonicity assertion is made at every consecutive pair.

## Proof

**1. Schur norm reduction.** For any real symmetric vertex-transitive \(N\)-by-\(N\) matrix \(T\), set \(H=|T|=(T^2)^{1/2}\), and extend the spectral sign of \(T\) on its zero eigenspace to \(+1\). The resulting real symmetric orthogonal matrix \(U\) satisfies \(T=UH\) and \(U^2=I\). Vertex transitivity makes every diagonal entry of \(H\) equal to \(\tau=\operatorname{Tr}(H)/N\). If \(x_i=H^{1/2}e_i\) and \(y_j=H^{1/2}Ue_j\), then \(T_{ij}=\langle x_i,y_j\rangle\), and \(\|x_i\|=\|y_j\|=\sqrt\tau\). The elementary Schur factorization \(T\circ B=V^*(B\otimes I)W\), obtained by applying these vectors at their respective row and column coordinates, gives \(\|T\|_{\mathrm S}\le\tau\) over real and complex matrices. Conversely, the real orthogonal test matrix \(U\) and normalized all-ones vector \(\mathbf1/\sqrt N\) give
\[
 \|T\circ U\|_{\mathrm{op}}\ge\frac1N\sum_{i,j}T_{ij}U_{ij}
 =\frac1N\operatorname{Tr}(TU)=\frac1N\operatorname{Tr}(H)=\tau.
\]
Thus \(\|T\|_{\mathrm S}=N^{-1}\operatorname{Tr}|T|\). This is a special case of the previously established symmetry/Mathias principle, not claimed as a new general lemma. In the present setting it proves that a real orthogonal test matrix attains the norm, even in the complex optimization.

**2. Full spectrum.** Since \(M_m=J-2A_m\), the cycle Fourier vectors \(e^{2\pi\mathrm{i}ki/m}\) times the two fiber characters \((-1)^{ta}\), indexed by \(0\le k<m\), \(t\in\{0,1\}\), diagonalize \(M_m\). Their eigenvalues are
\[
 \mu_{0,0}=2m-6,\qquad \mu_{k,t}=-2\bigl(2\cos(2\pi k/m)+(-1)^t\bigr)\quad((k,t)\ne(0,0)).
\]
(The eigenvalue at \((0,1)\) is \(-2\).) With \(h(\theta)=\max\{1,2|\cos\theta|\}\), the identity \(|z+1|+|z-1|=2\max\{1,|z|\}\) for real \(z\) yields
\[
 \boxed{\displaystyle s_m=1-\frac6m+\frac2m\sum_{k=0}^{m-1}h(2\pi k/m).}\tag{1}
\]
For \(m=3\), \(2m-6=0\) and the same calculation remains valid.

**3. Exact finite trigonometric sum.** Because \(h\) has period \(\pi\), reducing the sampling grid gives
\[
 \frac1m\sum_{k=0}^{m-1}h(2\pi k/m)
 =\frac1n\sum_{j=0}^{n-1}h(\pi j/n),\qquad n=\frac{m}{\gcd(m,2)}.
\]
For \(0\le j<n\), \(h(\pi j/n)=2|\cos(\pi j/n)|\) on \(j=0,\ldots,q\) and \(j=n-q,\ldots,n-1\), and equals \(1\) at all other indices; equality at cutoff points causes no ambiguity. Here \(q=\lfloor n/3\rfloor\). Pairing the two endpoint arcs and using the Dirichlet identity
\[
 1+2\sum_{j=1}^q\cos(jx)=\frac{\sin((q+1/2)x)}{\sin(x/2)}
\]
gives
\[
 \frac1n\sum_{j=0}^{n-1}h(\pi j/n)
 =1-\frac{2q+1}{n}+\frac2n\frac{\sin((2q+1)\pi/(2n))}{\sin(\pi/(2n))}.
\]
Substitution into (1) proves the exact expression, including all small values \(m\ge3\).

**4. Six-residue boundary layer.** Write \(r=n\bmod3\in\{0,1,2\}\), \(\delta=1-2r/3\), and \(h_0=\pi/(2n)\). Then
\[
 (2q+1)h_0=\frac\pi3+\delta h_0,\qquad\delta\in\{1,1/3,-1/3\}.
\]
The uniform Taylor expansion for this three-element set is
\[
 \frac{\sin(\pi/3+\delta h_0)}{\sin h_0}
 =\frac{\sqrt3}{2h_0}+\frac\delta2
 +\sqrt3 h_0\left(\frac1{12}-\frac{\delta^2}{4}\right)+O(h_0^2).
\]
In the exact expression the terms proportional to \(\delta/n\) cancel. Therefore
\[
 s_m=\frac53+\frac{4\sqrt3}{\pi}-\frac6m
 +\frac{\pi\sqrt3}{n^2}\left(\frac16-\frac{\delta^2}{2}\right)+O(n^{-3}).
\]
For odd \(m\), \(n=m\); for even \(m\), \(n=m/2\). Sorting by \(m\bmod6\) yields precisely the six listed coefficients. In particular,
\[
 s_{6k}-s_{6k-1}=
 \frac{6-13\pi\sqrt3/9}{(6k)^2}+O(k^{-3}),
\]
whose leading coefficient is strictly negative. This proves infinitely many strict adjacent decreases. The exact values at \(m=5,6\) follow directly from the finite formula.

## Verification

The accompanying `verify.py` uses only the Python standard library. It constructs each \(2m\)-by-\(2m\) sign matrix and an independently Fourier-synthesized real orthogonal witness for \(3\le m\le20\). It checks orthogonality, the witness Rayleigh value, the exact sampled-cosine formula, and the closed sine expression. It separately checks six asymptotic residue classes at larger mesh sizes. Its output is a finite numerical cross-check, not a substitute for the proofs in Sections 1–4.

## Relationship to prior work

Davidson and Donsig, *Norms of Schur Multipliers* (arXiv:math/0506073, Section 4, Theorem 4.4), already establish the invariant-matrix trace-norm principle used in Step 1, with examples such as Kneser graphs. Holbrook, Johnston, and Schoch, *Real Schur norms and Hadamard matrices* (arXiv:2206.02863, Sections 2–3 and 6.2), study sign matrices, real orthogonal witnesses, and exact circulant Schur norms. Those general methods and the prism graph's elementary Fourier diagonalization are established tools, not new here. The finding assessed is the complete signed-prism norm expression together with its explicit six-residue \(m^{-2}\) coefficient, infinite nonmonotonicity, and the corresponding finite-size arithmetic mechanism. Prior three-frequency cyclic Fourier-projection formulas have a related continuous limit but a different finite sampled absolute-value expression; they do not directly state the signed-prism six-residue law.

## Limitations

The result concerns exactly the signed adjacency-mask Schur norm of unweighted prism graphs, not arbitrary signings, general cubic graphs, or all dihedral Cayley generating sets. The asymptotic does not assert exact monotonicity signs for every finite \(m\). The symmetry reduction is classical, and novelty is asserted only for the explicit finite-size law after comparisons with accessible sources; an equivalent historical result under spectral-energy or association-scheme terminology remains possible. No independent mathematical audit has occurred.

## References

1. K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073 (first public version June 3, 2005), Section 4 and Theorem 4.4. https://arxiv.org/abs/math/0506073
2. J. Holbrook, N. Johnston, and J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863 (first public version June 6, 2022), Sections 2, 3, 6.2. https://arxiv.org/abs/2206.02863
