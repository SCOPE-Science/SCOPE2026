# Infinitely many exponentially narrow slow-switching stabilization windows

## Finding
Consider the equal-dwell periodically switched linear planar system
\[
\dot u=A_{s(t)}u,\qquad
A_0=\begin{pmatrix}0&-1\\1&a\end{pmatrix},\qquad
A_1=\begin{pmatrix}-2d&-1\\1&a\end{pmatrix},
\]
where \(0<a<2\), \(d>\max\{a,a^{-1}\}\), and the switching schedule uses \(A_0\) for \(t\) time units followed by \(A_1\) for \(t\) time units, repeated with period \(2t\). The dwell time \(t>0\) is the variable; the two parameters are fixed.

Let \(\mathcal S=\{t>0:\rho(e^{tA_1}e^{tA_0})<1\}\) denote the set of exponentially stabilizing dwell times. Define
\[
\begin{gathered}
\omega=\sqrt{1-a^2/4},\quad
\kappa=\sqrt{(d+a/2)^2-1},\quad
\eta=\frac{a(a+2d)/4-1}{\omega\kappa},\\
R=\sqrt{1+\eta^2},\quad\theta=\arctan\eta,\quad
\sigma=a-d+\kappa,\quad
r=e^{-\sigma\pi/\omega},\\
t_n=\frac{\theta+\pi/2+n\pi}{\omega}\quad(n=0,1,\ldots).
\end{gathered}
\]
Then \(\sigma>0\) and \(0<r<1\). There is an integer \(N\) such that, for every \(n\ge N\), exactly one connected component \(I_n=(\ell_n,u_n)\) of \(\mathcal S\) occurs near \(t_n\); these components exhaust \(\mathcal S\) for all sufficiently large dwell times. Their sharp endpoint and width asymptotics are
\[
\ell_n=t_n-\frac{e^{-\sigma t_n}}{\omega R}(1+o(1)),\quad
u_n=t_n+\frac{e^{-\sigma t_n}}{\omega R}(1+o(1)),
\]
\[
|I_n|=\frac{2e^{-\sigma t_n}}{\omega R}(1+o(1)).
\]
The stability set has infinitely many connected components but finite Lebesgue measure. More precisely,
\[
\boxed{\lim_{n\to\infty}e^{\sigma t_n}\operatorname{Leb}\bigl(\mathcal S\cap[\ell_n,\infty)\bigr)=\frac{2}{\omega R(1-r)}.}
\]
Neither frozen mode nor the average frozen mode is stable: \(A_0\) is an unstable focus, while \(A_1\) and \((A_0+A_1)/2\) are saddles. Thus isolated arbitrarily slow equal-dwell switching schedules stabilize a system all three of whose reference dynamics are unstable, though the permissible dwell-time precision shrinks exponentially.

## Assumptions and scope
This is a statement about the exact two-dimensional piecewise-constant linear ODE above. It also applies mode-by-mode to an exactly identical reduced transverse equation of an on-off coupled system. The parameter \(d\) is the coefficient in \(A_1\), not the graph-Laplacian effective coupling (which equals \(2d\) for a two-node unit-edge graph). Stability means exponential decay of every solution under the periodic linear evolution, not synchronization of an unreduced nonlinear Rössler network. The repeated schedule begins with \(A_0\); cyclic reordering does not change the monodromy eigenvalues.

## Proof
**1. Frozen modes and positivity of the exponents.** The characteristic polynomial of \(A_0\) is \(z^2-az+1\), so \(0<a<2\) gives an unstable focus. The determinants of \(A_1\) and \((A_0+A_1)/2\) are, respectively, \(1-2ad\) and \(1-ad\); they are negative because \(d>a^{-1}\), making both matrices saddles. Also \(d>a\) ensures the monodromy determinant is below one.

