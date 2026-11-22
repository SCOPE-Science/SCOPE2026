# A sharp positivity bifurcation for spectral powers of squared-cosine circle Markov kernels

## Finding
For every real \(0<\rho\le1\), convolution by the strictly normalized nonnegative circle kernel
\[
J_\rho(\theta)=\frac{(1+\rho\cos\theta)^2}{1+\rho^2/2}
\]
is a selfadjoint finite-rank Markov operator \(M_\rho\) on real or complex \(L^2(\mathbb T,d\theta/(2\pi))\). Its canonical nonzero-time spectral powers have a **complete positivity phase diagram**. There exists a unique \(\rho_c\in(0,1)\), approximately \(0.966626615582544742\), such that:

* If \(0<\rho\le\rho_c\), \(M_\rho^t\) preserves nonnegative functions exactly for \(t\in[t_-(\rho),\infty)\).
* If \(\rho_c<\rho\le1\), positivity holds exactly for \(t\in[t_-(\rho),u(\rho)]\cup[v(\rho),\infty)\), with \(t_-(\rho)<1\le u(\rho)<v(\rho)\). For \(\rho<1\) the first inequality \(1<u(\rho)\) is strict; at \(\rho=1\), \(u(1)=1\).

The two upper endpoints meet at a **square-root fold** as \(\rho\downarrow\rho_c\), with the same positive, explicitly defined constant on both branches. This is a sharp two-parameter statement rather than a single example of positivity loss.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with Haar probability measure. The spectral convention is \(0^t=0\) for every \(t>0\). Write
\[
a(\rho)=\frac{\rho}{1+\rho^2/2},\qquad
b(\rho)=\frac{\rho^2}{4+2\rho^2},\qquad
c(\rho)=\frac{\log a(\rho)}{\log b(\rho)}.
\]
Thus \(0<b<a<1\) and \(0<c<1/2\). Define
\[
t_0(\rho)=\frac{\log4}{\log(4/\rho)},\quad
F_\rho(t)=1-2a(\rho)^t+2b(\rho)^t,\quad
t_*(\rho)=\frac{\log(\log b(\rho)/\log a(\rho))}{\log(a(\rho)/b(\rho))}.
\]
There is a unique \(c_*\in(0,1/2)\) such that
\[
2(1-c_*)c_*^{c_*/(1-c_*)}=1,
\]
and \(\rho_c\) is the unique solution of \(c(\rho_c)=c_*\). Numerically \(c_*\approx0.227092195219348187\) and \(t_*(\rho_c)\approx1.043768636269559367\).

The first endpoint \(t_-(\rho)\in(0,t_0(\rho))\) is the unique root of
\[
1-2b(\rho)^t-\frac{a(\rho)^{2t}}{4b(\rho)^t}=0.
\]
For \(\rho>\rho_c\), the other endpoints \(u(\rho)<t_*(\rho)<v(\rho)\) are the two roots of \(F_\rho(t)=0\) in \([t_0(\rho),\infty)\). At \(\rho=1\), \(t_-(1)\approx0.9349375548491513\), \(u(1)=1\), and \(v(1)\approx1.1477203812370144\).

## Proof
The Fourier coefficients of \(J_\rho\) are \(1\) in degree zero, \(a\) in degrees \(\pm1\), \(b\) in degrees \(\pm2\), and zero elsewhere. Therefore \(M_\rho^t\) has continuous convolution kernel
\[
J_{\rho,t}(\theta)=1+2a^t\cos\theta+2b^t\cos2\theta.
\]
For a continuous convolution kernel, positivity preservation on \(L^2\) is equivalent to its pointwise nonnegativity: necessity follows by testing nonnegative approximate identities at a point of negative kernel value.

