# A sharp boundary-allocation transition under competing bulk and surface killing

## Finding

A reflected Brownian particle in an interval is stopped either by independent homogeneous bulk killing or by reaction at two partially absorbing endpoints. Fixing the *sum* of endpoint reactivities, the surface-before-bulk capture probability has a **unique** maximizing allocation. For a particle launched nearer the left endpoint, all the available reactivity goes to the left endpoint below one explicit positive total-budget threshold; above the threshold, both endpoints receive strictly positive reactivities. This sharp switch contrasts with the strictly interior two-endpoint allocation minimizing the ordinary mean reaction time without a competing bulk clock.

Write \(z=x/L\in[0,1]\), \(k=L\sqrt{p/D}>0\), and \(K=(\kappa_0+\kappa_L)/\sqrt{Dp}>0\). Let \(a=\kappa_0/\sqrt{Dp}\in[0,K]\), \(b=K-a\), \(S=\sinh k\), and \(C=\cosh k\). The probability of surface capture before bulk killing is exactly
\[
 \Phi_{k,z,K}(a)=
 \frac{a\cosh(k(1-z))+b\cosh(kz)
 +ab[\sinh(k(1-z))+\sinh(kz)]}
 {S+KC+abS}.
\]
For \(0\le z<1/2\), put \(t=kz\), \(u=k(1-z)\), and
\[
 \delta=\cosh u-\cosh t>0,\quad
 B_1=\cosh(k+t)-\cosh t>0,\quad
 B_2=S\cosh t-\sinh t-\sinh u\ge0.
\]
The sharp dimensionless budget threshold is
\[
 K_c(k,z)=\frac{2\delta S}{B_1+\sqrt{B_1^2+4B_2\delta S}}>0.
\]
Then the **unique** maximizer is
\[
 \boxed{\begin{cases}
 a_*=K,&0<K\le K_c(k,z),\\
 K/2<a_*<K,&K>K_c(k,z).
 \end{cases}}
\]
In the second case, \(a_*\) is the unique zero on \((K/2,K)\) of the explicitly specified polynomial \(P(a)\) in the proof. At \(z=1/2\), \(a_*=K/2\) for every \(K>0\). For \(z>1/2\), reflect \(z\mapsto1-z\) and exchange the endpoints. At launch from the left wall, \(K_c(k,0)=\sinh k\), so the dimensional threshold simplifies to
\[
 \boxed{\kappa_c=\sqrt{Dp}\,\sinh(L\sqrt{p/D}).}
\]
This gives an exact, strictly positive and physically dimensioned critical surface-reaction budget at every positive bulk-death rate.

## Assumptions and scope

Let \(D,L,p,Q>0\). Consider one-dimensional reflected Brownian motion on \([0,L]\) with interior generator \(D\partial_{xx}\), started at deterministic \(x\in[0,L]\). At the left and right endpoints, independent exponential killing in accumulated boundary local time gives nonnegative Robin reactivities \(\kappa_0\) and \(\kappa_L\), constrained by \(\kappa_0+\kappa_L=Q\). A separate independent exponential clock of rate \(p\) causes irreversible bulk death. Let \(T_s\) be the surface-killing time and \(E_p\sim\operatorname{Exp}(p)\) the independent bulk lifetime. The objective is \(\Pr_x(T_s<E_p)=\mathbb E_x e^{-pT_s}\), not the eventual surface-capture probability without bulk death (which is one), nor a mean first-passage time.

The boundary-local-time normalization is fixed by the unique backward boundary-value problem for \(\Phi(x)=\Pr_x(T_s<E_p)\):
\[
 D\Phi''=p\Phi\quad(0<x<L),\qquad
 D\Phi'(0)=\kappa_0(\Phi(0)-1),\quad
 D\Phi'(L)=\kappa_L(1-\Phi(L)).
\]
Endpoint allocations equal to zero are admitted as design choices, not as a claim that both endpoints must remain reactive. Since \(Q>0\), the surface reaction time is finite almost surely, while the competing bulk lifetime has strictly positive hazard. MSC2020 primary classification: 82C31.

