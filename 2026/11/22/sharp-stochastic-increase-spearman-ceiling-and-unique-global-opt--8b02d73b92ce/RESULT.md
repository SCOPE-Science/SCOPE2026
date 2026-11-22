# Sharp stochastic-increase Spearman ceiling and unique global optimizer for an exponentiated FGM copula

## Finding

For the two-parameter copula of Zachariah, Arshad and Pathak (2023), the largest **positive Spearman rank correlation compatible with stochastic increase** is exactly
\[
R_{\mathrm{SI}}=3\left(e^{1/2}\sqrt{\frac{\pi}{2}}\operatorname{erf}\left(\frac1{\sqrt2}\right)-1\right)^2
=0.505989303562664776\ldots.
\]
It is attained by the unique nonindependent shape and coupling pair \((\alpha,\delta)=(2,1/4)\). In contrast, the globally largest positive rank correlation is
\[
R_{\mathrm{all}}=\frac{3e}{2}\left(\frac{A(s_*)}{s_*^2}-\frac{e^{-s_*^2}}{s_*}\right)^2
=0.586623892839975836\ldots,
\]
where \(A(s)=\int_0^s e^{-t^2}\,dt\) and \(s_*\) is the **unique** root in \((1/\sqrt2,\infty)\) of
\[
A(s)=s(1+s^2)e^{-s^2}.
\]
The global maximizer is unique for positive rank correlation: \(\alpha_*=4s_*^2=3.746989957972222634\ldots\), \(\delta_*=e^{1-\alpha_*/2}/(2\alpha_*)\). Therefore any copula of this family with \(\rho_S>R_{\mathrm{SI}}\) is **not stochastically increasing**, even though it is positively quadrant dependent. The unrestricted negative bound is \(-R_{\mathrm{all}}\), by changing the sign of \(\delta\).

Moreover, among the upper-admissibility-boundary members \(\delta=\delta^*(\alpha)>0\), every rank correlation strictly between \(R_{\mathrm{SI}}\) and \(R_{\mathrm{all}}\) is attained at precisely two distinct shapes \(\alpha>2\), one on each side of \(\alpha_*\); their full copulas are distinct.

## Assumptions and scope

For \(u,v\in[0,1]\), let \(x(u)=u(1-u)\), \(f_\alpha(u)=1-e^{\alpha x(u)}\), and
\[
C_{\alpha,\delta}(u,v)=uv+\delta f_\alpha(u)f_\alpha(v),\qquad \alpha\in\mathbb R.
\]
For \(\alpha\ne0\), this is an absolutely continuous copula exactly when \(|\delta|\le\delta^*(\alpha)\), where
\[
\delta^*(\alpha)=
\begin{cases}
1/\alpha^2,&\alpha\le2,\quad\alpha\ne0,\\
e^{1-\alpha/2}/(2\alpha),&\alpha>2.
\end{cases}
\]
At \(\alpha=0\) the formula is the independence copula for every finite \(\delta\). The two coordinate marginals are uniform. Stochastic increase (SI) means that for every \(0<v<1\), the conditional CDF \(u\mapsto\Pr(V\le v\mid U=u)\) is nonincreasing on \((0,1)\). Rank correlation is \(\rho_S(C)=12\int_0^1\!\int_0^1 C(u,v)\,du\,dv-3\).

All maxima in this claim optimize over the complete admissible real-shape family, not a sampled range of shapes. Statements of SI here refer to nonindependent positive-dependence members unless explicitly stated otherwise. The findings concern this particular copula family, not all positively dependent copulas.

## Proof

