# Sharp peak, sparsity, and \(L^1\)-norm tradeoffs for power-tent Gabor duals

## Finding
Fix \(r>0\) and \(0<\beta\le1/2\). Let \(g_r(t)=(1-|t|)_+^r\), and consider all Bessel dual Gabor windows \(h\in L^1(\mathbb R)\cap L^2(\mathbb R)\) for the lattice \((\alpha,\beta)=(1,\beta)\), allowing arbitrary complex coefficients, with essential peak bound \(\|h\|_\infty\le T\). Write \(F_r(T)\) for the least \(L^1\)-norm and \(S_r(T)\) for the least Lebesgue measure of the essential support among these windows.

Put
\[
T_{\min}=\beta\max\{1,2^{r-1}\},\qquad T_{\max}=\beta2^r.
\]
There is a capped dual if and only if \(T\ge T_{\min}\). When \(T\ge T_{\min}\), the unique \(L^1\)-minimizer (up to equality almost everywhere) *also* attains the least support measure, and
\[
 S_r(T)=\max\left\{1,2(\beta/T)^{1/r}\right\}.
\]
For \(T_{\min}\le T<T_{\max}\), set \(u=1-(\beta/T)^{1/r}\) (so \(0\le u<1/2\)). The exact Pareto value is
\[
 F_r(T)=2\beta\int_0^u (1-x)^{-r}\,dx
 +2\int_u^{1/2}\left[T+\frac{\beta-T(1-x)^r}{x^r}\right]dx.
\]
For \(T\ge T_{\max}\), the value is independent of \(T\), namely
\[
 F_r(T)=2\beta\int_0^{1/2}(1-x)^{-r}\,dx
 =\begin{cases}2\beta(1-2^{r-1})/(1-r),&r\ne1,\\2\beta\log2,&r=1.\end{cases}
\]
The curve is strictly decreasing and strictly convex on \((T_{\min},T_{\max})\) and constant afterwards. For the linear tent \(r=1\), with \(t=T/\beta\in(1,2]\), it has the elementary form
\[
 F_1(T)=\beta\left[2\log t+4-2t+2(1-t)\log\left(\frac{t}{2(t-1)}\right)\right],
\]
continuously extended by \(F_1(\beta)=2\beta\). In particular, the sharp critical cusp is
\[
 F_1(\beta(1+\varepsilon))=2\beta+2\beta\varepsilon\log(2\varepsilon)-3\beta\varepsilon^2+O(\beta\varepsilon^3)
 \quad(\varepsilon\downarrow0).
\]
For \(0<r<1\) the boundary slope is finite but its first nonlinear correction is fractional:
\[
 \begin{aligned}
 F_r(\beta(1+\varepsilon))={}&F_r(\beta)+\beta F_r'(\beta+)\varepsilon\\
 &+\frac{2\beta\,r^{r-1}}{(1-r)(2-r)}\varepsilon^{2-r}+o(\varepsilon^{2-r}),\\
 F_r'(\beta+)={}&2\int_0^{1/2}\left[1-\left(\frac{1-x}{x}\right)^r\right]dx.
 \end{aligned}
\]
For \(r>1\), the feasible boundary starts at \(T_{\min}>\beta\), where the right derivative is finite.

## Assumptions and scope
The signal space is \(L^2(\mathbb R)\). The translation and modulation operations are \(T_n f(x)=f(x-n)\) and \(M_{m\beta}f(x)=e^{2\pi i m\beta x}f(x)\), respectively. By a dual window we mean that both Gabor systems indexed by \((m,n)\in\mathbb Z^2\) are Bessel and
\[
 f=\sum_{m,n\in\mathbb Z}\langle f,M_{m\beta}T_n g_r\rangle M_{m\beta}T_nh\quad\text{in }L^2(\mathbb R)
\]
for all \(f\in L^2(\mathbb R)\). Essential support is measured by Lebesgue measure. The peak constraint is the essential supremum, not a prescribed point value. No nonnegative or compact-support restriction is imposed on competitors; these properties emerge at the optimum. The exponent \(r\) and lattice parameter \(\beta\) vary continuously in the indicated ranges. At \(T=T_{\min}\), feasibility includes the endpoint; as usual null sets are immaterial.

