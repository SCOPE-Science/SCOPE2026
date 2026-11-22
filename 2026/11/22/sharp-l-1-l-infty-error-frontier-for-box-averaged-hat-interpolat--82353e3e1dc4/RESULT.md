# Sharp \(L^1\)–\(L^\infty\) error frontier for box-averaged hat interpolation of BV functions

## Finding
Let \(h>0\), \(0<\alpha\le2\), and let \(T_{\alpha,h}\) be the real-line, uniform-grid, piecewise-affine reconstruction whose nodal values are centered box averages of width \(\alpha h\). The *best constants* in
\[
\|f-T_{\alpha,h}f\|_{L^1(\mathbb R)}\le h C_1(\alpha)\operatorname{Var}(f),\qquad
\|f-T_{\alpha,h}f\|_{L^\infty(\mathbb R)}\le C_\infty(\alpha)\operatorname{Var}(f)
\]
for all real \(f\in BV(\mathbb R)\) are
\[
C_1(\alpha)=\begin{cases}
\frac12,&0<\alpha\le\frac32,\\
1-\frac{3}{4\alpha},&\frac32\le\alpha\le2,
\end{cases}
\]
\[
C_\infty(\alpha)=\begin{cases}
1-\frac{\alpha}{2},&0<\alpha\le\frac23,\\
\frac12+\frac{(2-\alpha)^2}{16\alpha},&\frac23\le\alpha\le2.
\end{cases}
\]
Both constants are attained by single unit-jump functions. In particular, the unique bandwidth within this family minimizing sharp \(L^\infty\) error subject to the minimum possible sharp \(L^1\) error \(h\operatorname{Var}(f)/2\) is \(\alpha=3/2\), and its sharp \(L^\infty\) coefficient is \(49/96\). The family is variation diminishing for every such bandwidth and reproduces affine functions wherever locally defined.

## Assumptions and scope
Define the cardinal hat \(\phi(s)=\max\{1-|s|,0\}\) and, for each integer \(k\),
\[
A_k f=\frac1{\alpha h}\int_{(k-\alpha/2)h}^{(k+\alpha/2)h}f(y)\,dy,\qquad
T_{\alpha,h}f(x)=\sum_{k\in\mathbb Z}A_k f\,\phi(x/h-k).
\]
The sum is locally finite. Here \(BV(\mathbb R)\) denotes the homogeneous finite-variation class: locally integrable functions with \(|Df|(\mathbb R)<\infty\), without a global \(L^1\) requirement. Functions are identified up to Lebesgue-null sets, \(\operatorname{Var}(f)=|Df|(\mathbb R)\), and output norms are essential norms. A constant input is fixed by \(T_{\alpha,h}\). A step \(H_t(x)=\mathbf 1_{[t,\infty)}(x)\) has total variation one and gives integrable, compactly supported reconstruction error. No periodic, bounded-domain, nonuniform-grid or vector-valued assertion is made.

## Proof
**Reduction to a single jump.** Every real \(BV(\mathbb R)\) function has an a.e. representation \(f(x)=c+\int_{\mathbb R}H_t(x)\,d\mu(t)\), where \(\mu=Df\) is a finite signed measure with \(|\mu|(\mathbb R)=\operatorname{Var}(f)\). The reconstruction preserves constants. Linearity and Tonelli/Minkowski for the integrable compactly supported step errors yield, for either displayed target norm, an operator bound equal to at most the supremum of the corresponding norm of \(H_t-T_{\alpha,h}H_t\). Conversely every such step is admissible. It suffices therefore to calculate one translated unit jump. Dilation reduces to \(h=1\), and the uniform grid plus reflection symmetry reduce jump location to \(0\le t\le1/2\).

**Exact step profile.** Put \(W=\max\{0,\frac12-\frac t\alpha\}\) and \(Z=\min\{1,\frac12+\frac{1-t}{\alpha}\}\). Since \(0<\alpha\le2\), the nodal reconstruction of \(H_t\) is zero at all integer nodes \(\le-1\), is \(W\) and \(Z\) at nodes zero and one, and is one at every node \(\ge2\). Its linear pieces lie in \([-1,0]\), \([0,1]\), and \([1,2]\). Direct integration on the two sides of the jump gives
\[
E_1(t,\alpha)=\|H_t-T_{\alpha,1}H_t\|_1
=\frac{-2Wt^2+4Wt+2Zt^2-2Z-2t+3}{2}.
\]
The possible pieces of this expression for \(0\le t\le1/2\) are
\[
\begin{array}{c|c|c}
\text{regime}&E_1(t,\alpha)&\partial_t E_1(t,\alpha)\\\hline
W>0,\ Z=1&\frac{\alpha t^2+\alpha+2t^3-4t^2}{2\alpha}&\frac{t(\alpha+3t-4)}\alpha\\
W=0,\ Z=1&t^2-t+\frac12&2t-1\\
W>0,\ Z<1&1-\frac{1-t+t^2}{\alpha}&\frac{1-2t}{\alpha}
\end{array}
\]
In the range where each regime can occur, the first and second expressions decrease as \(t\) increases, and the third increases. Therefore the largest error is at \(t=0\) or \(t=1/2\). Their errors are respectively \(1/2\), and \(1/4\) for \(\alpha\le1\), or \(1-3/(4\alpha)\) for \(1\le\alpha\le2\). This proves the formula for \(C_1\), with a switching threshold exactly \(\alpha=3/2\). At the threshold both a knot jump and a half-cell jump attain equality.

