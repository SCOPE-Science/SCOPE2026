# Optimal allocation of two sticky reactive walls: a finite-speed allocation law

## Finding

A finite-speed run-and-tumble particle can be absorbed while attached to either of two sticky walls. If the *sum* of the two wall-killing rates is fixed, the mean time to absorption has **exactly one minimizing allocation, with both rates strictly positive**, for every positive budget, every initial location including either wall, and all positive bulk-switching and wall-release rates. The favored wall is always the wall nearer the initial position. For an off-center start its share of the fixed budget grows strictly with the total budget.

Let the particle move at speed \(v>0\) on \([0,L]\), reverse its heading in the bulk at Poisson rate \(\alpha>0\), and, while outward-pointing and stuck at a wall, be released inward at rate \(\beta>0\) or permanently killed there at rate \(\kappa_0\) or \(\kappa_L\). The particle starts from \(x\in[0,L]\) with independent equiprobable headings. Set \(\kappa_0+\kappa_L=K>0\). Put
\[
 A=1+\frac{\alpha L}{v},\quad B=1+\frac{\beta L}{v},\quad
 h=\frac{\alpha(2x-L)}{2v},\quad
 \delta=\kappa_0-\kappa_L.
\]
Then the exact expected absorption time is
\[
 \boxed{
 \mathbb E_x T=\frac L{2v}+\frac{\alpha x(L-x)}{v^2}
 +B\frac{2\beta+AK/2+h\delta}{\beta K+A(K^2-\delta^2)/4}.}
\]
Define \(c=2\beta+AK/2\), \(d=\beta K+AK^2/4\), and \(b=Ac/2\). The unique optimal imbalance is
\[
 \boxed{\delta_*=-\frac{2hd}{b+\sqrt{b^2-Ah^2d}},\qquad
 \kappa_{0,*}=\frac{K+\delta_*}{2},\quad
 \kappa_{L,*}=\frac{K-\delta_*}{2}.}
\]
In particular, \(|\delta_*|<K\), and its sign is opposite to that of \(x-L/2\). The normalized imbalance \(t_*(K)=\delta_*/K\) is strictly increasing with \(K\) for \(x<L/2\), strictly decreasing for \(x>L/2\), and identically zero at the midpoint. Its **sharp two-limit law** is
\[
 \boxed{\lim_{K\downarrow0}t_*(K)=-\frac hA,\qquad
 \lim_{K\to\infty}t_*(K)=-\frac{2h}{A+\sqrt{A^2-4h^2}}.}
\]
The limiting fractions are independent of the common wall-release rate \(\beta\), although the crossover depends on \(K/\beta\). If the particle starts directly on the left wall, its *distant right wall* still receives an asymptotically positive share even when the budget diverges:
\[
 \boxed{\lim_{K\to\infty}\frac{\kappa_{L,*}}K
 =\frac{1+\sqrt{2A-1}}{2(A+\sqrt{2A-1})}>0.}
\]
The optimized mean also has the sharp strong-budget expansion
\[
 \boxed{\min_{\kappa_0+\kappa_L=K}\mathbb E_x T
 =\frac L{2v}+\frac{\alpha x(L-x)}{v^2}
 +\frac{B\big(A+\sqrt{A^2-4h^2}\big)}{AK}+o(K^{-1}).}
\]

## Assumptions and scope

All quantities \(v,L,\alpha,\beta,K\) are finite and strictly positive; the initial coordinate is any \(x\in[0,L]\). Interior heading reversals are Poisson with rate \(\alpha\) per heading. A particle hitting the left wall while heading left, or the right wall while heading right, enters the corresponding sticky state; its wall residence ends by an inward release at rate \(\beta\) or an absorption event at its assigned rate \(\kappa_j\). All exponential clocks are independent as specified by this continuous-time Markov model. At a wall start, the outward initial heading is interpreted as immediately entering the sticky state. The only constrained resource is the sum of the *physical wall-killing rates*, not the sum of per-collision capture probabilities. The open allocation segment has \(\kappa_0,\kappa_L>0\); both zero-endpoint allocations are allowed for comparison.

Because at least one wall has positive killing rate and wall release/bulk excursions recur on a compact interval, absorption occurs almost surely with a finite mean even for either zero-endpoint comparison allocation. No Brownian limit, reset protocol, directional launch bias, or nonexponential residence law is asserted.

