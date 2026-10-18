# Exact r-Lambert quantiles for the FEx-G family
## Finding
Let
\[
p=\frac{e}{e-1},
\qquad
F(x)=p\left(1-\exp\left[-\left(1-(1-G(x))^{G(x)}\right)\right]\right),
\]
where \(G\) is a continuous strictly increasing baseline distribution function on its support.

For \(u\in(0,1)\), define
\[
\kappa(u)=-\log\!\left[1+\log\!\left(1-\frac{u}{p}\right)\right].
\]
Because \(1-u/p\in(e^{-1},1)\), one has \(\kappa(u)>0\).

Let \(r(u)<0\) be the unique real solution of
\[
r(u)e^{r(u)}-r(u)=\kappa(u).
\]
Equivalently, this is the negative real branch of the \(r\)-Lambert equation \(y e^y+r y=a\) at parameter \(r=-1\). Then
\[
w(u)=1-e^{r(u)}
\]
is the exact baseline probability corresponding to the FEx-G \(u\)-quantile, and
\[
Q_F(u)=G^{-1}\!\left(1-e^{r(u)}\right).
\]

For the Kumaraswamy baseline
\[
G(x)=1-(1-x^a)^b,\qquad 0<x<1,\quad a,b>0,
\]
the exact quantile is
\[
Q_F(u)=\left[1-\exp\!\left(\frac{r(u)}{b}\right)\right]^{1/a}.
\]

The target paper reduces its general quantile to an implicit equation and recommends numerical root finding. Its later FExKw display is called a quantile function but still contains the unknown \(x\) through \(k=1-x^a\). The formula above removes that circularity and identifies the unique admissible generalized-Lambert branch.

## Assumptions and scope
The baseline \(G\) is continuous and strictly increasing so that \(G^{-1}\) is unambiguous. The FEx-G transformation is exactly equation (2.2) of Eldemery et al. The result concerns mathematical inversion; it does not claim that numerical evaluation of the generalized Lambert function is unnecessary.

The notation \(r(u)\) is defined self-containedly as the unique negative solution of \(t e^t-t=\kappa(u)\), so the statement does not depend on any software convention for generalized-Lambert branch names.

## Proof
Set \(w=G(x)\) and
\[
z(u)=1+\log\!\left(1-\frac{u}{p}\right).
\]
Inverting the outer exponential in the FEx-G CDF gives
\[
(1-w)^w=z(u).
\]
For \(u\in(0,1)\), \(0<z(u)<1\). Taking logarithms yields
\[
w\log(1-w)=\log z(u).
\]

Put \(t=\log(1-w)\). Then \(t<0\), \(w=1-e^t\), and
\[
(1-e^t)t=\log z(u),
\]
or
\[
t e^t-t=-\log z(u)=\kappa(u).
\]

For \(t<0\), define \(H(t)=t(e^t-1)\). Its derivative is
\[
H'(t)=e^t(1+t)-1<0.
\]
If \(-1<t<0\), then \(e^t(1+t)<1\); if \(t\le-1\), the first term is nonpositive. Also
\[
\lim_{t\to-\infty}H(t)=+\infty,
\qquad
\lim_{t\uparrow0}H(t)=0.
\]
Thus every \(\kappa(u)>0\) has exactly one negative solution \(r(u)\). Substitution gives \(w=1-e^{r(u)}\), hence the general quantile formula.

For the Kumaraswamy baseline, \(1-w=(1-x^a)^b=e^{r(u)}\). Therefore
\[
1-x^a=e^{r(u)/b},
\]
which yields the stated specialization.

## Verification
The included checker evaluates the unique negative root by bisection and substitutes the resulting baseline probabilities back into the original FEx-G CDF. It checks probability levels from \(10^{-6}\) through \(1-10^{-6}\).

For the Kumaraswamy parameters \(a=1.7\) and \(b=2.3\), it verifies the levels \(u=0.1\), \(0.5\), and \(0.9\) to absolute error below \(2\times10^{-12}\).

These calculations are consistency checks only; the infinite-domain claim follows from the exact algebra and the monotonicity proof above.

## Relationship to prior work
Eldemery et al. derive the FEx-G CDF and explicitly reduce quantile inversion to
\[
w\log(1-w)=\log z,
\]
then recommend Newton–Raphson. Their later FExKw display retains \(x\) through \(k=1-x^a\), so it is an implicit rearrangement rather than a function of \(u\) alone.

Mező and Baricz developed generalized Lambert functions for equations extending \(y e^y=a\). The present finding identifies the FEx-G inversion as the special case \(y e^y-y=a\), proves the probability-admissible branch is the unique negative one, and composes it with an arbitrary baseline quantile.

The 2025 paper with the same “flexible exponential-G” acronym defines a different family,
\[
1-\exp\!\left[-\frac{G_1(x)^\nu}{\overline G_2(x)^\omega}\right],
\]
so its quantile results do not cover this parameter-free 2026 transformation.

Focused searches for the target DOI together with Lambert, generalized Lambert, \(r\)-Lambert, and quantile terminology did not locate this inversion or a published correction.

## Limitations
The representation uses a generalized special function rather than elementary functions. Numerical evaluation of the selected branch is still required unless a dedicated implementation is available.

No claim is made that generalized-Lambert evaluation is faster than every direct root solver. The mathematical contribution is exact identification of the inverse and its admissible branch.

## References
1. E. M. Eldemery, H. M. Almongy, K. M. Mahfouz, M. M. El Genidy, I. Elbatal, H. M. Aljohani, and A. Z. Afify, “A unified parsimonious exponential-G family for modeling real-world data: theory and statistical inference,” AIMS Mathematics 11 (2026), 13865–13912. DOI: 10.3934/math.2026571.
2. I. Mező and Á. Baricz, “On the generalization of the Lambert W function,” Transactions of the American Mathematical Society 369 (2017), 7917–7934. DOI: 10.1090/tran/6911.
3. J. N. Al Abbasi, I. Elbatal, A. Z. Afify, and H. A. Mahran, “A novel flexible exponential-G family: Properties, estimation, and applications in environmental and engineering sciences,” Journal of King Saud University – Science 37 (2025), article 8202025. DOI: 10.25259/JKSUS_820_2025.
