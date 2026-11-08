# Mesoscopic spectral law and infinitely flat peak detachment for powers of Bergman shifts

## Finding
Let \(B=M_z\) be the weighted Bergman shift on \(A^2_\alpha(\mathbb D)\), \(\alpha>-1\). The positive self-commutator of its \(k\)-th power,
\[
D_k=B^{*k}B^k-B^kB^{*k},
\]
has a nontrivial **high-power spectral distribution** as \(k\to\infty\). The universal rescaled profile is the one-step difference of a Beta-type cumulative profile:
\[
\delta=\alpha+1,\quad F_\delta(t)=\begin{cases}0,&t\le0,\\(t/(1+t))^\delta,&t>0,\end{cases}\qquad h_\delta(t)=F_\delta(t)-F_\delta(t-1)\quad(t\ge0).
\]
For every real \(p>1/2\),
\[
\lim_{k\to\infty}\frac{\operatorname{Tr}(D_k^p)}k=\int_0^\infty h_\delta(t)^p\,dt,
\]
and for every real threshold \(s>0\),
\[
\lim_{k\to\infty}\frac1k\#\{n:s_n(D_k)>s\}=\operatorname{Leb}\{t\ge0:h_\delta(t)>s\}.
\]
Each monomial contributes one eigenvalue, with repeated values counted with multiplicity; \(s_n\) uses decreasing order and starts at one. In particular \(\lim_{k\to\infty}\|D_k\|=c_\delta:=\max_{t\ge0}h_\delta(t)\).

The maximum has an exact **parameter transition**. If \(0<\delta\le1\), it is unique at \(t=1\) and \(c_\delta=2^{-\delta}\). For \(\delta>1\) there is a unique \(t_\delta\in(1,\delta)\) with
\[
t_\delta^{2\delta}=(t_\delta-1)^{\delta-1}(t_\delta+1)^{\delta+1};
\]
this is the unique maximizer of \(h_\delta\). Every maximizing monomial index \(n_k\) satisfies \(n_k/k\to t_\delta\). The detachment at the classical Bergman value \(\alpha=0\) is infinitely flat: for \(\delta=1+\varepsilon\), \(\varepsilon\downarrow0\),
\[
t_\delta-1\sim\frac12\exp\!\left(-\frac{2\log2}{\varepsilon}\right),\qquad
c_\delta-2^{-\delta}\sim\frac{\varepsilon}{8}\exp\!\left(-\frac{2\log2}{\varepsilon}\right).
\]
The trace is exactly \(\operatorname{Tr}(D_k)=k\) for every \(k\). For the unweighted Bergman case \(\alpha=0\), \(\|D_k\|=1/2\) **for all** \(k\ge1\) and
\[
\lim_{k\to\infty}\frac{\|D_k\|_{\mathcal S_2}^2}k=3-4\log 2.
\]

## Assumptions and scope
Use normalized area \(dA/\pi\) and the standard Hilbert norm
\[
\|f\|_\alpha^2=(\alpha+1)\int_\mathbb D |f(z)|^2(1-|z|^2)^\alpha\frac{dA(z)}\pi.
\]
All limits \(k\to\infty\) hold with fixed \(\alpha>-1\). For \(0<p<1\), the Schatten quasi-norm power is defined by \(\operatorname{Tr}(D_k^p)=\sum_n d_{n,k}^p\). The operator is in \(\mathcal S_p\) for every \(p>1/2\), but is in no \(\mathcal S_p\) for \(0<p\le1/2\); the latter statement concerns fixed \(k\). Count all eigenvalues above \(s\), not just finitely many monomials.

## Proof
**1. Exact diagonal and trace.** The normalized monomial \(e_n=z^n/\|z^n\|_\alpha\) obeys
\[
B^ke_n=\sqrt{W_k(n)}e_{n+k},\qquad W_k(x)=\prod_{j=1}^k\frac{x+j}{x+j+\delta}.
\]
Consequently, for integers \(n\ge0\), \(D_ke_n=d_{n,k}e_n\), where
\[
d_{n,k}=W_k(n)-\mathbf1_{\{n\ge k\}}W_k(n-k).
\]
As \(W_k(x)\) is strictly increasing on \([0,\infty)\), all these eigenvalues are positive. Telescoping gives
\[
\sum_{n=0}^{N}d_{n,k}=\sum_{n=\max(0,N-k+1)}^{N}W_k(n).
\]
Because \(W_k(n)\to1\) as \(n\to\infty\), monotone convergence gives \(\operatorname{Tr}(D_k)=k\).

