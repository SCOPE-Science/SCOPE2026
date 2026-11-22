# Sharp log-concavity and discrete-aging phase boundaries for Poisson–Loai counts

## Finding
For the Poisson–Loai count law of Ahmadini, Ahsan-ul-Haq and Hussain (2024), with parameters \(\alpha>0\), \(\theta>0\), and masses
\[
p_n=\frac{\theta^2}{2(1+\alpha)(1+\theta)^3}
\left(\frac1{1+\theta}\right)^n
\{\alpha\theta n^2+(2+3\alpha\theta)n+2(2+\theta+\alpha\theta)\},\quad n=0,1,\ldots,
\]
the following **complete** phase diagram holds. Define
\[
L(\alpha,\theta)=\alpha(3\alpha-1)\theta^2+2\alpha\theta+1,
\qquad H(\alpha,\theta)=L(\alpha,\theta)+\alpha+2\alpha^2\theta.
\]
The full mass sequence is log-concave exactly when \(L\ge0\). The standard discrete hazard \(h_n=\Pr(X=n)/\Pr(X\ge n)\) is nondecreasing at every integer age exactly when \(H\ge0\). If \(H<0\), the hazard strictly decreases initially, then increases eventually, with **exactly one transition** and at most one flat consecutive step; its turning-age condition is explicit below. Thus failure of log-concavity and failure of increasing failure rate (IFR) have distinct sharp boundaries.

For \(\alpha\ge1/3\), both properties hold strictly throughout \(\theta>0\). For \(0<\alpha<1/3\), define
\[
\theta_L(\alpha)=\frac{\alpha+\sqrt{\alpha(1-2\alpha)}}{\alpha(1-3\alpha)},\qquad
\theta_H(\alpha)=\frac{\alpha(1+\alpha)+(1-\alpha)\sqrt{\alpha(1+\alpha)}}{\alpha(1-3\alpha)}.
\]
These obey \(0<\theta_L(\alpha)<\theta_H(\alpha)\). The mass is log-concave for \(0<\theta\le\theta_L\), is not log-concave for \(\theta>\theta_L\), and the hazard is IFR for \(0<\theta\le\theta_H\), but not IFR for \(\theta>\theta_H\). In particular, the nonempty band \(\theta_L<\theta\le\theta_H\) is **IFR without log-concavity**. At equality the relevant initial adjacent-pair inequality is exactly an equality, and all later ones are strict.

For the rational parameters \(\alpha=1/10\), \(\theta=28/5\), the mass is not log-concave but the hazard is strictly increasing; at \(\alpha=1/10\), \(\theta=6\), the hazard begins with a strict downward step.

## Assumptions and scope
The primary object is the properly normalized nonnegative-integer Poisson–Loai distribution with strictly positive \(\alpha,\theta\), exactly as defined by its displayed published probability mass function. The primary classification is a statement about the **count distribution**, not the continuous mixing Loai lifetime distribution. Log-concavity means \(p_n^2\ge p_{n-1}p_{n+1}\) for all integer \(n\ge1\). IFR means nondecreasing \(h_n=p_n/\sum_{k=n}^\infty p_k\) for all integer \(n\ge0\); the alternative convention \(p_n/\Pr(X>n)=h_n/(1-h_n)\), used in some count-model literature, has the same adjacent monotonicity because this transformation is increasing on \([0,1)\). All counts have positive mass, so both hazards are defined. Parameters outside \(\alpha>0\) are not treated.

## Proof
Let \(q=(1+\theta)^{-1}\in(0,1)\) and set
\[
A=\alpha\theta,\quad B=2+3\alpha\theta,\quad C=2(2+\theta+\alpha\theta),\quad
P(x)=Ax^2+Bx+C,\quad K=\frac{\theta^2}{2(1+\alpha)(1+\theta)^3}.
\]
Thus \(p_n=Kq^nP(n)\), with \(A,B,C,K>0\). The standard geometric-series sums give
\[
\sum_{n\ge0}p_n=K\left\{\frac{Aq(1+q)}{(1-q)^3}+\frac{Bq}{(1-q)^2}+\frac{C}{1-q}\right\}=1,
\]
so the normalization is independently recovered.

**Log-concavity.** A direct identity valid for every real \(x\) is
\[
P(x)^2-P(x-1)P(x+1)=2A^2x^2+2ABx+B^2-A^2-2AC.
\]
Its right side is strictly increasing for \(x\ge0\), since \(A,B>0\). Hence all infinite discrete log-concavity inequalities are equivalent to the first one at \(n=1\). Substituting \(A,B,C\) gives
\[
P(1)^2-P(0)P(2)=4[\alpha(3\alpha-1)\theta^2+2\alpha\theta+1]=4L(\alpha,\theta).
\]
The positive factor \(K^2q^{2n}\) does not affect the signs, and equality at \(n=1\) is followed by strict inequalities at every later index. When \(L<0\), failures, if more than one, occupy exactly an initial interval of indices \(n\ge1\), since this polynomial grows strictly with \(n\).

