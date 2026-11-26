# A sharp compact-entropy dichotomy at Chebyshev order one in a reciprocal-sine plane map

## Finding
For every \(a>0\), every real \(b\ne0\), and every Chebyshev order \(0\le\nu\le4\), consider the Jiang--Jiang--Wang--Shu map
\[
 F_{\nu,a,b}(x,y)=\left(T_\nu(y)\sin\Phi(x),\;T_\nu(x)\sin\Phi(y)\right),\qquad
 T_\nu(t)=\cos(\nu\arccos t),\qquad
 \Phi(t)=\frac{a}{t(1-t)}+b.
\]
Its natural regular interior is \(D=((-1,1)\setminus\{0\})^2\). Define compact recurrent entropy by
\[
 h_{\rm comp}(F)=\sup\{h_{\rm top}(F|_K):\varnothing\ne K\subset D\text{ compact},\ F(K)=K\}.
\]
Then the *sharp dichotomy* is
\[
 \boxed{h_{\rm comp}(F_{\nu,a,b})=0\text{ if }\nu=1,\qquad h_{\rm comp}(F_{\nu,a,b})=+\infty\text{ if }\nu\ne1.}
\]
More precisely, at \(\nu=1\), every invariant Borel probability supported on any compact invariant \(K\subset D\) is a finite convex combination of periodic-orbit measures, and both Lyapunov exponents of each of those periodic orbits are zero. For every other \(\nu\), every integer \(N\ge2\), and every \(\Lambda>1\), there exists a compact invariant Cantor set \(\mathcal K_{N,\Lambda}\subset D\) on the diagonal, conjugate to the one-sided full shift on \(N\) symbols. At every point of this set, the two eigenvalues of the ambient planar Jacobian have modulus strictly greater than \(\Lambda\). Thus both invariant Lyapunov exponents on this Cantor set exceed \(\log\Lambda\).

## Assumptions and scope
The parameter \(\nu\) is a real number in the source's range \([0,4]\), not necessarily an integer; \(a>0\) and \(b\ne0\). The map may be undefined after trajectories hit a zero coordinate; all invariant sets in this theorem lie strictly inside \(D\) and never meet the singularity. The function \(T_\nu\) is defined by the displayed cosine formula on \([-1,1]\). The supremum \(h_{\rm comp}\) is explicitly *not* the topological entropy of a presumed continuous self-map on a compactification of the singular domain.

## Proof
**1. The neutral order has a multiplicative Lyapunov function.** At \(\nu=1\), \(T_1(t)=t\). Thus
\[
 F(x,y)=(y\sin\Phi(x),x\sin\Phi(y)),\qquad
 P(F(x,y))=P(x,y)|\sin\Phi(x)\sin\Phi(y)|\le P(x,y),\quad P=|xy|.
\]
Let \(K\subset D\) be any nonempty compact invariant set, and let \(\mu\) be any invariant probability on \(K\). Since \(P>0\) is continuous on \(K\), \(\log P\) is bounded. Invariance gives
\[
 0=\int_K(\log P\circ F-\log P)\,d\mu
 =\int_K\log|\sin\Phi(x)\sin\Phi(y)|\,d\mu.
\]
The integrand is continuous and nonpositive on \(K\) (neither sine can vanish because \(F(K)=K\subset D\)), so it must vanish \(\mu\)-almost surely. Hence both sine factors have absolute value one on the support of \(\mu\). On each compact coordinate projection of \(K\), which avoids \(0\) and \(1\), the equation \(|\sin\Phi(t)|=1\) has only finitely many roots: its phase is bounded and analytic and is not constant on any interval. Therefore \(\mu\) is supported on a finite set. Every invariant probability of a map supported on a finite set is a convex combination of measures on its periodic cycles. The variational principle for the continuous map \(F|_K:K\to K\) then gives \(h_{\rm top}(F|_K)=0\). Nonempty such sets exist: choose \(t\in(0,1)\) with \(\Phi(t)=\pi/2+2\pi m\), which yields the fixed point \((t,t)\).

At every periodic state, both sines have absolute value one and both cosine factors vanish. The planar Jacobian at order one therefore has the form
\[
 DF(x,y)=\begin{pmatrix}0&\pm1\\\pm1&0\end{pmatrix}.
\]
Every factor is orthogonal, so every periodic orbit has both Lyapunov exponents equal to zero.

**2. Diagonal reduction away from order one.** The diagonal \(x=y=t\) is invariant, with scalar map
\[
 f_\nu(t)=T_\nu(t)\sin\Phi(t).
\]
For \(\nu\notin\{1,3\}\) in \([0,4]\), \(T_\nu(0)=\cos(\nu\pi/2)\ne0\), so \(|T_\nu(t)|\ge c_\nu>0\) for all sufficiently small \(t>0\). At the remaining nonneutral odd order, \(\nu=3\),
\[
 T_3(t)=4t^3-3t,\qquad |T_3(t)|\ge(5/2)t
\]
for all sufficiently small \(t>0\). In both cases, for every sufficiently small \(\delta>0\) and every \(t\in I_\delta=[\delta,2\delta]\), we have \(|T_\nu(t)|>2\delta\), and \(T_\nu\) has constant nonzero sign on \(I_\delta\).

**3. Arbitrarily many full branches.** The phase \(\Phi(t)\) decreases strictly for \(0<t<1/2\), and
\[
 \Phi(\delta)-\Phi(2\delta)=\frac{a}{2\delta}+O(1)\to+\infty.
\]
In each complete \(2\pi\)-phase period strictly inside the range \(\Phi(I_\delta)\), take just one quarter-wave running from a sine zero to the adjacent sine extremum whose sign agrees with \(T_\nu\). In this orientation \(f_\nu\) starts at zero and ends above \(2\delta\). Take the first crossing of \(2\delta\) and the last crossing of \(\delta\) before it. On the resulting closed subinterval, continuity puts \(f_\nu(t)\) in \(I_\delta\). There are arbitrarily many pairwise disjoint such quarter-waves as \(\delta\downarrow0\).

