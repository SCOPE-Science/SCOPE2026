# Entropy-optimal balancing of forward and reflected Hardy averages on real bounded variation

## Finding

For \(0\leq\alpha\leq1\), let the two one-sided normalized averages on \((0,1)\) be
\[
(Hf)(x)=\frac1x\int_0^x f(y)\,dy,\qquad
(Rf)(x)=\frac1{1-x}\int_x^1f(y)\,dy,
\qquad T_\alpha=\alpha H+(1-\alpha)R.
\]
The operator \(R\) is the reflection-conjugate of \(H\), **not** the integral adjoint (Copson operator) of \(H\). Define
\[
E_\alpha(s)=-\alpha s\log s-(1-\alpha)(1-s)\log(1-s),\qquad 0<s<1.
\]
Then the exact variation-to-integrated-error norm is
\[
\boxed{C_\alpha=\sup_{|Df|(0,1)>0}
 \frac{\|f-T_\alpha f\|_{L^1(0,1)}}{|Df|(0,1)}
 =\max_{0<s<1}E_\alpha(s).}
\]
There is a unique maximizing point \(s_\alpha\in(0,1)\), characterized by
\[
\alpha(-\log s_\alpha-1)+(1-\alpha)(\log(1-s_\alpha)+1)=0.
\]
For every \(0<\alpha<1\), equality in the norm inequality holds exactly for the functions \(f=c+a\mathbf1_{(s_\alpha,1)}\) almost everywhere, with real \(c\) and nonzero real \(a\). The endpoint constants are \(C_0=C_1=e^{-1}\).

Among **all fixed convex mixtures of these two directional averages**, the unique optimal mixture is the symmetric one:
\[
\boxed{\min_{0\le\alpha\le1}C_\alpha=C_{1/2}=\frac{\log2}{2},\qquad
\alpha_{\rm opt}=\tfrac12,\quad s_{1/2}=\tfrac12.}
\]
Moreover, the symmetric mixture obeys a **sharp quadratic localization inequality** for every real \(f\in BV(0,1)\):
\[
\boxed{\frac{\log2}{2}|Df|(0,1)-\|f-T_{1/2}f\|_{L^1(0,1)}
\geq\int_{(0,1)}(s-\tfrac12)^2\,|Df|(ds).}
\]
The numerical factor \(1\) multiplying the last integral cannot be increased uniformly. In comparison with either one-sided average, optimal balancing lowers the sharp worst-case coefficient from \(1/e\) to \((\log2)/2\).

## Assumptions and scope

All functions are **real** and regarded up to almost-everywhere equality on \((0,1)\). The notation \(BV(0,1)\) denotes distributional bounded variation; \(Df\) is its finite signed distributional derivative measure and \(|Df|(0,1)\) its total variation, excluding boundary traces. The unweighted \(L^1\) norm is \(\|g\|_{L^1(0,1)}=\int_0^1|g(x)|\,dx\). The weights \(\alpha\) and \(1-\alpha\) are constant in \(x\). Both averaging operators preserve constants. No endpoint values of a representative are used.

## Proof

**1. Jump-measure reduction.** Write \(\mu=Df\). The standard one-dimensional distributional BV representation gives, for almost every \(x\),
\[
f(x)=c+\int_{(0,1)}\mathbf1_{(s,1)}(x)\,\mu(ds).
\]
For the step \(u_s=\mathbf1_{(s,1)}\), a direct evaluation of the two averages yields
\[
((I-T_\alpha)u_s)(x)=K_\alpha(x,s)=
\begin{cases}
-\dfrac{(1-\alpha)(1-s)}{1-x},&x<s,\\[4pt]
\dfrac{\alpha s}{x},&x>s.
\end{cases}
\]
Thus \((I-T_\alpha)f(x)=\int K_\alpha(x,s)\mu(ds)\) a.e. Since \(\int_0^1|K_\alpha(x,s)|dx=E_\alpha(s)\leq1/e\), Fubini–Tonelli applies and gives
\[
\|f-T_\alpha f\|_1\leq\int E_\alpha(s)\,|\mu|(ds)
\leq\left(\sup_{0<s<1}E_\alpha(s)\right)|\mu|(0,1).
\]
Taking \(f=u_s\) attains \(E_\alpha(s)\), establishing the exact operator norm.

**2. Unique maximizing jump.** Differentiation gives
\[
E_\alpha'(s)=\alpha(-\log s-1)+(1-\alpha)(\log(1-s)+1),
\qquad E_\alpha''(s)=-\frac\alpha s-\frac{1-\alpha}{1-s}<0.
\]
For \(0<\alpha<1\), the derivative runs from positive infinity to negative infinity, so there is a unique interior maximizer. At \(\alpha=0\) and \(\alpha=1\), the limiting derivative equations give respectively \(s_0=1-e^{-1}\) and \(s_1=e^{-1}\); their maximal values are \(e^{-1}\). In particular, \(s_{1/2}=1/2\), and \(E_{1/2}(s)=\tfrac12h(s)\), where \(h(s)=-s\log s-(1-s)\log(1-s)\) is binary Shannon entropy in natural units.

