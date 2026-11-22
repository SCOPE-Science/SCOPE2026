# Short-pulse resonance and a quadratic Poisson boundary law for fractional circle smoothing

## Finding
For every real exponent \(1<\alpha<2\), let \(T_{\alpha,t}\) be the periodic fractional-heat semigroup with Fourier multipliers \(\exp[-t(2\pi |n|)^\alpha]\). On the probability circle \(\mathbb T=\mathbb R/\mathbb Z\) define the sharp squared bounded-variation approximation error
\[
C_{\alpha,t}^2=\sup_{f\in BV(\mathbb T;\mathbb R),\,V(f)>0}
\frac{\|f-T_{\alpha,t}f\|_{L^2(\mathbb T)}^2}{V(f)^2}.
\]
For all \(t>0\), the exact finite-time sharp constant is the attained one-variable maximum
\[
C_{\alpha,t}^2=\max_{0\le d\le1/2}
\frac{1}{2\pi^2}\sum_{n=1}^{\infty}
\frac{(1-e^{-t(2\pi n)^\alpha})^2\sin^2(\pi nd)}{n^2}.
\tag{1}
\]
Every maximizing arc indicator (plus constants and nonzero scalar factors) attains this operator norm; no classification of all possible equality functions is asserted.

Define, for \(u>0\),
\[
g_\alpha(u)=\frac{(1-e^{-u^\alpha})^2}{u^2},\qquad
F_\alpha(z)=\int_0^\infty g_\alpha(u)\cos(zu)\,du,
\]
\[
B_\alpha=\frac{\Gamma(1-1/\alpha)}{\pi}
\left(1-2^{1/\alpha-1}\right),\qquad
M_\alpha=B_\alpha-\frac{1}{2\pi}\min_{z\ge0} F_\alpha(z).
\tag{2}
\]
The minimum in (2) is strictly negative and attained in a nonempty compact subset of \((0,\infty)\). With \(h=t^{1/\alpha}\),
\[
\boxed{\displaystyle \lim_{t\downarrow0} C_{\alpha,t}^2/h=M_\alpha>B_\alpha.}
\tag{3}
\]
If \(d_t\in[0,1/2]\) maximizes (1), its rescaled position \(d_t/h\) remains in a compact subset of \((0,\infty)\) for sufficiently small \(t\); every limit point minimizes \(F_\alpha\).

More sharply, for \(\varepsilon=\alpha-1\downarrow0\),
\[
\boxed{\displaystyle
\frac{M_{1+\varepsilon}-B_{1+\varepsilon}}{\varepsilon^2}
\longrightarrow\frac\pi8,
\qquad
\varepsilon z_\varepsilon\longrightarrow\frac2\pi
}\tag{4}
\]
for **every** minimizer \(z_\varepsilon\) of \(F_{1+\varepsilon}\). At the Poisson endpoint \(\alpha=1\), \(F_1(z)>0\) for every finite \(z\ge0\), and \(\inf_{z\ge0}F_1(z)=0\) is attained only at infinity. Thus the finite short-pulse advantage begins at \(\alpha>1\) with a sharp quadratic onset, while the preferred rescaled pulse length diverges like \(2/[\pi(\alpha-1)]\) as the boundary is approached. These are successive limits: first small time at fixed exponent, then exponent approaching one.

## Assumptions and scope
The domain has length one, ordinary Lebesgue probability measure, and Fourier conventions \(\widehat f(n)=\int_0^1 f(x)e^{-2\pi inx}\,dx\). The periodic distributional derivative \(Df\) is a finite signed real measure of total mass zero and \(V(f)=|Df|(\mathbb T)\). The operator is positive and conservative for the stated stable exponents, but the proof of the sharp variational reduction requires only linearity, translation invariance and the stated Fourier multipliers. The fixed exponent is strictly between one and two; the boundary statement is one-sided at one. The parameter \(t\) is positive and unconstrained in (1). A circular arc has ordinary length \(d\), and its complement gives the same residual norm, so \(d\) can be restricted to \([0,1/2]\).

