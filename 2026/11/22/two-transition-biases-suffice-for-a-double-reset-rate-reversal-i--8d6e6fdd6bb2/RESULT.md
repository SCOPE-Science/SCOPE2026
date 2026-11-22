# Two transition biases suffice for a double reset-rate reversal in gambler's ruin

## Finding

A nearest-neighbor absorbing walk can have *two different strict interior extrema* of its eventual lower-boundary absorption probability as a geometric resetting rate varies, even when **every interior right-jump probability takes one of just two complementary values**. This occurs robustly for a one-parameter interval of such walks. In the class of finite nearest-neighbor gambler's-ruin chains with a single fixed reset site, two is the least possible number of distinct right-jump probabilities for this behavior: the one-valued, spatially homogeneous case has a monotone geometric-reset response [1].

More precisely, consider states \(\{0,1,\ldots,12\}\), with absorbing endpoints, initial and reset state \(z=5\), and right-jump probabilities, indexed by the transient states \(1,\ldots,11\),
\[
(p_1,\ldots,p_{11})=(1-\varepsilon,\varepsilon,1-\varepsilon,\varepsilon,1-\varepsilon,\varepsilon,1-\varepsilon,1-\varepsilon,\varepsilon,\varepsilon,\varepsilon).
\]
For **every** \(0<\varepsilon\le 3/50\), the eventual probability \(Q_\varepsilon(s)\) of absorption at zero with geometric step-survival parameter \(0<s<1\) has at least two distinct strict interior extrema. Here a step-survival parameter \(s\) means a nonabsorbed walk is reset to state \(5\) with probability \(1-s\), and otherwise takes its next ordinary step. At \(\varepsilon=1/20\), it has *exactly two*: a strict local minimum with squared survival parameter in \((13/20,33/50)\), followed by a strict local maximum with squared survival parameter in \((87/100,22/25)\). Their order is reversed if one lists extrema against increasing reset probability \(1-s\), but their types and count are unchanged.

This is an alphabet-size boundary, not a minimum-state-size theorem; examples with two extrema and more transition probabilities already exist.

## Assumptions and scope

All ordinary steps from an interior site \(i\) go to \(i+1\) with probability \(p_i\) and to \(i-1\) with probability \(q_i=1-p_i\). The endpoints are absorbing. Every interior probability lies strictly between zero and one. All geometric reset decisions are independent, and all resets return to the same deterministic site \(5\); reset decisions occur before ordinary steps. The process terminates upon first ordinary absorption. Both absorbing boundaries are reached almost surely, after potentially many cycles, because each independent cycle has positive probability of absorbing.

Write \(s=1-r\), where \(r\in(0,1)\) is the reset probability, and \(x=s^2\). An interior extremum means a strict local extremum of the ultimate absorption probability as a function of \(s\), equivalently of \(r\), not a reversal of the exact-time exit probabilities. The claim does not concern Poisson resetting, multiple reset destinations, continuous-time birth–death rates, or the smallest number of states needed for two extrema.

## Proof

**1. Renewal reduction.** Let \(T\) denote absorption time for the original walk without resetting and \(J\in\{0,12\}\) its absorbing boundary. The probabilities of completing a single uninterrupted cycle at the two boundaries are
\[
U(s)=\mathbb E_5[s^T\mathbf 1_{\{J=0\}}],\qquad V(s)=\mathbb E_5[s^T\mathbf 1_{\{J=12\}}].
\]
Every unsuccessful cycle ends at the reset site and begins afresh, so renewal gives
\[
Q_\varepsilon(s)=\frac{U(s)}{U(s)+V(s)}.
\]
The formula also extends continuously to \(s=1\).

