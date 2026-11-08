# Two phase transitions and exact physical basins in a piecewise-linear Gharaei–Homburg core

## Finding
For the canonical deterministic core of the three-branch piecewise-linear Gharaei–Homburg family in Nakamura–Nakano–Toyokawa–Yano [1, §1.2.3, (1.7)], the entire parameter interval \(1/2\leq\delta\leq2/3\) admits an explicit return-map conjugacy, an exact simplex of invariant probabilities, an exact pointwise empirical-measure limit, and a closed-form physical-basin law.

Put \(I=[1/4,1/2)\), \(J=[1/2,3/4)\), and \(Y=I\cup J\). Let \(h_\delta:Y\to Y\) be the deterministic core defined below. For \(1/2\leq\delta<2/3\), set
\[
a_\delta=\delta/2,\qquad b_\delta=1-\delta,\qquad w_\delta=b_\delta-a_\delta=1-3\delta/2,
\qquad S_\delta=[1/4,a_\delta]\cup[b_\delta,1/2).
\]
The full list of invariant Borel probabilities for \(h_\delta\) is
\[
\left\{\frac12(\eta+h_{\delta *}\eta):\ \eta\text{ is any Borel probability on }S_\delta\right\}.
\]
Its ergodic invariant probabilities are exactly \(\mu_u=(\delta_u+\delta_{h_\delta(u)})/2\), \(u\in S_\delta\); here \(\delta_u\) is the Dirac mass at \(u\), not the family parameter. At \(\delta=2/3\) the same statements hold with \(S_{2/3}=I\). Thus the invariant probability is unique at \(\delta=1/2\), whereas for each \(\delta\in(1/2,2/3]\) there are uncountably many ergodic invariant probabilities.

Relative to normalized Lebesgue measure \(m_Y=2\,\mathcal L^1|_Y\), for every \(\delta\in[1/2,2/3)\) exactly one of those measures is physical, namely
\[
\mu_{a_\delta}=\tfrac12\bigl(\delta_{\delta/2}+\delta_{\delta}\bigr).
\]
Its basin has exact normalized length
\[
\boxed{m_Y\bigl(\operatorname{Bas}(\mu_{a_\delta})\bigr)=4-6\delta.}
\]
At \(\delta=2/3\) **there is no physical invariant probability** relative to \(m_Y\). Every point of \(Y\) nevertheless has a convergent empirical measure for each parameter, given explicitly below.

Finally, conditional on \(x\) being uniformly distributed in the attracting gap \((a_\delta,b_\delta)\), the number \(K\) of initial expanding steps for the two-iterate return satisfies
\[
\Pr(K=0)=\frac23,\quad \Pr(K=k)=\frac{1}{3\cdot 2^k}\ (k\geq1),\quad
\Pr(K\geq k)=\frac{1}{3\cdot2^{k-1}}\ (k\geq1),\quad \mathbb EK=\frac23.
\]
This transient law is independent of \(\delta\), even though the physical basin shrinks linearly to zero.

## Assumptions and scope
For \(1/2\leq\delta\leq2/3\), define increasing continuous maps on \([0,1]\) by
\[
f_0(x)=\begin{cases}x/2&0\leq x<2/3,\\2x-1&2/3\leq x\leq1,\end{cases}
\qquad
f_{1,\delta}(x)=\begin{cases}
2x&0\leq x<\delta/2,\\
x+\delta/2&\delta/2\leq x<1-\delta,\\
(x+1)/2&1-\delta\leq x\leq1.
\end{cases}
\]
At \(\delta=2/3\) the middle branch of \(f_{1,\delta}\) is empty. With \(Y=[1/4,3/4)\), define \(h_\delta(x)=f_{1,\delta}(x)\) when \(x\in I=[1/4,1/2)\), and \(h_\delta(x)=f_0(x)\) when \(x\in J=[1/2,3/4)\). This is the deterministic core arising at \(c=1/2\) in [1]; \(h_\delta(I)=J\) and \(h_\delta(J)=I\). All statements concern \(h_\delta\), **not** the stationary probabilities or physical measures of the original random iterations of \(f_0,f_{1,\delta}\) on \([0,1]\).