## Proof
**1. Reduction from all bounded-variation functions to arcs.** Let \(\mu=Df\), \(v=|\mu|(\mathbb T)>0\), and \(\mu=\mu^+-\mu^-\); each positive part has mass \(v/2\), since \(\mu(\mathbb T)=0\). Couple the two probability measures \(2\mu^+/v\) and \(2\mu^-/v\) by a probability measure \(\pi\). For any ordered pair \((a,b)\), a signed, oriented circular arc indicator \(\mathbf 1_{(a,b)}\) has derivative \(\delta_a-\delta_b\). Thus, modulo an additive constant,
\[
f=\frac v2\int\mathbf 1_{(a,b)}\,d\pi(a,b).
\]
The Bochner integral is valid in \(L^2\). Because \(I-T_{\alpha,t}\) kills constants, the triangle inequality gives
\[
\frac{\|(I-T_{\alpha,t})f\|_2}{v}
\le\frac12\sup_{\text{arcs }I}\|(I-T_{\alpha,t})\mathbf1_I\|_2.
\]
Each nontrivial arc has variation exactly two and attains the right-hand ratio. For length \(d\), the nonzero Fourier coefficients of its indicator have squared modulus \(\sin^2(\pi nd)/(\pi^2n^2)\). Parseval proves (1), uniform convergence in \(d\), and existence of an optimal arc.

**2. The stable short-time scaling.** Put \(h=t^{1/\alpha}\) and write the single-arc ratio in (1) as
\[
R_{\alpha,h}(d)=h^2\sum_{n\ge1}
 g_\alpha(2\pi nh)\,[1-\cos(2\pi nd)].\tag{5}
\]
For \(\alpha>1\), \(g_\alpha(0)=0\), \(g_\alpha\in W^{1,1}(0,\infty)\), and \(g_\alpha(u)=O(u^{-2})\) at infinity. If \(d/h\to z\in[0,\infty)\), Riemann-sum convergence in (5), uniform for \(z\) on compact intervals, yields
\[
R_{\alpha,h}(d)/h\longrightarrow E_\alpha(z)
=\frac1{2\pi}\int_0^\infty g_\alpha(u)[1-\cos(zu)]\,du
=B_\alpha-\frac{F_\alpha(z)}{2\pi}.\tag{6}
\]
Integration by parts in the integral of \(g_\alpha\) and the Gamma integral gives
\[
\int_0^\infty g_\alpha(u)\,du
=2\Gamma(1-1/\alpha)(1-2^{1/\alpha-1}),
\]
which proves the stated normalization \(B_\alpha\). If instead \(d/h\to\infty\) with \(d\le1/2\), summation by parts using the integrable derivative of \(g_\alpha\) gives
\[
\left|h\sum_{n\ge1}g_\alpha(2\pi nh)e^{2\pi ind}\right|
\le \frac{C_\alpha h}{\sin(\pi d)}=O(h/d)\to0.
\]
Together with the nonoscillatory Riemann sum this yields \(R_{\alpha,h}(d)/h\to B_\alpha\).

**3. A negative cosine tail forces interacting jumps.** Near the origin,
\[
g_\alpha(u)=u^{2\alpha-2}-u^{3\alpha-2}+O(u^{4\alpha-2}).
\]
The standard cut-off power Fourier identity, obtainable by exponential damping and repeated integration by parts, reads
\[
\int_0^\infty \chi(u)u^p\cos(zu)\,du
=-\Gamma(p+1)\sin(\pi p/2)z^{-p-1}
+o(z^{-p-1})
\]
for a smooth compact cutoff equal to one near zero and \(p>-1\) away from even nonnegative integers (the zero coefficient cases follow by continuity). Applying it termwise, and bounding the smoother remainder, gives for any fixed \(1<\alpha<2\)
\[
F_\alpha(z)
=\Gamma(2\alpha-1)\sin(\pi\alpha)z^{1-2\alpha}
+o(z^{1-2\alpha})\quad(z\to\infty).\tag{7}
\]
Since \(\sin(\pi\alpha)<0\), the transform is negative for large finite \(z\), while \(F_\alpha(0)>0\) and \(F_\alpha(z)\to0\). Hence its negative global minimum occurs on a nonempty compact subset of \((0,\infty)\). Equation (6) and the alternative diverging-separation limit now prove (3) by a maximizing-sequence argument. The same strict comparison forces all maximizing \(d/h\) into a compact subset of \((0,\infty)\); its limit points belong to the stated minimum set.

