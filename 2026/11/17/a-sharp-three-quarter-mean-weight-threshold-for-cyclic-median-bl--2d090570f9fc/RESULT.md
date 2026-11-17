# A sharp three-quarter mean-weight threshold for cyclic median blends

## Finding
Let \(n\ge 6\). On real \(n\)-cycles, form the convex blend of a centered three-point running median and a centered three-point arithmetic mean,
\[
(T_\theta x)_i=(1-\theta)\operatorname{med}(x_{i-1},x_i,x_{i+1})
+\frac{\theta}{3}(x_{i-1}+x_i+x_{i+1}),\qquad 0\le\theta\le1,
\]
with indices interpreted modulo \(n\). Define cyclic total variation by \(V_n(z)=\sum_{i=0}^{n-1}|z_{i+1}-z_i|\). Its exact two-input variation Lipschitz coefficient is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(T_\theta x-T_\theta y)}{V_n(x-y)}
=\max\left\{1,3-\frac83\theta\right\}.}
\]
Consequently, \(T_\theta\) is nonexpansive for differences in cyclic variation **if and only if** \(\theta\ge3/4\). This is an exact phase transition for every cycle length \(n\ge6\), and the bound is attained by finite input pairs, not merely in a derivative limit.

## Assumptions and scope
The input space is \(\mathbb R^n\) with real, equally weighted, periodically indexed coordinates, \(n\ge6\), and the median is the middle order statistic of the three listed numbers. The mixing weight satisfies \(0\le\theta\le1\). All suprema are over pairs with positive variation of their difference. Because the filters commute with addition of constant sequences, the variation seminorm is well-defined for these perturbations on the quotient by constants. No probability model is imposed.

## Proof
**1. Difference factorization on a strict-order chamber.** Fix a vector \(x\) having pairwise distinct coordinates. In a neighborhood of \(x\), each median output selects one fixed coordinate \(x_{\sigma_i}\), with \(\sigma_i\in\{i-1,i,i+1\}\). Let \((Dz)_j=z_{j+1}-z_j\). The linearized three-point mean has \(D\)-factorization whose coefficient of \((Dz)_j\), on output differences at rows \(j-1,j,j+1\), is \((1/3,1/3,1/3)\). All other entries in that column vanish.

For the median selector, set \(a_j=\mathbf1_{\{\sigma_j=j+1\}}\) and \(c_j=\mathbf1_{\{\sigma_{j+1}=j\}}\), reading identities cyclically. Telescoping the differences \(z_{\sigma_{i+1}}-z_{\sigma_i}\) across the at most three intervening input edges gives, in the same three rows, precisely
\[
(a_j,\,1-a_j-c_j,\,c_j).
\]
For clarity, the first coefficient detects whether the selected value at output \(j\) crosses the input edge \((j,j+1)\), the third detects whether output \(j+1\) selects back across it, and the middle follows by the net unit coefficient. Since \(n\ge6\), these are three distinct output edges and their local lifts produce no ambiguous cyclic wrap. Hence, on the chamber, \(D T_\theta=B_\theta D\), and each column of \(B_\theta\) has three possibly nonzero entries
\[
\left((1-\theta)a_j+\frac\theta3,\ 
(1-\theta)(1-a_j-c_j)+\frac\theta3,\ 
(1-\theta)c_j+\frac\theta3\right).
\]

**2. Sharp column-sum bound.** The pair \((a_j,c_j)\) lies in \(\{0,1\}^2\). For the three cases other than \((1,1)\), all column entries are nonnegative and sum to one. For \((a_j,c_j)=(1,1)\), the entries are
\[
\left(1-\frac{2\theta}{3},\,-1+\frac{4\theta}{3},\,1-\frac{2\theta}{3}\right),
\]
whose absolute sum is
\[
2\left(1-\frac{2\theta}{3}\right)+\left|\frac{4\theta}{3}-1\right|
=\max\left\{1,3-\frac83\theta\right\}.
\]
Thus every linearization obeys \(V_n(T_\theta^\prime[x]h)\le L_\theta V_n(h)\), where \(T_\theta^\prime[x]\) denotes the derivative at a strict-order point and \(L_\theta\) is the displayed maximum. More explicitly, \(\|B_\theta Dh\|_1\le L_\theta\|Dh\|_1\). The filter is continuous and piecewise affine with finitely many rank-order chambers. Integrating along the segment between any two inputs, or taking a generic approximation if the segment lies in a tie hyperplane, yields the same bound globally.