**Uniform error.** The reconstructed step is nondecreasing. Its essential maximum difference from the step is \(\max\{U(t),1-U(t)\}\), where \(U(t)=T_{\alpha,1}H_t(t)=(1-t)W+tZ\). By reflection, for \(0\le t\le1/2\) one has \(U(t)\le1/2\). Where \(W>0,Z=1\),
\[
U(t)=\frac12+\frac t2-\frac{t-t^2}{\alpha},\qquad
\partial_t U(t)=\frac12-\frac1\alpha+\frac{2t}\alpha.
\]
Where \(W=0,Z=1\), \(U(t)=t\); where both nodal averages are interior, \(U(t)=1/2\). Consequently the minimum occurs at \(t=\alpha/2\) if \(0<\alpha\le2/3\), and at \(t=(2-\alpha)/4\) if \(2/3\le\alpha\le2\). Substitution gives precisely \(C_\infty\), including the limiting case \(\alpha=2\). These are explicit finite jump witnesses.

**Optimality and shape properties.** The formula for \(C_1\) shows that its minimum within \(0<\alpha\le2\) is \(1/2\), attained for the complete interval \(0<\alpha\le3/2\). The formula for \(C_\infty\) is strictly decreasing on \((0,2)\). Hence \(3/2\) is the unique minimizer of \(C_\infty\) among the bandwidths with minimum \(C_1\), with \(C_\infty(3/2)=49/96\). To see variation diminution, use
\[
A_{k+1}f-A_kf=\frac1{\alpha h}\int_{-\alpha h/2}^{\alpha h/2}\bigl[f((k+1)h+s)-f(kh+s)\bigr]\,ds
\]
and the fact that for each fixed \(s\), \(\sum_k|f((k+1)h+s)-f(kh+s)|\le\operatorname{Var}(f)\) for a suitable BV representative. Since the variation of a piecewise linear interpolant equals the total absolute variation of its nodal sequence, \(\operatorname{Var}(T_{\alpha,h}f)\le\operatorname{Var}(f)\). Centered averaging and linear interpolation reproduce every affine function (which is outside global \(BV(\mathbb R)\) except for constants, but is meaningful locally).

## Verification
The included `verify.py`, requiring only the Python standard library, independently constructs exact rational step reconstructions and integrates their absolute errors. It tests all rational bandwidths with denominator at most 32 and many rational phases (36,534 phase checks), verifies equality at predicted sharp jump locations, and checks 2,500 independently sampled finite signed-jump signals against both bounds and the variation-diminishing assertion. Its output is finite corroboration; the proof above establishes the infinite statement. Run `python3 verify.py` alongside this file.

## Relationship to prior work
Nochetto and Salgado's 2012 total-variation-diminishing Cartesian \(Q_1\) interpolant uses box averages and gives an \(L^1\) estimate with unspecified geometric constant; their stated setting is two-dimensional and does not establish a variable-width sharp \(L^1\)/\(L^\infty\) error frontier. Kristensen and Rindler's 2012 BV approximation theorem concerns adapted piecewise-affine approximations and trace control, rather than exact errors for this fixed uniform-grid reconstruction. Ern and Guermond's 2015 quasi-interpolation framework gives regularity-dependent estimates and a different projection construction, without the two sharp jump-error formulas. The structural contribution here is the full bandwidth phase diagram, with the \(2/3\) jump-location threshold and the \(3/2\) integrated-error threshold that identify a unique constrained shock-error design. Historical priority for equivalent unindexed formulations remains open.

## Limitations
The result is for a one-dimensional infinite uniform grid, scalar real data, the specific centered box average followed by the ordinary hat interpolant, and \(0<\alpha\le2\). No assertion is made for other kernels, larger widths, finite-domain boundary modifications, nonuniform meshes or higher dimensions. The optimality is **within the specified operator family**, not among all possible BV approximations or all TVD schemes. Exact constants for broader reconstruction classes may differ. Independent external validation has not occurred.

## References
1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069, first public version 2012-11-05, §§3–4. https://arxiv.org/abs/1211.1069
2. J. Kristensen and F. Rindler, *Piecewise affine approximations for functions of bounded variation*, arXiv:1211.1792, first public version 2012-11-08, Theorem 1 and §2. https://arxiv.org/abs/1211.1792
3. A. Ern and J.-L. Guermond, *Finite element quasi-interpolation and best approximation*, arXiv:1505.06931, first public version 2015-05-26, §§4–5. https://arxiv.org/abs/1505.06931