## Proof
**1. Reduction to a two-site fiber.** The painless range \(\beta\le1/2\) and support \([-1,1]\) imply that the Ron–Shen duality equations reduce, for \(n=0\), to
\[
\sum_{k\in\mathbb Z}g_r(x+k)h(x+k)=\beta\quad\text{for a.e. }x\in[0,1).
\]
Any candidate \(h\) can be truncated to \([-1,1]\), without affecting this identity; the off-diagonal equations \(n\ne0\) then vanish because the two window supports and their \(n/\beta\) translates are disjoint almost everywhere. Truncation preserves the peak cap and does not increase \(L^1\)-norm or support measure. Bounded compactly supported windows are Bessel by their finite overlap/Wiener-amalgam estimate. Thus every capped dual obeys a necessary fiber equation and each bounded compactly supported solution to it is a genuine dual.

Represent the two nonzero sites of each translation fiber by their distances \(x\) and \(1-x\) from the origin, where \(0<x<1/2\). The larger analysis coefficient is \(a=(1-x)^r\) and the smaller is \(b=x^r\), so \(a>b>0\). On either of the two reflection-related halves of the unit period the equation is \(aU+bV=\beta\). There is one such pair per fiber point, and reflection gives the factor two in all integral formulas below.

**2. Feasibility and the sharp peak threshold.** Necessarily
\[
 \beta=|aU+bV|\le T(a+b).
\]
Conversely, the nonnegative choice \(U=\min(T,\beta/a)\), \(V=(\beta-aU)/b\) is feasible whenever \(T(a+b)\ge\beta\). Its coordinates are both at most \(T\), with the latter inequality following from \(\beta\le T(a+b)\). The minimum of \((1-x)^r+x^r\) on \([0,1/2]\) equals \(1\) for \(0<r\le1\), and \(2^{1-r}\) for \(r>1\), proving exactly \(T\ge\beta\max\{1,2^{r-1}\}\).

**3. Pointwise sharp minimization and uniqueness, including complex duals.** Fix a fiber. For arbitrary complex feasible \(U,V\) put \(s=|U|\), so \(0\le s\le T\). The reverse triangle inequality gives
\[
 |U|+|V|=s+\frac{|\beta-aU|}{b}\ge s+\frac{|\beta-as|}{b}.
\]
The right-hand function decreases strictly for \(0\le s\le\beta/a\), since \(a>b\), and increases strictly for \(s\ge\beta/a\). It therefore has its unique minimum at \(s=\min\{T,\beta/a\}\). Equality in the reverse triangle inequality for \(\beta>0\) requires \(U\) to be positive real (except at vacuous zero endpoints), and then \(V=(\beta-aU)/b\) is necessarily nonnegative for the minimizing \(s\). Thus the nonnegative choice from Step 2 uniquely minimizes \(|U|+|V|\) even among complex-valued fibers, for almost every \(x\). The other half period follows by reflection. Explicitly, for \(u=1-(\beta/T)^{1/r}\), the pair is \((U,V)=(\beta/a,0)\) for \(0<x\le u\), and \((U,V)=(T,(\beta-aT)/b)\) for \(u<x<1/2\); when \(T\ge T_{\max}\) put \(u=1/2\). The choice is bounded by \(T\) and has support in \([-1,1]\), so is admissible. Fiber integration proves the displayed \(F_r(T)\).

**4. The support optimum is attained by this same minimizer.** For almost every fiber at least one of \(U,V\) must be nonzero. If \(aT<\beta\), the smaller-coefficient site must also be nonzero, by the strict inequality \(|aU|\le aT<\beta\). Conversely, if \(aT\ge\beta\) only the larger site suffices. The measure of the forced two-site fibers among \(0<x<1/2\) is \(\max\{0,(\beta/T)^{1/r}-1/2\}\). Consequently every capped dual has essential support measure at least \(1+2\max\{0,(\beta/T)^{1/r}-1/2\}\). The explicit minimizer has exactly that support, giving the formula for \(S_r\). This proves joint \(L^1\) and support optimality, not only separate attainability.

