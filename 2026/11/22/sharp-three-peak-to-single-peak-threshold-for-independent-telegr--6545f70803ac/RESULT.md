# Sharp three-peak to single-peak threshold for independent telegraph-driven harmonic filters

## Finding

Two independent finite-speed telegraph forces driving identical attracting linear filters exhibit a sharp stationary **shape transition** at switching-to-relaxation ratio \(\alpha=1/2\). At slower switching, their summed response has an infinite central density peak and two infinite *support-boundary* peaks separated by unique valleys. At and above the threshold it has just the central peak. In the slow-switching regime each half-support is strictly log-convex, and the positive valley approaches the right endpoint with a sharp linear law:

\[
\boxed{2-s_\alpha\sim4(1-2\alpha)\quad\text{as }\alpha\uparrow\tfrac12.}
\]

The boundary peaks are divergences of the density, **not atoms** of the stationary probability law. This is a complete shape classification for the symmetric two-channel model, not a claim about unequal filters or larger independent sums.

## Assumptions and scope

Let \(\theta,c,a>0\). Let \(\sigma_1(t),\sigma_2(t)\in\{-1,1\}\) be independent stationary continuous-time Markov sign processes, each switching sign at rate \(a\). Let independent stationary filter responses satisfy

\[
 dY_i(t)=-\theta Y_i(t)\,dt+c\sigma_i(t)\,dt,\qquad i=1,2.
\]

Define \(\alpha=a/\theta\), \(\beta=c/\theta\), and \(S=(Y_1+Y_2)/\beta\). Each normalized stationary coordinate \(Y_i/\beta\) has density

\[
 f_\alpha(x)=C_\alpha(1-x^2)^{\alpha-1}\mathbf1_{\{|x|<1\}},\qquad
 C_\alpha=\frac{\Gamma(\alpha+1/2)}{\sqrt\pi\,\Gamma(\alpha)}.
\]

This one-coordinate beta law is known [1,2]; it is **not** a new component of the finding. Independence makes the stationary sum density \(g_\alpha=f_\alpha*f_\alpha\), even, supported on \([-2,2]\) and positive on the interior. Throughout, mode statements refer to one-sided density behavior on the *closed support*, allowing diverging boundary peaks in the usual extended-density sense. The density is absolutely continuous, with no endpoint mass.

For every \(\alpha>0\), the following hold:

1. If \(0<\alpha<1/2\), then \(g_\alpha\) is strictly log-convex on \((0,2)\), diverges at \(s\downarrow0\) and \(s\uparrow2\), and has exactly one strict minimum \(s_\alpha\in(0,2)\). By evenness, there are exactly two valleys and three divergent density peaks at \(-2,0,2\).
2. If \(\alpha=1/2\), then \(g_\alpha\) is strictly log-convex and strictly decreasing on \((0,2)\); the center still diverges, while each boundary has a finite interior limit.
3. If \(\alpha>1/2\), then \(g_\alpha\) is strictly decreasing on \((0,2)\), continuous and finite at the center, and tends to zero at each boundary.
4. In regime 1, the unique positive valley obeys \(\lim_{\alpha\uparrow1/2}(2-s_\alpha)/(1-2\alpha)=4\). In dimensional coordinates the positive valley is \(\beta s_\alpha\).

## Proof

**1. Exact convolution and fixed-domain representation.** By the known stationary formula [1,2], the two independent normalized coordinates have the beta density above. For \(0<s<2\), convolution only uses \(x\in[s-1,1]\). Put \(t=1-s/2\), \(b=1+s/2\), and \(x=s/2+tu\), \(-1<u<1\). Then the product of the four endpoint distances is \(t^2(1-u^2)(b^2-t^2u^2)\), and \(dx=t\,du\). Thus

\[
 g_\alpha(s)=C_\alpha^2\,t^{2\alpha-1}\int_{-1}^{1}(1-u^2)^{\alpha-1}
 \bigl[b^2-t^2u^2\bigr]^{\alpha-1}\,du.\tag{1}
\]

The integral is finite for every fixed \(0<s<2\), since \(\alpha>0\). Equivalently, writing \(q=(t/b)^2\), Euler's beta integral gives

\[
 g_\alpha(s)=C_\alpha^2 B(1/2,\alpha)\,t^{2\alpha-1}b^{2\alpha-2}
 {}_2F_1(1-\alpha,1/2;\alpha+1/2;q).\tag{2}
\]

