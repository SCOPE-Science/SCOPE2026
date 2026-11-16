# Sharp second Taylor-section evaluation on sublinear Hardy spaces

## Finding

For every real \(0<p<1\), the endpoint evaluation of the degree-two Taylor section of an analytic Hardy function has a sharp coefficient norm given by one univariate quartic root. Write \(f(z)=\sum_{j\ge0}a_jz^j\), \(L(f)=a_0+a_1+a_2\), and \(t=2/p>2\). Define
\[
Q_t(x)=(t-1)^2(t-2)x^4+(t-1)(3t-4)x^3-2(t-1)(t-4)x^2-2(2t-3)x-2.
\]
There is exactly one positive zero \(x_t\) of \(Q_t\), and \(0<x_t<1\). Put \(y_t=x_t/(1+(t-1)x_t)\). Then
\[
\boxed{\ \sup_{\|f\|_{H^p}\le1}|a_0+a_1+a_2|=\frac{1+t(x_t+y_t)+\tfrac12t(t-1)x_t^2}{(1+x_t^2+y_t^2)^{t/2}}.\ }
\]
Up to multiplication by any unimodular constant, the **only** norm-one extremizer is
\[
f_t(z)=\frac{(1+x_tz+y_tz^2)^t}{(1+x_t^2+y_t^2)^{t/2}}.
\]
The power means the analytic logarithm branch normalized to one at the origin, and is unambiguous because its quadratic base is zero-free in the closed disk. For \(p=1/2\), this gives \(x_t\approx0.614776929197860\), \(y_t\approx0.216141150628259\) and optimal norm \(3.247498596339727\ldots\).

## Assumptions and scope

The analytic Hardy space \(H^p(\mathbb D)\) uses probability-normalized arclength:
\[
\|f\|_{H^p}^p=\lim_{r\uparrow1}\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^p\,d\theta.
\]
The range is all real \(0<p<1\), and \(a_j=f^{(j)}(0)/j!\). The functional equals evaluation at one of the *Taylor section*, not boundary evaluation of the full function. Uniqueness is modulo multiplication of the function by a complex constant of modulus one. We use the 2026 theorem of Brevig and Søvik [1] that every unit-norm extremizer of a nonzero continuous linear functional on \(H^p\), \(0<p<1\), is outer. Its publication date and theorem statement are independently checkable at the listed arXiv record.

## Proof

