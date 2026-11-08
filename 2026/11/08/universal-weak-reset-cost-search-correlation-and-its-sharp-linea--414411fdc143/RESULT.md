# Universal weak-reset cost–search correlation and its sharp linear-growth maximum

## Finding

**Theorem.** Fix a starting distance \(a>0\) and diffusion coefficient \(D>0\). For each Poisson resetting rate \(r>0\), let \(X\) be one-dimensional Brownian diffusion with generator \(D\partial_{xx}\) on \((0,\infty)\), started at \(a\), absorbed on reaching zero, and instantaneously restarted at \(a\) at rate \(r\) while alive. Let \(T_r\) be its time to absorption. At a reset occurring from position \(x>0\), pay \(c(|x-a|)\); let \(C_r\) be the sum of all such payments before absorption.

Suppose \(c:[0,\infty)\to[0,\infty)\) is measurable, locally bounded, eventually strictly positive and regularly varying at infinity with index \(\beta\ge0\): for every \(z>0\),
\[
\lim_{u\to\infty}\frac{c(zu)}{c(u)}=z^\beta.
\]
Then all means and variances at fixed \(r>0\) are finite, and
\[
\boxed{\lim_{r\downarrow0}\operatorname{Corr}(T_r,C_r)
=R(\beta):=\frac{(\beta+1)\Gamma(\beta+1)}{2\sqrt{\Gamma(2\beta+1)}}.}
\]
The limit is independent of \(D\), \(a\), and the slowly varying factor in \(c\). Moreover,
\[
\boxed{R(\beta)\le\frac1{\sqrt2}\quad(\beta\ge0),\qquad
R(\beta)=\frac1{\sqrt2}\ \Longleftrightarrow\ \beta=1.}
\]
Thus **linear asymptotic growth is the unique growth exponent maximizing the limiting cost–first-passage correlation**. Here \(R(0)=1/2\), while \(R(\beta)\to0\) as \(\beta\to\infty\).

There is also a finite-rate structural statement: for every fixed \(r>0\) and every nonnegative measurable cost function whose second-cost resolvent integral is finite and strictly positive, the exact covariance \(\operatorname{Cov}(T_r,C_r)\) is strictly positive. The stated weak-reset limit, not a finite-rate upper bound, is what is optimized.

## Assumptions and scope

The return to \(a\) is instantaneous; its displacement generates the book-keeping cost \(C_r\) but does not extend the physical first-passage clock \(T_r\). The reset clock is independent of the Brownian noise, and the absorption event terminates the process. The local boundedness assumption eliminates cost singularities at finite displacements; regular variation provides an eventual polynomial envelope, hence finiteness of fixed-rate moments. The exponent is a property of the *asymptotic displacement cost*, not of the reset-time distribution. The value of \(c(0)\) is unrestricted. Costs are not assumed monotone.

For the finite-rate covariance assertion, regular variation is unnecessary: the nonnegative cost need only give a nonzero, finite \(\int c(|x-a|)^2G_r(x\mid a)\,dx\). This condition also implies a finite positive mean and variance for \(C_r\). The first-passage time has finite positive variance for all \(r>0\).

## Proof