**2. Exact cofactor identity.** Let \(P\) be the \(11\)-by-\(11\) killed transition matrix on sites \(1,\ldots,11\), and let \(D(s)=\det(I-sP)\). For an interval of transient states \([l,h]\), define its parity continuant by \(D_{l,h}(x)=\det(I-sP_{[l,h]})\). With \(D_{l,l-2}=D_{l,l-1}=1\), it obeys
\[
D_{l,j}(x)=D_{l,j-1}(x)-x p_{j-1}q_j D_{l,j-2}(x)\quad (j>l),\qquad D_{l,l}(x)=1.
\]
Tridiagonal inverse cofactors then give
\[
U(s)=\frac{s^5(q_1q_2q_3q_4q_5)D_{6,11}(s^2)}{D(s)},\quad
V(s)=\frac{s^7(p_5p_6\cdots p_{11})D_{1,4}(s^2)}{D(s)}.
\]
For the specified two-valued environment, direct application of the displayed recurrence gives
\[
\begin{aligned}
H_\varepsilon(x)&:=D_{1,4}(x)=1-[2(1-\varepsilon)^2+\varepsilon^2]x+(1-\varepsilon)^4x^2,\\
T_\varepsilon(x)&:=D_{6,11}(x)=1-(1+\varepsilon-\varepsilon^2)x+\varepsilon(1-\varepsilon)(1+\varepsilon)x^2-\varepsilon^3(1-\varepsilon)^3x^3.
\end{aligned}
\]
Since the ratio of the two directed path-weight products is \(\varepsilon(1-\varepsilon)\), the exact answer is
\[
\boxed{\displaystyle Q_\varepsilon(s)=\frac{T_\varepsilon(s^2)}{T_\varepsilon(s^2)+\varepsilon(1-\varepsilon)s^2 H_\varepsilon(s^2)}.}
\]
Every restricted killed transition matrix is similar to a symmetric matrix, is substochastic with spectral radius strictly below one, and has real eigenvalues of modulus less than one. Thus all its continuant determinants, including \(H_\varepsilon(x)\) and \(T_\varepsilon(x)\), are strictly positive for \(0\le x\le1\). The rational formula has no pole or sign ambiguity on the interval of interest.

**3. Derivative and uniform sign certificate.** Differentiation gives
\[
Q_\varepsilon'(s)=\frac{-2s\varepsilon(1-\varepsilon)F_\varepsilon(s^2)}{[T_\varepsilon(s^2)+\varepsilon(1-\varepsilon)s^2H_\varepsilon(s^2)]^2},
\]
where
\[
F_\varepsilon(x)=[H_\varepsilon(x)+xH_\varepsilon'(x)]T_\varepsilon(x)-xH_\varepsilon(x)T_\varepsilon'(x).
\]
In particular \(F_\varepsilon(0)=1\), and exact polynomial expansion yields
\[
F_\varepsilon(1)=\varepsilon^2(\varepsilon-1)(3\varepsilon^2-5\varepsilon+3)[\varepsilon(1-\varepsilon)^2-1]>0
\]
for \(0<\varepsilon\le3/50\), since the last factor is negative and the quadratic is positive. At the rational intermediate point,
\[
256F_\varepsilon(3/4)=243\varepsilon^8-1134\varepsilon^7+2187\varepsilon^6-2538\varepsilon^5+2106\varepsilon^4-1413\varepsilon^3+468\varepsilon^2+105\varepsilon-8.
\]
Dropping only the negative seventh- and fifth-degree terms shows that the right side is bounded above by \(g(\varepsilon)-8\), where
\[
g(t)=105t+t^2(468-1413t)+2106t^4+2187t^6+243t^8.
\]
All summands of \(g\) are increasing on \([0,3/50]\): for the only non-obvious one, the derivative of \(t^2(468-1413t)\) is \(t(936-4239t)>0\) there. Finally,
\[
g(3/50)=\frac{301054212401823}{39062500000000}<8.
\]
Hence \(F_\varepsilon(3/4)<0\) throughout the entire asserted interval. The exact sign pattern
\[
F_\varepsilon(0)>0,\qquad F_\varepsilon(3/4)<0,\qquad F_\varepsilon(1)>0
\]
and continuity imply at least one sign-changing zero in each of \((0,3/4)\) and \((3/4,1)\). Since the derivative is an analytic rational function with a strictly positive denominator, these imply two distinct strict local extrema of \(Q_\varepsilon\). This establishes the robust family, rather than just a numerical witness at one bias.

**4. Exact count at the rational parameter.** At \(\varepsilon=1/20\), the derivative numerator is
\[
F_{1/20}(x)=\frac{P(x)}{25600000000},\qquad
P(x)=1035002523x^4-43678112000x^3+109747200000x^2-92544000000x+25600000000.
\]
The ordinary exact-rational Sturm chain \(P,P',-\operatorname{rem}(P,P'),\ldots\) has signs \((+,-,+,-,+)\) at \(x=0\) (four variations) and \((+,+,-,+,+)\) at \(x=1\) (two variations). Since neither endpoint is a root, Sturm's theorem gives **exactly two** distinct roots in \((0,1)\). Exact rational evaluation additionally locates them by
\[
P(13/20)>0>P(33/50),\qquad P(87/100)<0<P(22/25).
\]
Both roots are simple and the signs are \(+,-,+\), so the smaller root gives the strict minimum and the larger gives the strict maximum as \(s\) increases.

