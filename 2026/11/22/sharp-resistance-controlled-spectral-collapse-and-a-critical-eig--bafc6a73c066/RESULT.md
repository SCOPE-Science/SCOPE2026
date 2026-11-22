# Sharp resistance-controlled spectral collapse and a critical eigenfunction profile for symmetric weighted Poincaré inequalities

## Finding

Let \(\epsilon>0\), \(\alpha>0\), and \(w_{\epsilon,\alpha}(x)=(|x|+\epsilon)^\alpha\) on \([-1,1]\). Denote by \(\lambda_1(\epsilon,\alpha)\) the optimal positive constant in the squared, mean-subtracted weighted Poincaré inequality
\[
\lambda_1\int_{-1}^1|f-\langle f\rangle_w|^2w\,dx\leq\int_{-1}^1|f'|^2w\,dx.
\]
Set \(M=\int_0^1w(x)\,dx\) and \(H=\int_0^1w(x)^{-1}\,dx\). Uniformly for any parameters along which \(MH\to\infty\),
\[
\lambda_1 MH\longrightarrow1.
\]
More quantitatively, whenever \(MH>1/2\), the principal odd half-interval Rayleigh quotient \(\lambda_{\mathrm{odd}}\) satisfies
\[
\left(1+\frac1{\sqrt{2MH}}\right)^{-2}
\leq \lambda_{\mathrm{odd}}MH\leq
\left(1-\frac1{\sqrt{2MH}}\right)^{-2}.
\]
The global first nonzero eigenvalue equals the odd eigenvalue for all sufficiently large \(MH\).

For fixed \(\alpha>1\),
\[
\lambda_1(\epsilon,\alpha)\sim(\alpha^2-1)\epsilon^{\alpha-1}.
\]
For the critical window \(\alpha=1+t/\log(1/\epsilon)\) with fixed real \(t\),
\[
\lim_{\epsilon\downarrow0}\log(1/\epsilon)\lambda_1(\epsilon,\alpha)=\frac{2t}{e^t-1},
\]
with continuous value \(2\) at \(t=0\).

Let \(u_{\epsilon,\alpha}\) be the strictly positive odd-sector eigenfunction on \((0,1]\), normalized by \(u(0)=0\) and \(u(1)=1\). Let \(Q=\log((1+\epsilon)/\epsilon)\), \(x_\epsilon(s)=\epsilon(e^{sQ}-1)\), \(0\leq s\leq1\). In the critical window,
\[
\sup_{0\leq s\leq1}\left|u(x_\epsilon(s))-\frac{1-e^{-ts}}{1-e^{-t}}\right|\to0,
\]
where the expression is \(s\) when \(t=0\). Moreover the pushforward by \(s=Q^{-1}\log((x+\epsilon)/\epsilon)\) of the normalized half-interval derivative-energy probability measure \(w|u'|^2dx/\int_0^1w|u'|^2dx\) converges in total variation to the probability density \(t e^{-ts}/(1-e^{-t})\) on \([0,1]\) (uniform density if \(t=0\)).

## Assumptions and scope

The energy domain is \(H^1([-1,1])\), with natural Neumann conditions at \(\pm1\). For each strictly positive \(\epsilon\) the weight is positive and bounded, so the Neumann spectrum is discrete and the positive first eigenvalue exists. All integrals use unnormalized weighted Lebesgue measure; the mean \(\langle f\rangle_w\) is normalized by \(\int_{-1}^1w\). The symbol \(\sim\) means ratio tending to one. The fixed-exponent formula assumes \(\alpha>1\); the critical-window formula has fixed finite \(t\) and \(\epsilon\) small enough that \(\alpha>0\).

The underlying mechanism holds for any family of positive, continuous, *nondecreasing* weights \(w\) on \([0,1]\), extended evenly to \([-1,1]\), when \(MH\to\infty\). In that generality the same spectral ratio limit and uniform resistance-coordinate eigenfunction approximation hold; power weights are needed only for the explicit constants and logarithmic profile. No result is asserted here for arbitrary nonmonotone weights or higher dimensions.

## Proof

