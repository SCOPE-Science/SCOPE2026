# Two distinct endpoint density layers as a critical cusp vanishes

## Finding
For the explicit expanding, symmetric square-root-cusp family of Oltiboev–Vafoyev, the unique invariant probability density has two *different* endpoint boundary layers when the cusp coefficient vanishes and the dynamics becomes the full tent map. The exact profiles, their joint scaling, and both endpoint-derivative constants are established below.

Write \(c=1/2\), \(K_\theta=(2-\theta)/(2\sqrt2)\), \(\lambda_\theta=(1+\theta/2)^{-1}\). As \(\theta\uparrow2\), the normalized invariant densities satisfy \(h_\theta\to1\) in \(L^1(0,1)\) and locally uniformly in \((0,1)\). For every \(s\ge0\), with convergence uniform over bounded nonnegative \(s\)-intervals,
\[
\lim_{\theta\uparrow2}h_\theta\left(1-\frac{K_\theta^2}{\theta}s\right)=G(s):=1-\frac1{\sqrt{1+s}},
\]
\[
\lim_{\theta\uparrow2}h_\theta\left(\frac{K_\theta^2}{\theta}s\right)=H(s):=\sum_{j=1}^\infty 2^{-j}\left(1-\frac1{\sqrt{1+s/2^j}}\right).
\]
Both profiles grow from zero to one, but \(G'(0)=1/2\), while \(H'(0)=1/6\). The exact endpoint-slope formulas imply
\[
\lim_{\theta\uparrow2}(2-\theta)^2h'_\theta(1)=-8,\qquad
\lim_{\theta\uparrow2}(2-\theta)^2h'_\theta(0)=\frac83.
\]
Although \(h_\theta\to1\) in \(L^1\), the convergence fails in \(W^{1,1}\); furthermore, \(\|h_\theta\|_{W^{2,1}}\to\infty\).

## Assumptions and scope
Fix any real \(1<\theta<2\). Define \(f_\theta:[0,1]\to[0,1]\) by
\[
f_\theta(c\pm t)=1-\theta t-2K_\theta\sqrt t,\qquad 0\le t\le\tfrac12,
\quad K_\theta=\frac{2-\theta}{2\sqrt2}.
\]
Every branch covers \([0,1]\), with \(f_\theta(0)=f_\theta(1)=0\) and \(f_\theta(c)=1\). The normalized invariant density \(h_\theta\) is the unique nonnegative fixed point of the Perron–Frobenius operator with integral one. Its existence, uniqueness, and \(W^{2,1}\) regularity for each \(\theta<2\) are established in [1, Proposition 4.2]. The statement considers the one-sided limit \(\theta\uparrow2\), *not* the analytic perturbation in Bernoulli mixing probabilities studied in [1]. At \(\theta=2\), the limit map is the full tent map, whose normalized invariant density is one.

## Proof
**Step 1: explicit transfer operator.** For \(x\in[0,1]\), put
\[
u_\theta(x)=\frac{\sqrt{K_\theta^2+\theta(1-x)}-K_\theta}{\theta},\quad
g_{0,\theta}(x)=c-u_\theta(x)^2,\quad g_{1,\theta}(x)=c+u_\theta(x)^2.
\]
The weight is
\[
w_\theta(x)=\frac{u_\theta(x)}{K_\theta+\theta u_\theta(x)}
=\frac1\theta\left(1-\frac{K_\theta}{\sqrt{K_\theta^2+\theta(1-x)}}\right),
\quad (L_\theta\phi)(x)=w_\theta(x)\bigl[\phi(g_{0,\theta}(x))+\phi(g_{1,\theta}(x))\bigr].
\]
These are [1, equations (3.3)–(3.4)]. The continuous weight decreases from \(w_\theta(0)=\lambda_\theta\) to \(w_\theta(1)=0\), and each inverse branch is Lipschitz with constant \(\lambda_\theta\).

