# A first-order sampling-site transition for sparse weighted Bergman kernel approximation

## Finding

The one-kernel approximation of the sparse analytic polynomial \(f_a(z)=1+a z^m\) in a standard weighted Bergman space exhibits a sharp dichotomy between degree two and every higher degree. Fix \(\alpha>-1\), \(\beta=\alpha+2>1\), an integer \(m\ge2\), and \(a\ge0\). Minimize \(\|f_a-cK_\beta(\cdot,w)\|^2\) over \(w\in\mathbb D\) and \(c\in\mathbb C\), where \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\).

For \(m=2\), the center \(w=0\) is the unique optimal site when \(0\le a\le\beta/2\). For \(a>\beta/2\), precisely two sites are optimal, at \(w=\pm\sqrt{x_a}\), with
\[
x_a=\frac{2a-\beta}{a(\beta+2)}.
\]
They approach the origin continuously as \(a\downarrow\beta/2\).

For every integer \(m\ge3\), write \(q=m/2\) and \(v=\beta/2\). There is a unique interior root \(y_*\in(0,1)\) of
\[
q y(1-y^v)=v(1-y).
\]
Set \(x_*=1-y_*\) and
\[
a_c=\frac{y_*^{-v}-1}{(1-y_*)^q}.
\]
If \(0\le a<a_c\), the unique optimal site is the origin. At \(a=a_c\), exactly \(m+1\) sites are optimal: the origin and the \(m\) equally spaced points of radius \(\sqrt{x_*}\) with \(w^m>0\). If \(a>a_c\), exactly \(m\) nonzero equally spaced sites are optimal, of squared radius \(x_+(a)\), where \(x_+(a)\) is the larger positive solution of
\[
a x^{m/2-1}\bigl[m-(m+\beta)x\bigr]=\beta.
\]
In particular, the globally optimal radius jumps from zero to \(\sqrt{x_*}>0\) at the critical amplitude. The optimal captured squared norm has a positive right derivative and zero left derivative there.

There is also a sharp metastability threshold
\[
x_{\mathrm{sn}}=\frac{m-2}{m+\beta},\qquad a_{\mathrm{sn}}=\frac\beta2\left(\frac{m+\beta}{m-2}\right)^{(m-2)/2}<a_c.
\]
When \(a_{\mathrm{sn}}<a<a_c\), a noncentral strict local maximum already exists but remains strictly inferior to the origin; at \(a=a_{\mathrm{sn}}\) the two interior stationary points merge into one horizontal inflection. The noncentral maximizing branch is unique among positive-radius local maxima.

For the ordinary unweighted Bergman space \(\beta=2\) and \(m\ge3\),
\[
x_*=1-\frac2m,\qquad a_c=\frac m2\left(1-\frac2m\right)^{1-m/2}.
\]
In the first discontinuous case \(m=3,\beta=2\), the saddle-node is at \(a_{\mathrm{sn}}=\sqrt5\), whereas the global switch occurs later at \(a_c=3\sqrt3/2\) with squared optimal radius \(x_*=1/3\).

For every fixed \(\beta>1\) as \(m\to\infty\),
\[
m(1-x_*)\to\beta,\qquad a_c\sim(em/\beta)^{\beta/2},\qquad a_{\mathrm{sn}}\to (\beta/2)e^{(\beta+2)/2}.
\]
Consequently, the interval of metastability grows without bound in amplitude, with \(a_c/a_{\mathrm{sn}}\to\infty\).

## Assumptions and scope

The domain is the open disk \(\mathbb D\), with Hilbert norm determined by the weighted probability measure
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy,\qquad\alpha>-1.
\]
The kernel is \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\), with \(\beta=\alpha+2\). The scalar coefficient in the approximant is unrestricted complex; the polynomial coefficient \(a\) is real and nonnegative. For a general nonzero complex coefficient, a rotation gives the corresponding rotated optimal-site orbits. The theorem concerns one kernel, not approximation by multiple kernel atoms or derivative kernels.

