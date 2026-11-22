# A sharp stationary-memory oscillation threshold in a nonreciprocal kinetic Ising chain

## Finding
For the strictly positive continuous-time nearest-neighbor Ising flip process below, fix ferromagnetic equilibrium coupling \(J>0\), inverse temperature \(\beta>0\), and directional coupling \(K\in\mathbb R\). Put
\[
z=\tanh(\beta J),\qquad e=\tanh(2\beta J)=\frac{2z}{1+z^2},\qquad g=|\tanh(2\beta K)|.
\]
The stationary connected on-site temporal correlation \(C(t)=\mathbb E_\pi[\sigma_0(t)\sigma_0(0)]\), with time measured in units of the single-spin flip clock, has the following *complete eventual-sign classification* for every \(0<z<1\) and \(0\le g<1\). Define the additional threshold
\[
g_*(z)=\frac{2z}{1-z^2}=\sinh(2\beta J)>e.
\]

1. If \(0\le g\le e\), then \(C(t)>0\) at every finite \(t\ge0\). At \(g=e\), exactly \(C(t)=\exp[-(1-ez)t]\).
2. If \(e<g<g_*(z)\), then
\[
 C(t)=\exp\left[-\frac{g(1-z^2)}{2z}t\right](1+o(1)) \quad (t\to\infty),
\]
so it is eventually strictly positive.
3. If \(e<g=g_*(z)\), then \(C(t)=e^{-t}(1+o(1))\) and is eventually strictly positive.
4. If \(g>g_*(z)\), then \(C(t)\) takes strictly positive and strictly negative values infinitely often, and hence has infinitely many distinct positive-time zeros. More precisely, put
\[
\omega=\sqrt{g^2-e^2},\quad h=\sqrt{\frac{g+e}{g-e}},\quad q=zh,\quad p=-z/h,\quad H=\frac{1-z^2}{(1+iq)(1+ip)}.
\]
Then \(H\ne0\) and
\[
 C(t)=e^{-t}\sqrt{\frac{2}{\pi\omega t}}\operatorname{Re}\left[H e^{i(\omega t-\pi/4)}\right]
       +o(e^{-t}t^{-1/2}).
\]
The infinite-oscillation regime is physically accessible if and only if \(z<\sqrt2-1\), equivalently \(\beta J<\operatorname{arsinh}(1)/2\); the threshold lies *strictly beyond* the already-known propagator transition \(g=e\). No all-time positivity claim is made in case 2 or 3.

## Assumptions and scope
The spins \(\sigma_j\in\{-1,1\}\) occupy \(j\in\mathbb Z\); each spin flips, conditionally on its neighbors, with rate
\[
 w_j(\sigma)=\frac12\left[1-\frac{\sigma_j}{2}\{e(\sigma_{j-1}+\sigma_{j+1})+\eta(\sigma_{j-1}-\sigma_{j+1})\}\right],\qquad \eta=\tanh(2\beta K).
\]
All rates are strictly between zero and one because \(e,g<1\). The time-stationary, translation-invariant zero-field Gibbs measure \(\pi\) has \(\mathbb E_\pi\sigma_j=0\) and \(\mathbb E_\pi(\sigma_j\sigma_{j+n})=z^{|n|}\). This measure is stationary under the directional dynamics even when \(g>e\), by global balance, though the dynamics violates detailed balance for \(\eta\ne0\). Reflection symmetry makes \(C(t)\) depend only on \(g=|\eta|\). The statement concerns the thermodynamic infinite-chain stationary limit, not the small-system spectrum at fixed chain length.

## Proof
**1. Exact stationary correlation.** The one-point Markov generator closes linearly:
\[
 L\sigma_j=-\sigma_j+\frac{e+\eta}{2}\sigma_{j-1}+\frac{e-\eta}{2}\sigma_{j+1}.
\]
Evolving the later spin and pairing with the stationary earlier spin, then Fourier transforming the Gibbs initial pair function \(z^{|n|}\), yields the absolutely convergent identity
\[
 C(t)=\frac{1-z^2}{2\pi}\int_{-\pi}^{\pi}
 \frac{\exp[-t+et\cos k-i gt\sin k]}{1-2z\cos k+z^2}\,dk.\tag{1}
\]
For \(g\le e\), both off-diagonal generator coefficients are nonnegative; its exponential is a positive convolution kernel, and its convolution with the strictly positive sequence \(z^{|n|}\) proves \(C(t)>0\). At \(g=e\), the process becomes one-way at the level of one-point propagation. The series gives \(C(t)=e^{-t}\sum_{n\ge0}(ezt)^n/n!=e^{-(1-ez)t}\).

**2. Exact oscillatory-sector Bessel series.** For \(g>e\), define \(\omega,h,q,p\) as in the finding. The two directional coefficients are \(\omega h/2\) and \(-\omega/(2h)\). The Laurent identity
\[
\exp\left[\frac x2(h u-h^{-1}u^{-1})\right]
 =\sum_{n\in\mathbb Z}J_n(x)(hu)^n
\]
combined with \(\mathbb E_\pi(\sigma_0\sigma_n)=z^{|n|}\) gives
\[
 e^t C(t)=J_0(\omega t)+\sum_{n\ge1}(q^n+p^n)J_n(\omega t).\tag{2}
\]
For each fixed \(t\) this series converges absolutely, irrespective of whether \(q\) exceeds one. The threshold equivalences are exact:
\[
 q>1\iff g<g_*(z),\quad q=1\iff g=g_*(z),\quad q<1\iff g>g_*(z).\tag{3}
\]
Indeed \(q^2=z^2(g+e)/(g-e)\), and cross-multiplying the positive denominators gives \(g(1-z^2)\lessgtr e(1+z^2)=2z\).