**Hazard-age transitions.** Let \(R_n=\Pr(X\ge n)\). Summing the shifted geometric series yields
\[
R_n=Kq^nT(n),\quad
T(x)=\frac{P(x)}{1-q}+\frac{q(2Ax+B)}{(1-q)^2}+\frac{Aq(1+q)}{(1-q)^3}.
\]
In particular \(T(n)>0\) for every integer \(n\ge0\), and \(h_n=P(n)/T(n)\). Expanding the numerator of \(h_{n+1}-h_n\) gives the exact sign identity
\[
\operatorname{sgn}(h_{n+1}-h_n)=\operatorname{sgn} F(n),
\qquad F(x)=H(\alpha,\theta)+\frac{\alpha^2\theta^2}{2}x^2+
\left(\frac{5\alpha^2\theta^2}{2}+\alpha^2\theta+\alpha\theta\right)x.
\]
To verify the positive scaling, one may check algebraically that
\[
P(n+1)T(n)-P(n)T(n+1)
=\frac{4\theta q}{(1+\theta)(1-q)^3} F(n).
\]
All terms in \(F(n+1)-F(n)\) are strictly positive. Therefore IFR is exactly \(F(0)=H\ge0\). If \(H=0\), only \(h_1=h_0\) is a plateau; all later steps increase strictly. If \(H<0\), \(F\) has one positive real root \(\rho\) and its unique discrete sign change occurs when \(n\) crosses \(\rho\). Explicitly, with
\[
U=\frac{\alpha^2\theta^2}{2}>0,\quad
V=\frac{5\alpha^2\theta^2}{2}+\alpha^2\theta+\alpha\theta>0,\quad
\rho=\frac{-V+\sqrt{V^2-4UH}}{2U}>0,
\]
we have \(h_{n+1}<h_n\) exactly for integer \(0\le n<\rho\), equality exactly if integer \(n=\rho\), and \(h_{n+1}>h_n\) for \(n>\rho\). This proves the complete one-trough hazard shape and rules out further oscillations. The hazard tends to \(1-q=\theta/(1+\theta)\) as \(n\to\infty\).

**The sharp parameter boundaries.** The identity \(H=L+\alpha+2\alpha^2\theta\) implies \(H>L\) everywhere in the open parameter domain. When \(\alpha\ge1/3\), both are strictly positive. For \(0<\alpha<1/3\), both \(L\) and \(H\), viewed as quadratic functions of \(\theta\), have strictly negative leading coefficients and positive constant terms, hence exactly one positive root each. Solving yields \(\theta_L\) and \(\theta_H\) as displayed. The inequality \(H(\alpha,\theta_L)>0\) forces \(\theta_H>\theta_L\). These observations prove every open region and equality boundary above.

As checkable rational witnesses, at \((\alpha,\theta)=(1/10,28/5)\) one obtains \(L=-47/625\) and \(H=171/1250\), while at \((1/10,6)\), \(L=-8/25\) and \(H=-1/10\). Thus the two intermediate and non-IFR regimes genuinely occur.

## Verification
The standalone \(\texttt{check.py}\) uses exact SymPy arithmetic to recover total probability one, all polynomial determinant formulas, the infinite-index monotonicity increments, and the positive prefactor in the hazard sign identity. It independently checks the hazard and mass-curvature signs at several rational parameter pairs and multiple count indices. Its finite-index tests are **not** a proof that infinitely many inequalities hold; the strictly increasing polynomials in the proof establish that part. The mathematical proof requires no numerical search or asymptotic approximation.

## Relationship to prior work
Ahmadini, Ahsan-ul-Haq and Hussain (2024) give the Poisson–Loai mass, survival and hazard formulas as equations (2)–(4) and illustrate increasing hazard plots; their text does not provide a parameterwise necessary-and-sufficient IFR test, nor a log-concavity phase diagram. The present result derives both complete phase regions, establishes a strict IFR/non-log-concavity separation, and identifies an initial hazard decrease that the selected plots do not show. Shafiq and collaborators (2022) prove log-concavity and IFR for a different binomial–natural discrete Lindley count model. Their standard implication from log-concavity to IFR does not imply the reverse nor determine the exact different thresholds here. Other published count-distribution results (including Poisson–generalized Lindley and Poisson-mixture log-concavity studies) concern different mass families or impose different mixture restrictions, not this pair of sharp Poisson–Loai surfaces.

## Limitations
The statement applies only to the given two-parameter positive Poisson–Loai PMF and its standard discrete count hazard. It does not claim any property of the continuous Loai baseline, universal closure under mixing, or monotone dependence of the hazard on a parameter at fixed count. It is based on an analytical proof plus exact symbolic verification, and is not independently audited. Literature searching is not an exhaustive historical-priority guarantee.

## References
1. A. A. H. Ahmadini, M. Ahsan-ul-Haq and M. N. S. Hussain, “A new two-parameter over-dispersed discrete distribution with mathematical properties, estimation, regression model and applications,” *Heliyon* 10 (2024), e36764, first published 23 August 2024. DOI: https://doi.org/10.1016/j.heliyon.2024.e36764. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11400954/.
2. S. Shafiq, S. Khan, W. Marzouk, J. Gillariose and F. Jamal, “The Binomial–Natural Discrete Lindley Distribution: Properties and Application to Count Data,” *Mathematical and Computational Applications* 27 (2022), article 62. DOI: https://doi.org/10.3390/mca27040062.