An invariant probability \(\mu\) is *physical relative to \(m_Y\)* if the set of \(y\in Y\) for which \(N^{-1}\sum_{j=0}^{N-1}\delta_{h_\delta^j(y)}\) converges weakly to \(\mu\) has positive \(m_Y\)-measure. One-point endpoint conventions are as displayed above and do not affect the basin-length statement.

## Proof
**1. Exact two-step return.** Since \(h_\delta\) exchanges the two half-intervals, on \(I\) its square is \(P_\delta=f_0\circ f_{1,\delta}\). Write \(a=\delta/2\), \(b=1-\delta\), \(t=2/3-a\). For \(1/2\leq\delta<2/3\), the strict order is \(1/4\leq a<t<b\leq1/2\), with the endpoint equalities interpreted at \(\delta=1/2\) as needed. Direct substitution yields the exact continuous four-branch formula
\[
P_\delta(x)=\begin{cases}
x,&1/4\leq x<a,\\
(x+a)/2,&a\leq x<t,\\
2x-b,&t\leq x<b,\\
x,&b\leq x<1/2.
\end{cases}
\tag{1}
\]
Both transition values match. For \(\delta=2/3\), inspection of the nonempty branches gives \(P_{2/3}=\operatorname{id}_I\).

**2. Universal gap conjugacy and eventual limits.** If \(\delta<2/3\), then \(w=b-a>0\), \(t=a+2w/3\), and \(z=(x-a)/w\) conjugates (1) on \([a,b)\) to
\[
Q(z)=\begin{cases}z/2,&0\leq z<2/3,\\2z-1,&2/3\leq z<1.\end{cases}
\tag{2}
\]
Every \(z\in(0,1)\) satisfies \(0\leq Q(z)<z\). A decreasing orbit can only converge to a fixed point of continuous \(Q\) on the branch where it eventually lies; its limit is below its starting point and is not \(1\). Since the only fixed point in \([0,1)\) is \(0\), \(Q^n(z)\to0\). In fact the orbit must enter \([0,2/3)\) after finitely many iterations (otherwise its limit would be a fixed point of \(2z-1\), hence \(1\)), and thereafter halves forever. All points in \(S_\delta\) are fixed by (1). Define
\[
r_\delta(x)=\begin{cases}a,&a<x<b,\\x,&x\in S_\delta.\end{cases}
\tag{3}
\]
Then \(P_\delta^n(x)\to r_\delta(x)\) for every \(x\in I\). At \(\delta=2/3\), take \(r_\delta=\operatorname{id}_I\).

**3. Exact invariant simplex.** Any \(h_\delta\)-invariant probability \(\mu\) places mass \(1/2\) on each of \(I\) and \(J\) because \(h_\delta\) exchanges them. The probability \(\eta=2\mu|_I\) is invariant under \(P_\delta\); conversely any \(P_\delta\)-invariant \(\eta\) produces \(\mu=(\eta+h_{\delta*}\eta)/2\). Since \(P_\delta^n\to r_\delta\), bounded convergence applied to continuous test functions on the compact closure of \(I\) shows \(\eta=r_{\delta*}\eta\), so \(\eta\) is supported on \(S_\delta\), on which \(P_\delta\) is the identity. Conversely every probability on \(S_\delta\) is \(P_\delta\)-invariant. Ergodic measures for an identity map are exactly point masses; exchanging two halves gives precisely the two-cycle measures \(\mu_u\).

**4. All individual empirical limits and physical basins.** If \(x\in I\), the even iterates \(h_\delta^{2n}(x)=P_\delta^n(x)\to r_\delta(x)\). By continuity of \(h_\delta\) on \(I\), the odd iterates converge to \(h_\delta(r_\delta(x))\), so its empirical measure converges to \(\mu_{r_\delta(x)}\). If \(y\in J\), its empirical measure converges to \(\mu_{r_\delta(h_\delta(y))}\), by shifting one iterate. For \(\delta<2/3\), the preimage of \(a\) under the limit projection (3) is \([a,b)\); the only positive-length portion is the gap \((a,b)\). Thus the full \(m_Y\)-positive basin is, modulo a finite set, \((a,b)\cup(h_\delta|_J)^{-1}((a,b))\). All other two-cycles have finite basins and cannot be physical. At \(\delta=2/3\), \(P\) is the identity, and each basin is exactly a two-point orbit, hence no physical measures exist. At \(\delta=1/2\), the gap fills \(I\) up to endpoints, so the unique invariant probability is physical with full measure.