**1. Killed resolvent and renewal transform.** For \(q>0\), write \(k_q=\sqrt{q/D}\), and denote by \(G_q(x\mid a)\) the killed Brownian resolvent density:
\[
G_q(x\mid a)=\frac{e^{-k_q|x-a|}-e^{-k_q(x+a)}}{2Dk_q},\quad x>0.
\]
The no-reset absorption-time transform and resolvent mass are
\[
\phi(q)=e^{-ak_q},\qquad \int_0^\infty G_q(x\mid a)\,dx=\frac{1-\phi(q)}q.
\]
For fixed \(r>0\), define \(A(q)=r[1-\phi(q)]/q\) and, for \(j=1,2\),
\[
B_j(q)=r\int_0^\infty c(|x-a|)^jG_q(x\mid a)\,dx.
\]
Conditioning on the first reset or absorption and summing the geometric renewal expansion gives, for \(s,p\ge0\),
\[
\mathbb E[e^{-sT_r-pC_r}]
=\frac{\phi(r+s)}{1-r\int_0^\infty e^{-pc(|x-a|)}G_{r+s}(x\mid a)\,dx}.
\]
Differentiation (permitted by finite moments) gives the exact identities
\[
\begin{aligned}
\mathbb E C_r&=\frac{B_1(r)}{\phi(r)},\\
\operatorname{Var}(C_r)&=\frac{B_2(r)}{\phi(r)}+\left(\frac{B_1(r)}{\phi(r)}\right)^2,\\
\mathbb E T_r&=\frac{e^\gamma-1}r,\\
\operatorname{Var}(T_r)&=\frac{e^{2\gamma}-1-\gamma e^\gamma}{r^2},\qquad
\gamma=a\sqrt{r/D}.
\end{aligned}
\]
A mixed derivative further yields
\[
\boxed{\operatorname{Cov}(T_r,C_r)
=\mathbb E C_r\left[\frac{e^\gamma-1-\gamma/2}{r}
-\left.\frac{d}{dq}\log B_1(q)\right|_{q=r}\right].}
\]
Since \(q\mapsto B_1(q)\) is a strictly decreasing Laplace transform of a positive function, its logarithmic derivative is negative. Also \(e^\gamma-1-\gamma/2>0\). This proves the finite-rate strict positivity statement without a regularly varying assumption.