The number \(\kappa\) is real and positive because \(d>\max\{a,a^{-1}\}\). To show \(\sigma>0\), calculate
\[
\kappa^2-(d-a)^2=3ad-3a^2/4-1.
\]
If \(0<a\le1\), then \(ad>1\), so the right side exceeds \(3-3/4-1>0\). If \(1<a<2\), then \(d>a\), so the right side exceeds \(9a^2/4-1>0\). Since \(d-a>0\), we get \(\kappa>d-a\), as claimed. Put \(\mu=a-d-\kappa<0\).

**2. Exact Floquet trace and Jury condition.** Let \(\Phi(t)=e^{tA_1}e^{tA_0}\). The standard identity
\[
e^{tA_i}=e^{t\operatorname{tr}(A_i)/2}
\biggl[\cosh(\xi_it)I+\frac{\sinh(\xi_it)}{\xi_i}\Bigl(A_i-\tfrac12\operatorname{tr}(A_i)I\Bigr)\biggr],
\]
with \(\xi_0=i\omega\), \(\xi_1=\kappa\), gives, after multiplication,
\[
\begin{aligned}
H(t):=\operatorname{tr}\Phi(t)
&=e^{(a-d)t}\bigl(2\cos(\omega t)\cosh(\kappa t)
 +2\eta\sin(\omega t)\sinh(\kappa t)\bigr)\\
&=e^{\sigma t}\bigl(\cos(\omega t)+\eta\sin(\omega t)\bigr)
 +e^{\mu t}\bigl(\cos(\omega t)-\eta\sin(\omega t)\bigr),\\
D(t):=\det\Phi(t)&=e^{2(a-d)t}.
\end{aligned}
\]
For any real two-by-two matrix with positive determinant, the quadratic Jury criterion says both multipliers have modulus less than one exactly when \(D<1\) and \(|H|<1+D\). Here \(D<1\) holds for every \(t>0\). Writing \(g(t)=\cos(\omega t)+\eta\sin(\omega t)=R\cos(\omega t-\theta)\) and \(h(t)=\cos(\omega t)-\eta\sin(\omega t)\), the stability condition becomes
\[
\bigl|e^{\sigma t}g(t)+e^{\mu t}h(t)\bigr|<1+e^{2(a-d)t}.
\tag{1}
\]
All bounds below are for fixed \(a,d\), with \(t\to\infty\).

