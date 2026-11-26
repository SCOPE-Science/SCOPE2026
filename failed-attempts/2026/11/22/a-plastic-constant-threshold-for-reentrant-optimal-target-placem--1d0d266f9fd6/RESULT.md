# A plastic-constant threshold for reentrant optimal target placement in Brownian resetting

## Finding

**Theorem (a single exact one-third crossing and forced nonmonotonicity).** Fix a Brownian diffusivity \(D>0\), a Poisson reset rate \(r>0\), and a target at \(-L<0\). A single Brownian searcher, beginning at zero, must locate both that target and a second target at \(x>0\). On the first visit to either target, it is immediately returned to zero; the visited target is removed, while the remaining one stays absorbing. Between visits an independent Poisson clock of rate \(r\) also returns the searcher to zero. Let \(x_*(L)>0\) uniquely minimize the total mean completion time over \(x>0\).

Write \(b=L\sqrt{r/D}\), and let the **plastic constant** \(\rho>1\) be the unique positive root of \(\rho^3-\rho-1=0\). Then, with \(b_c=\tfrac32\log\rho=0.421799361484\ldots\), the exact all-parameter classification is
\[
\frac{x_*(L)}L
\begin{cases}
>\frac13,&0<b<b_c,\\
=\frac13,&b=b_c,\\
<\frac13,&b>b_c.
\end{cases}
\]
In addition,
\[
\lim_{b\downarrow0}\frac{x_*}L=\sqrt2-1,
\qquad
\frac{x_*}L=\frac13-\frac{\log2}{3b}+o(b^{-1})
\quad(b\to\infty).
\]
Consequently the optimal ratio is **not monotone**: it crosses below its large-distance limit, then returns toward that limit from below. In particular, at least one strictly attained global minimum of the ratio occurs at a finite \(b>b_c\). The uniqueness or exact location of that secondary minimum is not asserted.

## Assumptions and scope

On each free segment \(dX_t=\sqrt{2D}\,dW_t\) on the real line. A Poisson relocation and an absorption-triggered relocation take negligible time and restore the particle to zero. Each target is permanently removed when first hit. Both targets are absorbing until hit; there is no hidden random target and no distribution of reset sites. All first-passage times and the mean time to find **both** targets are averaged over Brownian and reset randomness. The optimization varies only \(x>0\) while \(L,D,r\) remain fixed; no reset-rate optimization is claimed.

Set the dimensionless right distance \(a=x\sqrt{r/D}>0\), left distance \(b=L\sqrt{r/D}>0\). The exact mean completion time, established in the cited source, is \(T_2=F(a,b)/r\) with
\[
F(a,b)=\frac{\sinh^2 a+\sinh^2 b}{\sinh a+\sinh b}+\cosh a+\cosh b-2.
\]

## Proof

**1. The exact derivative and unique global minimum.** Let \(S=\sinh b>0\) and \(u=e^a>1\). Direct differentiation of the displayed exact mean gives
\[
\partial_a F(a,b)=\frac{P(u,S)}{4u(\sinh a+S)^2},
\quad
P(u,S)=(u^2-1)^2+4Su(u^2-1)-4S^2.
\]
All denominator factors are positive. At \(u=1\), \(P(1,S)=-4S^2<0\). For \(u>1\),
\[
\partial_uP=4u(u^2-1)+4S(3u^2-1)>0,
\]
and \(P(u,S)\to+\infty\) as \(u\to\infty\). Thus there is exactly one critical \(a=a_*(b)>0\), the derivative changes from negative to positive there, and it is the unique global minimizer.