**2. Fixed-power tail and a uniform tail bound.** Extend \(W_k\) to real \(x\ge0\). Direct differentiation yields
\[
W_k'(x)=W_k(x)\sum_{j=1}^k\frac{\delta}{(x+j)(x+j+\delta)}.
\]
For fixed \(k\), this is \(\delta k x^{-2}(1+o(1))\) as \(x\to\infty\), so the mean value theorem gives \(d_{n,k}\sim\delta k^2n^{-2}\). This proves the fixed-power Schatten cutoff. Uniformly over \(n\ge2k\),
\[
0<d_{n,k}\le\frac{\delta k^2}{(n-k+1)^2}\le \frac{4\delta k^2}{n^2}.
\]
This bound supplies the integrable majorant for every \(p>1/2\).

**3. The mesoscopic limit.** Fix \(t>0\) and let \(n/k\to t\). Taking logarithms of the exact product gives
\[
\log W_k(n)=-\delta\sum_{j=1}^k\frac1{n+j}+O_\delta\!\left(\sum_{j=1}^k\frac1{(n+j)^2}\right)
\longrightarrow-\delta\log\frac{t+1}{t}.
\]
At \(t=0\), monotonicity and \(W_k(0)=\Gamma(1+\delta)\Gamma(k+1)/\Gamma(k+1+\delta)\to0\) give the same limiting continuous function \(F_\delta\). The monotonicity of \(W_k(n)\) and continuity of \(F_\delta\) make this convergence uniform when \(n/k\) lies in any bounded interval. Hence \(d_{n,k}-h_\delta(n/k)\to0\) uniformly on all such intervals.

The uniform tail estimate in step 2 then proves, by Riemann sums and tail domination,
\[
\frac1k\sum_{n=0}^\infty d_{n,k}^p\to\int_0^\infty h_\delta(t)^p\,dt\qquad(p>1/2).
\]
The function \(h_\delta\) is positive, continuous, tends to zero, and is strictly monotone on either side of its unique maximum (proved below); thus every positive level set has Lebesgue measure zero. Riemann-sum approximation of indicator functions, with the same uniform tail estimate, proves the eigenvalue counting limit. Uniform convergence on compact intervals and a vanishing supremum bound outside compact intervals prove the operator-norm limit and the convergence of every maximizing index.

**4. Exact peak and critical onset.** For \(0<t<1\), \(h_\delta(t)=\left(t/(t+1)\right)^\delta\) is strictly increasing. For \(t>1\), let \(A(t)=\left(t/(t+1)\right)^\delta\), \(G(t)=\left((t-1)/t\right)^\delta\). The derivative ratio is
\[
\frac{A'(t)}{G'(t)}=R_\delta(t):=\left(\frac{t^2}{t^2-1}\right)^\delta\frac{t-1}{t+1},\qquad
\frac{d}{dt}\log R_\delta(t)=\frac{2(t-\delta)}{t(t^2-1)}.
\]
For \(0<\delta\le1\), the ratio increases to \(1\) from below, and \(h_\delta\) strictly decreases for \(t>1\). For \(\delta>1\), the ratio starts at \(+\infty\), decreases through \(1\) once on \((1,\delta)\), and increases back towards \(1\) from below. This yields the claimed unique maximum and its critical parameter equation.

