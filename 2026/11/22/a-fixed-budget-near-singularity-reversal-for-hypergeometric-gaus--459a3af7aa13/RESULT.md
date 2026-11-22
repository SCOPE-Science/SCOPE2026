# A fixed-budget near-singularity reversal for hypergeometric Gaussian quadrature

## Finding

A fixed-node budget and a vanishing near-singularity distance select different transformations from the fixed-distance, increasing-order Bernstein-ellipse criterion. For both inverse-square and inverse-cube kernels, matching the kernel by a tangent or algebraic change of variables makes *relative* quadrature error vanish for every fixed positive Gauss–Legendre order, whereas the normalized inverse-hyperbolic-sine transformation has relative error tending to one. The exact error-separation factors below hold on a nonconstant class of smooth numerators, not just on constant-integrand cancellation tests.

Let \(f\in C^3([0,1];\mathbb R)\) satisfy \(a=f(0)>0\), \(f'(0)=0\), \(c=f''(0)/2>0\), and \(f(x)\ge a\) for \(0\le x\le1\). Fix any integer \(m\ge1\). For \(p\in\{2,3\}\), put
\[
 I_p(d)=\int_0^1\frac{f(x)}{(d^2+x^2)^{p/2}}\,dx,\qquad d>0,
\]
and set \(C_f=\int_0^1(f(x)-a)x^{-2}\,dx>0\). Let \(Q_{S,p}^{(m)}\) denote the \(m\)-point Gauss–Legendre rule after \(x=d\sinh(s\operatorname{arsinh}(1/d))\), with \(s\in[0,1]\). Let \(Q_{T,2}^{(m)}\) use \(x=d\tan(s\arctan(1/d))\); let \(Q_{A,3}^{(m)}\) use \(x=ds/\sqrt{1+d^2-s^2}\). Then, as \(d\downarrow0\) with \(m\) fixed,
\[
 I_2-Q_{T,2}^{(m)}\longrightarrow C_f,\qquad
 \frac{I_2-Q_{S,2}^{(m)}}{I_2}\longrightarrow1,
\]
\[
 \frac{I_3-Q_{A,3}^{(m)}}{\log(1/d)}\longrightarrow c,\qquad
 \frac{I_3-Q_{S,3}^{(m)}}{I_3}\longrightarrow1.
\]
In particular all four errors are positive for sufficiently small \(d\), and their **sharp absolute-error ratios** satisfy
\[
 \frac{|I_2-Q_{S,2}^{(m)}|}{|I_2-Q_{T,2}^{(m)}|}
 \sim \frac{\pi a}{2C_f}\,d^{-1},\qquad
 \frac{|I_3-Q_{S,3}^{(m)}|}{|I_3-Q_{A,3}^{(m)}|}
 \sim \frac{a}{c}\,\frac{d^{-2}}{\log(1/d)}.
\]
The matched-rule relative errors instead obey
\[
 \frac{I_2-Q_{T,2}^{(m)}}{I_2}\sim\frac{2C_f}{\pi a}d,\qquad
 \frac{I_3-Q_{A,3}^{(m)}}{I_3}\sim\frac ca d^2\log(1/d).
\]
The constants in these limiting laws are independent of the fixed quadrature order \(m\); the distance at which the asymptotic regime begins is not uniform in \(m\).

## Assumptions and scope

The rules have standard \(m\)-point Gauss–Legendre nodes \(0<s_j<1\) and strictly positive weights \(w_j\), \(\sum_jw_j=1\), on the full transformed interval \([0,1]\). No adaptive node insertion, interval splitting, analytical subtraction, or finite-precision cutoff is used. The near-singular source is at distance \(d\) beyond the endpoint \(x=0\). The exponent is exactly \(p=2\) or \(p=3\), and \(m\) is fixed **before** \(d\to0\). The numerator class includes \(f(x)=1+x^2\) and \(f(x)=1+x^2+x^4\); it excludes odd linear Taylor terms. The result is not a uniform-in-order assertion, nor a result for arbitrary geometric singularities.

Write \(U_d=\operatorname{arsinh}(1/d)\), \(A_d=\arctan(1/d)\), and \(H_d=1/(d^2\sqrt{1+d^2})\). The three algorithms are, exactly,
\[
 Q_{S,p}^{(m)}=U_d d^{1-p}\sum_{j=1}^m w_j
 \frac{f(d\sinh(U_ds_j))}{\cosh(U_ds_j)^{p-1}},
\]
\[
 Q_{T,2}^{(m)}=\frac{A_d}{d}\sum_{j=1}^m w_j f(d\tan(A_ds_j)),
 \qquad
 Q_{A,3}^{(m)}=H_d\sum_{j=1}^m w_j f\!\left(\frac{ds_j}{\sqrt{1+d^2-s_j^2}}\right).
\]
Every transformation maps \([0,1]\) monotonically onto \([0,1]\) for each \(d>0\).

## Proof

**Step 1: exact cancellation in the matched transformations.** Differentiation gives
\[
 \frac{d}{ds}\bigl[d\tan(A_ds)\bigr]
 =dA_d\sec^2(A_ds),\qquad
 (d^2+d^2\tan^2(A_ds))^{-1}=d^{-2}\cos^2(A_ds),
\]
so the transformed inverse-square weight is the constant \(A_d/d\). Similarly, let \(x(s)=ds/\sqrt{1+d^2-s^2}\). Since
\[
 \frac{x(s)}{d^2\sqrt{d^2+x(s)^2}}=sH_d,
\]
the transformed inverse-cube weight is the constant \(H_d\). This proves the exact rule expressions above.

**Step 2: the inverse-square matched error.** Split
\[
 I_2(d)=a\frac{A_d}{d}
 +\int_0^1\frac{f(x)-a}{d^2+x^2}\,dx.
\]
Since \(f'(0)=0\) and \(f\in C^3\), the quotient \((f(x)-a)/x^2\) has a finite continuous extension at zero. Dominated convergence shows that the remaining integral tends to \(C_f\). Because every fixed node satisfies \(s_j<1\), \(\tan(A_ds_j)\to\tan(\pi s_j/2)<\infty\). Consequently \(d\tan(A_ds_j)=O_m(d)\), and \(f(d\tan(A_ds_j))-a=O_m(d^2)\). The constant term is integrated exactly because the Gauss weights sum to one, so \(Q_{T,2}^{(m)}-aA_d/d=O_m(d)\). Hence \(I_2-Q_{T,2}^{(m)}\to C_f>0\), and \(I_2\sim \pi a/(2d)\).

**Step 3: the inverse-cube matched error.** With \(f(x)=a+cx^2+O(x^3)\),
\[
 I_3(d)=aH_d+c\int_0^1\frac{x^2}{(d^2+x^2)^{3/2}}\,dx+O(1).
\]
The remainder is uniformly bounded because \(\int_0^1x^3(d^2+x^2)^{-3/2}\,dx\le1\). The middle integral equals \(U_d-(1+d^2)^{-1/2}=\log(1/d)+O(1)\). At any fixed Gaussian node, \(x(s_j)=d s_j/\sqrt{1+d^2-s_j^2}=O_m(d)\). Thus \(f(x(s_j))-a=O_m(d^2)\), and, since \(H_d=O(d^{-2})\), \(Q_{A,3}^{(m)}-aH_d=O_m(1)\). Hence \(I_3-Q_{A,3}^{(m)}=c\log(1/d)+O_m(1)\), while \(I_3\sim a/d^2\). This proves both the logarithmic absolute error and the vanishing relative error.

**Step 4: the sinh rule under a fixed node budget.** Differentiating \(x=d\sinh(U_ds)\) yields the stated formula for \(Q_{S,p}^{(m)}\). For \(0<s<1\) fixed, \(U_d\sim\log(2/d)\to\infty\), so
\[
 \cosh(U_ds)^{-(p-1)}=O_s(d^{(p-1)s}).
\]
Because \(f\) is bounded on \([0,1]\), for \(p=2,3\),
\[
 \frac{Q_{S,p}^{(m)}}{d^{1-p}}
 = O_m\bigl(U_d d^{(p-1)s_{\min}}\bigr)\longrightarrow0,
 \quad s_{\min}=\min_j s_j>0.
\]
Both \(I_2(d)/d^{-1}\to\pi a/2\) and \(I_3(d)/d^{-2}\to a\); hence \(Q_{S,p}^{(m)}/I_p(d)\to0\). Combining this with Steps 2–3 and their positive leading terms proves all limits and ratios. In particular, no finite collection of interior sinh nodes captures the vanishing-distance boundary layer at \(s=0\). This completes the proof.

## Verification

Run `python verify.py` with Python 3 in the same directory. This standalone diagnostic checks transformed formula identities, Gaussian weights, positivity, and limiting error behavior for several finite orders and distances using closed-form integrals for \(f(x)=1+x^2\). It also checks the second numerator \(f(x)=1+x^2+x^4\), for which \(C_f=4/3\). The analytic proof, not the finite checks, establishes the all-\(m\) theorem and its limits. At extremely small \(d\), direct subtraction of two terms of magnitude \(d^{-2}\) loses floating-point precision; the verifier uses cancellation-free formulae for the small differences and reports this limitation.

For \(f(x)=1+x^2\), exact expressions used by the checker are
\[
 I_2(d)=A_d/d+1-dA_d,\qquad
 I_3(d)=H_d+U_d-(1+d^2)^{-1/2}.
\]

## Relationship to prior work

Hu, He and Sun (2026) study the inverse-hyperbolic-sine transformation and the two other hypergeometric cases, compare their complex-plane singularities and Bernstein ellipse rates, and recommend the sinh transform in their high-dimensional nearly singular setting. Their fixed-distance, increasing-order convergence criterion is different from the present fixed-order, vanishing-distance criterion. The transformation formulas themselves and the established theory of Gauss–Legendre quadrature are prior work; the new statement is the *sharp order-independent relative/absolute error reversal* for a nonconstant smooth numerator class and both cancellation exponents. In particular the present result does not disprove the source's fixed-distance exponential convergence analysis.

Hu, He, Rungamornrat and Gu (2026) provide a wider numerical comparison of near-singular quadrature transformations over surface geometries; their published abstract focuses on robust numerical performance of sinh and related radial rules, not the two exact fixed-budget asymptotic limits here. Huybrechs and Cools (2010) develop generalized Gaussian quadrature for nearly singular integrals, a different node-construction approach rather than these fixed standard Gauss nodes after the three specified transformations. Exact result precedence is not claimed beyond the sources actually compared.

## Limitations

The theorem is one-dimensional and requires \(f'(0)=0\) and \(c>0\) (with \(C_f>0\)); other numerator jets have different residual laws. It compares the unmodified transformed Gaussian rules, not a sinh rule with endpoint splitting, adaptivity, or singularity subtraction. The onset is not uniform in \(m\); at moderate distances the sinh rule can be considerably better, and the present asymptotics say nothing about the smallest cost for a prescribed finite tolerance. Numerical roundoff may dominate the small matched errors and must be treated separately. The originality comparison cannot exclude unindexed historical formulations or additional material unavailable in related papers. No claim is made for all multidimensional kernels or general \(p\).

## References

- Jing Hu, Luqiang He, Shuyu Sun, *Singular and nearly singular quadrature in arbitrary dimensions*, arXiv:2607.12440, first public version 2026-07-14. https://arxiv.org/abs/2607.12440
- Jing Hu, Luqiang He, Jaroon Rungamornrat, Xiaoqiang Gu, *Transformation techniques for weakly and nearly singular integrals: Comparative performance and numerical implementation*, *Computer Physics Communications* 325 (2026), article 110159. DOI: 10.1016/j.cpc.2026.110159. Associated public summary: https://data.mendeley.com/datasets/dtgfwfhg2t/1
- Daan Huybrechs, Ronald Cools, *On generalized Gaussian quadrature rules for singular and nearly singular integrals*, *SIAM Journal on Numerical Analysis* (2010). DOI: 10.1137/080723417. https://doi.org/10.1137/080723417
- MSC2020, code 65D32, numerical quadrature and cubature formulas. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=65D30
