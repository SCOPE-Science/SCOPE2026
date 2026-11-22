# Linear detuning law at integer resonances of quintic Hausdorff moments

## Finding
For each integer \(m\ge 2\), there is an explicit finite positive number \(\kappa_m\) such that the critical separation between the real pole and the two complex-pole pairs in a quintic reciprocal Hausdorff-moment problem obeys
\[
\Delta(m+\varepsilon)=\kappa_m|\varepsilon|+o(|\varepsilon|)\qquad(\varepsilon\to0).
\]
Here \(\Delta(r)\) is the smallest nonnegative normalized real-pole separation yielding a positive representing measure when the ratio of complex frequencies is \(r>1\). The exact coefficient is the two-phase variational expression
\[
\kappa_m=\max_{0<\theta\le\pi}\frac{\log M_m(\theta)}{\theta},\qquad
M_m(\theta)=\max_{0\le\phi\le2\pi}
\frac{m^2\cos\phi-\cos(m\phi+\theta)}{m^2-1}.
\]
In particular \(0<\kappa_m<\infty\). This law captures an \(O(|\varepsilon|^{-1})\) beating timescale not visible in tests of any fixed finite collection of moments or fixed logarithmic times.

## Assumptions and scope
Fix positive real parameters \(a,b,c\), and a frequency ratio \(r>1\). Define the quintic
\[
P_{a,b,c,r}(x)=(x+a)((x+b)^2+c^2)((x+b)^2+r^2c^2).
\]
On \(\ell^2(\mathbb N_0)\), define \(We_n=w_ne_{n+1}\), \(w_n^2=P(n+1)/P(n)\). Its Cauchy dual is \(W'=W(W^*W)^{-1}\). The weights are positive and bounded; \(W\) is expansive and a strict \(6\)-isometry, because \(\|W^ke_n\|^2=P(n+k)/P(n)\) is a degree-five polynomial in \(k\).

The contractive weighted shift \(W'\) has moments \(\gamma_n=P(0)/P(n)\). Hence \(W'\) is subnormal precisely when this sequence is Hausdorff. We only classify the normalized half-plane \(b\ge a\) in this result. Set \(\delta=(b-a)/c\ge0\), and for \(r>1\), \(t\ge0\), put
\[
G_{\delta,r}(t)=\frac1{r^2-1}\int_0^t e^{-\delta s}
\left(\sin s-\frac{\sin(rs)}r\right)\,ds.
\]
Define
\[
\Delta(r)=\inf\{\delta\ge0:G_{\delta,r}(t)\ge0\text{ for every }t\ge0\}.
\]
The set in braces is nonempty and is a closed upper ray, as proved below, so the infimum is attained. In these terms, for \(b\ge a\), the Cauchy dual is subnormal if and only if \(\delta\ge\Delta(r)\). At the integer resonance \(\Delta(m)=0\) for every \(m\ge2\). The theorem describes the two-sided detuning limit for fixed \(m\), restricting \(r=m+\varepsilon>1\).

## Proof
**1. Moment representation and the threshold ray.** Partial fractions or the Laplace convolution theorem yield, for every real \(x\ge0\),
\[
\frac1{P(x)}=\frac1{c^4}\int_0^\infty
 e^{-(x+a)u}G_{\delta,r}(cu)\,du.
\]
Indeed, the inverse Laplace transforms of the two quadratic factors first give
\[
\frac{e^{-bu}}{(r^2-1)c^3}
\left(\sin(cu)-\frac{\sin(rcu)}r\right),
\]
and convolution with the inverse transform \(e^{-au}\) of the real linear factor gives the displayed formula after rescaling. Equivalently, the unique finite signed representing measure for \(P(0)/P(n)\) has density
\[
\frac{P(0)}{c^4}\,x^{a-1}
G_{\delta,r}\!\left(c\log(1/x)\right),\qquad 0<x<1.
\]
It is finite since \(a>0\) and \(G_{\delta,r}\) is bounded for \(\delta\ge0\) (periodic and bounded at integer resonance; for other \(r\), its antiderivative at \(\delta=0\) is also bounded). Uniqueness of finite signed moment measures on \([0,1]\) follows by density of polynomials in \(C[0,1]\). Therefore positivity of the displayed density is necessary and sufficient for subnormality.

For fixed \(r>1\), the integrand in \(G_{0,r}\) starts with \((r^2-1)s^3/6+O_r(s^5)\). It is strictly positive for small positive \(s\). Exponential damping with sufficiently large \(\delta\) makes the integral over this initial positive interval dominate the bounded negative tail uniformly for all later times. Thus \(G_{\delta,r}\ge0\) for some finite \(\delta\).

For \(\delta_2>\delta_1\ge0\), integrating by parts gives
\[
G_{\delta_2,r}(t)=e^{-(\delta_2-\delta_1)t}G_{\delta_1,r}(t)
+(\delta_2-\delta_1)\int_0^t e^{-(\delta_2-\delta_1)s}
G_{\delta_1,r}(s)\,ds.
\]
Consequently the positivity set is an upper ray; continuity in \(\delta\) at every fixed \(t\) shows the ray is closed.

**2. Integer resonance and its quartic contact.** At \(r=m\in\{2,3,\dots\}\), \(\delta=0\), direct integration gives
\[
G_{0,m}(t)=\frac{1-\cos t-m^{-2}(1-\cos mt)}{m^2-1}.
\]
The elementary inequality \(|\sin(mz)|\le m|\sin z|\) shows that this is nonnegative, vanishing exactly at \(t\in2\pi\mathbb N_0\). At each \(t_k=2\pi k\),
\[
G_{0,m}(t_k+h)=\frac{h^4}{24}+O_m(h^6).
\]
For \(k\ge1\), differentiating under the integral sign and integrating by parts gives
\[
\left.\frac{\partial G_{\delta,r}(t_k)}{\partial\delta}\right|_{(0,m)}
=\int_0^{t_k}G_{0,m}(s)\,ds=\frac{t_k}{m^2},
\qquad
\left.\frac{\partial G_{0,r}(t_k)}{\partial r}\right|_{r=m}=0.
\]
The second equality follows directly from the cosine formula evaluated at \(t_k\).

**3. Exact beating-phase reduction.** Let \(A_w=(\delta^2+w^2)^{-1}\). Integration of each damped sine yields
\[
G_{\delta,r}(t)=\frac{A_1-A_r}{r^2-1}
\left(1-e^{-\delta t}Q_{\delta,r}(t)\right),
\]
where
\[
Q_{\delta,r}(t)=\frac{A_1(\cos t+\delta\sin t)
-A_r(\cos(rt)+(\delta/r)\sin(rt))}{A_1-A_r}.
\]
The prefactor is positive, so the moment measure is positive precisely when
\[
Q_{\delta,r}(t)\le e^{\delta t}\quad\text{for every }t\ge0.
\]
For fixed \(m\) and \(K>0\), write \(r=m+\varepsilon\), \(\delta=K|\varepsilon|\), and
\[
q_m(\phi,\theta)=\frac{m^2\cos\phi-\cos(m\phi+\theta)}{m^2-1}.
\]
Smoothness of the rational coefficients in \(Q\) and boundedness of the sine and cosine factors give the uniform **all-time** estimate
\[
\sup_{t\ge0}\big|Q_{K|\varepsilon|,m+\varepsilon}(t)
-q_m(t\bmod2\pi,\varepsilon t)\big|\le C_{m,K}|\varepsilon|,
\]
for sufficiently small nonzero \(\varepsilon\). No approximation of the long phase \(\varepsilon t\) is made here.

**4. The phase constant is finite and positive.** Define \(M_m(\theta)=\max_\phi q_m(\phi,\theta)\). It is continuous, even, and \(2\pi\)-periodic in \(\theta\), with \(M_m(0)=1\). Also
\[
M_m(\theta)\ge q_m(0,\theta)
=1+\frac{1-\cos\theta}{m^2-1}>1
\quad(0<\theta<2\pi).
\]
For \(\theta=0\), the strict inequality \(q_m(\phi,0)<1\) holds unless \(\phi\) is a multiple of \(2\pi\). Taylor's formula near those points gives
\[
q_m(\phi,0)\le1-c_m\phi^4,\qquad
q_m(\phi,\theta)-q_m(\phi,0)
\le C_m|\theta|\,|\phi|+C_m\theta^2.
\]
Outside their neighborhoods there is a fixed negative gap. Optimizing the quartic bound proves \(0\le\log M_m(\theta)=O_m(|\theta|^{4/3})\) as \(\theta\to0\). Thus the quotient \(\log M_m(\theta)/\theta\) tends to zero at the left endpoint, has a positive finite maximum on \((0,\pi]\), and defines \(0<\kappa_m<\infty\). Periodicity and evenness imply, for every real \(\theta\),
\[
M_m(\theta)\le e^{\kappa_m|\theta|}.
\]

**5. Upper bound on the critical separation.** Fix \(K>\kappa_m\). By the all-time estimate in step 3,
\[
Q_{K|\varepsilon|,m+\varepsilon}(t)
\le M_m(\varepsilon t)+C_{m,K}|\varepsilon|
\le e^{\kappa_m|\varepsilon|t}+C_{m,K}|\varepsilon|.
\]
Since \(e^{Kx}-e^{\kappa_m x}\ge(K-\kappa_m)x\) for \(x\ge0\), the inequality \(Q\le e^{K|\varepsilon|t}\) follows for every \(t\ge T_{m,K}:=C_{m,K}/(K-\kappa_m)\).

For \(t\) in the remaining compact interval \([0,T_{m,K}]\), positivity follows uniformly when \(\varepsilon\) is small: near zero, \(G_{\delta,r}(t)=t^4/24+O_{m,K}(t^5)\), and away from the finitely many positive resonance zeros, \(G_{0,m}>0\). For each positive \(t_k=2\pi k\le T_{m,K}\), Taylor's theorem and step 2 give, for sufficiently small \(|h|\),
\[
G_{K|\varepsilon|,m+\varepsilon}(t_k+h)
\ge c_m h^4+\frac{K t_k}{m^2}|\varepsilon|
-C_{m,K,T}(|\varepsilon|\,|h|+\varepsilon^2).
\]
The elementary minimization bound \(c_mh^4-C|\varepsilon|\,|h|\ge-C'|\varepsilon|^{4/3}\) makes the right side strictly positive for sufficiently small \(\varepsilon\). Therefore \(\Delta(m+\varepsilon)\le K|\varepsilon|\) for sufficiently small detuning. Letting \(K\downarrow\kappa_m\) yields
\[
\limsup_{\varepsilon\to0}\frac{\Delta(m+\varepsilon)}{|\varepsilon|}\le\kappa_m.
\]

**6. Lower bound and the long-time obstruction.** Fix \(0<K<\kappa_m\). By definition of \(\kappa_m\), there are \(\theta_*\in(0,\pi]\) and a phase \(\phi_*\in[0,2\pi]\) for which \(q_m(\phi_*,\theta_*)>e^{K\theta_*}\). By the evenness of \(M_m\), there is a (possibly different) phase satisfying the same strict inequality with \(-\theta_*\). For either fixed sign of \(\varepsilon\), choose positive times \(t_\varepsilon\) such that \(t_\varepsilon\bmod2\pi\to\phi_*\) and \(|\varepsilon|t_\varepsilon\to\theta_*\); these exist by choosing an appropriate integer multiple of \(2\pi\). The all-time phase approximation gives
\[
Q_{K|\varepsilon|,m+\varepsilon}(t_\varepsilon)
\longrightarrow q_m(\phi_*,\operatorname{sgn}(\varepsilon)\theta_*)
>e^{K\theta_*}
=\lim_{\varepsilon\to0}e^{K|\varepsilon|t_\varepsilon}.
\]
Thus the signed representing density is negative at a logarithmic time of order \(1/|\varepsilon|\), and \(\Delta(m+\varepsilon)\ge K|\varepsilon|\) for all sufficiently small detunings. Letting \(K\uparrow\kappa_m\) yields the reverse limit inequality. Combining the two proves the stated two-sided limit.

## Verification
The analytic argument covers **every** integer resonance \(m\ge2\), **both** signs of nonzero detuning, and **all** times \(t\ge0\). The phase-bound estimate in step 3 is uniform on the unbounded time axis; steps 5 and 6 address, respectively, compact times and the logarithmic beating scale. The finite diagnostic script `verify.py` checks the integral and rational expressions of \(G\), resonant positivity and quartic contact, the strict phase witness for several frequency ratios, and numerical consistency of the detuning scaling. Run with `python3 verify.py`; it uses only the Python standard library. Its finite samples are *not* the proof of positivity for every time or the limiting theorem.

## Relationship to prior work
Reza and Zhang's 2019 arXiv paper (Theorem 1.10 and the proof in Section 5) gives a complete criterion for the **coincident-real-part** quintic, namely \(\Delta(m)=0\) at integer frequency ratios and nonpositivity at noninteger ratios when \(\delta=0\). It explicitly leaves much of the quintic class with the real pole to the right of the nonreal pairs unclassified; in particular it does not give a detuning modulus or a beat-phase critical coefficient. The present result assumes exactly that pole configuration and gives a sharp first-order critical boundary near **every** integer resonance. Buchała's polynomial characterization of \(m\)-isometric weighted shifts supplies related general operator background, not this moment-positivity threshold.

Two narrower recorded results concern a repeated conjugate pair and a fixed \(3:2\) frequency pair, respectively; neither implies the near-integer asymptotic across varying frequency ratio. An earlier or unindexed general positive-exponential-spline stability theorem could encompass the calculation, so the historical priority is not independently certified.

## Limitations
The theorem gives the sharp leading coefficient but no second-order correction and no general closed elementary formula for \(\kappa_m\). It does not classify the threshold at arbitrary noninteger ratios in closed form, nor the case \(b<a\). The variational formula for \(\kappa_m\) is exact; numerical optimizers are illustrative only. The novelty assessment is based on inspected sources and targeted searches, not a proof of worldwide uniqueness. No independent mathematical audit has been performed.

## References
1. Md. Ramiz Reza and Genkai Zhang, *Hausdorff moment sequences induced by rational functions*, arXiv:1903.00116v1 (first public 2019-03-01), https://arxiv.org/html/1903.00116v1, especially Theorem 1.10 and Section 5.
2. Michał Buchała, *\(m\)-isometric weighted shifts with operator weights*, arXiv:2407.17233 (first version 2024-07-24; inspected version 2, 2025-03-03), https://arxiv.org/html/2407.17233v2, especially Section 3.
3. Akash Anand, Sameer Chavan, Zenon Jan Jabłoński, and Jan Stochel, *A solution to the Cauchy dual subnormality problem for 2-isometries*, arXiv:1702.01264 (2017), https://arxiv.org/abs/1702.01264, contextual reference only.
