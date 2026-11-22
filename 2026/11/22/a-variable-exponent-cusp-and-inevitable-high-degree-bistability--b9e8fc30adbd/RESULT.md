# A variable-exponent cusp and inevitable high-degree bistability in fixed-point-free interval maps

## Finding

Consider the piecewise-power map of Lawnik, Moysis and Volos [1],
\[
 F(x)=\begin{cases}
 1-(1-a)((b-x)/b)^d,&0\le x\le b,\\
 c((x-b)/(1-b))^d,&b<x\le1,
 \end{cases}
\]
under the strict-alternation assumptions \(0<c<b<a<1\) and \(d\ge1\). Put
\[
 q=\frac{1-a}{1-b},\qquad r=\frac cb,\qquad
 q_d=\frac{(d+1)^{d-1}}{d^d}\quad(d>1).
\]
All orbits alternate strictly between the two branches after the first step and converge to a primitive two-cycle. If \(d=1\), or if \(d>1\) and \(q<q_d\), there is exactly one such cycle, hyperbolically attracting. If \(d>1\) and \(q=q_d\), there is still exactly one cycle; it is attracting, neutral only when \(r=q_d\). For \(d>1\) and \(q>q_d\), the complete count is one, two, or three cycles, according to the exact fold boundaries below. In the open three-cycle region, exactly two cycles attract and the third separates their basins and repels.

Define
\[
 P_d(t)=t^{d-1}\bigl[d^2-(d^2-1)t\bigr],\qquad
 H_{d,q}(t)=\frac{1-t}{(1-qt^d)^d},\quad 0\le t\le1.
\]
For \(q>q_d\), the equation \(qP_d(t)=1\) has exactly two solutions \(t_-<d/(d+1)<t_+\), and \(r_-=H_{d,q}(t_-)<r_+=H_{d,q}(t_+)\). Subject to the physical restriction \(0<r<1\), there are exactly three primitive two-cycles if \(r_-<r<r_+\), exactly two distinct cycles if \(r=r_-\) or \(r=r_+\), and exactly one otherwise. Each double-root cycle at a fold is one-sided attracting; all other cycles are classified by the derivative inequalities in the proof. These statements include the cases \(r_+\ge1\), for which the upper fold lies outside the physical parameter range.

The two folds meet at a unique cusp
\[
 (q,r)=\bigl(q_d,q_d\bigr),\qquad
 u_*=(d+1)^{-1},
\]
where \(u=x/b\) is the left-coordinate normalization. At this cusp every nonstationary orbit converges to the sole cycle at the exact critical rate
\[
 \lim_{n\to\infty}\sqrt n\,\bigl(u_n-u_*\bigr)
 =\operatorname{sgn}(u_0-u_*)\sqrt{\frac{3d^2}{(d-1)(d+1)^3}}
\]
for left-branch iterates \(u_n\) of the two-step return, provided \(u_0\ne u_*\). For fixed \(d>1\), as \(q\downarrow q_d\) from above, the vertical width of the fold region satisfies
\[
 r_+(q)-r_-(q)\sim C_d(q-q_d)^{3/2},\qquad
 C_d=\frac{4(d+1)}3\sqrt{\frac{2}{d(d-1)q_d}}.
\]

The variable exponent gives an additional global conclusion absent from a fixed-degree analysis. For **every fixed** \(0<c<b<a<1\), all sufficiently large real exponents \(d\) produce exactly three primitive two-cycles, two attracting. Indeed \(q_d\sim e/d\), and if \(x_{\rm small}\) and \(x_{\rm large}\) denote the left coordinates of the two attracting cycles, then
\[
 x_{\rm small}\sim c(1-q)^d,\qquad
 x_{\rm large}=c-cdq(1-r)^d(1+o(1)).
\]
Both attracting cycle multipliers tend to zero. Their two limiting geometric locations are \((0,a)\) and \((c,1)\), in the sense of the ordered left/right phase points.

## Assumptions and scope

All exponents are real, \(d\ge1\), with \(0<c<b<a<1\). All powers use nonnegative real arguments. The map takes \([0,1]\) into itself, is discontinuous at \(b\), and is defined with the left value \(F(b)=1\). A cycle means two distinct points of the *original* map, one in each open branch. “Attracting” at a neutral fold refers to the specified one-sided local convergence, not hyperbolic attraction. The claimed large-exponent asymptotics fix \(a,b,c\) before allowing \(d\to\infty\); the cusp asymptotics instead fix \(d\) and let \(q\downarrow q_d\). These are distinct limits.

