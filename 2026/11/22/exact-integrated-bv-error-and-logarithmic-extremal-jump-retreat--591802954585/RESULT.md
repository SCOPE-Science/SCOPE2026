# Exact integrated BV error and logarithmic extremal-jump retreat for Szász–Mirakjan–Kantorovich averaging

## Finding

For each integer \(n\ge1\), let \(K_n\) be the classical Szász–Mirakjan–Kantorovich operator
\[
(K_nf)(x)=n\sum_{k=0}^{\infty}e^{-nx}\frac{(nx)^k}{k!}
\int_{k/n}^{(k+1)/n}f(t)\,dt,\qquad 0\le x\le1.
\]
For a real \(f\in BV(0,1)\), use its one-sided trace to extend it constantly for \(t\ge1\). Its sharp integrated error relative to interior Jordan variation is
\[
C_n=\sup_{|Df|(0,1)>0}\frac{\|f-K_nf\|_{L^1(0,1)}}{|Df|(0,1)}
=\max_{\substack{0\le m<n\\2p_m(m)>Q_m(n)}} E_{n,m}(a_{n,m}),
\]
where
\[
p_m(z)=e^{-z}\frac{z^m}{m!},\quad Q_k(n)=e^{-n}\sum_{j=0}^{k}\frac{n^j}{j!},\quad Q_{-1}(n)=0,
\]
\[
r_0=0,\qquad r_k=\frac{k}{n}Q_k(n)-Q_{k-1}(n)\quad(k\ge1),
\]
\[
E_{n,m}(a)=\frac{2(m+a)}{n}p_m(m+a)-(1-a)r_m-ar_{m+1},\quad 0\le a\le1,
\]
and \(a_{n,m}\in(0,1)\) is the **unique** solution of
\[
2(1-a)p_m(m+a)=Q_m(n).
\]
Every maximizer is an interior point of one grid cell. The complete norm-equality class consists of the nonconstant functions \(f(t)=c+d\mathbf1_{\{t>s\}}\), where \(d\ne0\) and \(s=(m+a_{n,m})/n\) is a global maximizing cell root. There may be more than one globally maximizing cell: no general uniqueness of that cell is claimed.

For **every** choice of global maximizing jump locations \(s_n\),
\[
\lim_{n\to\infty}\sqrt n\,C_n=\sqrt{\frac2\pi},
\qquad
\lim_{n\to\infty}(1-s_n)\sqrt{\frac{n}{\log n}}=1.
\]
Thus the worst jump approaches the right endpoint, but retreats by the larger-than-diffusive scale \(\sqrt{\log n/n}\); the leading sharp error remains on the diffusive scale \(n^{-1/2}\).

## Assumptions and scope

The operator acts on real, almost-everywhere classes in \(BV(0,1)\), with the canonical one-sided constant extension beyond \(1\). Its cell integrals do not depend on point representatives. Variation \(|Df|(0,1)\) excludes endpoint atoms, and the norm is the **unnormalized** Lebesgue \(L^1(0,1)\) norm. For a nonconstant function, the denominator is strictly positive. The underlying Poisson parameter is \(nx\), not \(x\) or \(n^2x\). The finite formula is valid for every \(n\ge1\), including \(m=0\), for which the zero-shape Gamma distribution below is an atom at zero.

## Proof

**Step 1 (step response and exact Gamma mixture).** For \(s\in(0,1)\), put \(h_s(t)=\mathbf1_{\{t>s\}}\), \(m=\lfloor ns\rfloor\), \(a=ns-m\). Writing \(N_x\sim\operatorname{Poisson}(nx)\),
\[
(K_nh_s)(x)=\Pr\{N_x\ge m+1\}+(1-a)\Pr\{N_x=m\}.
\]
The right side is the distribution function at \(x\) of \(T_{n,s}\), whose law is a mixture of \(\operatorname{Gamma}(m,n)\), weight \(1-a\), and \(\operatorname{Gamma}(m+1,n)\), weight \(a\). Here Gamma's second parameter is the **rate**, and \(\operatorname{Gamma}(0,n)=\delta_0\). Since \(\mathbb ET_{n,s}=s\), the step error is
\[
E_n(s)=\int_0^1|h_s(x)-(K_nh_s)(x)|\,dx
=\mathbb E\big|\min\{T_{n,s},1\}-s\big|
=\mathbb E|T_{n,s}-s|-\mathbb E(T_{n,s}-1)_+.
\]
The Gamma–Poisson tail identity and the Gamma first-moment identity give, by direct cancellation,
\[
\mathbb E|T_{n,s}-s|=2s\,p_m(ns),\qquad
\mathbb E(T_{n,s}-1)_+=(1-a)r_m+ar_{m+1}.
\]
This establishes the displayed finite formula. In particular it is not merely an upper bound or a quadrature approximation.