**3. Minimax balancing.** At the midpoint, for every \(\alpha\),
\[
E_\alpha(1/2)=\frac{\log2}{2}.
\]
Consequently \(C_\alpha\geq(\log2)/2\). For \(\alpha=1/2\), strict concavity of \(h\) shows that the maximum equals this value. For \(\alpha\ne1/2\),
\[
E'_\alpha(1/2)=(2\alpha-1)(\log2-1)\ne0,
\]
so the midpoint is not a maximizer and the strict inequality \(C_\alpha>(\log2)/2\) follows. Hence the minimizing mixture is unique.

**4. All equality cases for interior weights.** Suppose \(0<\alpha<1\), \(\mu\ne0\), and norm equality holds. Equality in the second inequality in Step 1 first forces \(|\mu|\) to be supported on the *singleton* \(\{s_\alpha\}\), because \(E_\alpha\) has exactly one maximum. Therefore \(\mu=a\delta_{s_\alpha}\) for some nonzero real \(a\); the distributional BV representation proves the asserted characterization. Conversely every such step gives equality. This argument avoids any assumption that the input is monotone or has finitely many jumps.

**5. Sharp quantitative midpoint rigidity.** The entropy satisfies
\[
h''(s)=-\frac1{s(1-s)}\leq-4,
\qquad h(1/2)=\log2,\quad h'(1/2)=0.
\]
Integrating this second-derivative inequality on either side of \(1/2\) yields
\[
E_{1/2}(s)=h(s)/2\leq(\log2)/2-(s-1/2)^2.
\]
Insert this pointwise inequality in the first estimate of Step 1 to obtain the asserted global BV stability inequality. For a single unit jump at \(s=1/2+\varepsilon\), Taylor's theorem gives
\[
\frac{(\log2)/2-\|u_s-T_{1/2}u_s\|_1}{(s-1/2)^2}
=1+O(\varepsilon^2)\quad(\varepsilon\to0),
\]
which proves the coefficient \(1\) is sharp.

## Verification

Run `python3 CHECKER.py` using Python 3 and only its standard library. The checker independently integrates the piecewise rational jump kernel by Simpson quadrature, tests signed multijump inputs against the analytic sharp bound, checks the unique mixture optimum and verifies the quadratic stability coefficient numerically. These finite tests are diagnostic; the universal, arbitrary-BV assertions and the sharp constant are proved above without numerical extrapolation.

## Relationship to prior work

Classical Hardy averaging and its operator-theoretic optimal-domain theory provide the natural setting. Nekvinda and Pick (2011) analyze the forward Hardy map between optimal Banach function spaces, not the real-BV-to-integrated-error norm for a balanced forward/reflected family. Soria (2010) treats the identity defect of one-sided Hardy averaging on the cone of radially decreasing functions with restricted Lorentz-space bounds; this does not give the two-sided minimax theorem or its sharp quadratic BV localization. Lu, Yan, and Zhao (2013) establish different higher-dimensional \(L^p\) Hardy estimates. The distinct fixed-mixture approximation objective, its entropy form and the full-BV stability statement are the additional claims here. This comparison does not independently certify absolute historical priority.

## Limitations

The theorem is for one real spatial dimension, fixed convex weights, full Lebesgue-integrated error and distributional variation on the open interval. It does not classify spatially dependent weights, signed mixing coefficients outside the convex range, multidimensional domains, nonuniform input measures or other loss norms. At the endpoint weights \(\alpha=0,1\), the norm is determined but the complete equality class is not asserted. Historical priority remains subject to unindexed or inaccessible equivalent work and independent verification.

## References

1. A. Nekvinda and L. Pick, *Duals of Optimal Spaces for the Hardy Averaging Operator*, Z. Anal. Anwend. **30** (2011), 435–456, DOI: https://doi.org/10.4171/ZAA/1443 ; full text: https://ems.press/content/serial-article-files/35810 ; publisher public date September 29, 2011.
2. J. Soria, *Optimal bounds of restricted type for the Hardy operator minus the identity on the cone of radially decreasing functions*, Studia Math. **197** (2010), 69–79, DOI: https://doi.org/10.4064/sm197-1-6 ; full text: https://www.impan.pl/shop/en/publication/transaction/download/product/89912 .
3. S. Lu, D. Yan and F. Zhao, *Sharp bounds for Hardy type operators on higher-dimensional product spaces*, J. Inequal. Appl. **2013** (2013), 148, https://doi.org/10.1186/1029-242X-2013-148 ; public date April 3, 2013.