**Step 2: a uniform bound in bounded variation.** Restrict \(\theta\) to a sufficiently small left neighborhood of 2. For the four inverse branches \(g_{j,\theta}\circ g_{i,\theta}\) of \(L_\theta^2\), the weights are \(v_{ij}(x)=w_\theta(x)w_\theta(g_{i,\theta}(x))\). Since \(w_\theta\) is monotone, \(\sup v_{ij}\le\lambda_\theta^2\) and \(\operatorname{Var}(v_{ij})\le2\lambda_\theta^2\). The four inverse-branch image intervals partition \([0,1]\) (up to endpoints) and approach the four dyadic quarters. Hence all their lengths are at least \(1/8\) near 2. By the product variation inequality and \(\sup_J|\phi|\le\operatorname{Var}_J\phi+|J|^{-1}\int_J|\phi|\),
\[
\operatorname{Var}(L_\theta^2\phi)
\le3\lambda_\theta^2\operatorname{Var}(\phi)
+16\lambda_\theta^2\|\phi\|_1.
\]
Here variation of the sum is bounded by the sum of variations, and the image intervals are disjoint, so their variation and integral contributions sum without multiplicity. Invariance and \(\|h_\theta\|_1=1\) give
\[
\operatorname{Var}(h_\theta)\le\frac{16\lambda_\theta^2}{1-3\lambda_\theta^2}
\]
whenever \(3\lambda_\theta^2<1\). This holds for every \(\theta\) sufficiently close to 2 because \(\lambda_\theta\to1/2\). Thus \(\|h_\theta\|_\infty\le1+\operatorname{Var}(h_\theta)\le M\) uniformly.

**Step 3: local uniform convergence.** At \(\theta=2\), every inverse branch of \(L_2^n\) has constant weight \(2^{-n}\) and images exactly the \(2^n\) dyadic intervals. For any \(\phi\in BV\), selecting one arbitrary point from each such interval yields a quadrature approximation to \(\int_0^1\phi\) with error at most \(2^{-n}\operatorname{Var}(\phi)\). For fixed \(n\) and fixed compact \(J\subset(0,1)\), the branch weights of \(L_\theta^n\) converge uniformly on \(J\) to \(2^{-n}\); their sample points converge uniformly to the dyadic sample points. For \(\theta\) close enough to 2, both sample points belong to the same dyadic cell, and the displacement segments in different cells are disjoint. Therefore their total sampling error, after multiplying by \(2^{-n}\), is at most \(2^{-n}\operatorname{Var}(h_\theta)\). Since \(L_\theta^n h_\theta=h_\theta\),
\[
\limsup_{\theta\uparrow2}\sup_{x\in J}|h_\theta(x)-1|\le2^{1-n}M.
\]
Let \(n\to\infty\). Uniform \(L^\infty\) bounds and the small measure of the two endpoint intervals also give \(\|h_\theta-1\|_1\to0\).

**Step 4: exact right-end layer.** Set \(x=1-K_\theta^2s/\theta\) with \(s\) in a fixed compact subset of \([0,\infty)\). Direct substitution yields
\[
w_\theta(x)=\frac1\theta\left(1-\frac1{\sqrt{1+s}}\right),\qquad
g_{0,\theta}(x),g_{1,\theta}(x)\to c
\]
uniformly. By Step 3 the two density values in the transfer equation converge to one. Hence the right-end profile is \(G(s)=1-(1+s)^{-1/2}\), uniformly for bounded \(s\).