**Step 2 (all cell maximizers).** Holding \(m\) fixed and differentiating within \(m/n<s<(m+1)/n\) gives
\[
\frac{dE_n(s)}{ds}=2(1-a)p_m(m+a)-Q_m(n).
\]
The first term strictly decreases from \(2p_m(m)\) to zero as \(a\) runs from zero to one, since
\[
\frac{d}{da}\log[(1-a)p_m(m+a)]
=-\frac1{1-a}-\frac{a}{m+a}<0,
\]
with the evident direct interpretation for \(m=0\). Thus a cell has one strict internal maximum precisely under the displayed condition; otherwise its error decreases throughout. For \(1\le m\le n-1\), the derivative approaching \(m/n\) from the left is \(-Q_{m-1}(n)<0\); therefore a grid knot is never a global maximum. The error tends to zero as \(s\downarrow0\), and has negative one-sided derivative as \(s\uparrow1\). At least the first cell has an interior maximum, since \(2p_0(0)=2>Q_0(n)\). Consequently the global maximum is exactly the stated maximum over cell roots.

**Step 3 (arbitrary BV inputs and equality).** For the signed distributional derivative \(\mu=Df\), the one-sided trace representation gives \(f(t)=c+\int h_s(t)\,\mu(ds)\) almost everywhere, including under the specified extension. Since \(K_n\) preserves constants, Fubini and the triangle inequality yield
\[
\|f-K_nf\|_1\le\int_{(0,1)}E_n(s)|\mu|(ds)\le C_n|Df|(0,1).
\]
Both inequalities become equalities for a maximizing single jump. Conversely, at any two distinct jump positions \(s<t\), the residuals \(h_s-K_nh_s\) and \(h_t-K_nh_t\) have opposite signs on \((s,t)\), and the same sign on \((0,s)\); each residual is strictly nonzero away from its jump. No fixed choice of nonzero signs for two jump masses makes their residuals agree in sign almost everywhere. The equality case of the integral triangle inequality, applied with Fubini to pairs from \(|\mu|\otimes|\mu|\), therefore forces \(|\mu|\) to be supported at a single point. The last bound then forces that point to maximize \(E_n\). This proves the entire equality class.

**Step 4 (sharp asymptotics).** Stirling's formula, uniformly for \(m\asymp n\) and \(0\le a\le1\), gives
\[
2s\,p_m(ns)=\sqrt{\frac{2s}{\pi n}}\big(1+O(n^{-1})\big).
\]
In particular, if \(s=1-c\sqrt{\log n/n}\) for a fixed \(c>1\), the full-line absolute-deviation term has the expansion
\[
\sqrt{\frac2{\pi n}}-\frac{c\sqrt{\log n}}{\sqrt{2\pi}\,n}+o(\sqrt{\log n}/n).
\]
For \(k\) within \(O(\sqrt{n\log n})\) of \(n\), let \(r_k=\mathbb E(\operatorname{Gamma}(k,n)-1)_+\). Gamma Chernoff bounds, using the test exponent \(n-k\), imply for \(k<n\)
\[
r_k\le\frac{\exp\{-(n-k)+k\log(n/k)\}}{n-k}.
\]
For \(n-k=(c+o(1))\sqrt{n\log n}\) with fixed \(c>1\), this is \(o(\sqrt{\log n}/n)\). Hence the candidate in the previous paragraph gives the same leading two-term lower bound for \(C_n\). Also \(E_n(s)\le2s p_m(ns)\), and Stirling at \(m\asymp n\), together with the elementary bound \(p_m(z)\le O((m+1)^{-1/2})\) for \(z=m+a\), yields \(\limsup\sqrt n C_n\le\sqrt{2/\pi}\). The candidate gives equality; any maximizing \(s_n\) must tend to one.