Write \(\delta=1+\varepsilon\), \(t_\delta=1+x_\varepsilon\). The critical equation is exactly
\[
x_\varepsilon^\varepsilon=\frac{(1+x_\varepsilon)^{2+2\varepsilon}}{(2+x_\varepsilon)^{2+\varepsilon}}.
\]
The unique maximum has \(x_\varepsilon\to0\), since for any fixed \(t>1\) the derivative ratio tends to \((t/(t+1))^2<1\). The logarithm of the exact equation first implies \(\varepsilon\log x_\varepsilon=-(2+\varepsilon)\log2+O(x_\varepsilon)\), uniformly as \(\varepsilon\to0\). For sufficiently small \(\varepsilon\), this yields \(x_\varepsilon\le2^{-1/\varepsilon}\), hence \(x_\varepsilon/\varepsilon\to0\). A second expansion then gives
\[
\log x_\varepsilon=-\frac{2\log2}{\varepsilon}-\log2+O(x_\varepsilon/\varepsilon),
\]
so \(x_\varepsilon\sim\frac12 4^{-1/\varepsilon}\). Uniform Taylor expansion near \(x=0\) gives
\[
h_{1+\varepsilon}(1+x)-2^{-(1+\varepsilon)}
=\frac{1+\varepsilon}{2^{2+\varepsilon}}x-x^{1+\varepsilon}+O(x^2).
\]
At \(x=x_\varepsilon\), the stationary equation gives \(x_\varepsilon^\varepsilon=2^{-(2+\varepsilon)}(1+O(x_\varepsilon))\). Thus the excess equals
\[
\frac{\varepsilon}{2^{2+\varepsilon}}x_\varepsilon+O(x_\varepsilon^2)
\sim\frac\varepsilon8 4^{-1/\varepsilon}.
\]
This exponential-in-inverse-parameter onset is smaller than every positive algebraic power of \(\varepsilon\).

**5. Classical Bergman checkpoint.** When \(\delta=1\), \(W_k(n)=(n+1)/(n+k+1)\). For \(0\le n<k\), \(d_{n,k}=(n+1)/(n+k+1)\), and for \(n\ge k\),
\[
d_{n,k}=\frac{k^2}{(n+1)(n+k+1)}.
\]
The maximum equals \(1/2\), attained at \(n=k-1\) (and nowhere else). Integration of the squared profile over \((0,1)\) and \((1,\infty)\), respectively, gives \(3/2-2\log2\) for each interval. Their sum proves the stated Hilbert–Schmidt coefficient.

## Verification
The accompanying standalone `check_bulk.py` uses only the Python standard library. It verifies exact rational positivity and telescoping for five integer weight parameters and ten powers over 42 monomial indices, checks the high-power maximum location/value for four real weight parameters and three powers, and tests fixed-power spectral tails. It reports `BERGMAN_HIGH_POWER_CHECK_OK 4245 checks`. No finite check is used as an infinite proof; the asymptotic and parameter-uniform statements above are analytic.

## Relationship to prior work
Xu and Yu (2026) classify the wandering-subspace property for powers of weighted Bergman shifts, motivating the study of high-power behavior of this natural operator family. Their accessible theorem statements concern invariant subspaces, not mesoscopic self-commutator eigenvalue distributions. Pushnitski (2017) proves fixed-operator spectral asymptotics for Bergman Toeplitz operators and banded matrices; such results provide context for the fixed-power \(n^{-2}\) tail but do not by themselves supply the simultaneous regime \(n\asymp k\to\infty\), the peak-location transition or its nonanalytic onset. The fixed-power tail and trace index are included as prerequisites rather than presented as independently novel. Distinct previously published stronger general principles may still exist; the priority assessment is provisional.

## Limitations
The large-power limits hold for fixed \(\alpha\), not uniformly as \(\alpha\to-1\) or \(\alpha\to\infty\). The exponentially small onset concerns the continuum profile and is not asserted to resolve a finite-\(k\) peak shift on the same exponentially small scale. Explicit power-law convergence rates in \(k\) are not established. A complete independent publication-priority audit has not been performed. Portions of the most directly related 2026 preprint beyond its introduction and theorem statements were not accessible for close comparison.

## References
1. Shibo Xu and Tao Yu, *The Beurling-type theorem for powers of weighted Bergman shifts*, arXiv:2610.37035, first submitted October 27, 2026. https://arxiv.org/abs/2610.37035
2. Alexander Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652 (2017), especially Section 1.2 and Theorem 1.2. https://arxiv.org/abs/1710.02652