**1. Reduction to a unit Hilbert-space root.** Coefficient evaluation is bounded on \(H^p\), and the unit ball is a normal family, so the coefficient functional attains its positive supremum (compact convergence of a maximizing sequence, plus Fatou's lemma). Any extremizer has quasi-norm exactly one by homogeneity. It is outer by [1, Theorem 1], hence zero-free in the disk. The analytic branch \(g=f^{p/2}\) lies in \(H^2\) and obeys \(\|g\|_2=1\). Conversely any zero-free \(H^2\) polynomial with norm one yields an admissible \(H^p\) function by taking its analytic \(t\)-th power. Write \(g(z)=b_0+b_1z+b_2z^2+\cdots\). Here \(b_0\ne0\), and direct expansion gives
\[
a_0=b_0^t,\quad a_1=t b_0^{t-1}b_1,\quad a_2=t b_0^{t-1}b_2+\tfrac12t(t-1)b_0^{t-2}b_1^2.
\]
These equalities hold for noninteger \(t\) using the analytic branch.

**2. Positive two-variable global upper bound.** Put \(x=|b_1|/|b_0|\ge0\), \(y=|b_2|/|b_0|\ge0\). Parseval gives \(|b_0|^2(1+x^2+y^2)\le1\). The triangle inequality and \(t>2\) yield
\[
|L(f)|\le F_t(x,y):=\frac{1+t(x+y)+\tfrac12t(t-1)x^2}{(1+x^2+y^2)^{t/2}}.
\]
Every pair \((x,y)\) can be realized by a normalized quadratic with aligned positive coefficients; for the particular maximizing pair below its quadratic is outer. Since the numerator grows at most quadratically while the denominator grows as \((x^2+y^2)^{t/2}\), \(F_t(x,y)\to0\) at infinity. Along either coordinate axis the derivative into the positive quadrant is strictly positive: at \(x=0\), \(\partial_x F_t>0\), and at \(y=0\), \(\partial_y F_t>0\). Thus any global maximizer lies in the strictly positive quadrant.

**3. Unique critical point and explicit quartic.** Let
\[
N=1+t(x+y)+\tfrac12t(t-1)x^2,\qquad R=1+x^2+y^2.
\]
The stationarity conditions for \(N/R^{t/2}\) at \(x,y>0\) are precisely
\[
[1+(t-1)x]R=xN,\qquad R=yN.
\]
Dividing gives \(y=x/[1+(t-1)x]\). Writing \(D=1+(t-1)x\), substitution yields the **exact identity**
\[
R-yN=-\frac{Q_t(x)}{2D^2}.
\]
For \(t>2\), the coefficient sequence of \(Q_t\), in descending order, is \((+,+,+,-,-)\) if \(2<t<4\), and \((+,+,-,-,-)\) if \(t>4\), with the middle coefficient zero when \(t=4\). In all cases there is exactly one sign change. Descartes' rule of signs therefore gives at most one positive root. As \(Q_t(0)=-2\) and \(Q_t(1)=(t-1)(t^2-2t+2)>0\), there is exactly one positive root \(x_t\in(0,1)\). Consequently there is exactly one positive critical pair, and the already-established existence of an interior maximizer forces it to be \((x_t,y_t)\). Evaluation gives the norm formula.

**4. Constructing the extremal and classifying equality.** The positive solution satisfies \(0<x_t<1\), \(0<y_t<1\), and \(x_t<1+y_t\). The real Schur–Cohn quadratic criterion now shows \(1+x_tz+y_tz^2\) has no zero in \(|z|\le1\). Thus its normalized analytic \(t\)-th power defines an \(H^p\) function with unit quasi-norm, because \(p t=2\) and Parseval yields \(\int|1+x_t e^{i\theta}+y_t e^{2i\theta}|^2\,d\theta/(2\pi)=1+x_t^2+y_t^2\). Its first three Taylor coefficients are positive and attain \(F_t(x_t,y_t)\).

Any other extremizer must give equality in the triangle inequality and in Parseval's coefficient bound, so its Hilbert root has no coefficients beyond degree two. After fixing its nonzero constant coefficient to be positive, equality of the four summands in \(L(f)\) forces both first and second coefficients to be positive real. The unique maximizing pair then forces the displayed function; restoration of the arbitrary global unimodular phase gives precisely the stated family. There are no equality cases with an inner factor, by [1].

## Verification

`CHECK.py` is a standalone standard-library script. It tests the quartic coefficient signs and endpoint values for a range of rational exponents, verifies the stationary polynomial identity in exact rational arithmetic, brackets the unique positive roots, confirms strict disk stability of the quadratic factors, and compares each computed optimum with a large reproducible grid of competitors. Its finite tests supplement, rather than replace, the all-real-exponent Descartes, existence and equality-case arguments. Run `python3 CHECK.py` without external packages.

## Relationship to prior work

Brevig–Søvik [1] supplies the essential outer-extremizer theorem for arbitrary nontrivial bounded Hardy functionals, but neither evaluates \(L=a_0+a_1+a_2\) nor determines its norming functions. Brevig–Saksman [2] computes the isolated second-coefficient norm \(\|a_2\|\) for all \(0<p<1\) and derives a general finite-coefficient structural reduction; it does not evaluate the **simultaneous** first-three-coefficient sum. Brevig–Grepstad–Instanes [3] studies the fixed-origin optimization of individual Taylor coefficients, especially the first, not this Taylor-section functional. The publicly accessible related result *A sharp two-jet Hardy quasi-norm transition and an exact second-coefficient frontier* [4] computes \(a_0+\tau a_2\) at \(p=1/2\): it omits the first coefficient, so its formula cannot imply the present all-exponent three-term optimization. An additional published all-exponent extension of that two-jet problem likewise omits \(a_1\). Prior work's broad extremal-structure theorems motivate and permit the reduction but do not supply the quartic solution for this particular natural functional.

## Limitations

The theorem is limited to the endpoint of the *degree-two* Taylor section, not arbitrary section degrees or other coefficient weights, and requires real \(0<p<1\). It invokes an independently published outer-extremizer theorem; that premise is not reproved here. Although checked sources and mathematical implications reveal no already published exact three-term formula, less discoverable classical Carathéodory–Fejér extremal literature could contain an equivalent result; historical priority thus remains a qualified best-knowledge assessment. Numerical tests do not establish the continuous theorem. No independent audit of this finding has been performed.

## References

[1] O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788v1, first posted 2026-10-15, Theorem 1. https://arxiv.org/abs/2610.21788

[2] O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547v1, first posted 2019-05-23, *Proc. Amer. Math. Soc.* 148 (2020), 3911–3924. https://arxiv.org/abs/1905.09547

[3] O. F. Brevig, S. Grepstad and S. M. Instanes, *F. Wiener's trick and an extremal problem for \(H^p\)*, arXiv:2011.07790v1, first posted 2020-11-16, *Comput. Methods Funct. Theory* 23 (2023), 697–722. https://arxiv.org/abs/2011.07790

[4] *A sharp two-jet Hardy quasi-norm transition and an exact second-coefficient frontier*, mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-two-jet-hardy-quasi-norm-transition-and-an-exact-second--416654e40ea0