**3. The dominant exponential branch.** For \(q>1\), the Bessel generating identity, evaluated at \(q\), is
\[
 e^{x(q-q^{-1})/2}=J_0(x)+\sum_{n\ge1}(q^n+(-q^{-1})^n)J_n(x).
\]
Subtracting this from (2) leaves the absolutely and geometrically weighted series
\[
 e^t C(t)=e^{x(q-q^{-1})/2}
   +\sum_{n\ge1}\bigl[p^n-(-q^{-1})^n\bigr]J_n(x),\qquad x=\omega t.
\]
Here \(|p|<1\) and \(q^{-1}<1\). Fixed-order Bessel asymptotics, together with geometric summation (split at \(n=\lceil c\log(2+x)\rceil\) and use \(|J_n(x)|\le1\) for the tail), show the remainder is \(O(x^{-1/2})\). Direct algebra gives \(\omega(q-q^{-1})/2=1-g(1-z^2)/(2z)>0\). The exponential dominates and proves case 2.

**4. The critical threshold.** If \(q=1\), the generating identity reduces to
\[
 e^t C(t)=1+\sum_{n\ge1}\bigl[p^n-(-1)^n\bigr]J_n(x).
\]
The \(p\)-series is \(O(x^{-1/2})\). The classical exact identity
\[
\sum_{n\ge1}(-1)^nJ_n(x)=\frac{1-J_0(x)-\int_0^x J_0(u)\,du}{2}
\]
and \(J_0(x)\to0\), \(\int_0^\infty J_0(u)\,du=1\) prove \(e^t C(t)\to1\), as claimed. Conditional convergence of the last improper Bessel integral is sufficient.

**5. The genuine oscillatory branch.** If \(q<1\), the corresponding \(|p|<1\) too. Use the fixed-order expansion
\[
 J_n(x)=\sqrt{\frac2{\pi x}}\cos\left(x-\frac{n\pi}{2}-\frac\pi4\right)+O_n(x^{-3/2})
\]
termwise through a geometrically controlled truncation. The tails \(\sum_{n>M}(q^n+|p|^n)|J_n(x)|\le O(\max(q,|p|)^M)\) permit \(M\) growing logarithmically, which makes their contribution \(o(x^{-1/2})\). Equivalently, dominated convergence follows for the rescaled series using standard fixed-order Bessel bounds. The leading complex coefficient is
\[
 1+\sum_{n\ge1}(-i)^n(q^n+p^n)
 =\frac1{1+iq}+\frac1{1+ip}-1
 =\frac{1+qp}{(1+iq)(1+ip)}
 =H.
\]
As \(qp=-z^2\), \(H\ne0\). Choose the unbounded sequences of times making \(\omega t-\pi/4+\arg H\) successively even and odd multiples of \(\pi\). The asymptotic then has alternating strict signs. Continuity gives infinitely many different zeros. Finally \(g_*<1\iff z<\sqrt2-1\), proving physical accessibility.

## Verification
The accompanying standalone `check_stationary_memory.py` performs exact symbolic identities, independently compares the Fourier integral and Bessel formula over physical parameter sets, tests oscillatory and exponential asymptotic regimes, and checks a full nine-spin generator against an exact Gibbs stationary measure and its infinite-chain short-time limit. Run `python check_stationary_memory.py` with Python 3.10+, NumPy, SciPy and SymPy. It reports **4743 deterministic assertions passed**. Direct numerical quadrature is restricted to moderate times to avoid catastrophic oscillatory cancellation; large-time tests use Bessel series and do not constitute infinite-time proof. The analytic argument above supplies that proof.

## Relationship to prior work
Weiderpass, Sharma and Sethi (arXiv:2410.23615v1, publicly submitted 2024-10-31) introduced the nonreciprocal chain and its exact one-/two-point evolution and wave/exceptional-point regimes. Their stationary equal-time Ising correlation and two-time propagator imply the integral (1). The present claim is **not** novelty of that kernel: it separates a further stationary *autocorrelation sign* threshold \(g_*=\sinh(2\beta J)\) from the previously known propagator threshold \(g=e\), and proves a full eventual-sign trichotomy including an explicit nonvanishing oscillatory coefficient. Godrèche (arXiv:1102.0141v2, 2011, Secs. 2 and 5.2, including Eq. (5.13)) analyzed the stationary two-time function of the directed Glauber chain with stochastic left/right influence weights \(0\le p\le1\), which implies \(|\eta|\le e\) and therefore does not cover the sign-changing branch. The mathematical formulas can be analytically continued outside that rate subfamily, but such continuation alone is not the stated oscillation classification.

## Limitations
The results establish eventual sign behavior in intermediate/critical regimes, not positivity for every transient time there; they do not count finite-time zeros or address arbitrary non-Glauber flip rates. The theorem is an analytic consequence of exact known dynamics rather than an independent derivation of the model, and an equivalent unindexed treatment in the special-function or nonequilibrium literature remains a possible originality risk. Finite numerical experiments and finite-ring checks are supplementary, not universal certificates. Independent external scientific review has not been performed.

## References
1. G. A. Weiderpass, M. Sharma and S. Sethi, *Solving the Kinetic Ising Model with Non-Reciprocity*, arXiv:2410.23615v1 (2024-10-31), https://arxiv.org/html/2410.23615v1, especially Sections 3 and 5.
2. C. Godrèche, *Dynamics of the directed Ising chain*, arXiv:1102.0141v2 (2011), https://arxiv.org/pdf/1102.0141, especially Sections 2 and 5.2.
3. Standard Bessel generating function and large-argument asymptotics, as in NIST Digital Library of Mathematical Functions, Chapters 10.12 and 10.17, https://dlmf.nist.gov/10.12 and https://dlmf.nist.gov/10.17.