The monomials are orthogonal, with \(\|z^m\|^2=m!/(\beta)_m\), where \((\beta)_m=\beta(\beta+1)\cdots(\beta+m-1)\). Thus \(\|f_a\|^2=1+a^2m!/(\beta)_m\). In every case the unique optimal scalar for a specified site is
\[
c_w=(1+a w^m)(1-|w|^2)^\beta.
\]
The minimum approximation error is \(\|f_a\|^2\) minus the maximum captured norm listed below.

## Proof

**1. Orthogonal projection and phase reduction.** The one-dimensional orthogonal projection onto the span of \(K_\beta(\cdot,w)\) captures squared norm
\[
\frac{|f_a(w)|^2}{K_\beta(w,w)}=|1+a w^m|^2(1-|w|^2)^\beta.
\]
For \(a>0\) and \(w\ne0\), equality in the triangle inequality \(|1+a w^m|\le1+a|w|^m\) holds precisely when \(w^m\) is positive real. Put \(x=|w|^2\), \(q=m/2\). The globally reduced objective, continuous up to \(x=1\), is
\[
F_a(x)=(1+a x^q)^2(1-x)^\beta,\qquad 0\le x\le1.
\]
It satisfies \(F_a(0)=1\), \(F_a(1)=0\). All nonzero optimal phases are the \(m\)-th roots of unity.

**2. Degree-two continuous onset.** When \(q=1\), the logarithmic derivative of \(F_a\) has the sign of
\[
2a-\beta-a(2+\beta)x.
\]
Hence for \(a\le\beta/2\) the center uniquely maximizes; for larger \(a\), precisely one positive radial maximizer occurs at the claimed \(x_a\). The site count follows from phase locking.

