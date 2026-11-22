# A sharp logarithmic norm gap for compact generalized Cesàro operators

## Finding
For \(0<t<1\), define \(C_t:\ell^2(\mathbb N_0)\to\ell^2(\mathbb N_0)\) by
\[
(C_t x)_n=\frac1{n+1}\sum_{j=0}^n t^{n-j}x_j.
\]
Then \(C_t\) is compact and \(\|C_t\|\uparrow2\) as \(t\uparrow1\), with the **sharp norm-gap law**
\[
\boxed{\displaystyle\lim_{t\uparrow1}\log^2\!\frac1{1-t}\,(2-\|C_t\|)=4\pi^2.}
\]
Equivalently, \(\|C_t\|^{-2}=1/4+(\pi^2+o(1))/\log^2(1/(1-t))\). The logarithm here is natural.

## Assumptions and scope
The Hilbert space is the unweighted complex sequence space \(\ell^2(\mathbb N_0)\), indexed from zero. The parameter approaches one through real values strictly below one. The theorem concerns the operator norm (largest singular value), not the eigenvalue radius, and does not assert a uniform fixed-parameter singular-value Weyl law. We use \(v_{-1}=0\) throughout, and finite sequences as a quadratic-form core.

## Proof
**1. An exact inverse-variational problem.** Write \(D=\operatorname{diag}((n+1)^{-1})\) and let \(S\) denote the forward unilateral shift. The identity \(C_t=D(I-tS)^{-1}\) implies compactness. Its densely defined inverse is \(B_t=(I-tS)D^{-1}\) on the domain of \(D^{-1}\). Its finite sequences form a form core. With \(v_n=(n+1)u_n\), the reciprocal squared norm is
\[
E(t):=\|C_t\|^{-2}=\inf_{0\ne v\in c_{00}}
\frac{\sum_{n\ge0}|v_n-tv_{n-1}|^2}{\sum_{n\ge0}|v_n|^2/(n+1)^2}.
\]
Both sums are finite (including the final zero-tail difference term). The identity
\[
\sum|v_n-tv_{n-1}|^2=t\sum|v_n-v_{n-1}|^2+(1-t)^2\sum|v_n|^2
\]
is exact. Put \(\epsilon=(1-t)/\sqrt t\), \(L=\log(1/\epsilon)\) and
\[
F(\epsilon)=\inf_{0\ne v\in c_{00}}
\frac{\sum|v_n-v_{n-1}|^2+\epsilon^2\sum|v_n|^2}
{\sum|v_n|^2/(n+1)^2}.
\]
Then \(E(t)=tF(\epsilon)\). We prove \(L^2(F(\epsilon)-1/4)\to\pi^2\).

**2. Exact discrete Hardy ground-state identity.** Set \(v_n=\sqrt{n+1}\,f_n\) and \(c_n=\sqrt{n(n+1)}\) for \(n\ge1\). Summation by parts, initially for finitely supported sequences, gives
\[
\sum|v_n-v_{n-1}|^2-\tfrac14\sum\frac{|v_n|^2}{(n+1)^2}
=\sum_{n\ge1}c_n|f_n-f_{n-1}|^2
+\sum_{n\ge0}(n+1)r_n|f_n|^2,
\]
where \(r_0=7/4-\sqrt2>0\) and for \(n\ge1\), writing \(h=(n+1)^{-1}\),
\[
r_n=2-\sqrt{1-h}-\sqrt{1+h}-\frac{h^2}{4}\ge0.
\]
The inequality follows by the even Taylor series of the two square roots: \(2-\sqrt{1-h}-\sqrt{1+h}=h^2/4+5h^4/64+\cdots\). Also \(r_n=O((n+1)^{-4})\). Thus if \(d_n=(n+1)^{-1}\), the gap \(F(\epsilon)-1/4\) is exactly the infimum of
\[
\frac{\sum_{n\ge1}c_n|\nabla f_n|^2+\sum_{n\ge0}(n+1)r_n|f_n|^2+\epsilon^2\sum_{n\ge0}(n+1)|f_n|^2}
{\sum_{n\ge0}d_n|f_n|^2}.
\]
All three numerator terms are nonnegative; the first is a logarithmic-coordinate Dirichlet energy, the second fixes the left boundary, and the third makes a right wall near \(n\asymp\epsilon^{-1}\).

**3. Upper bound.** Let \(a=L-\sqrt L\). Choose the finitely supported sequence
\[
f_n=\begin{cases}\sin(\pi\log(n+1)/a),&\log(n+1)\le a,\\0,&\log(n+1)>a.\end{cases}
\]
Direct sum-to-integral estimates using \(c_n\log((n+1)/n)=1+O(n^{-2})\) give
\[
\sum d_n|f_n|^2=a/2+O(1),\quad
\sum c_n|\nabla f_n|^2=\pi^2/(2a)+O(a^{-2}),\quad
\sum(n+1)r_n|f_n|^2=O(a^{-2}).
\]
Finally \(\epsilon^2\sum(n+1)|f_n|^2\le\epsilon^2e^{2a}\sum d_n|f_n|^2\le e^{-2\sqrt L}O(L)\). Hence \(\limsup_{\epsilon\downarrow0}L^2(F(\epsilon)-1/4)\le\pi^2\).