**Step 5: cascading left-end layer.** Define \(H_\theta(s)=h_\theta(K_\theta^2s/\theta)\) and \(G_\theta(s)=h_\theta(1-K_\theta^2s/\theta)\), on the ranges where their arguments lie in \([0,1]\). Write
\[
T_\theta(s)=\frac{\theta}{K_\theta^2}g_{0,\theta}(K_\theta^2s/\theta),\qquad
q_\theta(s)=w_\theta(K_\theta^2s/\theta).
\]
Since \(g_{1,\theta}=1-g_{0,\theta}\), the fixed-point equation gives the exact recursion
\[
H_\theta(s)=q_\theta(s)\bigl[H_\theta(T_\theta(s))+G_\theta(T_\theta(s))\bigr].
\]
As \(\theta\uparrow2\), \(q_\theta(s)\to1/2\) and \(T_\theta(s)\to s/2\) uniformly on compact intervals. Moreover, \(0\le q_\theta\le\lambda_\theta\le q<1\) and \(0\le T_\theta(s)\le\lambda_\theta s\), because \(g_{0,\theta}(0)=0\) and \(g'_{0,\theta}=w_\theta\). Iterate the recursion \(n\) times. The remainder is at most \(Mq^n\), uniformly for bounded \(s\), while the finite sum tends uniformly to \(\sum_{j=1}^n2^{-j}G(s/2^j)\), by Step 4. Sending \(n\to\infty\) yields the stated \(H\). The series converges uniformly on all compact \(s\)-intervals. Differentiating its absolutely convergent derivative series at zero gives \(H'(0)=\sum_{j\ge1}2^{-2j-1}=1/6\), whereas \(G'(0)=1/2\).

**Step 6: endpoint derivatives and Sobolev boundary.** The function \(h_\theta\) is \(C^1\), since it belongs to \(W^{2,1}\). At \(x=1\), the transfer weight vanishes and \(w'_{\theta}(1)=-1/(2K_\theta^2)\); both inverse branches approach \(c\). Hence
\[
h_\theta(1)=0,\qquad h'_\theta(1)=-\frac{h_\theta(c)}{K_\theta^2}.
\]
At \(x=0\), \(g_0(0)=0\), \(g_1(0)=1\), \(w_\theta(0)=\lambda_\theta<1\), so invariance implies \(h_\theta(0)=\lambda_\theta(h_\theta(0)+h_\theta(1))=0\). Differentiating there, with \(g'_0(0)=\lambda_\theta\) and \(g'_1(0)=-\lambda_\theta\), gives
\[
h'_\theta(0)=\lambda_\theta^2[h'_\theta(0)-h'_\theta(1)],\quad
h'_\theta(0)=-\frac{\lambda_\theta^2}{1-\lambda_\theta^2}h'_\theta(1).
\]
Since Step 3 gives \(h_\theta(c)\to1\) and \(K_\theta^2=(2-\theta)^2/8\), the two derivative constants follow. The trace inequality \(|u(1)|\le\|u\|_1+\|u'\|_1\) applied to \(u=h_\theta-1\) proves \(\|h_\theta-1\|_{W^{1,1}}\ge1\). Applied to \(u=h'_\theta\), it gives \(\|h_\theta\|_{W^{2,1}}\ge|h'_\theta(1)|\to\infty\). This completes the proof.

## Verification
Run `python verify.py` with Python 3 and NumPy installed. The program checks 845 algebraic and profile identities and approximates the invariant densities on two dense grids, confirming the two distinct rescaled profiles. Its finite-grid checks are diagnostics; the all-parameter assertions follow from the analytic proof above. Reproduction output: `GRID 1.9 iterations 43 L1 0.051577825357532595 max_err 0.07800221530033014`; `GRID 1.98 iterations 42 L1 0.011555144439164633 max_err 0.014704417626009714`; `VERIFY_OK algebra_and_series_checks= 845 grid_thetas=2`.

## Relationship to prior work
Oltiboev and Vafoyev [1], equations (3.1)–(3.4) and Proposition 4.2, establish the exact map, transfer operator, and existence of \(W^{2,1}\) densities for each *fixed* \(\theta<2\). Their Theorem 6.1 concerns analyticity in Bernoulli mixture probabilities between two fixed maps. It neither states nor implies the singular deterministic limit \(\theta\uparrow2\), the unequal endpoint profiles, or the optimal endpoint derivative constants. The related random-system study [2] assumes the strict cusp exponent range \(-1<\beta<-1/2\) and varies probabilities; it does not cover the critical exponent together with its disappearing coefficient. Bahsoun–Galatolo [3] studies linear response under perturbations of a cusp map with exponent \(-1<\beta<-3/4\), not cusp-to-tent degeneration. General statistical stability principles do not compute these profiles or the singular endpoint traces. This is a priority assessment for the inspected sources, not a claim of exhaustive historical novelty.

## Limitations
The result applies only to the specific symmetric, full-branch critical square-root family, and only to the one-sided endpoint \(\theta\uparrow2\). It neither provides a first-order global \(L^1\) expansion nor proves analogous profiles for general asymmetric cusp maps, random mixtures, or exponents other than \(-1/2\). The uniform layer assertions concern bounded values of the *rescaled* coordinate, not simultaneous \(s\to\infty\). Numerical transfer iterations are corroboration, not a substitute for the proof. A specialized earlier profile calculation could still affect historical priority.

## References
[1] D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (first public 2026-10-16), https://arxiv.org/pdf/2610.23180.

[2] D. Oltiboev, K. Rakhimov, M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (2026), https://arxiv.org/abs/2608.26969.

[3] W. Bahsoun and S. Galatolo, *Linear response due to singularities*, Nonlinearity 37 (2024), 075010, arXiv:2301.02301v3, https://arxiv.org/pdf/2301.02301.