**3. Stationary points and metastability for \(q>1\).** At positive \(x\), the derivative has the sign of
\[
a g(x)-\beta,\qquad g(x)=x^{q-1}[m-(m+\beta)x].
\]
On \((0,m/(m+\beta))\) the positive function \(g\) first strictly increases, then strictly decreases, with a unique maximum at \(x_{\mathrm{sn}}=(m-2)/(m+\beta)\). At that point \(g(x_{\mathrm{sn}})=2x_{\mathrm{sn}}^{q-1}\), yielding \(a_{\mathrm{sn}}=\beta/g(x_{\mathrm{sn}})\). Before the threshold no stationary point exists and \(F_a\) strictly decreases. At equality the sole stationary point has no change of derivative sign. Above it, the smaller stationary point is a strict local minimum and the larger is a strict local maximum. The center remains a strict one-sided local maximum for every \(a\), since \(q>1\) gives \(F_a'(0^+)=-\beta<0\).

**4. Unique global crossing.** At any \(0<x<1\),
\[
F_a(x)>1\quad\Longleftrightarrow\quad a>A(x),\qquad A(x)=\frac{(1-x)^{-v}-1}{x^q},\quad v=\beta/2.
\]
For \(q>1\), \(A(x)\to\infty\) at both endpoints. Writing \(y=1-x\), differentiation shows that its interior critical-point equation is
\[
H(y)=q y(1-y^v)-v(1-y)=0.
\]
Here \(H(0)=-v<0\), \(H(1)=0\), \(H'(1)=v(1-q)<0\), and \(H''(y)=-qv(v+1)y^{v-1}<0\) for \(0<y<1\). Therefore \(H\) has exactly one zero in the open interval. To see this directly, strict concavity makes its derivative strictly decreasing; positivity immediately left of \(1\) and negativity at \(0\) allow exactly one interior crossing. The endpoint blow-up makes \(x_*=1-y_*\) the unique global minimizer of \(A\). Thus \(a_c=\min A\) is the exact first value permitting a positive-radius site to match or beat the center, and the tie occurs only at \(x_*\). At the tie, \(x_*\) is the larger stationary root (a strict local maximum, because it is a global maximizer and \(F_a\) has only one positive-radius local maximum). This implies \(a_c>a_{\mathrm{sn}}\). For \(a>a_c\), the larger stationary point is the only possible nonzero global maximum, exceeds the center, and determines all \(m\) optimal phases.

For the positive-radius branch at its crossing, differentiation of the objective with respect to \(a\) gives
\[
\left.\frac{\partial F_a(x)}{\partial a}\right|_{(a_c,x_*)}
=2x_*^q(1+a_cx_*^q)(1-x_*)^\beta
=2x_*^q(1-x_*)^{\beta/2}>0.
\]
Since the center value is identically \(1\), the maximum captured norm has a genuine one-sided derivative jump.

**5. Exact unweighted formula and asymptotics.** When \(\beta=2\), the unique interior root of \(q y(1-y)=1-y\) is \(y=1/q=2/m\); substitution gives the stated formulas. At fixed \(\beta>1\) with \(q=m/2\to\infty\), for every fixed \(\varepsilon\in(0,1)\), \(H(\varepsilon)>0\) eventually, so the unique interior zero satisfies \(y_*<\varepsilon\). Thus \(y_*\to0\) and the defining equality yields \(q y_*\to v\). It follows that \(m y_*\to\beta\), \((1-y_*)^q\to e^{-v}\), and \(y_*^{-v}-1\sim(m/\beta)^v\), which proves \(a_c\sim(em/\beta)^v\). Finally, substituting the explicit \(a_{\mathrm{sn}}\) and taking logarithms gives its finite positive limit \((\beta/2)e^{(\beta+2)/2}\), and hence the diverging ratio.

## Verification

The file `check.py` uses only the Python standard library to evaluate the defining criticality equations, phase-locked objective, stationary points, the strict spinodal/transition order, the special unweighted expressions, and finite large-degree asymptotics for selected real parameters. It reports 428 finite diagnostics passed. The proof above, rather than finite sampling, justifies all quantified statements. Reproduction: run `python check.py` with Python 3.

## Relationship to prior work

The general best-kernel-existence framework in Qu–Qian–Deng (2020) establishes existence but no sharp global radial and angular phase classification for the sparse family here. Qu–Qian–Li–Zhu (2022), Section 5, equation (9) and Theorem 14, explicitly reduces the one-kernel Bergman problem to a weighted pointwise maximum and discusses nonuniqueness for pure monomials, but does not provide the binomial global transition, spinodal window, or large-degree law. Qu–Dang (2018) develops Bergman rational orthogonal systems and adaptive approximation, as distinct from this exact sparse one-atom phase diagram. The separate Qu–Dang (2019) algorithmic journal paper has relevant methodology, but its complete text could not be inspected; its potential examples remain a priority uncertainty.

A related published result about binomial *Hankel operator kernel tests* concerns a different extremal functional, and a two-kernel sampling result for a pure quadratic likewise does not imply this one-kernel binomial classification. These are implications-based comparisons, not a claim of proven exhaustive priority.

## Limitations

Only the standard power-weighted analytic Bergman disk, a single kernel atom, and the two-term target \(1+a z^m\) are covered. The result does not classify arbitrary polynomial targets, multiple-atom approximations, or non-power weights. The stated sharp transition is global for this exact family; it does not address algorithmic convergence of greedy schemes. Independent validation and exhaustive historical priority assessment have not been performed.

## References

1. W. Qu, T. Qian, and G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2006.03290, first posted 2020-06-05. https://arxiv.org/abs/2006.03290
2. W. Qu, T. Qian, H. Li, and K. Zhu, *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation 416 (2022), 126749, DOI:10.1016/j.amc.2021.126749. https://doi.org/10.1016/j.amc.2021.126749
3. W. Qu and P. Dang, *Rational Approximation in the Bergman Spaces*, arXiv:1803.04609, 2018. https://arxiv.org/abs/1803.04609
4. W. Qu and P. Dang, *Reproducing kernel approximation in weighted Bergman spaces: Algorithm and applications*, Mathematical Methods in the Applied Sciences 42 (2019), 4292–4304, DOI:10.1002/mma.5648. https://doi.org/10.1002/mma.5648
