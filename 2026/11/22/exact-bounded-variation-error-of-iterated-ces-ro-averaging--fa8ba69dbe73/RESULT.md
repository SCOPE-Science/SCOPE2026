# Exact bounded-variation error of iterated Cesàro averaging

## Finding
For every integer \(m\ge1\), set \(Hf(x)=x^{-1}\int_0^x f(t)\,dt\) for \(0<x<1\), and \(r_m=(m!)^{1/m}\). The exact sharp operator defect from real distributional bounded variation, modulo constants, to Lebesgue \(L^1(0,1)\) is
\[
\sup_{|Df|(0,1)>0}\frac{\|f-H^mf\|_{L^1(0,1)}}{|Df|(0,1)}
=C_m=e^{-r_m}\sum_{k=1}^{m}\frac{r_m^k}{k!}.
\]
Every equality case has the form \(f=a+b\mathbf1_{(e^{-r_m},1)}\) almost everywhere, with \(a\in\mathbb R\) and \(b\in\mathbb R\setminus\{0\}\); conversely all of these attain equality. In addition,
\[
C_1=e^{-1},\qquad C_m<C_{m+1}<1,\qquad \lim_{m\to\infty}C_m=1,
\]
and
\[
1-C_m\sim\frac{e}{e-1}(2\pi m)^{-1/(2e)}e^{-m/e}.
\]

## Assumptions and scope
Variation means the total mass \(|Df|(0,1)\) of the distributional derivative of a real \(BV(0,1)\) function; endpoint jumps are not counted. The domain is the open unit interval with unweighted Lebesgue \(L^1\) error. The integer \(m\) is fixed and positive for the sharp identity, and tends to infinity only in the stated asymptotic. Functions are identified almost everywhere. The operator fixes constants. This ratio is defined only when \(|Df|(0,1)>0\).

## Proof
**1. Exact single-jump response.** For each \(s\in(0,1)\), write \(g_s(x)=\mathbf1_{(s,1)}(x)\). Let \(U_1,\ldots,U_m\) be independent uniform variables on \((0,1)\). Iterated conditioning yields \(H^m f(x)=\mathbb E f(x\prod_{i=1}^m U_i)\) for bounded measurable \(f\). As \(-\sum_i\log U_i\) has a gamma distribution with integer shape \(m\), for \(x>s\), with \(u=\log(x/s)\),
\[
H^mg_s(x)=1-e^{-u}\sum_{j=0}^{m-1}\frac{u^j}{j!}.
\]
For \(x\le s\), both \(g_s\) and its averaged iterate vanish. Consequently \(g_s-H^mg_s\ge0\), and its exact \(L^1\) error equals
\[
E_m(s)=\int_s^1\frac{s}{x}\sum_{j=0}^{m-1}\frac{(\log(x/s))^j}{j!}\,dx
=s\sum_{k=1}^{m}\frac{(\log(1/s))^k}{k!}.
\]
The second equality follows on substituting \(u=\log(x/s)\).

**2. Strict optimization of jump location.** Write \(s=e^{-u}\) for \(u>0\) and \(F_m(u)=e^{-u}\sum_{k=1}^{m}u^k/k!\). Direct differentiation, including cancellation of neighboring terms, gives
\[
F_m'(u)=e^{-u}\left(1-\frac{u^m}{m!}\right).
\]
Hence \(F_m\) increases strictly up to the unique \(u=r_m=(m!)^{1/m}\) and decreases strictly thereafter; its boundary values at zero and infinity are both zero. Therefore \(\sup_s E_m(s)=C_m\), with a unique maximizing jump \(s_m=e^{-r_m}\).

**3. Arbitrary bounded variation and all equality cases.** Every real distributional \(BV(0,1)\) function has, up to a constant and almost-everywhere equality, the signed-jump representation
\[
f(x)=a+\int_{(0,1)}g_s(x)\,d\mu(s),\qquad \mu=Df,
\]
with \(|\mu|(0,1)=|Df|(0,1)\). Fubini applies because \(\mu\) is finite and all the jump kernels are bounded. Since \(I-H^m\) annihilates constants, the triangle inequality followed by Tonelli gives
\[
\|f-H^mf\|_1
\le\int_{(0,1)}\|g_s-H^mg_s\|_1\,d|\mu|(s)
=\int E_m(s)\,d|\mu|(s)
\le C_m|\mu|(0,1).
\]
The unique maximizer of \(E_m\) forces equality in the final inequality only when the entire variation measure is supported at \(s_m\). Such a measure is \(b\delta_{s_m}\), and the corresponding functions are precisely the claimed single jumps; their response has one sign, so they attain the bound. This also handles signed inputs and rules out other extremizers.

