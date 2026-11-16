# Sharp stretched-exponential inversion and Gaussian coefficient localization for a two-direction Fourier filter

## Finding

Let \(0<\alpha<1\), \(\tau>0\), and equip \(\mathbb Z^2\) with the symmetric Beurling weight
\[
\omega_{\alpha,\tau}(m,n)=\exp(\tau|m-n|^\alpha).
\]
For \(0<t<1\), set
\[
f_t=\delta_{(0,0)}-\frac t2(\delta_{(1,0)}+\delta_{(0,1)}).
\]
Write \(N_{\alpha,\tau}(t)=\|f_t^{-1}\|_{\ell^1_\omega}\), \(\beta=\operatorname{arcosh}(1/t)\), and
\[
r=\left(\frac{\alpha\tau}{\beta}\right)^{1/(1-\alpha)},\quad
\sigma=\frac{r^{1-\alpha/2}}{\sqrt{\tau\alpha(1-\alpha)}},\quad
H=(1-\alpha)\tau r^\alpha.
\]
The exact inverse norm and its sharp boundary equivalent are
\[
N_{\alpha,\tau}(t)=\frac{1+2\sum_{k\ge1}\exp(\tau k^\alpha-\beta k)}{\sqrt{1-t^2}},\qquad
N_{\alpha,\tau}(t)\sim\frac{2\sqrt{2\pi}\,\sigma\,e^H}{\sqrt{1-t^2}}
\quad(t\uparrow1).
\]
In particular, with \(\gamma=\alpha/[2(1-\alpha)]\),
\[
\lim_{t\uparrow1}(1-t)^\gamma\log N_{\alpha,\tau}(t)
=(1-\alpha)\alpha^{\alpha/(1-\alpha)}\tau^{1/(1-\alpha)}2^{-\gamma}.
\]
Normalize the nonnegative coefficients of \(\omega_{\alpha,\tau}f_t^{-1}\) to a probability distribution on \(\mathbb Z^2\), and let \(J=|m-n|\). Then
\[
\frac{J-r}{\sigma}\ \Longrightarrow\ \mathcal N(0,1)\quad(t\uparrow1).
\]
For every such \(\alpha,\tau\), the Gelfand spectrum of \(\ell^1_{\omega_{\alpha,\tau}}(\mathbb Z^2)\) is nevertheless the same ordinary torus \(\mathbb T^2\).

## Assumptions and scope

The convolution norm is \(\|h\|_{\ell^1_\omega}=\sum_{(m,n)\in\mathbb Z^2}|h(m,n)|\omega(m,n)\). Both parameters \(\alpha,\tau\) are fixed before \(t\uparrow1\). The weight is nonproper, because it equals one on the diagonal subgroup; this is deliberate and the weight remains submultiplicative and of Gelfand–Raikov–Shilov type. Fourier characters are normalized by \(\chi_{z,w}(m,n)=z^mw^n\) for \(|z|=|w|=1\).

## Proof

**The algebra and its spectrum.** Since \(0<\alpha<1\), \(|a+b|^\alpha\le|a|^\alpha+|b|^\alpha\), and hence \(\omega\) is symmetric, bounded below by one, and submultiplicative. Along each fixed lattice element \((m,n)\), \(\omega(jm,jn)^{1/j}=\exp(\tau j^{\alpha-1}|m-n|^\alpha)\to1\). For any continuous multiplicative character of the weighted convolution algebra, the coordinate generators and their inverses imply \(|z|\le\inf_{j\ge1}e^{\tau j^{\alpha-1}}=1\) and \(|z|^{-1}\le1\); similarly \(|w|=1\). Conversely each unitary pair is a bounded character. Thus the spectrum is exactly \(\mathbb T^2\), independently of the two weight parameters.

**Exact inverse.** The convolution geometric series converges in \(\ell^1_\omega\) for \(t<1\), since the terms on total degree \(s\) have weighted norm at most \(t^s e^{\tau s^\alpha}\) and their sum is finite. Its coefficient at \((m,n)\), for nonnegative \(m,n\), is
\[
f_t^{-1}(m,n)=2^{-(m+n)}t^{m+n}\binom{m+n}{m},
\]
and is zero for other coordinates. Under the binomial probability law this gives the *exact* identity
\[
N_{\alpha,\tau}(t)=\sum_{s\ge0}t^s\,\mathbb E\exp(\tau|S_s|^\alpha),
\]
where \(S_s\) is simple symmetric random walk started at zero. The generating Green function \(G_t(k)=\sum_{s\ge0}t^s\mathbb P(S_s=k)\) solves
\[
G_t(k)=\mathbf1_{\{k=0\}}+\frac t2(G_t(k-1)+G_t(k+1)).
\]
Its unique decaying solution is \(G_t(k)=e^{-\beta|k|}/\sqrt{1-t^2}\), because \(t\cosh\beta=1\), with the origin constant fixed by the recurrence. Tonelli's theorem then gives the claimed exact norm series.