**2. Dominant reset excursion and derivatives.** Put \(k=\sqrt{r/D}\). Split the resolvent integral at \(a\). For any nonnegative locally bounded \(f\),
\[
\int_0^\infty f(|x-a|)G_q(x\mid a)\,dx
=\frac{e^{-ak_q}}{Dk_q}\int_0^a f(a-x)\sinh(k_qx)\,dx
+\frac{e^{-ak_q}\sinh(ak_q)}{Dk_q}\int_0^\infty f(u)e^{-k_qu}\,du.
\]
The first term remains bounded as \(q\downarrow0\). For \(f=c^j\), \(j=1,2\), regular variation and the change of variable \(z=k_qu\), with standard Potter majorants near zero and infinity, give
\[
\int_0^\infty c(u)^j e^{-k_qu}\,du
\sim\frac{c(1/k_q)^j}{k_q}\Gamma(j\beta+1).
\]
Consequently,
\[
B_j(r)\sim\gamma\,c(1/k)^j\Gamma(j\beta+1),\qquad j=1,2.
\]
For the required derivative, let \(M(k)=\int_0^\infty c(u)e^{-ku}\,du\). The same dominated-convergence argument with one additional factor \(z\) proves
\[
-\frac{kM'(k)}{M(k)}\longrightarrow\beta+1.
\]
The bounded left-resolvent piece and its derivative are negligible compared with the right piece; the latter has prefactor \(e^{-ak}\sinh(ak)/(Dk)\to a/D\) with logarithmic derivative only \(O(1)\). Using \(q=Dk_q^2\), we obtain
\[
-\left.r\frac{d}{dq}\log B_1(q)\right|_{q=r}\longrightarrow\frac{\beta+1}{2}.
\]

**3. Normalized moments.** As \(\gamma\to0\), the exact formulas imply
\[
\begin{aligned}
\operatorname{Var}(T_r)&\sim\frac\gamma{r^2},\\
\operatorname{Var}(C_r)&\sim\gamma c(1/k)^2\Gamma(2\beta+1),\\
\operatorname{Cov}(T_r,C_r)&\sim\frac{\gamma c(1/k)}r\frac{\beta+1}{2}\Gamma(\beta+1).
\end{aligned}
\]
Indeed, the square of the mean cost is lower by a factor \(O(\gamma)\) than the leading second-cost contribution, and the first term inside the exact covariance bracket is only \(O(\gamma/r)\), versus the derivative term of order \(1/r\). Dividing by the product of standard deviations proves the universal formula.

**4. Sharp maximizer.** Let \(\psi\) and \(\psi_1\) denote di- and trigamma. For \(L(\beta)=\log R(\beta)\),
\[
L'(\beta)=\frac1{\beta+1}+\psi(\beta+1)-\psi(2\beta+1),\qquad L'(1)=0.
\]
The trigamma duplication identity gives
\[
L''(\beta)=-\frac1{(\beta+1)^2}
+\frac{\psi_1(\beta+1)-\psi_1(\beta+1/2)}2<0,
\]
because trigamma is strictly decreasing on the positive axis. Thus \(L\) is strictly concave, and its unique maximizer is \(\beta=1\). Substitution yields \(R(1)=1/\sqrt2\). Finally, Stirling's formula gives \(R(\beta)\to0\) as \(\beta\to\infty\).

## Verification

`check_cost.py` independently evaluates the killed-resolvent integrals and their \(q\)-derivatives for powers \(c(u)=u^\beta\), including \(\beta=0\), and compares the resulting finite-rate correlations to the asserted limiting gamma ratio. A second quadrature evaluates \(c(u)=u^\beta[1+\log(1+u)]\), where the slowly varying factor is nonconstant. The script checks positivity, positive variances, derivative slopes and the strict discrete maximizer inequalities. The program requires Python 3, SciPy and NumPy (SciPy installs NumPy). Execute `python check_cost.py` in the directory containing this document. The calculations provide reproducible finite-parameter checks only; the quantified statement for all \(\beta\ge0\) and all regularly varying costs is proved above, not inferred from numerical sampling.

## Relationship to prior work

Sunil, Blythe, Evans and Majumdar (arXiv:2304.09348, first submitted 19 April 2023) derive the general joint Laplace transform of first-passage time, reset count and additive reset cost, and study mean costs, cost moments, cost-optimal reset rates and heavy tails. That renewal transform is explicitly the starting point for Step 1 above, not an original contribution. The present result extracts a *weak-reset cross-observable Pearson limit* for a class of regularly varying costs and proves the exact unique maximizing exponent. These claims are not stated in the inspected main text or appendices of that source. They require long-excursion resolvent asymptotics and the trigamma comparison beyond writing down the transform.

Radice (arXiv:2201.01829) studies finite-speed returns and gamma-distributed resetting, including stationary laws and mean first-passage times; the physical clock there includes a return phase and is not the instantaneous-search clock used here. Singh (arXiv:2407.02071) studies a stochastic-return work–time Pareto front for expected quantities; its model includes the return phase and does not supply this instantaneous-reset cost–time Pearson law. The general transform from Sunil et al. remains a strong implicit-derivability priority risk, even though the specific gamma-function correlation optimization was not located in the inspected texts.

## Limitations

The Pearson law is a limit as \(r\downarrow0\), not an exact finite-rate value and not a bound on finite-rate correlations. Costs whose growth is not regularly varying, e.g. exponential costs, are outside the universality statement. This result makes no assertion about operational return-phase durations, thermodynamic work during a physical return, or higher-dimensional diffusion. The strictly positive finite-rate covariance does not imply that cost and search time are independent or perfectly correlated. Publication-priority verification is incomplete for potentially unindexed or implicit general-theorem treatments, and no independent scientific audit is asserted.

## References

1. J. C. Sunil, R. A. Blythe, M. R. Evans, S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348v1 (19 April 2023), https://arxiv.org/abs/2304.09348; J. Phys. A: Math. Theor. 56, 395001 (2023). Full text: https://arxiv.org/html/2304.09348v2.
2. M. Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829 (5 January 2022), https://arxiv.org/abs/2201.01829.
3. P. Singh, *Emerging cost-time Pareto front for diffusion with stochastic return*, arXiv:2407.02071 (2 July 2024), https://arxiv.org/abs/2407.02071.
4. N. H. Bingham, C. M. Goldie, J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), Chapters 1 and 4 (standard Potter bounds and Laplace asymptotics).