**4. Order dependence.** The products \(\prod_{i=1}^{m}U_i\) strictly decrease when an independent factor is added; for each fixed \(s\in(0,1)\), \(H^{m+1}g_s(x)<H^mg_s(x)\) for \(x>s\) with positive mass of the relevant interval. Thus \(E_{m+1}(s)>E_m(s)\), giving \(C_{m+1}>C_m\) by using the previous optimizer. Each \(C_m<1\) because \(E_m(s)<1-s<1\). For fixed \(s\), \(H^mg_s(x)\to0\) for almost every \(x\), so \(E_m(s)\to1-s\). Choosing arbitrarily small positive \(s\) proves \(C_m\to1\). For \(m=1\), \(r_1=1\) and \(C_1=e^{-1}\).

**5. Sharp large-order deficiency.** Since \(r_m^m/m!=1\), the exponential-series remainder gives exactly
\[
1-C_m=e^{-r_m}\left(1+\sum_{j=1}^{\infty}\frac{r_m^j}{(m+1)(m+2)\cdots(m+j)}\right).
\]
Stirling implies \(r_m/m\to1/e\), hence the parenthesis tends to \(1+\sum_{j\ge1}e^{-j}=e/(e-1)\), by dominated convergence using an eventual geometric majorant. A stronger Stirling expansion yields
\[
r_m=\frac{m}{e}+\frac{\log(2\pi m)}{2e}+o(1),
\]
which inserted into the exact remainder proves the displayed asymptotic.

## Verification
A standalone Python checker numerically integrates the independently evaluated single-jump kernel at and away from its predicted maximizing location for twelve iteration orders; tests 960 random signed multijump configurations for the global upper bound; and checks the asymptotic expression at five orders up to \(m=640\). All checks pass. They complement the analytical proof and do not establish its universal quantifiers. Run `python check_cesaro.py` with Python, SciPy and mpmath installed.

## Relationship to prior work
Galaz Fontes and Solís [1] establish Cesàro-iterate convergence criteria, and Adell and Lekuona [2] give probabilistic iterate representations and sharp sup-norm rates to a boundary limit. These furnish the operator context and gamma representation but do not state this all-order sharp \(BV\)-to-\(L^1\) identity-defect norm or the unique optimizing discontinuity. Albanese, Bonet and Ricker [3] examine spectral, ergodic and function-space properties, not this approximation norm. Birou [4] addresses sharp convergence estimates of iterates to a constant in a different norm. Related exact finite-matrix averaging results concern discrete norms and do not imply the continuous integral calculation here. A prior publication of the same calculation, possibly under a Hausdorff-operator or probability interpretation, has not been definitively excluded; independent historical-priority review remains necessary.

## Limitations
The theorem does not assert boundedness of \(H\) on all of \(L^1(0,1)\). It is limited to real one-dimensional \(BV(0,1)\), unweighted Lebesgue error, classical prefix averaging, and integer powers. It does not classify weighted Cesàro operators, noninteger orders, higher-dimensional versions or other norms. All novelty comparisons are conditional on the primary works that were accessible and inspected.

## References
[1] F. Galaz Fontes and F. J. Solís, *Iterating the Cesàro operators*, Proceedings of the American Mathematical Society 136 (2008), 2147–2153, electronically published 2008-02-14, https://doi.org/10.1090/S0002-9939-08-09197-1.

[2] J. A. Adell and A. Lekuona, *Rates of convergence for the iterates of Cesàro operators*, Proceedings of the American Mathematical Society 138 (2010), 1011–1021, electronically published 2009-10-22, https://doi.org/10.1090/S0002-9939-09-10127-2.

[3] A. A. Albanese, J. Bonet and W. J. Ricker, *Mean ergodic properties of the continuous Cesàro operators*, arXiv:1310.5083v1, 2013-10-18, https://arxiv.org/abs/1310.5083.

[4] M. Birou, *Sharp inequalities for rates of convergence of iterates of some operators preserving constants*, Studia Universitatis Babeș-Bolyai Mathematica (2021), https://doi.org/10.24193/subbmath.2021.2.05.
