# A Cauchy velocity occupation law with a sharp total-variation coefficient in a cubic global center

## Finding
Fix \(\beta>0\) and \(\alpha\in\mathbb R\) with \(\Delta=4\beta-\alpha^2>0\). Consider the planar polynomial flow
\[
\dot x=v,\qquad \dot v=-x\,p(v),\qquad p(v)=1-\alpha v+\beta v^2.
\]
For \(A>0\), let \(\Gamma_A\) denote the periodic orbit through \((A,0)\), with minimal original-time period \(T(A)\). Sample \(t\) uniformly in \([0,T(A))\), and write \(V_A=v(t)\). Put
\[
K(v)=\int_0^v\frac{s}{p(s)}\,ds,\qquad
I_0=\int_{\mathbb R}\frac{dv}{p(v)}=\frac{2\pi}{\sqrt\Delta},\qquad
\bar K=\frac1{I_0}\int_{\mathbb R}\frac{K(v)}{p(v)}\,dv.
\]
Then \(V_A\) converges in total variation to the Cauchy probability law
\[
\nu(dv)=\frac{dv}{I_0p(v)}
=\frac1\pi\frac{\sigma\,dv}{(v-m)^2+\sigma^2},\qquad
m=\frac\alpha{2\beta},\quad\sigma=\frac{\sqrt\Delta}{2\beta}.
\]
More precisely, with \(d_{\rm TV}(\rho,\nu)=\tfrac12\int|d\rho-d\nu|\),
\[
\boxed{d_{\rm TV}(\mathcal L(V_A),\nu)
=\frac{C_{\alpha,\beta}}{A^2}+O_{\alpha,\beta}(A^{-4}),\qquad
C_{\alpha,\beta}=\frac1{2I_0}\int_{\mathbb R}\frac{|K(v)-\bar K|}{p(v)}\,dv>0.}
\]
On the symmetric slice \(\alpha=0\), the coefficient has the exact closed form
\[
\boxed{C_{0,\beta}=\frac{\operatorname{Cl}_2(\pi/3)}{\pi\beta}},\qquad
\operatorname{Cl}_2(\theta)=\sum_{n=1}^{\infty}\frac{\sin(n\theta)}{n^2}.
\]
In addition, write \(S_A=\operatorname{sgn}x(t)\) and \(D_A=A(A-|x(t)|)\). **At every finite amplitude**, \(S_A\) is a fair sign independent of \(V_A\). As \(A\to\infty\), the joint law of \((S_A,V_A,D_A)\) converges weakly to \((S,V,K(V))\), where \(S\) is a fair independent sign and \(V\sim\nu\). Thus physical time concentrates near the two extreme position faces while retaining an unbounded Cauchy velocity distribution.

## Assumptions and scope
All parameters are fixed, \(\beta>0\), \(\Delta>0\), and all amplitudes \(A>0\) refer to the positive position-axis crossing in the displayed original time. The limit \(A\to\infty\) is not uniform when \(\Delta\downarrow0\). The exact period, the Cauchy law, and the coefficient all depend on this normalization. The sign at the two points where \(x=0\) is irrelevant to the probability law.

## Proof
**(1) Periodic foliation.** Since \(p(v)=\beta(v-m)^2+\Delta/(4\beta)>0\), the exact first integral
\[
H(x,v)=x^2/2+K(v)
\]
satisfies \(\dot H=xv+(v/p(v))(-xp(v))=0\). The function \(K\) has its unique minimum zero at the origin, strictly decreases as \(v\) moves from negative infinity towards zero, strictly increases for positive \(v\), and satisfies \(K(v)=\beta^{-1}\log|v|+O(1)\) at both ends. Therefore every level \(H=A^2/2>0\) is a smooth compact oval without equilibria, hence a single periodic orbit.

**(2) The exact time-sampling density.** Write \(E=A^2/2\), and let \(v_-(E)<0<v_+(E)\) solve \(K(v_\pm)=E\). At each interior velocity there are exactly two points on the oval with \(x=\pm\sqrt{A^2-2K(v)}\), and \(|\dot v|=|x|p(v)\). Consequently the time spent per full period in \((v,v+dv)\) is
\[
\frac{2\,dv}{p(v)\sqrt{A^2-2K(v)}}.
\]
With \(w_A(v)=\mathbf1_{\{K(v)<E\}}(1-2K(v)/A^2)^{-1/2}\), set \(Z_A=\int_{\mathbb R}w_A(v)p(v)^{-1}dv\). Exact normalization gives
\[
T(A)=2Z_A/A,\qquad
\mathcal L(V_A)(dv)=\frac{w_A(v)}{Z_Ap(v)}\,dv
=\frac{w_A(v)}{\mathbb E_\nu w_A}\,\nu(dv).
\]
The two \(x\)-sign branches have identical time weights at each velocity. This proves the exact independence and fair-sign property.

**(3) An \(L^1\) density expansion, including the moving endpoints.** Under \(\nu\), the random variable \(U=K(V)\) has density
\[
\frac{g(u)}{I_0},\qquad g(u)=\frac1{v_+(u)}+\frac1{|v_-(u)|},\qquad u>0.
\]
Indeed \(du=v\,dv/p(v)\), treating the negative branch with reversed orientation. Since \(K(v)=\beta^{-1}\log|v|+O(1)\) as \(|v|\to\infty\) and \(K(v)=v^2/2+O(v^3)\) near zero, \(g(u)=O(u^{-1/2})\) near zero and \(g(u)=O(e^{-\beta u})\) at infinity. Therefore every nonnegative integer moment of \(U\) is finite.