**2. A strict convexity lemma.** For fixed \(-1<u<1\), let \(A=1-u^2>0\), \(D=1+u^2\), and

\[
 B_u(s)=b^2-t^2u^2=A+Ds+As^2/4.
\]

It satisfies \(B_u(s)>0\) and \(B_u'(s)=D+As/2>0\). Further,

\[
 B_u(s)B_u''(s)-B_u'(s)^2
 =\frac{A^2}{2}-D^2-\frac{AD}{2}s-\frac{A^2}{8}s^2<0,\tag{3}
\]

because \(0<A\le D\) and \(s>0\). Hence \(\log B_u(s)\) is *strictly concave* for all \(0<s<2\).

For \(0<\alpha\le1/2\), the log of the \(s\)-dependent integrand in (1) is

\[
 (2\alpha-1)\log(1-s/2)+(\alpha-1)\log B_u(s).
\]

The first summand is convex, and the second is strictly convex by (3), since \(\alpha-1<0\). Every integrand is therefore strictly log-convex in \(s\), and so is its positive integral: apply the strict integrand inequality followed by Hölder's inequality to the two endpoint integrals. Thus \(\log g_\alpha\) is strictly convex on \((0,2)\).

**3. Endpoint/central behavior and uniqueness.** Let \(B(\cdot,\cdot)\) denote Euler's beta function. For \(0<\alpha<1/2\), isolating the two overlapping endpoint neighborhoods in the original convolution gives

\[
 g_\alpha(s)\sim 2^{2\alpha-1}C_\alpha^2
 B(\alpha,1-2\alpha)\,s^{2\alpha-1},\quad s\downarrow0.\tag{4}
\]

For every \(\alpha>0\), the endpoint limit from (1) is

\[
 g_\alpha(2-\varepsilon)\sim2^{2\alpha-2}C_\alpha^2
 B(\alpha,\alpha)\,\varepsilon^{2\alpha-1},\quad\varepsilon\downarrow0.\tag{5}
\]

To derive (4), near either endpoint change the local distance variable \(y\) to \(s v\); the limiting positive integral is \(\int_0^\infty v^{\alpha-1}(1+v)^{\alpha-1}\,dv=B(\alpha,1-2\alpha)\), finite precisely when \(\alpha<1/2\). The remaining compact interior contributes only bounded terms. Equation (5) follows directly by the substitution in (1) and dominated convergence, since \(B_u(2)=4\) for all \(u\in(-1,1)\). For \(0<\alpha<1/2\), both (4) and (5) diverge. The continuous, strictly log-convex density therefore has exactly one strict minimizer on \((0,2)\), with derivative negative before and positive after. Evenness gives its negative counterpart and all three singular peaks.

At \(\alpha=1/2\), equation (1) loses its prefactor \(t^{2\alpha-1}\). Since \(B_u'(s)>0\) and \(\alpha-1=-1/2\), the integrand is strictly decreasing with \(s\), so \(g_{1/2}\) is strictly decreasing; it diverges logarithmically at the center by the borderline two-endpoint integral and tends to \(1/(2\pi)\) at \(s\uparrow2\) by (5). For \(1/2<\alpha<1\), both \(t^{2\alpha-1}\) and \(B_u(s)^{\alpha-1}\) in (1) are strictly decreasing in \(s\), giving strict monotonicity. For \(\alpha=1\), convolution of two uniforms yields \(g_1(s)=(2-s)/4\) for \(0<s<2\). For \(\alpha>1\), \(f_\alpha\) is positive, symmetric and strictly decreasing on \((0,1)\). Its superlevel sets are nested centered intervals. The layer-cake representation of the convolution integrates their overlap lengths, which never increase and strictly decrease on a positive-measure family of interval-width pairs for every \(0<s<2\); hence \(g_\alpha\) is strictly decreasing there. When \(\alpha>1/2\), \(\int f_\alpha^2<\infty\), proving a finite center value; (5) proves a zero edge limit.

**4. Sharp valley boundary layer.** Write \(\delta=1-2\alpha>0\), \(\varepsilon=2-s\), \(t=\varepsilon/2\), \(b=2-\varepsilon/2\). The hypergeometric argument in (2) is \(q=(\varepsilon/(4-\varepsilon))^2\). For \(\alpha\) in a fixed compact neighborhood below \(1/2\), the hypergeometric function and its first derivative are uniformly analytic near \(q=0\), with positive value one there. Differentiating (2) with respect to \(\varepsilon\) therefore yields

\[
 \frac{d}{d\varepsilon}\log g_\alpha(2-\varepsilon)
 =-\frac{\delta}{\varepsilon}+\frac{1-\alpha}{b}+O(\varepsilon),\tag{6}
\]

uniformly there. Strict decrease of \(g_{1/2}\) on every compact subset of \((0,2)\), continuity of the derivatives in \(\alpha\), and strict log-convexity for \(\alpha<1/2\) imply \(s_\alpha\uparrow2\). At its unique minimizer (6) vanishes. Hence

\[
 \frac{\delta}{2-s_\alpha}=\frac{1-\alpha}{2-(2-s_\alpha)/2}+O(2-s_\alpha)
 \longrightarrow\frac14,
\]

and consequently \(2-s_\alpha\sim4(1-2\alpha)\). This completes all regimes, quantifiers, and the threshold.

## Verification

The reproducibility script `checker.py` uses exact fractions to confirm the strict sign in (3) on 429 rational parameter pairs, evaluates the convergent hypergeometric expansion in (2), checks logarithmic convexity for representative subcritical ratios, verifies the triangular law at \(\alpha=1\), tests strict decrease for critical/supercritical ratios below one, and brackets the unique valleys and their boundary scaling. It reports 1,341 successful finite conditions. These computations are consistency checks only; equations (1)–(6) constitute the proof for all real \(\alpha>0\). Execute from the package directory using `python checker.py` (Python 3, standard library only).

## Relationship to prior work

Duong, Auffenberg and Steidl [1, Theorem 3.2], building on Ratanov [2,5], identify the stationary symmetric Beta law for **one** finite-speed OU-K coordinate and its convergence. Our claim begins *after* that known law, with the shape and critical-rate analysis for a sum of two independent stationary coordinates. Ratanov [2, Section 4] concerns invariant distributions of a single two-state-modulated process. Kolesnik [3] studies a sum of independent unfiltered telegraph *positions* at fixed time, not the sum of stationary linearly filtered responses. The convolution theorem of Lefèvre and Utev [4] concerns **symmetric unimodal** summands, and thus explains general monotonicity only when the individual Beta density is already unimodal; it does not imply the subcritical three-peak phase or the new transition at \(\alpha=1/2\).

Searches for symmetric Beta convolution modality, telegraph-filter sums and their shape transitions did not identify the specific sharp threshold and boundary-layer law. A published stronger theorem or classical special-function identity may nonetheless have implicitly established them; no claim of exhaustive historical priority is made.

## Limitations

Identical speeds, relaxation rates and switching rates, independence of driving telegraph chains, stationarity and symmetric two-state rates are essential to the asserted classification. The theorem is not a claim for shared drivers, unequal rates, finite-time distributions or three or more filters. Boundary peaks are density singularities, not probability point masses. This is an analytical result with finite numerical cross-checks, not an externally validated proof. The full publisher version [5] was inaccessible; its related open preprint [2] and the later open source [1] were read, but hidden implications in the publisher version remain an explicit originality risk.

## References

1. R. Duong, J. Auffenberg and G. Steidl, *Finite speed Ornstein-Uhlenbeck-Kac processes and their applications in generative modeling*, arXiv:2611.17625v1, first posted 2026-11-13, Theorem 3.2, https://arxiv.org/abs/2611.17625.
2. N. Ratanov, *First-passage probabilities and invariant distributions of Kac-Ornstein-Uhlenbeck processes*, arXiv:2102.13308, Section 4, https://arxiv.org/abs/2102.13308.
3. A. D. Kolesnik, *The explicit probability distribution of the sum of two telegraph processes*, arXiv:1402.6866, https://arxiv.org/abs/1402.6866.
4. C. Lefèvre and S. Utev, *Convolution property and exponential bounds for symmetric monotone densities*, ESAIM: Probability and Statistics **17** (2013), 605–613, https://doi.org/10.1051/ps/2012012.
5. N. Ratanov, *Kac-Ornstein-Uhlenbeck Processes: Stationary Distributions and Exponential Functionals*, Methodology and Computing in Applied Probability **24** (2022), 2703–2721, https://doi.org/10.1007/s11009-022-09956-z (full text not accessed).
