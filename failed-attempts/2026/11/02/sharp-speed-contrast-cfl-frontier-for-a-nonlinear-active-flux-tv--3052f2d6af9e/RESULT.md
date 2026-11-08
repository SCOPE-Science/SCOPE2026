# Sharp speed-contrast CFL frontier for a nonlinear Active Flux TVD correction interval

## Finding

The explicit nonlinear flux-correction interval of Barsukow (2026, Theorem 4, equation (118)) admits a sharp slope- and speed-dependent feasibility classification. Write
\[
 s=\frac{\Delta t}{\Delta x}\,a_{\max},\qquad
 r=\frac{a_{\min}}{a_{\max}},\qquad
 p=\frac{1}{1+R},
\]
where the characteristic-speed bounds satisfy \(0<a_{\min}\le a_{\max}\), the monotone cell-increment ratio satisfies \(R\ge0\), and \(0<s\le1\). For Simpson endpoint weight \(\gamma=1/6\), the prescribed correction parameter \(\rho\) belongs to
\[
 \mathcal I(s,r,p)=\left[
  \max\left(0,\frac{s-p}{1-s/6}\right),\;
  \min\left(1,\frac{rs+1-p}{1+s/6}\right)
 \right]. \tag{1}
\]
This interval is nonempty **if and only if**
\[
 p\ge \max\left\{
 0,\;\frac{7s}{6}-1,\;
 \frac{1+(1+r)s}{2}-\frac{3[1+(r-1)s]}{s}
 \right\}. \tag{2}
\]
Equivalently, fixing the speed ratio \(r\) and slope parameter \(p\), the exact largest feasible Courant parameter is
\[
 \boxed{\quad s_{\max}(r,p)=\min\left\{
 1,\;\frac{6(1+p)}{7},\;
 \frac{\sqrt{(7-6r-2p)^2+24(1+r)}-(7-6r-2p)}{2(1+r)}
 \right\}.\quad} \tag{3}
\]
Thus \(\mathcal I(s,r,p)\ne\varnothing\) precisely for \(0<s\le s_{\max}(r,p)\).

The largest Courant number that guarantees nonemptiness **for every finite** \(R\ge0\), at a fixed speed ratio \(0<r\le1\), is
\[
 \boxed{\quad s_*(r)=
 \begin{cases}
 \dfrac{\sqrt{(7-6r)^2+24(1+r)}-(7-6r)}{2(1+r)},
 &0<r<1/6,\\[3pt]
 6/7,&1/6\le r\le1.
 \end{cases}\quad} \tag{4}
\]
Both branches meet at \(r=1/6\). In the high-contrast limit \(r\downarrow0\), the sharp constant approaches \((\sqrt{73}-7)/2=0.7720018726\ldots\); for \(r\ge1/6\) it is \(6/7=0.8571428571\ldots\). These are sharper guaranteed feasibility ceilings for the **specified sufficient interval** than the previously stated \((\sqrt{97}-7)/4=0.712214\ldots\) bound. The strict failure beyond the threshold concerns this interval, **not** all possible TVD schemes or the more detailed exact-wave-speed inequalities.

## Assumptions and scope

The initial data are monotonically ordered locally as in the source's positive-wave-speed case; \(R\ge0\) is its ratio of consecutive nonnegative increments. The characteristic speeds used in the source's flux update are uniformly positive and lie between \(a_{\min}\) and \(a_{\max}\), and its endpoint time-quadrature coefficient is \(\gamma=1/6\). The point-update parameter \(\rho\in[0,1]\) must obey the explicit conservative speed-bound prescription (1), equivalent to the source's equation (118). We study **only feasibility of that prescribed interval**. No assertion is made about global TVD of a complete implementation at extrema, about nonlinear point-update accuracy, or about feasibility of more permissive inequalities with actual rather than bounding speeds.

For a fixed \(r\in(0,1]\) and \(p\in(0,1]\), all quantifiers in (1)--(3) range over \(s\in(0,1]\). In (4), \(r\) is fixed and the quantifier covers every \(R\ge0\), equivalently every \(p\in(0,1]\). The limiting value at \(r=0\) is an infimum for strictly positive speeds, not a claim about a zero characteristic speed.

## Proof

Because \(0<s\le1\), both denominators \(1\pm s/6\) are strictly positive, and \(rs+1-p\ge0\). Put \(L\) and \(U\) for the left and right endpoints of (1). If \(p\ge s\), then \(L=0\le U\). If \(p<s\), the condition \(L\le U\) is equivalent to the two inequalities
\[
 \frac{s-p}{1-s/6}\le1,\qquad
 \frac{s-p}{1-s/6}\le\frac{1+rs-p}{1+s/6}. \tag{5}
\]
The first inequality in (5) gives \(p\ge7s/6-1\). Multiplying the second by its positive denominators and collecting terms gives
\[
 1+rs-s-\frac{s(1+rs+s)}6+\frac{sp}{3}\ge0,
\]
which is equivalent to
\[
 p\ge \frac{1+(1+r)s}{2}-\frac{3[1+(r-1)s]}s. \tag{6}
\]
Each right-hand threshold lies strictly below \(s\) in the stated domain: for the first this follows from \(7s/6-1-s=s/6-1<0\), while the difference between the right side of (6) and \(s\) is \((1+rs-s)(1/2-3/s)\le0\). Consequently these inequalities also hold automatically if \(p\ge s\), establishing (2) for every permitted parameter.