**5. Alphabet minimality.** If all sitewise right-jump probabilities coincide, the walk is spatially homogeneous. For even intervals the global monotone reset response is established in [1, Theorem 6.1]; for odd intervals it is established in [1, Theorem 5.3(a)] (the reversed starting-location cases follow by reflection). In particular no one-valued environment can have two strict interior reset-rate extrema. The present examples use exactly two distinct right-jump values \(\varepsilon\ne1-\varepsilon\); therefore the minimum alphabet size *for existence of two or more strict interior extrema in this model* is exactly two. This conclusion does not assert minimality of the thirteen-state example in state count.

## Verification

The accompanying standalone `CHECK.py` uses Python's exact `fractions.Fraction` arithmetic and no third-party dependencies. Running `python3 CHECK.py` checks both displayed continuants, the complete rational quartic, the exact Sturm variations, two rational root brackets, the all-parameter upper-bound endpoint, and the resolvent formula against seven independently solved rational tridiagonal systems. Successful replay gives `PASS`. These computations verify the finite algebraic certificates; the continuum of bias parameters and the number of extrema follow from the analytical monotonicity and Sturm arguments above, not sampling. A separate unrestricted numerical search is neither assumed nor needed.

## Relationship to prior work

The motivating source [1], first publicly available November 1, 2026, proves monotone geometric-reset responses for homogeneous gambler's ruin and discusses general inhomogeneous birth–death chains. Its Section 10.3 poses classification of reset-rate extrema at multiply switching sites as an open question. Its Proposition 7.6 and Corollary 7.9 exhibit *temporal* reversals of exact-time exit odds with many distinct site probabilities; they do not establish the two-bias reset-rate result here. Earlier examples of one, two, or three reset-rate extrema with general heterogeneous coefficients are acknowledged; existence of multiple extrema in unrestricted environments is **not** claimed new.

[2] studies spectral and reset-neutral probabilities with a spatially homogeneous nearest-neighbor walk; its multi-site reset distribution is a different control from the fixed single-site, two-valued heterogeneous dynamics here. [3] treats spectral invariants for the homogeneous gambler's-ruin model and does not imply the two-bias example. The novelty asserted is the sharp transition-alphabet boundary, the open parameter interval of double turning, and the exact small quartic certificate, not an unrestricted extremum-count classification.

## Limitations

The parameter interval \(0<\varepsilon\le3/50\) is sufficient, not claimed maximal. For a general parameter in that interval, the argument proves *at least* two strict extrema, not an exact count. Exact count two is certified only for \(\varepsilon=1/20\). This model has thirteen total states and is not a smallest-state example. There is no claim of general algorithmic optimality, of independence from any prior unpublished result, or of independent mathematical audit. Historical-priority uncertainty remains possible in unlocated literature on rational reset responses and tridiagonal resolvents.

## References

[1] Tony Newton and Juan Antonio Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1, first posted 2026-11-01, https://arxiv.org/html/2611.01756v1 (especially Theorems 5.3 and 6.1, Proposition 7.6, and Section 10.3).

[2] *Spectral Duality and Reset-Neutral Distributions in Random Walks with Multi-Site Geometric Resetting*, arXiv:2605.00657v1, https://arxiv.org/html/2605.00657v1.

[3] Juan Antonio Vega Coso, *Critical Spectral Invariants in Random Walks with Geometric Resetting*, arXiv:2603.24803v1, first posted 2026-03-25, https://arxiv.org/html/2603.24803v1.