**2. Exact crossover factorization.** At the test ratio \(a=b/3\), put \(t=e^{b/3}>1\). Then \(u=t\) and \(S=(t^3-t^{-3})/2\). Multiplication by the positive factor \(t^6\) gives the **exact algebraic identity**
\[
t^6P\left(t,\frac{t^3-t^{-3}}2\right)
=(t-1)^2(t+1)^2(t^2+1)(t^6-t^2-1).
\]
The first three right-hand factors are strictly positive. Writing \(y=t^2>1\), the sign is therefore exactly that of \(y^3-y-1\), a strictly increasing polynomial on \((1,\infty)\) with unique zero \(\rho>1\). Since \(P\) is strictly increasing in \(u\), \(P(e^{b/3},\sinh b)<0\) is equivalent to \(a_*(b)>b/3\), and likewise for equality and positivity. Because \(t^2=e^{2b/3}\), the sole threshold is \(b_c=(3/2)\log\rho\). This proves all three branches with strict inequalities, not merely a numerical crossover.

**3. Both ends and nonmonotonicity.** As \(b\downarrow0\), the unique positive-root equation \(P(e^a,\sinh b)=0\) has leading terms \(4a^2+8ab-4b^2=0\), so \(a_*/b\to\sqrt2-1\). As \(b\to\infty\), the same equation gives \(e^{3a_*}/\sinh b\to1\) (the remaining quartic term is lower order), hence \(a_*=(b-\log2)/3+o(1)\), yielding the stated ratio expansion. The ratio is a real-analytic function of \(b>0\) by the strictly positive derivative \(\partial_uP\) at its root. It is greater than one third for \(b<b_c\), less than one third thereafter, and tends to one third from below. Thus it achieves some global minimum strictly below one third at an interior finite \(b>b_c\); analyticity and nonconstancy make every isolated minimizing point a strict local minimum. Existence is asserted, not uniqueness.

## Verification

Run `python verify.py` with SymPy and SciPy. The code checks the exact derivative factorization and the exact algebraic crossover factorization symbolically, verifies the unique-root sign rule for sample dimensionless distances, and independently compares the analytic minimizers to nearby mean-time values and finite-difference derivatives. It also checks small-/large-distance asymptotics. These finite calculations do not prove the global sign classification; that follows from the displayed polynomial factorization and monotonicity.

## Relationship to prior work

Calvert and Evans, *Searching for clusters of targets under stochastic resetting* (2021), derive the **same exact mean time and the same unique-optimum quartic** in their Eqs. (30) and (35). They obtain the limiting ratios \(\sqrt2-1\) and \(1/3\) in their Eqs. (37) and (40), and exhibit fixed-parameter optimization numerically. The new statement is specifically the exact plastic-constant **all-intermediate-parameter sign classification** and its forced nonmonotone optimal relative placement; it does not claim the underlying optimizer or limiting values as new. This crossover is algebraically derivable from their quartic, so independent priority assessment against implicit treatment and later work remains important.

Pal and Prasad, *First passage under stochastic resetting in an interval* (2018), supply the two-boundary first-hit and splitting-probability ingredients but not the completed two-target optimization or its relative-placement crossover. A separate public result titled *Two-target bang–bang resetting: exact bias thresholds and universal discounted optimality* concerns a hidden **single** target and optimal **reset-site distribution**, not deterministic placement of a second target that must also be found. Its conclusions do not give the sign classification here.

## Limitations

The result is for one-dimensional diffusion, exponentially distributed reset intervals and instantaneous relocations, with the first-found target removed. The optimizer's existence and uniqueness are inherited from and independently checked against the source's exact mean-time formula. The new statement does **not** prove a unique minimum of the ratio itself or optimize reset rate. As the threshold follows by a special substitution into a previously published quartic, the increment in originality is the exact parameter-phase classification and nonmonotonicity, not a new renewal law. Unindexed implicit consequences in other treatments could reduce priority. Independent scientific validation has not occurred.

## References

1. G. R. Calvert and M. R. Evans, *Searching for clusters of targets under stochastic resetting*, arXiv:2111.02335v1, first posted 2021-11-03, https://arxiv.org/abs/2111.02335; full text, Sections 3.2–3.4, Eqs. (30), (35)–(40).
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009v1, first posted 2018-12-07, https://arxiv.org/abs/1812.03009; two-boundary first-hit and splitting-probability formulas.