On \(0\le U\le A^2/4\), Taylor's formula and a uniform bound on the remainder give
\[
w_A=1+U/A^2+O(U^2/A^4).
\]
On \(A^2/4<U<A^2/2\), integrating \(g(u)(1-2u/A^2)^{-1/2}\) gives an exponentially small contribution in \(A^2\), notwithstanding the integrable endpoint square root. The omitted tail \(U\ge A^2/2\) also has exponentially small \(\nu\)-mass. Thus, as an \(L^1(\nu)\) identity,
\[
w_A=1+K/A^2+O_{L^1(\nu)}(A^{-4}),\qquad
\mathbb E_\nu w_A=1+\bar K/A^2+O(A^{-4}).
\]
Division gives
\[
\frac{d\mathcal L(V_A)}{d\nu}
=1+\frac{K-\bar K}{A^2}+O_{L^1(\nu)}(A^{-4}).
\]
The reverse triangle inequality for the \(L^1\) norm yields the claimed sharp total-variation expansion. The coefficient is positive since \(K\) is not constant.

**(4) The closed symmetric coefficient.** If \(\alpha=0\), put \(\theta=\arctan(\sqrt\beta v)\). Under \(\nu\), \(\theta\) is uniform on \((-\pi/2,\pi/2)\), and \(K(v)=-\beta^{-1}\log\cos\theta\), so \(\bar K=(\log 2)/\beta\). The sign of \(K-\bar K\) changes at \(|\theta|=\pi/3\). Symmetry and the fact that this deviation has mean zero give
\[
C_{0,\beta}=\frac2{\pi\beta}\int_0^{\pi/3}\log(2\cos\theta)\,d\theta
=\frac{\operatorname{Cl}_2(\pi/3)}{\pi\beta},
\]
using \(2\int_0^{\pi/3}\log(2\cos\theta)d\theta=\operatorname{Cl}_2(\pi/3)\).

**(5) Joint concentration.** On the orbit,
\[
D_A=A\big(A-\sqrt{A^2-2K(V_A)}\big)
=\frac{2K(V_A)}{1+\sqrt{1-2K(V_A)/A^2}}.
\]
This converges to \(K(v)\) locally uniformly on the finite velocity axis. Total-variation convergence of \(V_A\) makes its laws tight. Applying bounded-continuous-test-function convergence on compact velocity sets, and using the exact independent sign, proves the stated joint weak limit. No moment convergence for \(D_A\) is required.

## Verification
The file `check_cauchy.py` symbolically differentiates an explicit primitive of \(v/p(v)\), checks the exact Clausen integral and samples the finite-amplitude symmetric total-variation integral. It runs with Python 3, SymPy, SciPy and mpmath. The reported values of \(A^2d_{\rm TV}\) for \(A=3,4,5\) decrease towards the analytic coefficient \(\operatorname{Cl}_2(\pi/3)/\pi\approx0.3230659472\). Finite quadrature checks corroborate but do not establish the asymptotic proof; the moving endpoint is handled analytically in step (3).

## Relationship to prior work
Appis and Llibre (2024), Theorem 4(c), classify the complete positive-discriminant parameter region as a global-center case; they do not state physical-time occupation distributions. Rousseau and Toni (1997) analyze local critical-period coefficients in an equivalent time-reversed reduced Kukles family, not the present whole-orbit occupation probability. The published *Two-term boundary-period law and velocity skew for a cubic global center* (2026) studies this exact same system, including its first integral, period expansion and velocity extrema; these facts are reused here, **not claimed as new**. Its proved scalar period and peak-ratio statements do not specify the time-sampled velocity law, the sharp total-variation coefficient, or the exact fair-sign joint law. A separate Cauchy occupation result for \(\dot x=(1+\kappa x^2)y,\ \dot y=-x\) concerns a different cubic vector field and a different coordinate. The shared Cauchy shape alone is not the same theorem.

## Limitations
The result is for fixed parameters in the strict positive-discriminant regime. No uniform estimate at the discriminant boundary, finite-energy formula for the sharp coefficient, classification of critical periods, or convergence in higher moments of the unbounded velocity is asserted. The exact period quadrature and first integral used here already appear in prior literature; priority is claimed only for the full occupation and quantitative joint distribution statement. An equivalent unpublished or unindexed statistical consequence remains possible. Independent mathematical validation has not been performed.

## References
- Appis, R. F., and Llibre, J. *Global centers of a family of cubic systems*. Aequationes Mathematicae **98** (2024), 1373–1389, first publicly available 2024-04-05, DOI 10.1007/s00010-024-01051-7, open full text: https://ddd.uab.cat/pub/artpub/2024/292038/aeqmat_a2024m4v98.pdf.
- Rousseau, C., and Toni, B. *Local Bifurcations of Critical Periods in the Reduced Kukles System*. Canadian Journal of Mathematics **49** (1997), 338–358, DOI 10.4153/CJM-1997-017-4, open PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/869FA375B7431E8C5C90F156E2795F8F/S0008414X00029060a.pdf/local_bifurcations_of_critical_periods_in_the_reduced_kukles_system.pdf.
- *Two-term boundary-period law and velocity skew for a cubic global center*. published-finding corpus public mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-term-boundary-period-law-and-velocity-skew-for-a-cubic-globa--c61200f602fe.
- *Cauchy time concentration and the order-one moment threshold in a cubic global center*. published-finding corpus public mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cauchy-time-concentration-and-the-order-one-moment-threshold-in--0ac06783efe2.