On every such subinterval where \(f_\nu(t)\in I_\delta\),
\[
 |\sin\Phi(t)|\le\frac{2\delta}{|T_\nu(t)|}\le\rho_\nu<1,
\]
where \(\rho_\nu\) can be chosen independent of sufficiently small \(\delta\) (for \(\nu=3\), take \(\rho_3=4/5\)); hence \(|\cos\Phi(t)|\ge c_0>0\). Also
\[
 |\Phi'(t)|=\frac{a(1-2t)}{t^2(1-t)^2}\ge\frac{a}{8\delta^2}\quad(t\in I_\delta).
\]
Writing \(A(t)=T_\nu(t)\cos\Phi(t)\Phi'(t)\), \(B(t)=T_\nu'(t)\sin\Phi(t)\), we have
\[
 |A(t)|\ge C\delta^{-2}\ (\nu\ne1,3),\qquad
 |A(t)|\ge C\delta^{-1}\ (\nu=3),\qquad
 |B(t)|\le C'.
\]
Consequently \(|A(t)|-|B(t)|>\Lambda\) on the selected level-crossing intervals once \(\delta\) is small enough. On each such interval \(f_\nu'=A+B\) is nonzero and continuous, hence of constant sign. Each selected interval is therefore a closed branch \(J_j\subset\operatorname{int}I_\delta\) with \(f_\nu:J_j\to I_\delta\) bijective and \(|f_\nu'|>\Lambda\). Select any \(N\) pairwise disjoint branches. Their inverse functions are contractions of Lipschitz constant less than \(\Lambda^{-1}\); the standard nested inverse-branch construction produces a nonempty Cantor set \(K_N\subset I_\delta\), with \(f_\nu(K_N)=K_N\), on which \(f_\nu\) is conjugate to the one-sided full \(N\)-shift. (The branch intervals are separated by gaps, so the coding is one-to-one.) Therefore \(h_{\rm top}(f_\nu|_{K_N})=\log N\).

**4. Both ambient directions expand.** At every diagonal point \((t,t)\), the planar Jacobian is
\[
 DF(t,t)=\begin{pmatrix}A(t)&B(t)\\B(t)&A(t)\end{pmatrix}.
\]
The fixed orthogonal diagonal/antidiagonal basis diagonalizes this matrix with eigenvalues \(A+B\) and \(A-B\). On \(K_N\) both moduli have a common lower bound \(m>\Lambda\) by compactness. The logarithmic expansion rates on the two lines are time averages of the respective log moduli. These bounded observables have almost-sure time-average limits for every invariant probability by the pointwise ergodic theorem, and both limits are at least \(\log m>\log\Lambda\). The embedded planar set \(\mathcal K_{N,\Lambda}=\{(t,t):t\in K_N\}\) is compact and invariant. Since \(N\) is arbitrary, the compact recurrent entropy is infinite for all \(\nu\ne1\). This completes the proof.

## Verification
The conclusion follows from the exact product identity, the explicit exceptional Chebyshev values at zero, the divergent phase-window count, and the uniform Jacobian eigenvalue estimates. A separate Python diagnostic evaluates representative branch intervals at \(\nu=1.0001,1.5,2,3,3.5\) for \(a=20,b=2.5\). The finite diagnostic corroborates sample branch availability and expansion but is **not** used as proof of the uniform statement. Execute `python3 verify_example.py` with Python 3's standard library.

## Relationship to prior work
Jiang, Jiang, Wang, and Shu (2023), Equation (4), introduced this two-dimensional map and examined numerical Lyapunov exponents and encryption behavior, without giving an exact Chebyshev-order classification of entropy on compact invariant sets. Yan, Jiang, Huang, and Ding (2021) studied a different three-dimensional infinite-collapse map; its equations do not specialize to this order-one multiplicative product. The standard full-branch symbolic-coding argument is established general theory; the result asserted here is the model-specific exact dichotomy, including the sole neutral order and expansion of both ambient directions. The literature inspection does not prove worldwide novelty.

## Limitations
The entropy is the supremum over **compact invariant subsets contained in the nonsingular interior**, not a claim of a continuous compactification or an entropy formula for the full partially defined map. The arbitrarily large-entropy sets are repellers on the diagonal and may occupy zero area; nothing here establishes typical chaotic dynamics, physical invariant measures, security properties, or a large basin. The boundary \(\nu=1\) claim concerns compact invariant measures only, not transient orbits that approach the excluded singularities. Publicly indexed but undiscovered equivalent proofs remain a priority risk.

## References
1. X. Jiang, G. Jiang, Q. Wang, and D. Shu, *Image encryption algorithm based on 2D-CLICM chaotic system*, IET Image Processing 17 (2023), 2127--2141, first available online March 9, 2023, https://doi.org/10.1049/ipr2.12778.
2. W. Yan, Z. Jiang, X. Huang, and Q. Ding, *A Three-Dimensional Infinite Collapse Map with Image Encryption*, Entropy 23 (2021), 1221, https://doi.org/10.3390/e23091221.
3. E. de Faria, P. Hazard, and C. Tresser, *Genericity of Infinite Entropy for Maps with Low Regularity*, arXiv:1709.02431 (background on infinite entropy in non-Lipschitz dynamics; not a theorem about the present map).