For \(\delta\in[1/2,2/3)\), the first gap has length \(w\). Splitting \(J\) at \(2/3\), the inverse image under \(f_0\) of \((a,b)\) has length
\[
2(1/3-a)+(b-1/3)/2=1-3\delta/2=w.
\]
Since \(|Y|=1/2\), its normalized total basin length is \(2(w+w)=4-6\delta\), as claimed.

**5. Exact expanding-prefix law.** For uniform \(x\in(a,b)\), \(z=(x-a)/w\) is uniform in \((0,1)\). Let \(K\) be the number of initial iterates for which the expanding branch \(z\mapsto2z-1\) of (2) is taken, stopping at first entry into \([0,2/3)\). Requiring at least \(k\geq1\) expanding steps is exactly \(z\geq1-1/(3\cdot2^{k-1})\). Its Lebesgue probability is \(1/(3\cdot2^{k-1})\). Subtracting successive tails yields \(\Pr(K=k)=1/(3\cdot2^k)\) for \(k\geq1\) and \(\Pr(K=0)=2/3\). Summing the tails gives \(\mathbb EK=2/3\). This calculation is exact for every \(w>0\).

## Verification
Run \(`python3 verification.py`\) with a standard Python 3 interpreter. The script uses \(`fractions.Fraction`\) only, verifies the piecewise return and endpoint formulas for six rational parameters, checks rational sample iterates and fixed-point projection, and verifies basin-length and geometric-prefix tail identities. Its observed output is \(`PASS exact-rational branch, limit, basin-length and tail threshold checks: 9365`\). The verification is finite; statements for all real parameters, all points and all invariant probabilities follow from the analytic proof above, not from sample enumeration.

## Relationship to prior work
The family \(f_0,f_{1,\delta}\), the core construction, the equal-probability random intermittency framework, and the fact that at \(\delta=1/2\) the core has one attracting two-cycle and a unique invariant probability are from Nakamura–Nakano–Toyokawa–Yano [1, §1.2.3, (1.7), pp. defining the example]. The generalized Hata–Yano case in [1, §1.2.2] is a different family with a different parameter range. Gharaei–Homburg [2] studies the broader random-interval framework, not this specific deterministic-core phase diagram. The new assertions here concern all \(\delta\in[1/2,2/3]\), the exact return conjugacy, the invariant-probability simplex, the disappearance of the physical measure at the upper endpoint, the exact basin-length law, and the uniform gap transient distribution. These do not follow from the published \(\delta=1/2\) uniqueness result alone; they are obtained by the direct all-parameter calculation (1)–(3).

## Limitations
This finding does not classify stationary or physical probabilities for the **original random process** on \([0,1]\), does not assert new arcsine laws, and does not address \(0<\delta<1/2\). The core map is piecewise defined on a half-open state space; all endpoint values and negligible exceptional sets are accounted for. Exact formulas arise from an elementary affine computation, and equivalent prior consequences elsewhere in the interval-dynamics literature may exist despite the focused source comparisons. No independent audit of the mathematical argument has been performed.

## References
[1] F. Nakamura, Y. Nakano, H. Toyokawa, K. Yano, *Arcsine law for random dynamics with a core*, arXiv:2206.00226, first submitted 2022-06-01, especially §1.2.3, equation (1.7), and §1.2.1. https://arxiv.org/abs/2206.00226

[2] M. Gharaei and A. J. Homburg, *Random interval diffeomorphisms*, arXiv:1611.07248, 2016. https://arxiv.org/abs/1611.07248

[3] G. Hata and K. Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, arXiv:2108.01332, 2021. https://arxiv.org/abs/2108.01332
