# All-sweep exponential mass blow-up on a conservative exchange flow

## Finding

Consider the two-node Gauss–Lobatto form of the positive exponential integral deferred-correction method of Pezzella (2026), with any fixed finite correction count \(m\geq0\), applied to the two-species reversible exchange equation
\[
\dot x=y-x,\qquad \dot y=x-y,
\]
starting from **any** \(x_0,y_0>0\). Its exact flow is positive and preserves \(x(t)+y(t)=x_0+y_0\). Yet the following sharp dichotomy holds: for every fixed finite \(m\), the computed one-step total mass remains bounded as \(h\to\infty\) **if and only if** \(x_0=y_0\). In the equal case every predictor and correction equals the equilibrium. For every unequal positive start the computed total mass tends to infinity, although both computed components stay strictly positive for every finite \(h\).

There is a more precise, all-sweep law. Let \(r=y_0/x_0\ne1\), let \(R_m(h)\) be the ratio of the computed second and first components after \(m\) corrections, and put \(L_m(h)=\log R_m(h)\). Then
\[
L_0=\log r+h(r^{-1}-r),\qquad
L_m=\log r+\frac h2\left(r^{-1}-r+e^{-L_{m-1}}-e^{L_{m-1}}\right)\quad(m\ge1).
\]
For every **fixed** integer \(m\ge0\), as \(h\to\infty\),
\[
\operatorname{sgn}(L_m)=(-1)^{m+1}\operatorname{sgn}(\log r)
\quad\text{eventually};
\qquad |L_0|\sim h|r-r^{-1}|;
\]
and, for each fixed \(m\ge1\),
\[
\boxed{\quad |L_m|\sim\frac h2\exp(|L_{m-1}|),\qquad
\log\bigl(x_m(h)+y_m(h)\bigr)\sim |L_m|.\quad}
\]
Thus each finite correction adds a further exponential level to the stiff-limit explosion, and the dominant output species alternates with the sweep parity. The initial predictor (zero corrections) already has exponentially growing mass. The limits concern fixed correction count first, then unbounded stepsize; no statement about interchanging these limits is made.

For the natural positive start \((x_0,y_0)=(1,2)\), the first corrected endpoint is explicitly
\[
\boxed{\quad
x_1(h)=\exp\!\left(he^{-3h/2}\right),\qquad
y_1(h)=2\exp\!\left(-\frac{3h}{4}+\frac h4e^{3h/2}\right).
\quad}
\]
Hence \(x_1(h)\to1\), whereas \(y_1(h)\) grows double-exponentially, against the exact total mass of three.

## Assumptions and scope

All calculations are in exact real arithmetic. The underlying positive ODE is the symmetric, unit-rate, two-species exchange with **strictly positive** starting components. The timestep \(h>0\) varies without an imposed upper bound. The numerical map uses exactly two Gauss–Lobatto nodes \(0,1\), endpoint weights \((1/2,1/2)\), the exponential predictor, and exactly \(m\) explicit-in-sweep corrections as defined below. The correction count \(m\) is a fixed nonnegative integer for each limit; there is no floating-point saturation, projection, adaptive damping, timestep subdivision, or mass renormalization. This is a statement about one completed step, not asymptotic growth under repeated time integration.

Write \(g_1(x,y)=y/x-1\) and \(g_2(x,y)=x/y-1\). Let \(z_0=(x_0e^{hg_1(x_0,y_0)},y_0e^{hg_2(x_0,y_0)})\) be the predictor. For \(m\ge1\) set
\[
z_m=(x_0,y_0)\odot\exp\!\left[\frac h2\bigl(g(x_0,y_0)+g(z_{m-1})\bigr)\right],
\]
where products and exponentials are componentwise. The components of \(z_m\) are denoted \(x_m(h),y_m(h)\).

## Proof