## Proof

**1. Backward equations and boundary kinetics.** Let \(m_\pm(z)\) be the expected remaining absorption time from the interior position \(z\) and heading \(\pm\). The backward generator yields
\[
 vm_+'+\alpha(m_--m_+)=-1,\qquad
 -vm_-'+\alpha(m_+-m_-)=-1.
\]
When the outward state is attached to a wall, the competing exponential clocks give the exact boundary equations
\[
 (\beta+\kappa_0)m_-(0)=1+\beta m_+(0),\qquad
 (\beta+\kappa_L)m_+(L)=1+\beta m_-(L).
\]
Define \(M=(m_++m_-)/2\), \(d=m_+-m_-\). Subtraction and addition give \(d'=-2/v\) and \(M'=\alpha d/v\), so for a constant \(d_c\),
\[
 d(z)=d_c+\frac{L-2z}{v},\qquad
 M(z)=M(0)+\frac\alpha v\left(d_cz+\frac{Lz-z^2}{v}\right).
\]
The two wall conditions give
\[
 d_c=\frac{(1+\beta L/v)(\kappa_0-\kappa_L)}{
 (1+\alpha L/v)\kappa_0\kappa_L+\beta(\kappa_0+\kappa_L)}
 =\frac{B\delta}{A\kappa_0\kappa_L+\beta K}
\]
and, independently,
\[
 M(0)=\frac{1}{\kappa_0}+
 \left(\frac{\beta}{\kappa_0}+\frac12\right)
 \left(d_c+\frac Lv\right).
\]
Substitution and collection of terms, or taking the continuous limit when one killing rate vanishes, produces the exact mean formula stated above. The denominator is strictly positive on \(|\delta|\le K\), because it is \(\beta K+A\kappa_0\kappa_L\).