**5. Strict curvature, saturation, and critical regularity.** Differentiating the integral at an interior cap, the moving boundary contributes zero because the two integrands agree at \(a(u)T=\beta\). Thus
\[
 F_r'(T)=2\int_{u(T)}^{1/2}\left[1-\left(\frac{1-x}{x}\right)^r\right]dx<0,
\]
and \(F_r''(T)=-2u'(T)[1-((1-u(T))/u(T))^r]>0\) when \(u(T)>0\). At the feasible endpoint for \(r\le1\), use right derivatives; the same strict convexity follows for positive \(T-T_{\min}\). At \(T_{\max}\), \(u=1/2\), so the derivative vanishes and the curve saturates.

For \(r=1\), directly integrate the two pieces with \(u=1-\beta/T\), yielding the stated elementary formula. Expanding at \(T=\beta(1+\varepsilon)\) gives the logarithmic cusp with the exact quadratic correction. For \(0<r<1\), subtract the derivative at \(\beta\):
\[
 F_r'(\beta(1+\varepsilon))-F_r'(\beta+)
 =-2\int_0^{u(\beta(1+\varepsilon))}\left[1-\left(\frac{1-x}{x}\right)^r\right]dx.
\]
As \(u\sim\varepsilon/r\), the right side is \(2r^{r-1}\varepsilon^{1-r}/(1-r)+o(\varepsilon^{1-r})\). Integration with respect to \(T\) yields the fractional coefficient in the theorem. For \(r>1\), \(u(T_{\min})>0\), so the derivative integral has a finite lower endpoint.

## Verification
Run `python checker.py` with Python's standard library. It tests 9,913 exact-rational two-variable fiber linear programs for integral exponents, 51 independent numerical integrations/closed-form comparisons, and 36 numerical support-measure comparisons. Checks include strict feasibility and the full cap interval. The analytic proof, not these finitely sampled tests, establishes the all-real-exponent, all-dual claims.

## Relationship to prior work
Díaz Martín–Lammers–Miller–Powell (first publicly available July 18, 2026; later journal version November 13, 2026) prove an unrestricted \(L^1\)-minimum and characterize unrestricted minimizers in the painless regime (their Theorems 2.1 and 2.7, and Corollary 2.8). **The saturated cap interval \(T\ge T_{\max}\) here follows from that prior theorem and is not claimed as original.** What is added is the entire peak-constrained Pareto curve, exact feasibility/support thresholds and joint uniqueness, together with the logarithmic and fractional threshold laws for this natural power-tent family. Perraudin–Holighaus–Søndergaard–Balazs give a broad convex-optimization method for designing dual Gabor windows; they do not state these analytic cap/support formulas. Related published Gabor work on hat splines and power tents calculates sharp frame bounds or conditioning rather than the present constrained dual norms.

## Limitations
This is an analytic classification for \(r>0\), \(0<\beta\le1/2\), translation spacing exactly one, and an essential-amplitude bound on the dual. It is not a result for more general lattices or non-painless duality, nor does it bound the frame condition number or assert that all optimal duals are continuous. The support minimum is a Lebesgue measure, not a minimum number of knots or a frequency-support claim. The \(\ell^1\)-coefficient-to-\(L^\infty\) synthesis estimate is a motivation for imposing the cap, not a new reconstruction inequality. Existing literature could contain an equivalent formula under different terminology; novelty is assessed against the identified papers and indexed records, not independently certified.

## References
1. R. Díaz Martín, M. Lammers, B. Miller, and A. M. Powell, *Gabor duals with minimal \(L^1\)-norm*, arXiv:2607.16915 (initial version July 18, 2026), https://arxiv.org/abs/2607.16915; *J. Fourier Anal. Appl.* 32 (2026), article 105, https://doi.org/10.1007/s00041-026-10315-6.
2. N. Perraudin, N. Holighaus, P. L. Søndergaard, and P. Balazs, *Designing Gabor windows using convex optimization*, arXiv:1401.6033, https://arxiv.org/html/1401.6033v4.
3. Ron–Shen/Janssen duality conditions are quoted with normalization and references in item 1, Section 1.1, equation (1.4).