**1. Exact baseline and the source method.** The sum of the differential equations vanishes. The difference solves \((x-y)'=-2(x-y)\), giving
\[
x(t)=\frac{x_0+y_0}2+\frac{x_0-y_0}2e^{-2t},\qquad
y(t)=\frac{x_0+y_0}2-\frac{x_0-y_0}2e^{-2t}.
\]
These remain positive and sum to \(x_0+y_0\). The stated predictor and correction formulas are the exact two-node Gauss–Lobatto specialization of the source's exponential update (its equation (3)); they are well defined and strictly positive by induction for all finite \(h>0\) and \(m\ge0\).

**2. Exact reduction.** Put \(r=y_0/x_0>0\), and \(R_m=y_m/x_m\). Since the initial per-capita rates are \(r-1,r^{-1}-1\),
\[
x_0(h)=x_0e^{h(r-1)},\qquad y_0(h)=y_0e^{h(r^{-1}-1)},\qquad R_0=r e^{h(r^{-1}-r)}.
\]
Here \(x_0(h),y_0(h)\) mean the **predictor outputs**, while plain \(x_0,y_0\) mean initial data. For every \(m\ge1\), direct substitution in the two correction equations yields
\[
\boxed{\quad
x_m=x_0\exp\!\left[\frac h2(r+R_{m-1}-2)\right],\qquad
y_m=y_0\exp\!\left[\frac h2(r^{-1}+R_{m-1}^{-1}-2)\right].\quad}
\]
Taking the ratio gives the two scalar recurrences in the finding. No approximation or stability-function argument is used here.

**3. Rigorous alternating exponential asymptotics.** If \(r=1\), all initial per-capita rates vanish, hence every stage remains \((x_0,x_0)\). Suppose \(r\ne1\), and let \(\sigma=\operatorname{sgn}(\log r)=\operatorname{sgn}(r-r^{-1})\). Then
\[
L_0=\log r-h(r-r^{-1}),
\]
so \(\operatorname{sgn}L_0=-\sigma\) eventually and \(|L_0|\sim h|r-r^{-1}|\). In particular, \(|L_0|/\log h\to\infty\).

Inductively suppose \(L_{m-1}\) has eventual sign \((-1)^m\sigma\) and \(|L_{m-1}|/\log h\to\infty\). In the recurrence for \(L_m\), the term \((h/2)(e^{-L_{m-1}}-e^{L_{m-1}})\) has the **opposite** sign and magnitude asymptotic to \((h/2)e^{|L_{m-1}|}\). The other terms \(\log r+(h/2)(r^{-1}-r)\) are \(O(h)\), negligible against that magnitude. Therefore \(L_m\) has eventual sign \((-1)^{m+1}\sigma\) and
\[
|L_m|\sim\frac h2e^{|L_{m-1}|},
\]
which also implies \(|L_m|/\log h\to\infty\). This proves the induction for every fixed integer \(m\).

**4. Actual mass and its dominant species.** For \(m\ge1\), if \(L_{m-1}\to+\infty\), then from the boxed endpoint formulas
\[
\log x_m=\frac h2e^{L_{m-1}}+O(h),\qquad \log y_m=O(h).
\]
If \(L_{m-1}\to-\infty\), then
\[
\log y_m=\frac h2e^{-L_{m-1}}+O(h),\qquad \log x_m=O(h).
\]
In both cases the exploding logarithm dominates, so \(\log(x_m+y_m)\sim(h/2)e^{|L_{m-1}|}\sim|L_m|\), and the output mass diverges. For \(m=0\), one of \(r-1,r^{-1}-1\) is strictly positive and the other negative; the positive exponent produces exponential mass growth. The signs from Step 3 show the dominant species swaps at each correction. Conversely, the equilibrium case is exactly constant. The if-and-only-if classification follows.

**5. Explicit double-exponential witness.** For \((x_0,y_0)=(1,2)\), \(r=2\) and \(R_0=2e^{-3h/2}\). Substitute into Step 2 for \(m=1\), obtaining the displayed closed forms. The first tends to one; the second has logarithm asymptotic to \((h/4)e^{3h/2}\), proving the stated growth and completing the proof.

## Verification

The accompanying standalone standard-library script `verify.py` implements the original two-species exponential predictor and all correction sweeps directly and separately implements the scalar ratio reduction. It checks direct endpoints, log ratios, an exact first-correction identity and the exact conservative solution over multiple starts, steps and correction counts. Running `python3 verify.py` in this package prints `CHECK_OK 584`. These finite diagnostics do not establish the quantified fixed-sweep asymptotics; Steps 3–4 establish them analytically. The script does not attempt to represent enormous stiffness-limit towers in finite floating-point arithmetic.

## Relationship to prior work

Pezzella (2026), arXiv:2606.29523, introduces the exponential SPIDeC method, its unconditional positivity, equilibrium preservation and exactness on scalar/diagonal decay, plus small-step accuracy and collocation contractivity statements. In the inspected complete source, Section 5.1 explicitly restricts exact linear reproduction to diagonal operators; Sections 5.2–6 do not assert a bound on the total mass of fixed finite sweeps of a *coupled conservative exchange* at unbounded stiffness.

A published earlier mathematical record, *A sharp all-sweep exchange-stability wall for two-node positive integral deferred correction* (2026), treats **the same exchange model and numerical map**, but its theorem concerns local *transverse derivatives at the equilibrium line*: all finite sweep counts have the same small-step linear contraction threshold. The present all-initialization, one-step mass classification and iterated-exponential large-step growth are not implications of a local Jacobian criterion (local instability alone does not determine the fate or magnitude of a fixed off-equilibrium point as \(h\to\infty\)). The logistic-flow result *Sharp correction-sweep flip boundary for two-node positive deferred correction on logistic flow* (2026) concerns a distinct scalar field and correction count tending to infinity at fixed stepsize, yielding bounded two-cycles instead of the present fixed-sweep stiff-limit towers. Scheiber (2019) analyzes additive numerical Picard iterations and their convergence under step restrictions, not this multiplicative exchange recurrence. This comparison supports a distinct statement but is not a proof of historical uniqueness.

## Limitations

The classification is exact for one symmetric two-species exchange, positive initial data, two Gauss–Lobatto nodes and fixed finite correction count. It does not prove the same blow-up for higher-node schemes, Gauss–Radau nodes, all conservative positive systems, or the implicit collocation limit. The order of limits matters: nothing here says that infinite corrections at a fixed step have the same fate. The exponential growth is a mathematical exact-arithmetic phenomenon; finite floating-point implementations can overflow or use safeguards. The result does not invalidate positivity, diagonal exactness, or valid *small-step* convergence bounds in the source paper. Historical priority has not been independently certified.

## References

1. M. Pezzella, *Stable Positive Integral Deferred Correction Methods for Positive Dynamical Systems*, arXiv:2606.29523v1, first public version 2026-06-28, especially equations (3), Sections 2, 3, 5 and 6. https://arxiv.org/abs/2606.29523
2. *A sharp all-sweep exchange-stability wall for two-node positive integral deferred correction*, published mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-all-sweep-exchange-stability-wall-for-two-node-positive--f64f37a39bd2
3. *Sharp correction-sweep flip boundary for two-node positive deferred correction on logistic flow*, published mathematical record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-correction-sweep-flip-boundary-for-two-node-positive-defer--90014a7600e9
4. E. Scheiber, *On the numerical Picard iterations with collocations for the initial value problem*, J. Numer. Anal. Approx. Theory 48 (2019), 89–105, DOI:10.33993/jnaat481-1146. https://ictp.acad.ro/jnaat/journal/article/view/1146
