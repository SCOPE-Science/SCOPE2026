# A budget-independent polarity reversal in distributed-reset diffusion with two reactive boundaries

## Finding

For a Brownian searcher on an interval, Poisson-reset independently to a spatial law, consider optimally distributing a fixed total partial-absorption reactivity between its two endpoints. **The optimal allocation is unique for every positive reset rate and positive reaction budget. Its left-versus-right majority is determined by one hyperbolic odd moment of the reset-position distribution, independent of the size of the reaction budget.** For two reset positions on opposite sides of the midpoint, this moment has at most one positive zero, and a sharp necessary-and-sufficient criterion determines whether the optimizer switches polarity as the reset frequency varies.

In particular, if resets choose \(0.1L\) with probability \(1/4\) and \(0.7L\) with probability \(3/4\), the unique optimal allocation is right-heavy when
\[
0<rL^2/D<25\operatorname{arcosh}^2(3/2),
\]
is exactly balanced at equality, and is left-heavy above it, **for every total reaction budget \(Q>0\)**. The dimensionless crossing is \(25\operatorname{arcosh}^2(3/2)=23.156482057719\ldots\).

## Assumptions and scope

Let \(D,L,Q,r>0\). A Brownian particle has generator \(D\partial_{xx}\) in \([0,L]\), with partially absorbing/reflecting Robin endpoints of reactivities \(\kappa_0,\kappa_L\ge0\) satisfying \(\kappa_0+\kappa_L=Q\). At time zero, and independently at each event of a Poisson process of rate \(r\), its position is freshly drawn from a fixed **arbitrary Borel probability law** \(\mu\) on \([0,L]\). The surface reaction mechanism is memoryless under resets (equivalently, any random surface-local-time absorption threshold is exponential); absorption terminates motion. There are no other killing mechanisms, and the two endpoint Robin coefficients are not modified during a reset.

Set \(y=x/L\), \(k=L\sqrt{r/D}>0\), \(K=QL/D>0\), \(a=\kappa_0 L/D\in[0,K]\), and \(b=K-a\). In all integrals below, \(\mu\) denotes the induced law of the dimensionless reset location \(y\in[0,1]\). Define
\[
\begin{aligned}
 A&=\int\cosh(k(1-y))\,d\mu(y),& B&=\int\cosh(ky)\,d\mu(y),\\
 C&=\frac1k\int[\sinh(k(1-y))+\sinh(ky)]\,d\mu(y),&
 E&=\frac{\sinh k}{k},\\
 Q_0&=k\sinh k+K\cosh k,&\delta&=A-B,\\
 Z&=CQ_0-EKB.&&
\end{aligned}
\]

**Complete allocation theorem.** The discounted probability of surface capture before an independent exponential deadline of rate \(r\) is
\[
 f_\mu(k,a)=\frac{aA+(K-a)B+a(K-a)C}{Q_0+Ea(K-a)}.
\]
The mean absorption time under independent position resetting is exactly
\[
 M_r(a)=\frac{1-f_\mu(k,a)}{r f_\mu(k,a)}.
\]
The unique minimizer \(a_*\in[0,K]\) is characterized without optimization ambiguities as follows. Put
\[
 H(a)=\delta Q_0+(K-2a)Z+E\delta a^2.
\]
If \(H(0)\le0\), then \(a_*=0\); if \(H(K)\ge0\), then \(a_*=K\); otherwise \(a_*\) is the unique zero of \(H\) in \((0,K)\). The ties in these endpoint tests do not create additional optimizers. Most importantly,
\[
\boxed{\quad\operatorname{sgn}(a_*-K/2)=
\operatorname{sgn}\int_0^1\sinh\bigl(k(1/2-y)\bigr)\,d\mu(y).\quad}
\]
Thus the optimal side of the budget depends only on the reset law and the reset frequency, not on \(Q\), even if the allocation is an endpoint solution.

