# The largest-storm-first rule holds through three pulses but fails at four

## Finding
For every capacity \(C>0\), common inter-pulse retention \(q\in(0,1)\), and multiset of at most three nonnegative rainfall depths, there is a temporal permutation minimizing cumulative saturation runoff from an **initially empty** finite water store that begins with a largest rainfall depth. This largest-first existence theorem is sharp in the number of pulses: at four pulses it can fail even with distinct positive depths. Specifically, \(C=14\), \(q=1/4\), and depths \(\{1,11,12,13\}\) give a unique runoff-minimizing order \((12,11,1,13)\), producing runoff \(1/8\), whereas every order beginning with the largest depth \(13\) produces at least \(1/4\). Thus the best largest-first policy generates twice the optimal runoff in this exact example.

## Assumptions and scope
For a finite sequence \(h_1,\ldots,h_n\ge0\), define post-storm storage \(s_0=0\) and, for \(i=1,\ldots,n\),
\[
 s_i=\min\{C,qs_{i-1}+h_i\},\qquad r_i=(qs_{i-1}+h_i-C)_+.
\]
Here \(C\) is finite capacity, \(q\) is the fixed proportion of water retained between equally spaced events, \(r_i\) is immediate overflow, and \(R_n=\sum_{i=1}^{n}r_i\) is total overflow through the final event. All orders use the same multiset and same \(q,C\). The initial empty condition and finite—not periodic—time horizon are essential to this claim. Inter-event loss is \((1-q)s_i\); no additional loss is charged after the final pulse. This may represent a simple canopy/interception bucket or soil/depression-storage analogue, but it is not a mechanistic watershed model.

## Proof
The one-pulse case is immediate. We prove two exchange inequalities, both for \(0<q<1\).

**Adjacent initial exchange.** For \(x\ge y\ge0\), starting empty, put \(a=\min(C,x)\), \(b=\min(C,y)\), \(u=\min(C,qa+y)\), \(v=\min(C,qb+x)\). Then
\[
0\le v-u\le(1-q)(a-b).
\]
If \(x\le C\), this follows because the clipping map \(z\mapsto\min(C,z)\) is increasing and 1-Lipschitz, and the inputs differ by \((1-q)(x-y)\). If \(x\ge C\) and \(y<C\), then \(v=C\) and \(v-u=((1-q)C-y)_+\le(1-q)(C-y)\). If \(y\ge C\), all four post-event storages equal \(C\). By two-step mass balance,
\[
R_2(x,y)=x+y-(1-q)a-u,
\]
so \(R_2(x,y)\le R_2(y,x)\). Moreover \(u\le v\); subsequent runoff is a nondecreasing function of the preceding storage. Thus the same ordering remains no worse after *any identical suffix*. In particular, placing the larger of the first two depths first never increases the total runoff.

**Endpoint exchange for three pulses.** For \(z\ge\max\{x,y\}\), we claim
\[
R_3(z,y,x)\le R_3(x,y,z).
\]
Write \(a=\min(C,x)\), \(c=\min(C,z)\), \(A=\min(C,qa+y)\), \(B=\min(C,qc+y)\), \(U=\min(C,qA+z)\), and \(V=\min(C,qB+x)\). Put \(e=B-A\ge0\). Since three-step mass balance reads
\[
R_3=\sum h_i-(1-q)(s_1+s_2)-s_3,
\]
it is enough to establish \((1-q)(c-a+e)+V-U\ge0\).

If \(z\le C\) and \(B<C\), then \(a=x,c=z,e=q(z-x)\). The two unclipped third-event inputs differ by \(z-x-qe=(1-q^2)(z-x)\), so the 1-Lipschitz clipping property gives \(U-V\le(1-q^2)(z-x)=(1-q)(c-a+e)\). If \(z\le C\) and \(B=C\), then \(U=C\): indeed \(qz+y\ge C\), \(A\ge y\), and \(z\ge y\) imply \(qA+z\ge qy+z\ge qz+y\). Also \(V=\min(C,qC+x)\). If \(V=C\), the desired inequality is automatic. Otherwise, if \(A<C\) then \(A=qx+y\), and the difference \((1-q)(c-a+e)+V-U\) simplifies to \((1-q)(z-y)+q^2x\ge0\). If \(A=C\), the difference becomes \(qx-(1-q)(C-z)\ge0\), because \(qx+y\ge C\) and \(z\ge y\) imply \(qx\ge C-z\).

