# Sharp three-time self-return onset for integer circle expanders

## Finding

For an expanding integer circle map, the first three equally spaced self-return events have a sharp common-resonance threshold. Fix integers \(b\ge 2\) and \(t\ge 1\), put \(a=b^t\) and \(N=a^2+a+1\), and initialize \(X\) with normalized Haar measure on \(\mathbb R/\mathbb Z\). For \(0\le r\le 1/2\), let
\[
J_a(r)=\mathbb P\{\|T_b^tX-X\|<r,\ \|T_b^{2t}X-X\|<r,\ \|T_b^{3t}X-X\|<r\},
\]
where \(T_bx=bx\bmod 1\) and \(\|u\|=\min_{k\in\mathbb Z}|u-k|\). Boundary conventions do not change the probability. Define
\[
\rho_a=\frac{a}{a^2+a+2}=\frac{a}{N+1},\qquad
\eta_a=\frac{a}{2N(N+1)}.
\]
Then, for every real \(0\le r\le \rho_a\),
\[
\boxed{J_a(r)=\frac{2r}{N}.}
\]
This is the exact *maximal* interval on which the three events intersect only in neighborhoods of the common fixed phase: for \(\rho_a<r\le \rho_a+\eta_a\),
\[
\boxed{J_a(r)=\frac{2r}{N}+\frac{2(N+1)}{N}(r-\rho_a).}
\]
Thus the right derivative jumps by \(2(N+1)/N\) at the first off-diagonal three-return resonance. By comparison, the first off-diagonal **two-return** overlap occurs at \(1/(a+2)\); the separation of these two thresholds equals
\[
\boxed{\rho_a-\frac1{a+2}=\frac{a-2}{(a+2)(N+1)}.}
\]
It is strictly positive for \(a>2\), and zero for \(a=2\). This provides a sharp distinction between pairwise and genuine three-time recurrence clustering.

In the basic doubling-map case \(b=2\), \(t=1\), the complete three-time law, not just its onset, is
\[
J_2(r)=\begin{cases}
2r/7,&0\le r\le1/4,\\
(18r-4)/7,&1/4\le r\le3/10,\\
(74r-18)/21,&3/10\le r\le1/3,\\
(38r-6)/21,&1/3\le r\le3/8,\\
(86r-24)/21,&3/8\le r\le2/5,\\
(106r-32)/21,&2/5\le r\le1/2.
\end{cases}
\]
All adjacent formulas agree at their shared endpoints. The exact third factorial moment of the number of returns among the three observation times is \(6J_a(r)\).

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar probability and geodesic (shortest-arc) distance. The expansion base \(b\) and spacing \(t\) are positive integers as stated, and all three target radii are equal. No independence between observations is imposed. The event at time \(jt\) compares the same initial position to its \(jt\)-th iterate; it is not a comparison to a separately randomized center. The formula concerns finite-time stationary joint probabilities, not almost-sure infinite-time shrinking-target laws.

## Proof

**1. Haar reduction to three integer frequencies.** Put \(Y=(a-1)X\bmod1\). Multiplication by the positive integer \(a-1\) preserves Haar measure, and
\[
a-1=(a-1),\quad a^2-1=(a-1)(a+1),\quad a^3-1=(a-1)N.
\]
Therefore
\[
J_a(r)=\lambda\{y\in\mathbb T:\|y\|<r,\ \|(a+1)y\|<r,\ \|Ny\|<r\}.
\]
The set is invariant under \(y\mapsto-y\). For \(r<1/2\), its measure is twice the length of its intersection with \((0,r)\).

**2. No off-diagonal intersections up to the sharp threshold.** Let \(0<r\le\rho_a\) and \(0<y<r\) satisfy the second and third window conditions. Because \((a+1)r\le(a+1)\rho_a=(N-1)/(N+1)<1\), the nearest integer to \((a+1)y\) can only be \(0\) or \(1\).

If it is \(0\), then \(y<r/(a+1)\). Since \(r\le\rho_a<(a+1)/(N+a+1)\),
\[
0<Ny<\frac{Nr}{a+1}<1-r.
\]
The third condition can then only be satisfied near the integer \(0\), giving \(0<y<r/N\). Conversely every such \(y\) satisfies all three conditions.

If the nearest integer to \((a+1)y\) is \(1\), then \((a+1)y>1-r\), so
\[
a-1<a(1-r)<Ny<Nr\le N\rho_a=a-\rho_a<a.
\]
The strict lower inequality follows from \(a\rho_a<1\). Thus the only possible integers within distance \(r\) of \(Ny\) are \(a-1\) and \(a\). In the \(a-1\) case, set \(u=(a+1)y-1\) and \(v=Ny-(a-1)\). Then
\[
(a+1)v-Nu=a+2,
\]
so \(a+2<(N+a+1)r\), contradicting \(r\le\rho_a<(a+2)/(N+a+1)\). In the \(a\) case, \(Ny>a-r\) and \(y<r\), hence \((N+1)r>a\), again contradicting \(r\le\rho_a\). The only surviving intervals on the whole circle are consequently \((-r/N,r/N)\bmod1\), with measure \(2r/N\).