**Two-site crossing theorem.** Take \(\mu=w\delta_{1/2-u}+(1-w)\delta_{1/2+v}\), where \(0<u,v<1/2\) and \(0<w<1\). If \(u>v\), there is exactly one positive frequency \(k_c\) at which the unique optimizer is balanced if and only if \(w<v/(u+v)\); the optimum is right-heavy for \(0<k<k_c\) and left-heavy for \(k>k_c\). If \(u<v\), there is one crossing precisely when \(w>v/(u+v)\), with opposite order. If \(u=v\), the optimizer is on the side selected by \(\operatorname{sgn}(2w-1)\) for all positive rates, or is balanced for all rates when \(w=1/2\). When the strict crossing condition fails in either unequal-distance case, the optimizer has a single fixed polarity for all positive reset rates.

## Proof

**1. Discounted Robin capture.** Let \(T\) be the absorption time without resetting and \(f_r(x)=\mathbb E_x[e^{-rT}]\). Standard backward boundary conditions give \(Df_r''=rf_r\) on the interior, together with \(Df_r'(0)=\kappa_0(f_r(0)-1)\) and \(Df_r'(L)=\kappa_L(1-f_r(L))\). Solving this two-point linear problem with \(a,b,k,y\) as above gives, at every \(y\in[0,1]\),
\[
 f_r(y)=\frac{a\cosh(k(1-y))+b\cosh(ky)+\frac{ab}{k}[\sinh(k(1-y))+\sinh(ky)]}{k\sinh k+(a+b)\cosh k+\frac{ab}{k}\sinh k}.
\]
This formula remains valid if one endpoint is reflecting, since \(a+b=K>0\). Integrating in \(\mu\) gives the displayed formula for \(f_\mu\). Positivity of the numerator and denominator shows \(0<f_\mu<1\). A reset cycle ends in capture before its exponential alarm with probability \(f_\mu\); its expected length is \((1-f_\mu)/r\). The strong Markov renewal identity therefore yields \(M_r=(1-f_\mu)/(rf_\mu)\), so minimizing \(M_r\) is maximizing \(f_\mu\).

