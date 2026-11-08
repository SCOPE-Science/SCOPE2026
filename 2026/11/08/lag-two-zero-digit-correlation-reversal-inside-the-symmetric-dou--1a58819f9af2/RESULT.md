# Lag-two zero-digit correlation reversal inside the symmetric-doubling frequency plateau

## Finding

The one-symbol frequency of zero is identically \(2/3\) on a known interval of parameters, yet short-lag dependence is not frozen there. For each \(\alpha\in[5/4,3/2]\), let \(Z_n\) be the indicator of a zero signed digit at iteration \(n\) of the symmetric doubling map, with stationary initial distribution. Then

\[
\mathbb E Z_0=\frac23,\quad
\mathbb E(Z_0Z_1)=\frac1{2\alpha},\quad
\mathbb E(Z_0Z_2)=1-\frac3{4\alpha}.
\]

Consequently

\[
\operatorname{Cov}(Z_0,Z_1)=\frac{9-8\alpha}{18\alpha}<0,\qquad
\operatorname{Cov}(Z_0,Z_2)=\frac{20\alpha-27}{36\alpha}.
\]

The lag-two covariance is negative below \(\alpha=27/20\), vanishes exactly at \(27/20\), and is positive above it. For the signed digits \(D_n\in\{-1,0,+1\}\), the complete stationary consecutive-symbol law is

\[
\big(\Pr(D_0=i,D_1=j)\big)_{i,j=-1,0,+1}=
\begin{pmatrix}
u&\frac16-\nu&0\\
\frac16-\nu&\frac13+2\nu&\frac16-\nu\\
0&\frac16-\nu&\nu\end{pmatrix},\qquad
\nu=\frac{3-2\alpha}{12\alpha}.
\]

Except for null boundary conventions, no orbit has three consecutive nonzero digits in this parameter interval. Every stated stationary event probability equals its typical-orbit time frequency.

## Assumptions and scope

For every real parameter \(\alpha\in[5/4,3/2]\), define the Borel map \(S_\alpha:[-1,1]\to[-1,1]\) by

\[
S_\alpha(x)=\begin{cases}2x+\alpha,&-1\le x<-1/2,\\2x,&-1/2\le x\le1/2,\\2x-\alpha,&1/2<x\le1.\end{cases}
\]

Let \(\mu_\alpha\) be its unique ergodic absolutely continuous invariant probability, established for \(1<\alpha\le2\) in Dajani--Kalle [1]. Let \(X\sim\mu_\alpha\), \(D_n=-1,0,+1\) according as \(S_\alpha^n(X)\) belongs to the left, middle or right branch, and \(Z_n=\mathbf1_{\{D_n=0\}}\). Statements concern this stationary distribution, and hence almost every initial point relative to the same measure; no independence or Markov-order assumption is made. Endpoints and their countably many preimages have measure zero and do not affect probability formulas.

## Proof

**1. Stationary density from the transfer operator.** Put \(a=\alpha-1\), \(c=2\alpha-2\), and \(d=2-\alpha\). Throughout the stated range, \(1/4\le a\le1/2\), \(1/2\le c\le1\), \(1/2\le d\le3/4\), \(a\le d\), and \(|4-3\alpha|\le a\). Define

\[
H(x)=1+\mathbf1_{\{|x|<a\}}+\tfrac12\mathbf1_{\{|x|<c\}}+\tfrac12\mathbf1_{\{|x|<d\}},\qquad h_\alpha(x)=\frac{H(x)}{3\alpha}.
\]

As an immediate integral of the symmetric step function,
\(\int_{-1}^1H(x)\,dx=2+2a+c+d=3\alpha\). The Perron--Frobenius operator on Lebesgue densities is

\[
(\mathcal Pf)(y)=\frac12 f(y/2)+\frac12\mathbf1_{(\alpha-2,\alpha-1)}(y)f((y-\alpha)/2)
+\frac12\mathbf1_{(1-\alpha,\,2-\alpha)}(y)f((y+\alpha)/2).
\]

We verify \(\mathcal PH=H\) almost everywhere, explicitly. By symmetry it suffices to take \(0<y<1\) outside finitely many breakpoints. On this half-line \(H(y/2)=2+\mathbf1_{\{y<c\}}\). If \(0<y<a\), both outer inverse branches occur. Writing \(v=4-3\alpha\), their contributions sum to

\[
H((y-\alpha)/2)+H((y+\alpha)/2)=
2+\tfrac12\big(\mathbf1_{\{y>v\}}+\mathbf1_{\{y<v\}}\big)
+\tfrac12\big(\mathbf1_{\{y>-v\}}+\mathbf1_{\{y<-v\}}\big)=3.
\]

Consequently \(2\mathcal PH(y)=3+3=6=2H(y)\), since \(y<a\le c,d\). If \(a<y<d\), only the right-outer inverse branch remains and, using \(|v|\le a<y\), its \(H\)-value is \(1\); hence \(2\mathcal PH(y)=3+\mathbf1_{\{y<c\}}=2H(y)\). If \(y>d\), only the central inverse branch remains, giving \(2\mathcal PH(y)=2+\mathbf1_{\{y<c\}}=2H(y)\). This also covers equality between breakpoints by disregarding null endpoints. Thus \(h_\alpha\) is an invariant probability density. The uniqueness established in [1] identifies it with \(\mu_\alpha\).