Solving \(p\ge7s/6-1\) for \(s\) gives \(s\le6(1+p)/7\). Multiplying (6) by \(2s>0\) gives
\[
 (1+r)s^2+(7-6r-2p)s-6\le0. \tag{7}
\]
This upward-opening quadratic is negative at \(s=0\), has one positive root and one negative root, and is nonpositive on the positive half-line exactly below its positive root. Combining (7), the first inequality and \(s\le1\) proves the exact formula (3).

For a uniform guarantee in \(R\), let \(p\downarrow0\), corresponding to \(R\to\infty\). Both bounds in (3) are nondecreasing in \(p\); equivalently, in (2) the restrictive terms are independent of \(p\). Thus the uniform limit of the positive roots occurs at \(p=0\). The two limiting ceilings are \(6/7\) and the unique positive solution of
\[
 (1+r)s^2+(7-6r)s-6=0. \tag{8}
\]
At \(s=6/7\), the left-hand side of (8) is \(36(1-6r)/49\). Since the left side strictly increases with \(s>0\) for \(0<r\le1\), its positive root is below, equal to, or above \(6/7\) exactly when \(r<1/6\), \(r=1/6\), or \(r>1/6\). This yields (4).

Sharpness is intrinsic to the interval. Above a finite-\(p\) threshold (3), (5) fails and \(L>U\). Above the uniform threshold (4), at least one lower bound on \(p\) in (2) is strictly positive; choose a sufficiently small **positive** \(p\), hence a finite \(R=1/p-1\), below that bound. The interval is then empty. The boundary itself remains feasible by the non-strict inequalities.

## Verification

The standalone script `verify_frontier.py` uses exact rational arithmetic to compare the interval endpoints with both equivalent algebraic conditions. It checks 34,400 parameter triples with \(s\in\{1/40,\ldots,1\}\), \(t=rs\in\{0,1/40,\ldots,s\}\), and \(p\in\{1/40,\ldots,1\}\). It also checks the exact branch meeting \(r=1/6\), the two distinct failure mechanisms (upper bound below the lower bound, and lower bound above one), and prints the analytic boundary values. The geometric-grid tests include \(t=0\) solely as an algebraic limiting case; the theorem's genuine speed ratio is positive. These finite checks supplement, and do not replace, the all-parameter proof above.

## Relationship to prior work

Barsukow's *A TVD Active Flux method for scalar conservation laws* (arXiv:2610.05920v1, October 5, 2026), Theorem 4, supplies the interval (1) through its equation (118) and establishes nonemptiness for \(s\le(\sqrt{97}-7)/4\), using a conservative quadratic estimate in equation (134). It explicitly notes that the CFL estimate may be improved by refining the sufficient conditions. This result retains exactly the paper's operational interval and optimizes its feasibility without changing its construction, giving an exact phase diagram in speed contrast and local increment ratio. The interval itself, the underlying TVD argument, and the basic method are not claimed as new. The earlier nonlinear Active Flux paper (Barsukow, 2021) discusses monotone power-law reconstruction, not the sharp feasibility frontier for this 2026 fully discrete flux-correction interval. General nonlinear or discontinuous Galerkin TVD criteria address different admissibility sets and do not by themselves give (2)--(4).

## Limitations

The improved numbers describe the source's **conservative sufficient bounds**. They are not a sharp CFL stability limit for Active Flux as a whole; other flux corrections and the source's inequalities involving actual local speeds may work at larger steps. The speed contrast \(r\) must be known as a valid positive lower-to-upper speed ratio. At discrete extrema, the source discusses a separate fallback choice and the present interval does not certify its behavior. No new convergence theorem, entropy inequality or extension to systems is asserted. The novelty comparison cannot exclude obscure unpublished or inaccessible computations of the same elementary optimization; the mathematical originality is the new sharp bound and complete feasible-region classification, not a new flux-limiting algorithm.

## References

1. W. Barsukow, *A TVD Active Flux method for scalar conservation laws*, arXiv:2610.05920v1 (first public October 5, 2026), Sections 3--5, especially Theorem 4, equations (118), (127), (130)--(134): https://arxiv.org/html/2610.05920
2. W. Barsukow, *The Active Flux Scheme for Nonlinear Problems*, Journal of Scientific Computing **86**, article 3 (2021), first published December 21, 2020. https://doi.org/10.1007/s10915-020-01381-z
3. W. Barsukow, *Approximate evolution operators for the Active Flux method*, arXiv:2105.13403 (2021), background on nonlinear evolution operators. https://arxiv.org/abs/2105.13403