**3. Localization and uniqueness of every late window.** The simple zeros of \(g\) are exactly \(t_n\). Since \(|h|\le R\), (1) implies \(|g(t)|\le C e^{-\sigma t}\) for all sufficiently large stable \(t\), where \(C\) is independent of \(t\). As the zeros of \(g\) are separated by \(\pi/\omega\), this forces every sufficiently large stable \(t\) into a neighborhood \(|t-t_n|\le C'e^{-\sigma t_n}\) of one of those zeros. Conversely, at \(t_n\), the trace equals \(e^{\mu t_n}h(t_n)\to0\), and the determinant tends to zero; hence \(t_n\in\mathcal S\) for all large \(n\).

Choose a small fixed \(\delta>0\) so that on each \((t_n-\delta,t_n+\delta)\), \(g'\) has fixed nonzero sign and \(|\sigma g|\le|g'|/2\). This is possible uniformly in \(n\) by periodicity and the simplicity of the zeros. Differentiating the trace shows
\[
H'(t)=e^{\sigma t}(\sigma g(t)+g'(t))+e^{\mu t}(\mu h(t)+h'(t));
\]
for all large \(n\), its sign is fixed throughout this neighborhood. Furthermore \(D'(t)=2(a-d)D(t)\) is exponentially small there, so the functions \(H(t)-(1+D(t))\) and \(H(t)+(1+D(t))\) each cross zero exactly once, and the interval between the crossings is precisely the stable component \(I_n\). The localization argument excludes other components at large \(t\).

**4. Sharp edge scale.** Define \(\varepsilon_n=e^{-\sigma t_n}/(\omega R)\). Since \(g'(t_n)=(-1)^{n+1}\omega R\), the Taylor expansion of (1), uniformly for bounded real \(x\), yields
\[
H(t_n+x\varepsilon_n)=(-1)^{n+1}x+o(1),\qquad D(t_n+x\varepsilon_n)=o(1).
\]
At the two boundary crossings the scaled coordinate must therefore tend to \(-1\) and \(+1\), establishing both endpoint estimates and the width asymptotic.

**5. Total tail measure.** The centers satisfy \(t_{n+k}-t_n=k\pi/\omega\). Consequently \(\varepsilon_{n+k}/\varepsilon_n=r^k\). By the width asymptotic, for all sufficiently large \(j\), \(|I_j|\le 3\varepsilon_j\). This gives a summable geometric bound and allows termwise passage to the limit:
\[
\lim_{n\to\infty}\frac{\operatorname{Leb}(\mathcal S\cap[\ell_n,\infty))}{\varepsilon_n}
=\sum_{k=0}^{\infty}2r^k=\frac2{1-r}.
\]
The late components have finite total measure; the bounded initial part of \(\mathcal S\) also has finite measure. This completes the proof.

## Verification
A standalone script, `verify.py`, independently evaluates \(\operatorname{tr}(e^{tA_1}e^{tA_0})\) via numerical matrix exponentials and compares it with the derived closed form, checks the Jury inequalities, and finds boundaries using bracketing. At \((a,d)=(0.1,11)\), its width-to-asymptotic ratios for window indices \(n=2,4,6,8,10\) are approximately \(1.03993,1.00981,1.00257,1.00069,1.00018\). At \((a,d)=(0.4,3)\), the ratio is within \(0.00045\) of one already at index two. These are finite-precision corroborations only; infinitude, uniqueness, and asymptotics follow from the proof above.

## Relationship to prior work
Jeter, Boateng, Porfiri, and Belykh (2026) derive the focal-plane reduction and the complete finite-dwell-time monodromy trace, determinant, and Jury criterion (their Eqs. (17)–(26)); they illustrate a few bounded windows and state that favorable angular alignments can recur. Their exact decision criterion underlies Step 2, but they do not state or establish the infinite component count, the universal long-dwell endpoint scale, or the exact stable-time tail measure. The present result is a global asymptotic analysis of that criterion, not a new model or a proof of stability for the full chaotic system.

Porfiri, Jeter, and Belykh (2021) analyze a transformed pair of triangular Hurwitz matrices arising from a different nonlinear switched oscillator; their finite antiresonance window does not give the present late-winding law. Xiedeng, Celli, and Porfiri (2026) develop related mechanical focus/saddle antiresonance, but with another switched matrix family and without these parameter-specific endpoint and tail constants.

## Limitations
All parameters are fixed as the dwell time tends to infinity, and both phases have exactly equal dwell times. The asserted infinite sequence pertains to a planar linear switched system (and exact copies of that reduced mode), not arbitrary switching, noise, switching-time jitter, noncommuting network modes, or the unreduced Rössler equations. Stability bands become exponentially small and are therefore not robust to any fixed absolute dwell-time uncertainty at sufficiently late indices. Historical priority beyond the inspected literature is not independently established.

## References
1. R. Jeter, A. Boateng, M. Porfiri, and I. Belykh, *Rate-selective synchronization in switching networks: when timing meets structure*, arXiv:2611.03355v1 (first public 2026-11-02), https://arxiv.org/html/2611.03355v1.
2. M. Porfiri, R. Jeter, and I. Belykh, *Antiresonance in switched systems with only unstable modes*, Physical Review Research **3**, L022001 (2021), https://doi.org/10.1103/PhysRevResearch.3.L022001.
3. D. Xiedeng, P. Celli, and M. Porfiri, *Dynamic stabilization of a mechanical oscillator in the absence of any stable feature*, Nature Communications **17**, 6024 (2026), https://doi.org/10.1038/s41467-026-70493-1.