**2. One-digit and lag-one probabilities.** On \(0<x<1/2\), one has \(c,d\ge1/2\), and hence \(h_\alpha(x)=(2+\mathbf1_{\{x<a\}})/(3\alpha)\). Since \(a\in[1/4,1/2]\),

\[
\Pr(Z_0=1)=2\left(\int_0^a\frac{dx}{\alpha}+\int_a^{1/2}\frac{2\,dx}{3\alpha}\right)=\frac23.
\]

Two successive zeros occur precisely for \(|X|<1/4\), because the middle branch is doubling. Since \(a\ge1/4\), the density there equals \(1/\alpha\), so \(\mathbb E(Z_0Z_1)=1/(2\alpha)\).

**3. Lag two.** If \(|X|\le1/2\), the first iterate is \(2X\). Checking the three branches of its next iterate shows that the event \(Z_0=Z_2=1\) is, modulo null endpoints, exactly the disjoint union

\[
[-1/8,1/8]\ \cup\ [-b,-1/4]\ \cup\ [1/4,b],\qquad b=\frac{\alpha+1/2}{4}.
\]

Here \(1/4\le a\le b\le1/2\). By the density formula, the symmetric core has mass \(1/(4\alpha)\), while the two exterior components contribute

\[
2\left[\int_{1/4}^{a}\frac{dx}{\alpha}+\int_a^b\frac{2\,dx}{3\alpha}\right]
=\frac{2(a-1/4)}{\alpha}+\frac{4(b-a)}{3\alpha}.
\]

Substitution of \(a=\alpha-1\) and \(b=(\alpha+1/2)/4\) gives
\(\mathbb E(Z_0Z_2)=1-3/(4\alpha)\). Subtracting the squared mean \(4/9\) gives the stated covariance and sign threshold. The first-lag covariance is strictly negative because \(\alpha\ge5/4>9/8\).

**4. Consecutive signed digits and run bound.** A positive digit occurs on \(X>1/2\). The next digit is positive exactly when \(X>t=(\alpha+1/2)/2\). Since \(t\ge\max(a,c,d)\) throughout the parameter range, \(h_\alpha=1/(3\alpha)\) on \((t,1)\); hence \(\Pr(D_0=D_1=+1)=(1-t)/(3\alpha)=(3-2\alpha)/(12\alpha)=\nu\). Symmetry gives the same negative-negative probability. A positive digit maps to at least \(1-\alpha\ge-1/2\), so an immediate negative digit is impossible (and conversely). Each of the marginal probabilities of positive and negative digits is \(1/6\), and stationarity equates row and column marginals. These facts uniquely determine the displayed \(3\)-by-\(3\) table. Finally, after two positive digits the orbit lies in \((1/2,2-\alpha]\); because \(2-\alpha\le t\), a third positive digit is impossible. The negative case is symmetric; opposite signs cannot be adjacent. Ergodicity of \(\mu_\alpha\) and the Birkhoff theorem turn these exact cylinder masses into almost-sure frequencies.

## Verification

A standalone exact-rational Python program `verify_digit_lags.py` checks the Perron--Frobenius density identity on every piece of the finite interval partition induced by all branch and density breakpoints, verifies normalization, and integrates the two zero-cylinder events and equal-sign two-digit events exactly. It passes at parameters \(5/4,51/40,13/10,4/3,27/20,7/5,29/20,3/2\). The symbolic argument above, not finite tests, establishes the assertions for every real parameter in the interval.

Run `python3 verify_digit_lags.py` with Python standard library only.

## Relationship to prior work

Dajani and Kalle [1] define these maps, prove uniqueness and ergodicity of their absolutely continuous invariant probabilities, derive general invariant-density formulas, and show that the **single-zero frequency is constant** on the larger plateau \([6/5,3/2]\). Their published density machinery can be specialized and integrated for finite digit cylinders; this is acknowledged. The present finding instead evaluates the full adjacent signed-digit law and both first two zero-digit correlations and isolates the **interior, sharp lag-two sign-reversal point**. Dajani, Kraaikamp, and Liardet [2] study the nonadjacent signed-binary system at the limiting parameter \(3/2\); they do not give a parameter-dependent interior sign change on this interval. No claim is made about a new invariant-density construction or about changing the known one-digit plateau.

## Limitations

The formulas are proved only on \(5/4\le\alpha\le3/2\), a subinterval of the full known one-digit plateau. They concern the invariant absolutely continuous state, not arbitrary singular invariant laws or every initial point. No long-lag mixing rate or asymptotic variance is computed. The full-density formula in [1] makes related observable calculations in principle accessible, and the possibility of an unindexed previous explicit two-lag computation remains a priority risk. Only self-review was performed; there is no independent audit.

## References

[1] K. Dajani and C. Kalle, *Invariant measures, matching and the frequency of 0 for signed binary expansions*, arXiv:1703.06335 (first public version March 18, 2017), https://arxiv.org/abs/1703.06335 . Sections 1, 2, 5 and Appendix; especially the invariant-density formula (3) and Theorem 5.2.

[2] K. Dajani, C. Kraaikamp, and P. Liardet, *Ergodic properties of signed binary expansions*, Discrete Contin. Dyn. Syst. 15 (2006), 87–119, https://doi.org/10.3934/dcds.2006.15.87 .