## Proof

**1. Alternation and reduction.** The left branch has image \([a,1]\subset(b,1]\); the right branch has image \((0,c]\subset[0,b)\). Thus every orbit alternates, and there are no fixed points. If \(x=bu\) is in the left branch, the two-step return is \(x\mapsto bG(u)\), where
\[
 G(u)=r[1-q(1-u)^d]^d,\qquad 0\le u\le1.
\]
It is continuous and strictly increasing, with \(G(0)>0\) and \(G(1)=r<1\). Its iterates converge to fixed points: after the first step an orbit is monotonic, and boundedness and continuity identify the limit. Consequently no original-map orbit can have a least period other than two, and every such cycle is obtained by solving \(G(u)=u\). For \(t=1-u\), this equation is \(H_{d,q}(t)=r\).

**2. Complete root count.** If \(d=1\), \(H'_{1,q}(t)<0\) throughout \([0,1]\) since \(q<1\). Suppose \(d>1\). Direct differentiation gives
\[
 \frac{H'_{d,q}(t)}{H_{d,q}(t)}
 =\frac{qP_d(t)-1}{(1-t)(1-qt^d)}\qquad(0<t<1).
\]
The function \(P_d\) increases strictly on \((0,d/(d+1))\) and decreases strictly on \((d/(d+1),1)\). Also \(P_d(0)=0\), \(P_d(1)=1\) and
\[
 P_d\!\left(\frac{d}{d+1}\right)=\frac1{q_d}.
\]
Because \(0<q<1\), this proves strict decrease of \(H\) for \(q<q_d\), and monotone decrease with a horizontal stationary inflection for \(q=q_d\). For \(q>q_d\), it proves the strict decrease/increase/decrease pattern separated by \(t_-\) and \(t_+\). Since \(H(0)=1\) and \(H(1)=0\), the stated exact one/two/three root census follows, including equality and out-of-range upper-fold cases. The unique meeting of folds is at \(q=q_d\), where \(H_{d,q_d}(d/(d+1))=q_d\).

**3. Stability, basins, and invariant measures.** At a fixed point with \(t=1-u\), the two-step multiplier is
\[
 m=G'(u)=\frac{d^2qt^{d-1}(1-t)}{1-qt^d}.
\]
Consequently \(m<1\), \(m=1\), or \(m>1\) exactly when \(qP_d(t)<1\), \(=1\), or \(>1\). Therefore each outer root in the three-root phase attracts and the middle root repels. The fold point is semistable from one side, with the other (simple) root attracting. Monotonicity of \(G\), together with the signs of \(G(u)-u\), gives the basins without any measure-theoretic assumption. Any invariant Borel probability is a convex combination of the equidistributions on the finitely many primitive two-cycles: recurrence under the invariant measure and pointwise convergence exclude mass off these cycles. In the three-cycle phase, the repelling cycle has a zero-Lebesgue basin, while both attracting cycles have basins containing nonempty intervals.

**4. Cubic cusp and fold opening.** At the cusp put \(u_*=(d+1)^{-1}\). Differentiating the exact return map (all derivatives exist at \(u_*\in(0,1)\)) gives
\[
 G(u_*)=u_*,\quad G'(u_*)=1,\quad G''(u_*)=0,\quad
 G'''(u_*)=-\frac{(d-1)(d+1)^3}{d^2}.
\]
Thus for \(v=u-u_*\),
\[
 v_{n+1}=v_n-\kappa_d v_n^3+O(v_n^4),\qquad
 \kappa_d=\frac{(d-1)(d+1)^3}{6d^2}>0.
\]
Global monotone convergence, sign preservation, and the telescoping relation \(v_{n+1}^{-2}-v_n^{-2}=2\kappa_d+o(1)\) prove the critical \(n^{-1/2}\) constant. The initial cusp fixed point is excluded from that limit.

For the width calculation, with \(t_* =d/(d+1)\), direct differentiation yields
\[
 q_d P_d''(t_*)=-\frac{(d-1)(d+1)^2}{d}.
\]
The critical-point equation \(qP_d(t)=1\), at \(q=q_d+\epsilon\), has solutions
\[
 t_\pm=t_*\pm s_d\sqrt\epsilon+O(\epsilon),\quad
 s_d=\sqrt{\frac{2d}{(d-1)(d+1)^2q_d}}.
\]
Integrate the exact derivative \(H'=H(qP_d-1)/[(1-t)(1-qt^d)]\) between these roots. Taylor's theorem gives the \(3/2\)-power width with coefficient \(C_d=4(d+1)^2s_d/(3d)\), exactly as stated.

**5. High-exponent theorem.** The formula \(q_d=(1+1/d)^d/(d+1)\) gives \(q_d\sim e/d\). Fix \(q,r\in(0,1)\). For large \(d\), \(t_A=1-2\log(d)/d\) and \(t_B=1-1/d^2\) obey \(0<t_A<t_B<1\). They satisfy
\[
 H_{d,q}(t_A)\longrightarrow0,\qquad
 H_{d,q}(t_B)\longrightarrow+\infty,
\]
using \(t_A^d\le d^{-2}\) and \(t_B^d\ge1-1/d\). Since \(H(0)=1>r>0=H(1)\), the intermediate value theorem supplies three roots, and Step 2 proves there are no others. For the lower-\(t\) root, \(t\to1-r\) and expansion of \((1-qt^d)^d\) gives \(x_{\rm large}=c-cdq(1-r)^d(1+o(1))\). For the upper-\(t\) root, set \(u=1-t\). Since this upper-\(t\) root satisfies \(t>t_B=1-1/d^2\), it obeys \(t^d\ge1-1/d\), hence \(u=r(1-qt^d)^d\le r(1-q+q/d)^d=O((1-q/2)^d)\). Thus \(d^2u\to0\), which allows the relative expansion \(1-qt^d=(1-q)(1+O(du))\), and yields \(u=r(1-q)^d(1+o(1))\). Finally the exact derivative \(G'(u)=rd^2q(1-u)^{d-1}[1-q(1-u)^d]^{d-1}\) shows both outer multipliers vanish exponentially. This proves all assertions.

## Verification

The accompanying `verify.py` checks, independently of the limit arguments: the exact cusp derivatives for several integer exponents, the cusp width constants at high precision for integer and noninteger exponents, the full one/two/three phase census at selected parameters, exact alternation, and the asymptotic stable-branch locations. The script is supplemental numerical and symbolic corroboration; the infinite-exponent claims and the continuum parameter classification follow from the proof, not from a finite experiment.

## Relationship to prior work

Lawnik, Moysis and Volos [1] introduce the full real-power family and numerically examine Lyapunov/bifurcation patterns, without a complete strictly alternating, variable-exponent two-cycle phase diagram. The public indexed result [2] already identifies a cusp and its \(n^{-1/2}\) critical relaxation for the **quadratic** specialization \(d=2\). Thus none of the \(d=2\) consequences here are claimed as new. The separate indexed result [3] treats a contracting region and the discontinuity boundary, not the all-parameter sharp two-cycle cusp for every real \(d>1\). The precise additional assertions are the all-real-exponent cusp threshold, exact fold-width coefficient, and the forced high-exponent coexistence and location laws. The search record and limits of published-source access are in the accompanying review.

## Limitations

This is a statement only for \(0<c<b<a<1\). Outside strict alternation there may be higher-period and chaotic dynamics, and no classification is asserted. The cusp asymptotic is for fixed \(d>1\), whereas the high-exponent result fixes \(a,b,c\) and takes \(d\to\infty\). No uniform crossover between these two limits is proved. Priority relative to unindexed publications and inaccessible full records remains unresolved.

## References

[1] M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, published 27 June 2023. https://doi.org/10.3390/sym15071311 ; full author text is available at https://www.academia.edu/121832692/A_Family_of_1D_Chaotic_Maps_without_Equilibria .

[2] *A cusp of coexisting two-cycles in a fixed-point-free quadratic interval map*, publicly indexed result (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-cusp-of-coexisting-two-cycles-in-a-fixed-point-free-quadratic--dd9acbf9570b .

[3] *An attracting two-cycle disappears into a nonstationary ghost at a discontinuity*, publicly indexed result (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-attracting-two-cycle-disappears-into-a-nonstationary-ghost-at--3ab687079720 .