**4. Lower bound and control of the two boundaries.** Choose finite sequences nearly minimizing the gap, with denominator normalized to \(\sum d_n|f_n|^2=L\). By the upper bound, their total excess numerator is at most \((\pi^2+o(1))/L\). Consequently
\[
\sum c_n|\nabla f_n|^2=O(L^{-1}),\quad
f_0=O(L^{-1/2}),\quad
\epsilon^2\sum(n+1)|f_n|^2=O(L^{-1}).
\]
Define logarithmic mesh points \(x_n=\log(n+1)/L\) and let \(G_L\) be the piecewise-linear interpolation of \(f_n\) in the variable \(x\). On every fixed compact interval of \([0,\infty)\), the interpolation has uniformly bounded \(H^1\) seminorm, because
\[
\int_{x_{n-1}}^{x_n}|G_L'|^2dx
=\frac{L}{\log((n+1)/n)}|f_n-f_{n-1}|^2,
\qquad c_n\log((n+1)/n)\longrightarrow1.
\]
The finitely many low-index mesh edges are controlled by the positive left-boundary term; by Cauchy–Schwarz,
\[
|f_n-f_0|^2\le\left(\sum_{j=1}^n c_j^{-1}\right)
\left(\sum_{j=1}^n c_j|f_j-f_{j-1}|^2\right)
\le O(L^{-1})\bigl(1+\log(n+1)\bigr).
\]
Thus the interpolation is uniformly bounded on compact \(x\)-intervals, and any subsequential locally uniform limit \(G\) satisfies \(G(0)=0\). By the logarithmic Riemann-sum comparison and the preceding bound near \(x=0\),
\[
L^{-1}\sum d_n|f_n|^2-\int_0^R |G_L(x)|^2dx\longrightarrow0
\]
for each fixed \(R\) once the tails outside \([0,R]\) are treated separately. Indeed for every \(\delta>0\), the mass at indices \(n+1\ge e^{(1+\delta)L}\) is at most
\[
\sum_{n+1\ge e^{(1+\delta)L}}d_n|f_n|^2
\le e^{-2\delta L}\epsilon^2\sum(n+1)|f_n|^2=O(e^{-2\delta L}/L).
\]
It follows that \(G(x)=0\) for every \(x>1\). Local compactness, normalization of the discrete mass, and the negligible tails give \(\int_0^1|G|^2dx=1\); in particular \(G\in H_0^1(0,1)\).

For each \(\delta>0\), the exact energy/interpolation identity above and \(c_n\log((n+1)/n)\to1\) imply
\[
\liminf_{L\to\infty} L\sum c_n|\nabla f_n|^2
\ge\int_\delta^{1+\delta}|G'(x)|^2dx.
\]
Letting \(\delta\downarrow0\), and invoking the sharp Dirichlet Poincaré inequality on \((0,1)\), gives
\[
\liminf_{\epsilon\downarrow0}L^2(F(\epsilon)-1/4)
\ge\int_0^1|G'|^2dx\ge\pi^2.
\]
This matches Step 3. The argument also covers complex sequences by using absolute values and the complex Hilbert-space Poincaré inequality. The discrete-to-continuum estimates are proved in the text and do not rely on numerical experiments.

**5. Return to the operator norm.** Since \(E(t)=tF((1-t)/\sqrt t)\), since \(1-t=o(\log^{-2}(1/(1-t)))\), and since \(L=\log(1/(1-t))+o(1)\),
\[
E(t)=\frac14+\frac{\pi^2+o(1)}{\log^2(1/(1-t))}.
\]
Expanding \(E^{-1/2}\) at \(1/4\) (derivative \(-4\)) proves the boxed result.

## Verification
The algebraic identity for the inverse form and the discrete ground-state identity are independently replayable using the accompanying `check.py`. Numerical finite sections only supplement, and do not certify, the logarithmic limit. The proof uses a matching variational construction and compactness/liminf comparison rather than extrapolation of finite-size data.

## Relationship to prior work
Curbera–Ricker (2023), Sections 1 and 3, introduces the same matrices and their compactness and spectral behavior. Albanese–Bonet–Ricker (2023), Proposition 2.12, supplies general \(\ell^p\) bounds while Proposition 2.13 gives \(\|C_1\|_{\ell^2}=2\). Their assertions do not quantify the *approach* of the Hilbert-space norm to two. The present claim identifies the sharp logarithmic endpoint coefficient, using a discrete Hardy ground-state transformation rather than fixed-parameter spectral compactness. Other related results concern Hardy-space operator norms and fixed-parameter singular-value distributions, neither of which by itself implies this singular joint limit.

## Limitations
The theorem is restricted to the exact unweighted \(\ell^2\) model and the real limit \(t\uparrow1\). It does not prove a higher-order correction, an explicit finite-\(t\) closed form, or analogous constants for general Banach \(\ell^p\) spaces. The priority assessment is based on the inspected accessible primary texts and semantic search, not exhaustive historical verification.

## References
1. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices*, arXiv:2302.08750 (first arXiv submission 17 February 2023), https://arxiv.org/abs/2302.08750.
2. A. A. Albanese, J. Bonet, and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805 (2023), https://arxiv.org/abs/2305.04805.
3. A. A. Albanese, J. Bonet, and W. J. Ricker, *Generalized Cesàro operators in the disc algebra and in Hardy spaces*, *Advances in Operator Theory* (first online 22 October 2024), https://doi.org/10.1007/s43036-024-00396-9.