Putting \(x=\cos\theta\in[-1,1]\) gives the strictly convex quadratic \(1-2b^t+2a^tx+4b^tx^2\). Its vertex is \(x=-a^t/(4b^t)\); hence its exact minimum is
\[
\min_\theta J_{\rho,t}(\theta)=
\begin{cases}
1-2b^t-a^{2t}/(4b^t),&0<t\le t_0(\rho),\\
1-2a^t+2b^t,&t\ge t_0(\rho).
\end{cases}
\]
The branches agree at \(t_0\). The first branch has strictly negative second derivative because \(b<1\) and \(a^2/b>1\). Its limit as \(t\downarrow0\) is \(-5/4\). At \(t=t_0\), it equals \(1-6b^{t_0}\), nonnegative, with equality only at \(\rho=1\). To verify this boundary inequality, put \(x=-\log\rho\ge0\), \(h(x)=\log(1+e^{-2x}/2)\), and \(L=\log4\). Then \(-\log b=2x+L+h(x)\), and \((-\log b)/(x+L)\) is strictly greater than \(\log6/L\) for \(x>0\): the difference after clearing positive denominators is \((2-\log6/L)x+h(x)-\log(3/2)\), whose derivative is strictly positive since \(h'\ge-2/3\) and \(2-\log6/L-2/3>0\). Thus the first branch has exactly one zero, \(t_-\), with the claimed signs.

For the second branch, put \(q=b^t\in(0,1)\). Then
\[
F_\rho(t)=1-2q^{c(\rho)}+2q.
\]
It is strictly convex in \(q\), with unique unrestricted minimum at \(q=c^{1/(1-c)}\), of value \(1-2(1-c)c^{c/(1-c)}\). The factor \(2(1-c)c^{c/(1-c)}\) is strictly decreasing in \(c\), as the logarithmic derivative is \(\log c/(1-c)^2<0\). The map \(\rho\mapsto c(\rho)\) is strictly decreasing. Indeed, for \(x=-\log\rho\),
\[
c=\frac{x+h(x)}{2x+h(x)+L},\quad
\frac{dc}{dx}=\frac{L-h(x)+h'(x)(x+L)}{(2x+h(x)+L)^2}>0,
\]
since the numerator starts positive at zero and its derivative is \(h''(x)(x+L)>0\). Consequently the minimum crosses zero at exactly one \(\rho_c\), characterized above.

For \(\rho\ge\rho_c\), the minimizer \(t_*(\rho)>1\ge t_0(\rho)\). One elementary way to check the strict first inequality is that \(t_*(\rho)=\int_0^1[(1-s)(-\log a)+s(-\log b)]^{-1}ds\) increases with \(\rho\), while already \(t_*(19/20)>1\); and \(\rho_c>19/20\), as follows by inserting \(19/20\) into the displayed strict convex minimum (the positive margin exceeds \(10^{-3}\)). Also \(F_\rho(1)=(1-\rho)^2/(1+\rho^2/2)\ge0\). The one-minimum shape of \(F_\rho\), together with its positive limit as \(t\to\infty\), now proves every stated positivity interval and the endpoint inclusion rules.

At \((\rho_c,t_c)=(\rho_c,t_*(\rho_c))\), \(F=F_t=0\), \(F_{tt}>0\), and \(F_\rho<0\). Taylor expansion and the implicit-function theorem after introducing a square-root parameter give
\[
u(\rho)=t_c-K\sqrt{\rho-\rho_c}+O(\rho-\rho_c),\qquad
v(\rho)=t_c+K\sqrt{\rho-\rho_c}+O(\rho-\rho_c),
\]
where
\[
K=\sqrt{-\frac{2\partial_\rho F_{\rho_c}(t_c)}{\partial_{tt}F_{\rho_c}(t_c)}}
\approx0.4419236913915855.
\]
The derivative signs follow from \(a',b'>0\), \(b'/a'=\rho/(2-\rho^2)\le1\), \(b/a=\rho/4<1\), and \(t_c>1\). Explicitly \(F_{tt}(t_c)=2(-\log a)a^{t_c}(\log(a/b))>0\). This completes the classification.

## Verification
A standalone `checker.py` uses arbitrary-precision arithmetic to bracket the unique threshold, compute the fold, test the two exact minimum branches against their quadratic minimizers, and test all sampled points on the cosine interval for representative parameters. Its sampled checks passed. The infinite-dimensional positivity equivalence and uniqueness claims rest on the analytic proof, not on finite sampling. All quantitative approximations are labeled as such.

## Relationship to prior work
Fejér-type nonnegative trigonometric kernels motivate the squared-cosine density; however spatial integer powers of a kernel and operator-theoretic fractional spectral powers are distinct operations. Existing work on locally eventually positive \(C_0\)-semigroups concerns asymptotic positivity and generator spectra; in contrast, this finite-rank spectral-power family is not strongly continuous at zero on the full \(L^2\) space. A previously studied quadratic Bernstein–Durrmeyer operator has disconnected positivity times, but the present convolution family has a different Fourier spectrum and a new global parameter threshold and square-root merger. Statements from close published summaries do not imply this two-parameter classification.

## Limitations
No claim is made for arbitrary trigonometric polynomials, other Fourier bands, or strong continuity at time zero. The proof establishes the phase diagram for \(0<\rho\le1\) and \(t>0\) only. Literature searches and comparisons cannot establish comprehensive historical priority; related spectral-functional-calculus and probability-kernel treatments may exist.

## References
- J. Mui, *Spectral properties of locally eventually positive operator semigroups*, arXiv:2210.06135 (first public posting 2022-10-12); open-access journal version, *Semigroup Forum* 106 (2023), 460–480, doi:10.1007/s00233-023-10347-0.
- Classical Fejér kernel and nonnegative Fourier summability kernels, https://en.wikipedia.org/wiki/Fej%C3%A9r_kernel.
- *Sharp rough-input Lipschitz norms of powered Fejér–Jackson kernels* (published result; distinguished spatial powers), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rough-input-lipschitz-norms-of-powered-fej-r-jackson-kerne--cf9850093a62.
- *Exact Fejér–Riesz positivity and universal criticality for sum-modulated circle heat kernels* (published result; distinct positive-definiteness problem), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-fej-r-riesz-positivity-and-universal-criticality-for-sum-m--e633380c7a14.