**3. The first new components and their length.** Take \(\rho_a<r\le\rho_a+\eta_a\), with \(\eta_a=a/[2N(N+1)]\). The elementary inequalities
\[
\rho_a+\eta_a<\frac{a+1}{N+a+1}<\frac{a+2}{N+a+1},\qquad
\rho_a+\eta_a<\frac aN<\frac2{a+2}
\]
show that the nearest-integer analysis of step 2 still leaves only \(0\) for the second frequency followed by \(0\) for the third, or \(1\) for the second followed by \(a\) for the third. The rejected combination \((1,a-1)\) remains impossible by the same integer identity. In the new combination the first and third windows say
\[
\frac{a-r}{N}<y<r.
\]
Throughout this interval the second condition holds: its lower endpoint satisfies \((a+1)(a-r)/N>1-r\), because \(r>\rho_a\ge 1/a^2\), and its upper endpoint satisfies \((a+1)r<1+r\), because \(ar<1\). The new interval length is exactly \((N+1)(r-\rho_a)/N\). By reflection it has a second copy; together with the original interval of length \(2r/N\) this proves the stated local formula and shows that the threshold is sharp. The strict comparison to the two-time threshold follows from elementary subtraction. For two windows, the same signed-coordinate argument gives just the central interval until \(r=1/(a+2)\), with a new interval immediately above it.

**4. The complete doubling-map phase diagram.** For \(a=2\), the three multipliers are \(1,3,7\). For a positive half-circle phase \(0<y<r\), the relevant intervals for multiplier \(d\in\{3,7\}\) are the intersections of \((0,r)\) with
\[
\left(\frac{j-r}{d},\frac{j+r}{d}\right),\qquad j=0,1,\ldots,d.
\]
Taking all pairwise intersections for \(d=3,7\) produces a finite sum of positive parts of affine functions of \(r\). Every possible change of boundary order lies in
\[
\left\{0,\frac1{10},\frac18,\frac16,\frac15,\frac14,
\frac3{10},\frac13,\frac38,\frac25,\frac12\right\}.
\]
These are obtained by equating endpoints \((j\pm r)/d\) for \(d\in\{1,3,7\}\). Direct exact-rational interval intersection at the listed radii gives the displayed six affine branches; at the intervening candidates \(1/10,1/8,1/6,1/5\), the slope remains \(2/7\). Since no endpoints cross inside consecutive candidate intervals, the measure is affine there, so the endpoint calculation proves the entire continuum identity, not merely values on a finite grid. The accompanying code implements this finite exact certificate independently of the general all-integer proof.

## Verification

The standalone `check_triple.py` constructs rational circle-window intervals, takes exact intersections, enumerates all possible endpoint crossings for multipliers \(1,3,7\), and verifies the announced affine formula at every crossing. Affinity between consecutive crossings makes that a complete finite symbolic certificate for the all-radius doubling case. It also performs 174 exact-rational tests of the universal small-radius and pair-threshold formulas for integers \(2\le a\le30\). Finite parameter tests are corroboration only; the argument in proof steps 1–3 covers all admissible integers.

## Relationship to prior work

Kirsebom, Kunde, and Persson introduce the self-return sets for integer expanding circle maps and develop exact Fourier representations and estimates for **two** such events in Section 6, and multi-event unions for eventual hitting in Section 8. Those pairwise constructions provide important context, but they do not state the sharp threefold common-resonance threshold, its local derivative jump, or the complete first-three-time probability law. He and Liao derive quantitative recurrence results and correlation estimates for more general expanding maps, focusing on infinite-time zero-one laws and Hausdorff dimension rather than this exact finite-time triple-overlap diagram. General interval-intersection and Fourier methods are standard and are not claimed as new; the claim here is their sharp three-event application and arithmetic transition.

## Limitations

The circle is equipped with geodesic distance, not the nonperiodic absolute distance on \([0,1]\). The three events have a shared initial phase and shared radius. The general formula provides the exact onset and an explicit post-onset interval, not the entire large-radius phase diagram for every expansion factor. The complete large-radius diagram is proved only for the first three times of the doubling map. No claim of independent audit, comprehensive indexing, or publication priority is made. Equivalent unindexed formulations and other higher-order symbolic accounts remain a novelty risk.

## References

1. M. Kirsebom, P. Kunde, T. Persson, *On shrinking targets and self-returning points*, arXiv:2003.01361, first posted 2020-03-03; Section 6 (pairwise Fourier overlaps), Section 8 (eventual hitting). https://arxiv.org/abs/2003.01361
2. Y. He, L. Liao, *Quantitative recurrence properties for piecewise expanding maps on [0,1]^d*, arXiv:2302.05149, first posted 2023-02-10; introduction and recurrence-correlation estimates. https://arxiv.org/abs/2302.05149