**1. A uniform endpoint estimate.** For a positive nondecreasing \(w\) on \([0,1]\), put \(E(v)=\int_0^1w|v'|^2dx\). Cauchy–Schwarz gives
\[
|v(1)-v(x)|^2\le E(v)\int_x^1w(s)^{-1}ds.
\]
Since \(w(s)\geq w(x)\) for \(s\geq x\), multiplying by \(w(x)\) and integrating yields
\[
\|v-v(1)\|_{L^2(w;(0,1))}^2\leq\frac12E(v).\tag{1}
\]
The factor \(1/2\) follows from \(\int_0^1(1-x)dx\).

**2. Separation of parities.** The Neumann operator associated with the even weight reduces into even and odd functions. Its even, nonconstant sector on \([0,1]\) has weighted mean zero, so \(|v(1)|\sqrt M\leq\|v-v(1)\|\) and then \(\|v\|\leq2\|v-v(1)\|\). By (1), the first positive even eigenvalue is at least \(1/2\). The odd sector has boundary conditions \(v(0)=0\), \(v'(1)=0\). For any odd-sector test \(v\), Cauchy–Schwarz from 0 to 1 gives \(|v(1)|\leq\sqrt{H E(v)}\). Combining this with (1) gives
\[
\|v\|_{L^2(w)}\leq\left(\sqrt{MH}+\frac1{\sqrt2}\right)\sqrt{E(v)},
\]
so \(\lambda_{\mathrm{odd}}\geq(\sqrt{MH}+1/\sqrt2)^{-2}\).

**3. Matching resistance test and spectral dominance.** Define
\[
h(x)=H^{-1}\int_0^xw(s)^{-1}ds.
\]
It has \(h(0)=0\), \(h(1)=1\), and \(E(h)=1/H\). Equation (1) gives \(\|h-1\|\leq1/\sqrt{2H}\); therefore \(\|h\|\geq\sqrt M-1/\sqrt{2H}\). Applying the odd Rayleigh principle yields the asserted upper bound for \(MH>1/2\). When \(MH\to\infty\), the odd eigenvalue tends to zero, while the positive even eigenvalues remain at least \(1/2\). Hence the first positive eigenvalue is precisely the odd ground eigenvalue and \(\lambda_1 MH\to1\). Standard regular Sturm–Liouville theory makes this odd ground eigenfunction simple and strictly positive on \((0,1]\).

**4. Eigenfunction and energy-measure rigidity.** Normalize the odd ground eigenfunction by \(u(1)=1\). Its equation and Neumann condition give
\[
w(x)u'(x)=\lambda_1\int_x^1w(s)u(s)ds.
\]
Positivity forces \(u'\geq0\), so \(0\leq u\leq1\) and \(\|u\|^2\leq M\). With \(E(u)=\lambda_1\|u\|^2\), steps 2–3 imply
\[
1\leq H E(u)\leq\left(1-1/\sqrt{2MH}\right)^{-2}\longrightarrow1.
\]
An exact quadratic identity, using \(u(1)-u(0)=h(1)-h(0)=1\), is
\[
\int_0^1w|u'-h'|^2dx=E(u)-H^{-1}.
\]
For every \(x\), Cauchy–Schwarz up to \(x\) then gives
\[
|u(x)-h(x)|\leq\sqrt{H(E(u)-H^{-1})}\to0.
\]
In particular the uniform error is \(O((MH)^{-1/4})\). The normalized derivative vectors have unit \(L^2\) norm and inner product \(1/\sqrt{HE(u)}\); Cauchy–Schwarz applied to their difference of squares yields
\[
\int_0^1\left|\frac{w|u'|^2}{E(u)}-\frac1{Hw}\right|dx
\leq2\sqrt{2\left(1-\frac1{\sqrt{HE(u)}}\right)}\to0.
\]
Thus the *normalized* derivative-energy probability law approaches the reciprocal-weight probability \(w^{-1}dx/H\) in total variation. This argument is uniform whenever \(MH\to\infty\), and any measurable coordinate pushforward preserves the bound.

**5. Power-law evaluation and critical coordinate.** Direct integration gives
\[
M=\frac{(1+\epsilon)^{\alpha+1}-\epsilon^{\alpha+1}}{\alpha+1},\quad
H=\begin{cases}
\dfrac{(1+\epsilon)^{1-\alpha}-\epsilon^{1-\alpha}}{1-\alpha},&\alpha\ne1,\\
\log((1+\epsilon)/\epsilon),&\alpha=1.
\end{cases}
\]
For fixed \(\alpha>1\), \(M\to1/(\alpha+1)\) and \(H\sim\epsilon^{1-\alpha}/(\alpha-1)\), giving the fixed-power formula. Write \(L=\log(1/\epsilon)\). If \(\alpha=1+t/L\), then \(M\to1/2\) and \(H/L\to(e^t-1)/t\), interpreted as 1 when \(t=0\). The spectral crossover follows.

The normalized resistance coordinate is explicitly
\[
h(x_\epsilon(s))=
\begin{cases}
\dfrac{1-e^{-t(Q/L)s}}{1-e^{-tQ/L}},&t\ne0,\\
s,&t=0.
\end{cases}
\]
Since \(Q/L\to1\), it converges uniformly to the stated profile. Its normalized derivative-energy measure, expressed in \(s\), has density
\[
\frac{(tQ/L)e^{-(tQ/L)s}}{1-e^{-tQ/L}},
\]
with continuous uniform limit at \(t=0\). Its densities converge uniformly for fixed \(t\), hence in total variation. Step 4 transfers the result to the eigenfunction's derivative-energy measure. This completes the proof.

## Verification

The algebraic mass and resistance integrals, quantitative brackets, Sturm shooting boundary condition, and critical rescaled profile are independently evaluated in the accompanying `check.py`. The script reports finite numerical diagnostics, not an exhaustive spectral certificate. The existence, uniqueness of the odd ground state, quantitative estimates, uniform convergence, and energy-law convergence are established analytically above.

## Relationship to prior work

Cruz-Uribe, Dal, and Rodney (2026), `arXiv:2608.20498`, prove broad degenerate Sobolev and Poincaré inequalities via extrapolation; their Poincaré theorems are sufficient estimates involving weight integrability and do not calculate the sharp spectral gap, a singular internal bottleneck, or its critical-window normalized eigenfunction and energy law. Claros (2025), `arXiv:2512.03651`, gives sharp dependence on Muckenhoupt characteristics for weighted Poincaré–Sobolev estimates, not the exact small-gap leading coefficient or the critical spectral eigenfunction. The one-dimensional diffusion framework of Bonnefont–Joulin–Ma (2016) concerns spectral-gap methods and some exact examples, but its inspected published description does not itself establish this power-bottleneck critical-window law. Classical electrical-resistance and Sturm–Liouville arguments underpin the present proof; the novelty claim is specifically the coupled asymptotic and its normalized eigenfunction/energy profile, not the variational principles or weighted Poincaré theory.

## Limitations

The result uses symmetry and monotonicity, with a *single internal* bottleneck and a continuum one-dimensional Neumann problem. It does not assert novelty of resistance-capacity approximations in general metastability literature. The exact named critical-window law and energy distribution have been compared with identified sources, but implicit coverage by a more general published one-dimensional capacity theorem is still a bibliographic risk. Numerical examples support normalizations only and cannot prove infinite-dimensional statements.

## References

- D. Cruz-Uribe, F. E. Dal, S. Rodney, *Degenerate Sobolev and Poincaré inequalities via extrapolation*, arXiv:2608.20498, first public 2026-08-20. https://arxiv.org/abs/2608.20498
- A. Claros, *Degenerate Poincaré-Sobolev inequalities via fractional integration*, arXiv:2512.03651, first public 2025-12-03. https://arxiv.org/abs/2512.03651
- M. Bonnefont, A. Joulin, Y. Ma, *A note on spectral gap and weighted Poincaré inequalities for some one-dimensional diffusions*, ESAIM: Probability and Statistics 20 (2016), 18–29. https://numdam.org/item/PS_2016__20__18_0/
- A. Bovier, V. Gayrard, M. Klein, *Metastability in reversible diffusion processes II: precise asymptotics for small eigenvalues*, J. Eur. Math. Soc. 7 (2005), 69–99. https://ems.press/journals/jems/articles/173