**3. Exact attainment for every cycle length.** For \(n=6\), take
\[
x=(0,2,1,5,3,4).
\]
For \(n\ge7\), take a distinct-coordinate vector with
\[
x_0=0,\ x_1=2,\ x_2=1,\ x_3=5,\ x_{n-3}=6,\ x_{n-2}=3,\ x_{n-1}=4,
\]
and set all as-yet unspecified coordinates to \(x_i=10+i\). Let \(h_i=1\) at indices \(2\le i\le n-2\), and \(h_i=0\) elsewhere. Then \(V_n(h)=2\). Across the two jump edges of \(h\), the strict rank inequalities force the median selector's local difference response to be \((1,-1,1)\), with opposite overall signs at the two boundaries. The mean has local difference response \((1/3,1/3,1/3)\), likewise with opposite signs. The three output edges belonging to one interface are disjoint from those of the other interface. For every \(0<\varepsilon<1\), the ranks are unchanged by \(x\mapsto x+\varepsilon h\), and hence
\[
\frac{V_n(T_\theta(x+\varepsilon h)-T_\theta x)}{V_n(\varepsilon h)}
=2\left(1-\frac{2\theta}{3}\right)+\left|\frac{4\theta}{3}-1\right|
= L_\theta.
\]
This proves equality and, in particular, the sharp \(3/4\) threshold.

## Verification
Run `python checker.py` using Python 3 standard library only. Exact rational tests directly verify finite sharpness witnesses for every \(6\le n\le23\) at six rational mixture weights. Rank-order chamber enumeration for \(n=6,7,8\) independently checks the local telescoping identity and all three-edge column absolute sums for seven further rational weights. The finite checks corroborate the structural steps; the all-dimensional, all-real-weight conclusion is established by the proof above, not by exhaustive finite testing.

## Relationship to prior work
Mean–median convex combination filters predate this theorem: Ben Hamza and Krim (2001) defined and investigated mean/median blends, with an emphasis on statistical influence, asymptotic variance, and filter root properties. Arias-Castro and Donoho (first public preprint 2006) compared median and linear filtering through worst-case mean squared error and edge-preservation behavior, not this exact two-input cyclic-variation modulus. Previously established results for the pure three-point cyclic median identify its variation perturbation coefficient as three for cycles of at least six sites; setting \(\theta=0\) recovers that endpoint, but the known endpoint bound and convexity alone give only \(3-2\theta\), which cannot locate the nonexpansivity threshold. The new cancellation formula explicitly resolves the intervening weights.

## Limitations
This is not a claim that the convex-blended filter itself is newly invented, nor that it optimizes a statistical denoising risk. The exact phase law is proved only for three-point uniform windows on cycles with at least six sites. Smaller cycles, unequal window weights, different order statistics, open-boundary filters, multi-pass iteration, and higher-dimensional lattices are outside the statement. Older and unindexed literature may affect historical priority; the identified 2014 improved-hybrid paper could not be fully read and studies a differently specified filtering algorithm.

## References
1. A. Ben Hamza and H. Krim, *Nonlinear image filtering: trade-off between optimality and practicality*, Proceedings of ICIP, vol. 3, pp. 126–129 (2001), DOI: 10.1109/ICIP.2001.958067. Author-posted text: https://www.researchgate.net/publication/3919864_Nonlinear_image_filtering_trade-off_between_optimality_and_practicality
2. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, Annals of Statistics 37 (2009), 1172–1206. Original public arXiv submission dated 2006-12-14: https://arxiv.org/abs/math/0612422
3. T. K. Thivakaran and R. M. Chandrasekaran, *Nonlinear Filter Based Image Denoising Using AMF Approach* (2010), https://arxiv.org/abs/1003.1803
4. F. Jia, D. C. Xu and X. Fu, *An Improved Hybrid Median-Mean Filter Algorithm* (2014), DOI: 10.4028/www.scientific.net/AMM.701-702.288. Abstract consulted; full text was not available for comparison.