**Saddle asymptotic.** Let \(h(x)=\tau x^\alpha-\beta x\) for \(x>0\). Strict concavity gives a unique maximizer \(r=(\alpha\tau/\beta)^{1/(1-\alpha)}\), with \(h(r)=H\) and \(-h''(r)=\sigma^{-2}\). As \(t\uparrow1\), \(r,\sigma\to\infty\), \(\sigma/r\to0\), and \(\tau r^\alpha\to\infty\). Uniformly on \(|k-r|\le M\sigma\) for fixed \(M\), Taylor expansion gives
\[
h(k)-H=-\frac{(k-r)^2}{2\sigma^2}+o(1).
\]
The error is uniform there because \(\sup|h'''|\,\sigma^3=O(r^{-\alpha/2})\). Choose a slowly growing \(M\), so the remainder remains uniform. On \([r/2,2r]\) strict concavity gives Gaussian tail domination beyond \(M\sigma\); outside that interval the height deficit is at least a fixed positive multiple of \(\tau r^\alpha\), and the upper infinite tail also has a geometric slope of order \(\beta\). These bounds make the omitted sum negligible against \(\sigma e^H\). The central sum is a Riemann sum for the Gaussian integral (mesh \(1/\sigma\to0\)), so
\[
\sum_{k\ge1}e^{h(k)}=\sqrt{2\pi}\,\sigma e^H(1+o(1)).
\]
The \(k=0\) contribution is negligible. This proves the full equivalent. Since \(\beta=\operatorname{arcosh}(1/t)\sim\sqrt{2(1-t)}\), taking logarithms yields the displayed stretched-exponential exponent and constant.

**Coefficient localization.** After summing inverse coefficients over the fibers \(|m-n|=k\), the normalized law of \(J\) assigns mass proportional to \(2e^{h(k)}\) for \(k\ge1\), and mass proportional to one for \(k=0\). The same central Taylor approximation and tail estimates prove convergence of the rescaled probability law to the standard Gaussian. The signs \(m-n>0\) and \(m-n<0\) each carry asymptotically half the total mass.

## Verification

The accompanying standalone `checker.py` tests the exact random-walk Green function against direct finite-step probabilities, compares the weighted inverse norm against a separate degree-by-degree binomial expansion, and checks the sharp logarithmic saddle prefactor at five parameter configurations. Its 82 finite checks passed. The proofs above, not the finite checks, establish the full parameter range and the Gaussian weak limit.

## Relationship to prior work

Spronk and Zhang classify spectra of Beurling algebras, including their GRS spectral equivalence; that work supplies the contemporary motivation for separating spectral identity from quantitative inverse stability, but it does not state the displayed two-direction filter equivalent or Gaussian coefficient law. Chen and Wang prove subexponential/Gevrey spectral invariance and inverse seminorm estimates in general group settings. Jaure proves stretched-exponential norm-controlled inversion in a broader covariant-kernel setting, but the inspected theorem gives general bounds rather than this filter's asymptotic constant and localization. Samei and Shepelska establish an earlier framework for norm-controlled inversion in weighted convolution algebras, including stretched-exponential weights, without this evaluated filter asymptotic. The classical simple-random-walk Green recurrence and the discrete Laplace method are established ingredients, not claimed innovations.

## Limitations

The result concerns this exact filter and the stated difference-coordinate weight; it is not a sharp worst-case bound over all elements of a Beurling algebra. The weight is not a proper length weight. All asymptotics fix \(\alpha,\tau\); they are not uniform when either parameter varies with \(t\). The coefficient-limit statement is a weak limit, not a total-variation Gaussian approximation for the full two-dimensional coefficient vector. Previously published equivalent evaluations using random-walk Green functions or lattice saddle methods cannot be categorically excluded; the literature search is not a proof of priority. Independent mathematical audit has not been performed.

## References

1. Nico Spronk and Zhihao Zhang, *Spectra of Beurling algebras of abelian groups*, arXiv:2611.03437v1, 2026-11-02, https://arxiv.org/html/2611.03437v1.
2. Lin Chen and Qin Wang, *Spectral Invariance and Gevrey Regularity for Groups with strongly subexponential growth*, arXiv:2607.03074v1, 2026-07-03, https://arxiv.org/abs/2607.03074.
3. Diego Jaure, *Wiener's lemma for quasicrystals: hull-uniform decay of covariant kernels on Delone sets*, arXiv:2610.12770v1, 2026-10-08, https://arxiv.org/abs/2610.12770.
4. Ebrahim Samei and Varvara Shepelska, *Norm-controlled inversion in weighted convolution algebras*, arXiv:1809.04097v1, 2018-09-11, https://arxiv.org/abs/1809.04097.
5. Standard simple symmetric random-walk Green functions and the discrete Laplace/saddle-point method, used here only as mathematical ingredients.