**4. Uniform critical Fourier expansion.** Let \(\varepsilon=\alpha-1\) and fix a sufficiently small \(\eta>0\). With one smooth compact cutoff \(\chi\) equal to one near zero, decompose
\[
g_\alpha(u)=\chi(u)u^{2\alpha-2}
-\chi(u)u^{3\alpha-2}+r_\alpha(u).
\]
For \(1\le\alpha\le1+\eta\), the remainder has a uniformly bounded \(L^1\) third derivative: at zero its first unused power is \(u^{4\alpha-2}\), whose third derivative is integrable with uniformly bounded integral (including the coefficient vanishing at the integer endpoint); at infinity it is \(O(u^{-2})\) with corresponding derivative decay. Three integrations by parts, including vanishing boundary terms, give a uniform \(O(z^{-3})\) cosine-transform remainder. The cutoff-power identity therefore gives, uniformly in this exponent range for \(z\ge1\),
\[
F_\alpha(z)=
-\Gamma(2\alpha-1)\sin[\pi(\alpha-1)]z^{1-2\alpha}
+\Gamma(3\alpha-1)\sin[\pi(3\alpha-2)/2]z^{1-3\alpha}
+O(z^{-3}).\tag{8}
\]
For \(z=u/\varepsilon\) with \(u\) in a fixed compact subset of \((0,\infty)\), divide by \(\varepsilon^2\). Uniformly on such sets,
\[
\frac{F_{1+\varepsilon}(u/\varepsilon)}{\varepsilon^2}
\longrightarrow \phi(u)=\frac1{u^2}-\frac\pi u.\tag{9}
\]
The unique global minimum of \(\phi\) is \(-\pi^2/4\), at \(u=2/\pi\).

To justify unrestricted minimizers, observe that
\[
g_1(u)=\int_0^1\!\int_0^1e^{-(s+r)u}\,ds\,dr,
\quad F_1(z)=\int_0^1\!\int_0^1\frac{s+r}{(s+r)^2+z^2}\,ds\,dr>0
\]
for every finite \(z\). Convergence of \(F_\alpha\) to \(F_1\) is uniform on compact \(z\)-sets. A negative minimizing sequence \(z_\varepsilon\) must therefore diverge. Expansion (8) shows that \(F_{1+\varepsilon}(z)>0\) if \(z\to\infty\) but \(\varepsilon z\to0\), since its positive \(z^{-2-3\varepsilon}\) term dominates both the \(O(\varepsilon z^{-1-2\varepsilon})\) term and the remainder. If \(\varepsilon z\to\infty\), (8) gives \(F_{1+\varepsilon}(z)=o(\varepsilon^2)\), strictly less negative than the test value from (9). Thus all minimizers have \(\varepsilon z\) confined between two positive finite constants; (9) forces every limit point to be \(2/\pi\), and the minimal value to be \(-\pi^2\varepsilon^2/4+o(\varepsilon^2)\). Formula (2) proves (4).

## Verification
Run `python CHECKER.py` with Python 3, NumPy and SciPy to repeat 39 numeric/identity assertions, including quadrature for the cosine transform, Gamma normalization, strict negative Fourier tails, finite-circle Parseval series versus FFT, and the critical limit trend at three exponents. The checker is a finite independent numerical consistency test; the all-parameter and infinite-series assertions follow from the proof, not from sampling. The comparisons of two singular limits are **successive**, and the claimed uniform Fourier expansion is local to the Poisson endpoint.

## Relationship to prior work
Roncal and Stinga (arXiv:1209.6104, publicly available September 27, 2012) develop fractional Laplacians and semigroup regularity on tori, including pointwise and Hölder formulas, but their inspected arguments do not state a sharp periodic \(BV\)-to-\(L^2\) residual norm or the optimization of interacting jumps. Ponce and Spector (arXiv:1603.08663, March 29, 2016) study nonlocal limits that extract the singular part of \(Df\), including a fractional-Laplacian \(L^1\) endpoint; their theorem has different functionals, norm and limiting parameter. Knopova (2022) proves Besov/Triebel–Lizorkin smoothing bounds for subordinated semigroups, not this exact sharp variation-residual constant. Earlier analyses of Poisson-type and classical heat endpoints do not imply the full intermediate-exponent strict short-pulse advantage or the quadratic boundary coefficient. These are statement-level comparisons, not assertions of exhaustive historical priority.

## Limitations
The result excludes the Gaussian endpoint \(\alpha=2\) from (3) and proves no uniqueness of the short-pulse optimizer at a fixed interior exponent. For general real inputs, arcs are guaranteed sharp extremizers, not necessarily the *only* ones. The critical law involves sequential parameter limits, not a two-parameter uniform theorem. The cosine-integral minimization in (2) is an exact variational characterization; no elementary closed form is claimed for its minimizer at arbitrary interior exponent. Unindexed or inaccessible past work may contain an equivalent theorem; no independent audit has been performed.

## References
- L. Roncal and P. R. Stinga, *Fractional Laplacian on the torus*, first public arXiv version September 27, 2012, https://arxiv.org/abs/1209.6104.
- A. C. Ponce and D. Spector, *On formulae decoupling the total variation of BV functions*, first public arXiv version March 29, 2016, https://arxiv.org/abs/1603.08663.
- V. Knopova, *Bochner's subordination and fractional caloric smoothing in Besov and Triebel–Lizorkin spaces*, Mathematische Nachrichten 295 (2022), https://doi.org/10.1002/mana.202000061.