If \(z>C\), then \(c=C\) and \(U=C\). If \(x\ge C\), both candidate sequences have identical saturation patterns and the difference is zero. If \(x<C\) and \(B<C\), then \(e=q(C-x)\) and \(A=qx+y\); when \(V<C\) the difference simplifies to \(q^2x+qy\ge0\), while \(V=C\) is immediate. Finally if \(x<C\) and \(B=C\), then \(V=\min(C,qC+x)\) and
\[
(1-q)(c-a+e)+V-U\ge (1-q)(C-x)-((1-q)C-x)_+\ge0.
\]
The endpoint exchange is proved in all cases, including exact saturation boundaries.

**Global conclusion for three pulses.** If a largest depth is first there is nothing to do. If it is second, the adjacent initial exchange moves it first without increasing runoff. If it is third, the endpoint exchange moves it first, keeping the middle event unchanged, without increasing runoff. This proves the universal existence assertion. For two pulses the adjacent exchange suffices.

**Sharp failure at four.** With the stated \(C,q\), compute the recurrence exactly. The six orders beginning with 13 have respective runoff values
\[
\begin{array}{c|cccccc}
(h_1,h_2,h_3,h_4)&(13,1,11,12)&(13,1,12,11)&(13,11,1,12)&(13,11,12,1)&(13,12,1,11)&(13,12,11,1)\\
R_4&65/64&17/64&1/4&7/4&5/4&7/4
\end{array}
\]
where the row consists of exact rational values. The order \((12,11,1,13)\) produces \(1/8\), strictly below the smallest largest-first value \(1/4\). Direct evaluation of all 24 permutations shows this order is the unique minimizer. Therefore the largest-first property is genuinely false at four, the smallest possible number of pulses.

## Verification
`verify.py` uses only Python standard-library rational arithmetic. Run `python verify.py` in the same directory. It checks every multiset of three depths from an eight-value rational grid at seven rational retentions and seven rational capacities, checks both structural inequalities, evaluates all 24 four-storm orders exactly and checks mass balance. These finite checks corroborate but do not replace the universal exchange proof. The four-storm certificate is finite and exhaustive because all 24 distinct permutations are evaluated.

## Relationship to prior work
Keim et al. (2004) analyze stochastic throughfall and its dependence on rainfall extremes; Miralles et al. (2010) implement and validate Gash's canopy interception model, including the common assumption that the canopy dries between events. Bartlett et al. (2015) model stochastic instantaneous rainfall jumps, moisture states, and threshold runoff. These papers motivate finite capacity and rainfall timing but do not state the transient empty-start, three-pulse largest-first theorem or the sharp four-pulse failure. A publicly indexed prior result titled *A sharp storm-ordering window for saturation runoff in a periodic linear store* compares two three-event orders in a **unique periodic stationary regime** and identifies a capacity interval: its cyclic initial state is endogenous, its objective is settled-cycle runoff, and it neither implies an optimal first pulse in an empty-start finite horizon nor supplies the four-event counterexample. The classical finite-dam, rearrangement, and scheduling literature remains a residual priority risk; no claim is made that clipping/bucket recurrences are new.

## Limitations
The theorem requires initially empty storage, identical inter-event retention, immediate excess spill and an unweighted sum of runoff volumes through the final event. It does not address maximum discharge, finite storm duration, varying inter-event gaps, evapotranspiration depending on wetness, arbitrary initial storage, long-run periodic state, sediment response, or realistic landscape heterogeneity. In four-pulse scenarios the displayed numbers are one exact counterexample, not an optimization formula for arbitrary four-pulse parameters. The numerical checks are finite tests, not proofs of the universal inequality. Historical novelty beyond inspected literature is not independently established.

## References
1. Keim, R. F., Skaugset, A. E., Link, T. E., and Iroumé, A. (2004), *A stochastic model of throughfall for extreme events*, Hydrology and Earth System Sciences 8, 23–34, published 29 February 2004. https://doi.org/10.5194/hess-8-23-2004.
2. Miralles, D. G., Gash, J. H., Holmes, T. R. H., de Jeu, R. A. M., and Dolman, A. J. (2010), *Global canopy interception from satellite observations*, Journal of Geophysical Research: Atmospheres 115, published 31 August 2010. https://doi.org/10.1029/2009JD013530.
3. Bartlett, M. S., Daly, E., McDonnell, J. J., Parolari, A. J., and Porporato, A. (2015), *Stochastic rainfall-runoff model with explicit soil moisture dynamics*, Proceedings of the Royal Society A 471, 20150389. https://doi.org/10.1098/rspa.2015.0389.
4. *A sharp storm-ordering window for saturation runoff in a periodic linear store* (2026), public published-finding corpus mathematical record, identifier d7dd28e86fa3, available in https://github.com/published-finding corpus/2026.