## Proof

**Exact transform.** In the coordinate \(z=x/L\), the interior equation is \(\Phi_{zz}=k^2\Phi\), with \(\Phi_z(0)=ka(\Phi(0)-1)\) and \(\Phi_z(1)=kb(1-\Phi(1))\). Write \(\Phi(z)=A\cosh(kz)+B\sinh(kz)\). The first boundary relation gives \(B=a(A-1)\). The second gives
\[
 A=\frac{aC+b+abS}{S+(a+b)C+abS}.
\]
Substitution and the addition identities for hyperbolic functions produce the displayed formula for \(\Phi_{k,z,K}(a)\), whose denominator is positive on the entire closed allocation interval.

**Optimality derivative.** For \(z<1/2\), abbreviate \(H=\sinh u+\sinh t\), \(d_0=S+KC\), \(\delta=\cosh u-\cosh t\), and
\[
 Z=H d_0-SK\cosh t=SH+K(C-1)\sinh u>0.
\]
Direct differentiation yields
\[
 \frac{\partial\Phi}{\partial a}=\frac{P(a)}{[d_0+S a(K-a)]^2},
 \qquad P(a)=\delta S a^2-2Za+KZ+\delta d_0.
\]
Here \(P(0)=KZ+\delta d_0>0\), and \(P(K/2)=\delta[d_0+S K^2/4]>0\), so the optimum cannot be at the right-only allocation or below a balanced allocation. Moreover
\[
 Z-\delta SK=SH+KB_2>0,
\]
where \(B_2=(C-1)\sinh u-\delta S=S\cosh t-\sinh t-\sinh u\). To verify \(B_2\ge0\), note that as a function of \(t\in[0,k/2]\), it vanishes at zero and its derivative is \(S\sinh t+\cosh(k-t)-\cosh t\ge0\). Thus \(P'(a)=2\delta Sa-2Z<0\) for all \(0\le a\le K\): the derivative of the objective changes sign at most once, from positive to negative, and a unique global maximizer exists.

**Threshold and classifications.** Hyperbolic addition formulas simplify the boundary derivative numerator to
\[
 P(K)=\delta S-B_1K-B_2K^2,
 \quad B_1=\cosh(k+t)-\cosh t>0.
\]
Because \(\delta S>0\), \(B_1>0\), and \(B_2\ge0\), this expression is strictly decreasing in \(K\ge0\) from positive to negative and has exactly one positive zero \(K_c\), given above. If \(K\le K_c\), then \(P(a)>0\) for \(a<K\), so the unique maximum is \(a_*=K\). If \(K>K_c\), then \(P(K)<0<P(K/2)\), and the strictly decreasing \(P\) has exactly one root \(a_*\in(K/2,K)\); the objective increases then decreases. At \(z=1/2\), \(\delta=0\) and \(P(a)=Z(K-2a)\), proving the balanced unique optimum. Reflection handles \(z>1/2\). At \(z=0\), \(B_2=0\), \(\delta=B_1=C-1\), giving \(K_c=S\). The preceding inequalities include all equality and boundary cases and establish the claimed quantifiers for arbitrary positive \(D,L,p,Q\).

## Verification

The included `checker.py` is self-contained Python (standard library only). Running `python3 checker.py` independently solves the Robin differential boundary problem by a second-order finite-difference/ghost-point Thomas tridiagonal solver for 100 seeded parameters and compares against the closed-form transform, with maximum observed error \(4.1\times10^{-7}\). A separate golden-section maximization checks 100 optimized capture probabilities against the derivative-based formula (maximum observed discrepancy below \(3.4\times10^{-16}\)). It also checks 30 cases straddling the exact allocation threshold, 3030 independent sampled allocations, and the boundary-launch identity at three distinct bulk rates. These are numerical checks of the analytic proof, not substitutes for its global inequalities.

For example, \(D=L=p=1\) with \(x=0\) has \(Q_c=\sinh(1)=1.1752011936\ldots\). At \(Q=0.5\), all of the reactivity goes to the launch endpoint and \(\Phi_*=0.3963239665\ldots\). At \(Q=3\), the optimal left dimensionless share is \(a_*=2.6668653573\ldots\) and \(\Phi_*=0.8019835132\ldots\), strictly exceeding \(0.7975342037\ldots\) for all-left allocation.

## Relationship to prior work

Ye (arXiv:2609.05247, first public 2026-09-04) develops the bulk-versus-surface competition, the splitting probability and general Robin spectral framework, with explicit examples for a three-dimensional ball. These general probabilistic and Robin facts are **prior work**. The allocation problem and the sharp two-endpoint budget threshold are the present contribution. The publicly accessible abstract specifies neither an allocation objective nor this threshold; complete full text could not be inspected, which is recorded as a priority risk rather than treated as negative evidence.

The public result *Optimal allocation of two reactive Brownian boundaries: a unique interior split and sharp budget laws* (2026-10-26) proves a unique **interior** allocation minimizing the *un-discounted mean* surface reaction time, with no competing bulk death. It treats precisely the same geometry, Robin budget and deterministic starts, so it is the closest implication comparison. Its theorem does not imply the asserted all-on-one-side phase: the mean-time optimum never occupies a budget endpoint, whereas the present capture-before-bulk optimum does so for a nonempty open budget region. The different objective introduces the modified Helmholtz parameter \(k>0\) and a new positive threshold. The mean-time formula is not claimed new.

The public result *A sharp reactivity-budget transition for two drift-biased resetting traps* (2026-11-08) obtains a superficially similar allocation switch for two **interior point sinks on an infinite line with nonzero drift and positional resetting**, optimizing mean eventual capture time. Its zero-drift case is balanced at all budgets, whereas the present zero-drift, off-center, confined Brownian system exhibits a finite corner-to-interior threshold. No parameter restriction or reduction of that theorem yields the present boundary-value problem or stated \(K_c(k,z)\).

Nicolaou and Mulder (Scientific Reports 13 (2023), DOI 10.1038/s41598-023-49566-4) optimize steady incoming flux to an exterior partly reactive body with an external source/at-infinity concentration. Their problem formulation does not prescribe an independent bulk killing clock in a bounded interval with a deterministic initial point; it does not provide the above exact conditional capture threshold in the inspected material. These distinctions are mathematical, not merely different titles.

## Limitations

The theorem is specific to constant diffusivity, one spatial dimension, exponential bulk lifetime, Robin boundary killing and a budget in the *sum of the two dimensioned reactivities*. The probability of eventual surface reaction in the absence of bulk death is always one and is not being optimized. This result does not optimize mean reaction times, optimize physical costs of implementing reactivity, or establish multi-boundary, higher-dimensional, or non-Markovian analogues. The most relevant 2026 primary source was available in abstract but not complete full text; specialized unindexed allocation literature may contain an equivalent stronger statement. Independent expert priority verification remains necessary.

## References

1. Y. Ye, *Diffusion under competing bulk and surface stopping mechanisms*, arXiv:2609.05247, first publicly submitted 2026-09-04, https://arxiv.org/abs/2609.05247.
2. *Optimal allocation of two reactive Brownian boundaries: a unique interior split and sharp budget laws*, public mathematical research record (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-optimal-allocation-of-two-reactive-brownian-boundaries-a-unique--562e72eb5093.
3. *A sharp reactivity-budget transition for two drift-biased resetting traps*, public mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-reactivity-budget-transition-for-two-drift-biased-resett--7d56da6d7bd3.
4. K. Nicolaou and B. M. Mulder, *A probabilistic algorithm for optimising the steady-state diffusional flux into a partially absorbing body*, Scientific Reports 13 (2023), DOI 10.1038/s41598-023-49566-4.