**2. Unique optimum, including endpoints.** Differentiating the rational expression shows
\[
 \frac{\partial f_\mu}{\partial a}=
 \frac{H(a)}{[Q_0+Ea(K-a)]^2}.
\]
Write \(s_0=\int\sinh(k(1-y))\,d\mu(y)\) and \(s_1=\int\sinh(ky)\,d\mu(y)\). Hyperbolic angle addition gives the two exact positive identities
\[
 Z=Ck\sinh k+\frac{K(\cosh k-1)}{k}s_0>0,\qquad
 Z-EK\delta=Ck\sinh k+\frac{K(\cosh k-1)}{k}s_1>0.
\]
Because \(C,k,\sinh k>0\), both inequalities are strict even for point masses at endpoints. Consequently \(H'(a)=-2Z+2E\delta a\) is strictly negative on \([0,K]\): if \(\delta\le0\), use \(Z>0\); if \(\delta>0\), use \(Z-EK\delta>0\). The sign of the derivative of \(f_\mu\) therefore changes at most once, strictly from positive to negative. This gives existence, **uniqueness**, and the endpoint/interior cases in the theorem.

At the middle allocation,
\[
 H(K/2)=\delta[Q_0+EK^2/4],
\qquad \delta=2\sinh(k/2)\int\sinh(k(1/2-y))\,d\mu(y).
\]
The bracket and \(\sinh(k/2)\) are positive. As \(H\) decreases strictly, the optimizer lies on the same side of \(K/2\) as the sign of the integral, proving budget-independent polarity including endpoint optima.

**3. Two reset positions and the sharp crossing.** The determining odd moment equals
\[
 J(k)=w\sinh(uk)-(1-w)\sinh(vk).
\]
For \(u>v\), the ratio \(R(k)=\sinh(uk)/\sinh(vk)\) increases strictly from \(u/v\) to infinity as \(k>0\) increases. Indeed,
\[
 (\log R)'=u\coth(uk)-v\coth(vk)>0,
\]
since \(t\mapsto t\coth t\) is strictly increasing for \(t>0\): its derivative has numerator \(\sinh t\cosh t-t>0\). Thus \(J(k)=0\) exactly once if and only if \((1-w)/w>u/v\), equivalently \(w<v/(u+v)\). The signs on either side and the mirrored \(u<v\) classification follow by the same comparison; equality produces no positive crossing. When \(u=v\), \(J(k)=(2w-1)\sinh(uk)\). This exhausts every parameter boundary.

For the explicit distribution at \(y=0.1\) and \(y=0.7\), take \(u=0.4\), \(v=0.2\), \(w=1/4\). The odd moment factorizes exactly as
\[
 J(k)=\frac14\sinh(k/5)[2\cosh(k/5)-3],
\]
so \(k_c=5\operatorname{arcosh}(3/2)\) and \(r_cL^2/D=k_c^2\), independently of \(K\). This establishes the claimed reversal.

## Verification

Run the accompanying standalone Python 3 standard-library script \(\texttt{CHECK.py}\) from the same directory. It checks 11,430 deterministic assertions: backward Robin boundary conditions at both endpoints; the explicit discounted transform against its differential equation; exact averaging over reset sites; the rational derivative identity against finite differences; finite-grid optimality for randomly selected legal parameters; the sign of the optimizing budget split; and the exact two-site crossing for four widely separated positive budgets. The script reports \(k_c=4.812118250596\) and \(r_cL^2/D=23.156482057719\). Analytical uniqueness and all-distribution quantifiers are proved above; random finite tests alone are not proofs of those statements.

## Relationship to prior work

Ghosh, Pal, Ghosh and Pal, arXiv:2609.02355v1 (public 2 September 2026), develop the exact forward Robin fluxes and first-passage observables for two reactive boundaries with intermittent position resetting, but do not give a fixed-total-reaction-budget allocation classification. Méndez, Flaquer-Galmés and Campos, arXiv:2401.01125 (public 2024), provide general random-location resetting renewal tools. Classical Robin backward equations and Poisson renewal are not new. A prior deterministic-position calculation for allocating two boundary reactivities **with competing bulk exponential killing** contains the point-source discounted optimization as a special algebraic component; that result does not by itself assert the arbitrary-law budget-independent polarity criterion or the unique change of optimal side as reset rate varies for a two-point law. A relevant separate result for two drift-biased point traps studies budget-dependent onset of positive investment in both traps, but not this distributed-source Robin-boundary polarity reversal. The contribution assessed here is specifically the arbitrary-law optimal-side identity and exact two-site frequency-crossing classification.

## Limitations

The conclusion assumes fresh independent reset positions at every alarm, exponential alarm times, memoryless Robin surface capture, fixed positive \(D,L,Q,r\), and a single shared budget for the two endpoints. It does not cover retained non-exponential surface-contact thresholds, drift, simultaneous optimization of source law or reset rate, robustness to estimated reset distributions, or finite-time conditional capture preferences. An algebraically equivalent theorem in general optimal-reaction allocation literature cannot be definitively excluded by the cited searches; independent scholarly review of novelty and proof remains outstanding.

## References

- S. Ghosh, S. Pal, D. Ghosh, P. S. Pal, *Effect of reactive targets on diffusive transport with intermittent restarts*, arXiv:2609.02355v1, first submitted 2026-09-02, https://arxiv.org/html/2609.02355v1 .
- V. Méndez, I. Flaquer-Galmés, D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, https://arxiv.org/abs/2401.01125 .
- P. C. Bressloff, *Diffusion-mediated surface reactions and stochastic resetting*, arXiv:2202.01119, https://arxiv.org/abs/2202.01119 .
- *Optimal allocation of two reactive Brownian boundaries: a unique interior split and sharp budget laws*, published-finding corpus published record 2026/10/26/562e72eb5093, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-optimal-allocation-of-two-reactive-brownian-boundaries-a-unique--562e72eb5093 .
- *A sharp reactivity-budget transition for two drift-biased resetting traps*, published-finding corpus published record 2026/11/8/7d56da6d7bd3, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-reactivity-budget-transition-for-two-drift-biased-resett--7d56da6d7bd3 .