It remains to determine its distance. Write \(c_n=(1-s_n)\sqrt{n/\log n}\). If \(c_n\ge1+\varepsilon\) along a subsequence, the full-line term above gives a strictly larger order-\(\sqrt{\log n}/n\) deficit than a fixed competitor with \(1<c<1+\varepsilon\), even before subtracting a nonnegative overshoot. Thus \(\limsup c_n\le1\). If \(c_n\le1-\varepsilon\), a Stirling estimate for either adjacent Gamma density on the interval \(t\in[1+(\sqrt n(1+d))^{-1},1+2(\sqrt n(1+d))^{-1}]\), where \(d=(n-m)/\sqrt n\), supplies the uniform lower bound
\[
(1-a)r_m+ar_{m+1}\ge
\frac{\exp\{-d^2/2-O(1+d^3/\sqrt n)\}}{C\sqrt n(1+d)^2}
\]
for \(d=O(\sqrt{\log n})\) and a numerical \(C>0\). In that range the bound is asymptotically **much larger** than \(\sqrt{\log n}/n\), contradicting the fixed \(c>1\) competitor. Therefore \(\liminf c_n\ge1\), completing the second limit. This is an analytic moderate-deviation argument, not an extrapolation from numerical roots.

## Verification

Run `python check_szasz.py` with Python 3.10+ and SciPy. The script independently compares Poisson-response quadrature with Gamma-mixture formulas, tests the derivative sign at numerically resolved cell roots, and checks BV bounds on signed multi-jump inputs. It does **not** purport to check infinitely many \(n\) or to prove the moderate-deviation limit. The formula for finite \(n\) requires only Poisson probabilities and one strictly monotone scalar root per eligible cell. Example values: \(C_1\approx0.4395399956\), \(C_2\approx0.3344824328\), \(C_3\approx0.2889456716\), \(C_{10}\approx0.1873364308\).

## Relationship to prior work

The classical operator and integral approximation framework were established well before this result. Walczak (2002), particularly its formulas (1.1)–(1.2) and Theorems 3.5–3.7, studies convergence and non-sharp weighted \(L^1\) rates for the classical and modified operators. Nowak–Sikorska-Nowak (2009) studies pointwise convergence for modified Szász–Kantorovich operators. Acar–Gupta–Aral (2011) addresses a **different** generalized Szász–Baskakov integral kernel and approximation of functions with derivatives of BV. None of the inspected primary statements supplies this sharp finite-interval BV-to-integrated-error constant, cell-maximizer classification, or its \(\sqrt{\log n/n}\) jump-location law. Closely related published approximation-norm and Poisson-tail results use different kernels or norms; their techniques and general identities remain prior art.

## Limitations

The theorem is for one-dimensional real BV inputs with the specified constant continuation beyond one, the **classical** integral Szász–Mirakjan–Kantorovich operator, and unweighted integrated error on the fixed observation interval \((0,1)\). It does not give a closed elementary formula for the globally winning cell at each finite \(n\), prove uniqueness of that winning cell, classify other interval lengths, or handle weighted or generalized kernels. Older hard-to-index work on Poissonized positive approximation remains a historical-priority risk; no independent mathematical audit or priority certification has occurred.

## References

- Z. Walczak, *On approximation by modified Szasz-Mirakyan operators*, Glasnik Mat. 37 (2002), 303–319, https://web.math.pmf.unizg.hr/glasnik/37.2/37%282%29-08.pdf ; publisher record https://hrcak.srce.hr/en/clanak/7837 (public date recorded as 2002-12-01).
- G. Nowak and A. Sikorska-Nowak, *Some approximation properties of modified Szasz-Mirakyan-Kantorovich operators*, Rev. Anal. Numér. Théor. Approx. 38 (2009), https://doi.org/10.33993/jnaat381-903 ; full text https://ictp.acad.ro/jnaat/journal/article/download/2009-vol38-no1-art7/Nowak-SikorskaNowak-pdf/903.
- T. Acar, V. Gupta and A. Aral, *Rate of convergence for generalized Szász operators*, Bull. Math. Sci. 1 (2011), https://doi.org/10.1007/s13373-011-0005-4 (published 2011-03-25).
- V. Totik, *Approximation by Szász–Mirakjan–Kantorovich operators in \(L^p\)*, Analysis Math. 9 (1983), https://doi.org/10.1007/BF01982010 (historical context; complete primary text not inspected).