**1. Admissibility and rank correlation.** Direct differentiation gives
\[
c_{\alpha,\delta}(u,v)=1+\delta\alpha^2g_\alpha(u)g_\alpha(v),\quad
g_\alpha(u)=(1-2u)e^{\alpha u(1-u)}.
\]
Since \(g_\alpha(1-u)=-g_\alpha(u)\), positivity of the density for every pair is equivalent to \(|\delta|\alpha^2\max_{[0,1]}|g_\alpha|^2\le1\). From
\[
g_\alpha'(u)=e^{\alpha x(u)}\{\alpha(1-2u)^2-2\},
\]
its absolute maximum is \(1\) for \(\alpha\le2\), and \(\sqrt{2/\alpha}e^{\alpha/4-1/2}\) for \(\alpha>2\); this proves the stated exact admissibility. Put \(h(\alpha)=\int_0^1(e^{\alpha x(u)}-1)\,du\). Separability of the copula yields
\[
\rho_S(C_{\alpha,\delta})=12\delta\,h(\alpha)^2.
\]
For \(\alpha\ne0\), \(h(\alpha)\ne0\), so its sign is the sign of \(\delta\).

**2. Exact stochastic-increase boundary.** The conditional CDF is \(v+\delta f_\alpha'(u)f_\alpha(v)\), with derivative \(\delta f_\alpha''(u)f_\alpha(v)\). For \(\alpha\ne0\), \(0<v<1\), and \(\delta>0\), the sign of this derivative is precisely the sign of \(\alpha(1-2u)^2-2\): indeed \(f_\alpha''=-\alpha e^{\alpha x(u)}\{\alpha(1-2u)^2-2\}\), while \(f_\alpha(v)\) has the opposite sign from \(\alpha\). Consequently SI holds exactly for \(\alpha\le2\). At every \(\alpha>2\) the derivative is positive for some near-endpoint \(u\) and negative at \(u=1/2\), so even the weaker SI property fails. For \(\delta<0\) no nonindependent member is SI: at \(\alpha\le2\) the sign is reversed, and at \(\alpha>2\) it changes with \(u\). Independence is SI by convention.

**3. The sharp SI ceiling.** For \(\delta>0\), maximize first over \(\delta\), giving
\[
R(\alpha)=12\left(\frac{h(\alpha)}{\alpha}\right)^2,\qquad\alpha\le2,\ \alpha\ne0.
\]
The positive function \(h(\alpha)/\alpha\) is strictly increasing over the real line, as the identity
\[
\frac{h(\alpha)}\alpha
=\int_0^1x(u)\left(\int_0^1e^{t\alpha x(u)}\,dt\right)du
\]
shows by differentiation. It has limit \(1/6\) at zero, while the actual \(\alpha=0\) copula is independent. Hence the unique SI maximizing shape is \(\alpha=2\), with \(\delta=1/4\). Completing the square in \(2u(1-u)\) evaluates \(h(2)=e^{1/2}\sqrt{\pi/2}\operatorname{erf}(1/\sqrt2)-1\) and gives \(R_{\mathrm{SI}}\).

**4. The unique global optimizer.** For \(\alpha>2\), the admissible positive-correlation envelope is
\[
R(\alpha)=\frac6\alpha e^{1-\alpha/2}h(\alpha)^2.
\]
Write \(s=\sqrt\alpha/2>1/\sqrt2\), \(A(s)=\int_0^s e^{-t^2}\,dt\). A change of variables gives \(h(\alpha)=e^{s^2}[A(s)/s-e^{-s^2}]\), so
\[
R(\alpha)=\frac{3e}{2}J(s)^2,\qquad J(s)=\frac{A(s)}{s^2}-\frac{e^{-s^2}}s>0.
\]
Let \(Q(s)=A(s)-s(1+s^2)e^{-s^2}\). Exact differentiation yields
\[
J'(s)=-\frac{2Q(s)}{s^3},\qquad Q'(s)=s^2(2s^2-1)e^{-s^2}.
\]
As \(Q(0)=0\), \(Q(s)<0\) on \((0,1/\sqrt2]\); it increases strictly on \((1/\sqrt2,\infty)\), tending to \(\sqrt\pi/2>0\). Thus it has one root \(s_*\) there. The positive function \(J\), and hence \(R\), strictly increases up to \(s_*\) and strictly decreases thereafter. Since \(R(2)=R_{\mathrm{SI}}<R(4s_*^2)\), this is the unique global positive maximum. Changing \(\delta\) to its negative produces the equally sharp negative minimum.

The strict two-branch statement follows from continuity and strict increase/decrease of \(R(\alpha)\) on \((2,\alpha_*)\) and \((\alpha_*,\infty)\), with \(R(\alpha)\to0\) as \(\alpha\to\infty\). Different \(\alpha\) yield distinct nonzero kernels \(f_\alpha(u)f_\alpha(v)\): proportionality would force \(e^{\alpha x}-1\) and \(e^{\beta x}-1\) proportional as functions of \(x\in(0,1/4)\), which the first two Taylor coefficients exclude unless \(\alpha=\beta\).

## Verification

A standalone checker, `check.py`, uses symbolic differentiation, high-precision numerical evaluation, independent quadrature, direct conditional-CDF derivative sign checks, and a separate numerical optimization. It reports the unique-root and correlation values to high precision, and checks the analytic derivative formulas. Execute `python check.py` from the extracted package directory (requires Python with mpmath, sympy, scipy). The analytic sign proof above establishes the global statements; finite grid or optimizer checks alone are not asserted to prove uniqueness. The computed values are illustrative decimals of exact, uniquely defined quantities.

## Relationship to prior work

Zachariah, Arshad and Pathak introduced the copula and its admissibility region, gave Spearman's-rho formulas, and reported an approximate maximum of \(0.5866\) at grid shape \(\alpha=3.8\). They also proved the sufficient \(\mathrm{TP}_2\) condition \(\delta\ge0,\alpha\le2\), which implies SI. Those facts are prior work, not claimed as new. The contribution here is the converse SI classification, its exact sharp Spearman ceiling, the unique globally optimizing shape specified by a one-root equation, and the resulting identifiable tradeoff and two-branch boundary behavior. The later 2025 dissertation by Zachariah repeats the tabulated range and sufficient \(\mathrm{TP}_2\) condition in Chapter 2, and treats distinct PGF-generated copulas in Chapter 3; the relevant passages do not supply these sharp converses or the global optimizer equation. General facts about rank-one copulas and stochastic ordering underpin this proof and are not claimed as new.

## Limitations

There is no claim of novelty in the copula construction, density, admissibility bounds, rank-correlation integral, or sufficient \(\mathrm{TP}_2\) condition. The result is exact for the stated symmetric family only; it does not establish a universal Spearman ceiling among all SI copulas. Parameterization at \(\alpha=0\) is discontinuous along admissibility-boundary rescalings, but the actual member there is independence and cannot maximize the rank correlation. No independently conducted mathematical audit or historical-priority certification is claimed. The exact global optimum numerically refines the original table only slightly; the substantive distinction is the sharp SI constraint and necessity of losing stochastic increase to exceed it.

## References

1. S. G. Zachariah, M. Arshad, and A. K. Pathak, *A new class of copulas having dependence range larger than FGM-type copulas*, arXiv:2304.02231, first submitted 5 April 2023; later *Statistics & Probability Letters* 206 (2024), 109988. https://arxiv.org/abs/2304.02231 . DOI: https://doi.org/10.1016/j.spl.2023.109988 .
2. S. G. Zachariah, *Dependence and Uncertainty: A Copula-Based Framework*, doctoral dissertation, Indian Institute of Technology Indore, April 2025; Chapter 2 (exponentiated FGM copula) and Chapter 3 (PGF copulas). https://dspace.iiti.ac.in/bitstream/123456789/16598/1/TH_745_Swaroop_Georgy_Zachariah_2001241009.pdf .
3. M. Longla, M. M. Nthiani, and F. D. Ndikwa, *Dependence and mixing for perturbations of copula-based Markov chains*, arXiv:2106.05766 (2021), *Statistics & Probability Letters* 180 (2022), 109239. https://arxiv.org/abs/2106.05766 .
