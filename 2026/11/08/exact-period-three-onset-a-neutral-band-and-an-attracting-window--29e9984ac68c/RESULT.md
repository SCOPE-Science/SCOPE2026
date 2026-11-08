# Exact period-three onset, a neutral band, and an attracting-window cutoff in a Parrondo tent composite

## Finding
Let \(f_1(x)=\min\{x,1-x\}\), and let \(g_{t,1/4}\) be the increasing two-slope homeomorphism of \([0,1]\) given by \(g_{t,1/4}(u)=tu\) for \(u\le1/4\) and \(g_{t,1/4}(u)=((4-t)u+t-1)/3\) for \(u\ge1/4\). Consider \(F_t=g_{t,1/4}\circ f_1\) for \(1<t<4\). Define
\[
 t_0=\frac{3+\sqrt{21}}2,\qquad q(t)=t^2(4-t),\qquad
 t_1\in(3,4):q(t_1)=1.
\]
The root \(t_1\) is unique (approximately \(3.93543233197003\)); \(t_0\approx3.79128784747792\). **All primitive (least-period-three) orbits** of \(F_t\) are as follows.

* For \(1<t<t_0\), there are none.
* At \(t=t_0\), every \(b\in[1/2,3/4]\) yields a distinct primitive three-cycle
\[
\left(\frac b{t_0},\ b,\ 1-\frac b{t_0^2}\right)
\]
written in dynamical order. These exhaust the primitive three-cycles. Three disjoint nondegenerate intervals are cyclically permuted, and the third iterate is the identity there.
* For \(t_0<t<4\), there are exactly **two** distinct primitive three-cycles, \(E_t\) and \(R_t\), written in increasing (also dynamical) order. Let
\[
 R_t=\left(\frac{t}{t^2+t+1},\ \frac{t^2}{t^2+t+1},\ \frac{t(t+1)}{t^2+t+1}\right).
\]
The second is
\[
 E_t=\begin{cases}
 \left(\dfrac{t(4-t)}{3+q},\dfrac q{3+q},\ 1-\dfrac{4-t}{3+q}\right),& t_0<t\le t_1,\\[3pt]
 \left(\dfrac t{1+t^3},\dfrac{t^2}{1+t^3},\dfrac{t^3}{1+t^3}\right),&t_1\le t<4.
 \end{cases}
\]
The two expressions agree at \(t=t_1\). The return multiplier of \(R_t\) is \(t^3>1\). For \(t_0<t<t_1\), the return multiplier of \(E_t\) is \(-q(t)/3\), strictly between \(-1\) and \(-1/3\): this orbit is locally attracting. For \(t_1<t<4\), its return multiplier is \(-t^3\), so both primitive three-cycles are repelling. No two-sided smooth stability statement is made at the branch-collision parameter \(t=t_1\).

## Assumptions and scope
The map acts on the full compact interval \([0,1]\), with parameter \(1<t<4\); at the join points the continuous branch formulas agree. A periodic orbit is counted once, independent of its starting point, and has *least* period three. The analysis addresses only period three, not all possible periods, entropy values, or global basins. The chosen tent slope \(1\) and homeomorphism breakpoint \(1/4\) are parameters in the family studied by Cánovas (2021); the latter breakpoint is also represented in that work's parameter study.

Writing \(\alpha=(4-t)/3\), the exact affine pieces are
\[
F_t(x)=\begin{cases}
 t x,&0\le x\le1/4,\\
 \alpha x+(t-1)/3,&1/4\le x\le1/2,\\
 1-\alpha x,&1/2\le x\le3/4,\\
 t(1-x),&3/4\le x\le1.
\end{cases}
\]
The map is strictly increasing to \(1/2\) and strictly decreasing thereafter; its peak is \((t+2)/6\).

## Proof
**1. Excluding smaller parameters.** For \(1<t\le3\), set \(M=(t+2)/6\), and \(J=[1/2,M]\). The map is decreasing on \(J\), and maps \(J\) into itself. Indeed, if \(M\le3/4\), then \(F_t(M)=(t^2-2t+10)/18\ge1/2\), since \((t-1)^2\ge0\); if \(3/4\le M\le5/6\), then \(F_t(M)=t(4-t)/6\ge1/2\) since \((t-1)(3-t)\ge0\). Also \(F_t(1/2)=M\). For \(0<x<1/2\), strict monotonicity of the homeomorphism and \(t>1\) give \(F_t(x)>x\). An orbit that hits \(0\) is then fixed. Otherwise, if an orbit remains below \(1/2\) after some time, its positive states would increase toward a fixed point there; no positive such point exists, and continuity at \(1/2\) (where \(F_t(1/2)>1/2\)) rules out approach to that endpoint from below. Hence each orbit either hits \(0\) or enters the forward-invariant interval \(J\). A decreasing interval map has no primitive odd period exceeding one. Zero is fixed. Hence no primitive period-three cycle exists for \(t\le3\).