**2. Exactly one global optimum.** The allocation-dependent quotient is
\[
 F(\delta)=\frac{c+h\delta}{d-A\delta^2/4},
 \qquad -K\le\delta\le K.
\]
The numerator is positive throughout: \(c+h\delta\ge2\beta+K/2>0\), since \(2|h|\le A-1\). Therefore the sign of \(F'(\delta)\) is the sign of
\[
 G(\delta)=hd+\frac{Ac}{2}\delta+\frac{Ah}{4}\delta^2.
\]
Its derivative \(G'(\delta)=\frac A2(c+h\delta)\) is **strictly positive** across the entire admissible interval. Moreover
\[
 G(-K)\le -\frac{(A+1)\beta K}{2}-\frac{AK^2}{4}<0,
 \quad
 G(K)\ge \frac{(A+1)\beta K}{2}+\frac{AK^2}{4}>0.
\]
The inequalities use \(|h|\le(A-1)/2\). Thus exactly one critical point lies inside \((-K,K)\); the derivative changes from negative to positive there and it is the unique global minimizer. Solving \(G=0\) with the numerically stable quadratic root yields the stated formula, including \(h=0\), for which \(\delta_*=0\). Since \(G(0)=hd\), the optimizer's sign is opposite to \(h\).

**3. Budget monotonicity and sharp limits.** Put \(t=\delta/K\). Dividing the critical-point equation by \(K\) gives the strictly increasing-in-\(t\) equation
\[
 H(t,K)=\beta(h+At)+\frac{AK}{4}\{h(1+t^2)+At\}=0,
 \qquad -1<t<1.
\]
Indeed \(\partial_t H=A\beta+\frac{AK}{4}(A+2ht)>0\), because \(A>2|h|\) and \(|t|<1\). For \(h>0\), the unique root is strictly less than \(-h/A\) since \(H(-h/A,K)>0\). At that root, \(h+At<0\), and hence \(h(1+t^2)+At>0\) by the defining equation. Implicit differentiation therefore yields \(\partial_Kt=-H_K/H_t<0\). Reversing signs gives \(\partial_Kt>0\) for \(h<0\); for \(h=0\), the root is always zero. Taking \(K\downarrow0\) gives \(t=-h/A\). Taking \(K\to\infty\), compactness of the root and strict monotonicity of \(h(1+t^2)+At\) on \([-1,1]\) give its unique interior zero, \(-2h/(A+\sqrt{A^2-4h^2})\). Both are sharp pointwise limits for fixed physical parameters.

**4. Finite-speed boundary share and strong-budget correction.** At \(x=0\), \(h=-(A-1)/2\), giving \(\sqrt{A^2-4h^2}=\sqrt{2A-1}\) and the stated strictly positive distant-wall fraction. For an interior limiting fraction \(t\), the exact quotient has the uniform expansion
\[
 B F(Kt)=\frac{4B}{AK}\frac{A/2+ht}{1-t^2}+O(K^{-2})
\]
on any compact subinterval of \((-1,1)\). The coefficient is uniquely minimized when \(h(1+t^2)+At=0\), where its minimum equals \(B(A+\sqrt{A^2-4h^2})/A\). Since the optimizer stays in a compact interior interval, substitution proves the expansion. This concludes the theorem.

## Verification

Execute `python checker.py` under Python 3 using only its standard library. The checker compares the closed mean to a separately solved *two-equation backward boundary system* at 600 exact rational parameter sets, then at 300 numerical parameter sets. It independently minimizes the full mean by golden-section search at 300 seeded parameter sets, checks 120 budget-ordering cases, and 120 weak/strong limit cases. The recorded run passed all 1,440 assertions/cases. In the floating-point wall-residual check an absolute tolerance of \(10^{-6}\) is used to accommodate cancellation for extreme rate and length ratios; exact-rational comparisons avoid that issue. These tests check implementations and selected cases, not the entire parameter continuum, which is covered by the proof.

## Relationship to prior work

Bressloff (2023, arXiv:2302.01158) establishes the partially absorbing sticky-wall run-and-tumble process, its bulk and bound-state boundary equations, and distinct-wall absorption rates. Sections 2 and 5 develop first-passage quantities and the two-occupation-time formulation; those equations supply the established microscopic model, not the fixed-sum *reactivity-allocation optimization*. Angelani (2024) studies optimal escape by varying the bulk tumbling rate or wall desorption parameters, with a one-sided reactive channel, rather than dividing a fixed killing-rate budget between two sticky boundaries.

For comparison, a separately published result on *Brownian diffusion* with reactive Robin endpoints (published-finding corpus, October 2026) proves unique interior allocation and its own sharp budget laws. A distinct published result on a persistent particle with **instantaneous** probabilistic capture and immediate reversal at the endpoints (published-finding corpus, November 2026) finds a phase transition between concentrated and equal allocations of per-collision absorption probabilities. Neither setup is the present rate-controlled sticky-residence process. The new qualitative statement is that at a wall start the *strong-budget distant-wall fraction stays positive for every fixed finite run-speed and tumble rate*, unlike the vanishing distant fraction for a Brownian Robin model. The model-level differences prevent implication of this theorem from either published optimization result, although closely related constrained-optimization literature remains a priority risk.

## Limitations

The exact optimality statement assumes the known initial coordinate and an initially unbiased heading, equal positive release rates at both walls, exponential wall residence and bulk heading flips, and a linear sum budget in killing *rates*. It does not optimize a sum of individual per-collision probabilities, impose a nonlinear chemical cost, accommodate unequal release rates, or extend the finite-speed contrast to a uniform joint Brownian/large-budget limit. The mean is finite, but no moment beyond the mean and no stochastic ordering of full passage-time laws is claimed. The arithmetic checks are finite and no independent scientific validation is claimed.

## References

1. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1, first posted 2023-02-02, https://arxiv.org/abs/2302.01158.
2. L. Angelani, *Optimal escapes in active matter*, European Physical Journal E 47, article 9 (2024), https://doi.org/10.1140/epje/s10189-023-00402-7.
3. *Optimal allocation of two reactive Brownian boundaries: a unique interior split and sharp budget laws*, publicly indexed result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-optimal-allocation-of-two-reactive-brownian-boundaries-a-unique--562e72eb5093.
4. *Boundary-capture allocation transition and variance selection for a persistent particle*, publicly indexed result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-boundary-capture-allocation-transition-and-variance-selection-fo--61f92a1dbbba.
5. *Sharp fluctuation-optimal tumbling threshold for sticky reactive run-and-tumble walls*, publicly indexed result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fluctuation-optimal-tumbling-threshold-for-sticky-reactive--c5e90a3196ae.
