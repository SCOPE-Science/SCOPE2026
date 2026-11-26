# Independent mathematical audit

## correctness

PASS

Peng et al. Eq. (3) has opposite sine coupling in the two signal coordinates and z'=z+x−y; at mu=0 its scalar map is identically q=k/log(3). Thus x'+y'=2q and, at h=1/2, (w',u')=(w−u,u cos w). Before crossing, strict amplitude order and reverse phase-deficit order follow because cos is positive and strictly decreasing on (0,1). Their phase gap increases after the first step. The set of amplitudes that reach a strictly negative w is open by finite-iterate continuity and upward by order, nonempty near u=w since w_2=w−u(1+cos w), and separated from zero by the geometric bound while w≥w_0/2. Hitting zero leads to a negative w the next step, so the boundary stays positive. If its limit were ell>0, take a finite iterate with w>3ell/4 and u<(ell/4)(1−cos(ell/2)); these are strict conditions preserved at the entry time under perturbation, and geometric tail loss keeps all those trajectories above ell/2, a contradiction. Smaller amplitudes keep at least the initial amplitude gap in w after time one, giving exponential decay; all larger amplitudes cross. This proves uniqueness for every stated initial w. For the threshold orbit summing u_j−u_(j+1) gives the upper rectangle sum for f(t)=1−cos t. Its error over [0,w] is at most (w/2) sum u_j²≤u w²/2, giving u=w³/6+O(w⁵). For quintic precision, each rectangle error is sin(w_j)u_j²/2+O(u_j³). The sum of the cubic errors is ≤u_n²w_n=O(w_n⁷); also sin(w_j)u_j=w_j⁴/6+O(w_j⁶) and the rectangle sum for t⁴ differs from w_n⁵/5 by at most 2w_n³ sum u_j²=O(w_n⁷). Thus the additional term is w⁵/60, yielding +w⁵/120 after adding w−sin w. Finally w_(n+1)^−2−w_n^−2→1/3 by u_n∼w_n³/6; Cesàro summation gives n w_n²→3 and n^(3/2)u_n→sqrt(3)/2. All estimates are for the specified pre-crossing sector only.

## originality

PASS

The map, gain slice and neutral multiplier are not the new result. Under inspected evidence the exact real positive-sector separation, uniform odd-power opening through order five and critical orbit constants survive the comparisons. This is best-of-knowledge only; two potentially related memristive-coupling papers were not available as inspected full texts.

## value

PASS

The slice is forced by an actual stability boundary: zero input gain leaves the coupled memory dynamics intact, and h=1/2 is exactly where the largest positive-phase transverse factor first reaches one. The result explains which trajectories converge before reaching that neutral phase, with a unique exceptional orbit and two explicit nonlinear scales. The quintic correction distinguishes the discrete threshold from its first integral approximation. This is more than substituting parameters in the source linearization and does not promise properties of later crossing dynamics or of nonzero gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