**2. Ordering and itinerary reduction for \(t>3\).** Write any three distinct cycle points \(a<b<c\). Strict unimodality forces the dynamical orientation \(a\mapsto b\mapsto c\mapsto a\): the other orientation \(a\mapsto c\mapsto b\mapsto a\) contradicts strict increase on the left if \(b\le1/2\) (because \(F_t(a)<F_t(b)\)) and contradicts strict decrease on the right if \(b>1/2\) (because \(F_t(b)>F_t(c)\)). Also \(a<1/2<c\): if all three were on one monotonic side, period three would be impossible, and the orientation yields the stated crossing. More directly the ordering and orientation place the smallest point on the increasing side and the largest on the decreasing side. Since \(F_t(c)=a<1/2\), we must have \(c>3/4\), because on \([1/2,3/4]\), \(F_t\ge t/4>3/4\). Finally \(a<1/4\). Otherwise \(b=F_t(a)\ge t/4>3/4\), but then \(c=F_t(b)=t(1-b)<b\) since \(b\ge t/4>t/(t+1)\), a contradiction. Hence \(b=ta\), \(a=t(1-c)\), and \(c=F_t(b)\). In particular \(a=b/t\), \(c=1-b/t^2\).

**3. Exhaustive four-way solution.** Split the *middle-in-order* point \(b\) by the four defining intervals of \(F_t\).

(i) If \(0\le b\le1/4\), the equation \(1-b/t^2=tb\) yields \(b=t^2/(1+t^3)\) and the displayed \(E_t\) with coordinates \(a=t/(1+t^3)\), \(b=t^2/(1+t^3)\), and \(c=t^3/(1+t^3)\). Its branch inequalities hold precisely for \(q(t)\le1\), hence \(t\ge t_1\) on \((3,4)\).

(ii) If \(1/4\le b\le1/2\), \(1-b/t^2=\alpha b+(t-1)/3\) yields \(b=q/(3+q)\) and the other displayed \(E_t\). The branch inequalities are exactly \(1\le q(t)\le3\), or \(t_0\le t\le t_1\).

(iii) If \(1/2\le b\le3/4\), \(1-b/t^2=1-\alpha b\) requires \(t^2\alpha=q(t)/3=1\); this occurs only at \(t=t_0\), where every such \(b\) supplies the claimed neutral cycle and \(F_{t_0}^3\) acts identically on its first interval. Every one of these points is distinct, because \(a<1/4<b<c\) and \(c>3/4\).

(iv) If \(3/4\le b\le1\), \(1-b/t^2=t(1-b)\) yields \(b=t^2/(t^2+t+1)\), and so \(R_t\). Feasibility is \(t^2\ge3t+3\), equivalently \(t\ge t_0\). The three points satisfy the strict order \(a<b<c\) and the other required branch conditions throughout their stated ranges. At \(t=t_0\) this solution is already the endpoint \(b=3/4\) of the neutral continuum, and at \(t=t_1\) the formulas in (i) and (ii) coincide. No other itineraries are possible by steps 1–2. Since \(q\) is strictly decreasing on \((3,4)\), these feasibility ranges are exhaustive.

**4. Stability.** Multiplication of the three applicable affine slopes gives \(t^3\) for \(R_t\), \(-t^2\alpha=-q/3\) on the (ii) branch of \(E_t\), and \(-t^3\) on the (i) branch. The neutral continuum in (iii) has multiplier \(+1\) and is pointwise fixed by the third iterate. This proves every claim.

## Verification
The standalone `check_period_three.py` independently solves all \(4^3=64\) affine branch itineraries over 65 rational choices of \(t\), compares the exact least-period-three orbit sets to the stated formulas, and checks 41 representative points of the neutral cycle parametrization plus the algebraic threshold identity. It reports 188 parameter/family test groups; the analytic proof, not the finite checker, establishes the universal theorem. Execute `python3 check_period_three.py` with Python 3 standard library.

## Relationship to prior work
Cánovas (2021), *Parrondo's Paradox for Tent Maps*, defines exactly the parent family \(g_{t,p}\circ f_s\), analyzes entropy comparisons and numerical parameter regions, and studies \(p=1/4\). The present classification concerns the precise least-period-three orbit census along the natural \(s=1,p=1/4\) slice, the one-parameter neutral interval at \(t_0\), and the second stability change at \(t_1\). Existing general descriptions of border collisions and skew-tent periodic windows explain why such local phenomena may occur but are not themselves an exact implication of these parameter-specific formulas. No claim of a novel universal border-collision mechanism or an entropy formula is made.

## Limitations
The claim does not classify other periodic orbits, overall entropy, basins, or stability at the nonsmooth collision parameter \(t=t_1\). The index and literature comparisons cannot rule out an unindexed equivalent special-case calculation; an independent mathematical audit is not yet performed.

## References
1. J. S. Cánovas, “Parrondo's Paradox for Tent Maps,” *Axioms* **10** (2021), 85, first publicly available 2021-05-06, DOI: 10.3390/axioms10020085. https://doi.org/10.3390/axioms10020085
2. I. Sushko, V. Avrutin, and L. Gardini, “Bifurcation structure in the skew tent map and its application as a border collision normal form,” *Journal of Difference Equations and Applications* (2015/2016). https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Journals/SAG_JDEA_2015.pdf
3. J. Li and J. A. Yorke, “Period Three Implies Chaos,” *American Mathematical Monthly* **82** (1975), 985–992; background for the significance of an exact period-three threshold, not used in the orbit census proof.
