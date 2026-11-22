# Mesh-independent sharp \(BV\) variation gain of discontinuous affine \(L^2\) projection

## Finding

For every finite partition of an interval into \(N\ge1\) nondegenerate cells, let \(P_{\mathcal T}\) be the cellwise \(L^2\)-orthogonal projector onto the space of (possibly discontinuous) piecewise-affine functions. Its **exact** seminorm from one-dimensional \(BV\) to \(BV\), using the full distributional variation including interior-cell interface jumps, is
\[
\sup_{f\in BV(a,b),\;|Df|((a,b))>0}\frac{|D(P_{\mathcal T}f)|((a,b))}{|Df|((a,b))}
=\begin{cases}\frac32,&N=1,\\\frac{16}{9},&N=2,\\2,&N\ge3.\end{cases}
\]
Every constant is **attained by a single step**, independently of all cell lengths. The same constants hold for the two-input seminorm ratio \(\operatorname{Var}(P_{\mathcal T}f-P_{\mathcal T}g)/\operatorname{Var}(f-g)\), because the projector is linear.

## Assumptions and scope

Fix real \(a<b\), an integer \(N\ge1\), and strict knots \(a=x_0<x_1<\cdots <x_N=b\); the mesh need not be uniform. Define \(I_j=(x_{j-1},x_j)\) and
\[
\mathcal V_{\mathcal T}=\{v\in L^2(a,b):v|_{I_j}\text{ is affine for each }j\}.
\]
The map \(P_{\mathcal T}:L^2(a,b)\to\mathcal V_{\mathcal T}\) is the unique orthogonal projection, equivalently the independent least-squares affine fit on every cell. For a \(BV\) function, \(\operatorname{Var}(f)=|Df|((a,b))\) is the distributional Jordan total variation on the **open** interval. If \(v\in\mathcal V_{\mathcal T}\) has left and right traces \(L_j,R_j\) on cell \(I_j\), then
\[
\operatorname{Var}(v)=\sum_{j=1}^{N}|R_j-L_j|+\sum_{j=1}^{N-1}|L_{j+1}-R_j|.
\]
This definition counts interior mesh jumps and ignores artificial jumps between the boundary traces and values outside \((a,b)\). Variation is insensitive to additive constants, and \(P_{\mathcal T}\) preserves constants. All real \(BV(a,b)\) inputs belong to \(L^2(a,b)\).

## Proof

**Step 1: local projection of one jump.** Write \(H_s(x)={\bf1}_{(s,b)}(x)\). If \(s\in I_k\), set \(t=(s-x_{k-1})/(x_k-x_{k-1})\in(0,1)\). In the local coordinate \(u=(x-x_{k-1})/(x_k-x_{k-1})\), the projection of \({\bf1}_{(t,1)}(u)\) onto \(\operatorname{span}\{1,u\}\) has left and right traces
\[
A(t)=(1-t)(1-3t),\qquad B(t)=(1-t)(1+3t),
\]
from the two exact moment equations
\[
\int_0^1 p(u)\,du=1-t,\qquad \int_0^1u p(u)\,du=(1-t^2)/2.
\]
Its internal variation is \(B-A=6t(1-t)\ge0\). On preceding cells the projection is zero; on following cells it is one. In particular, no local length parameter enters these traces.

**Step 2: sharp one-jump profiles.** With just one cell, the total variation is \(6t(1-t)\le3/2\), with equality only at \(t=1/2\). For a jump in the first cell and at least one later cell, it equals
\[
V_{\rm edge}(t)=6t(1-t)+|1-B(t)|
=\begin{cases}8t-9t^2,&0<t\le2/3,\\4t-3t^2,&2/3\le t<1.\end{cases}
\]
The sharp maximum is \(16/9\) at \(t=4/9\); a jump in the last cell obeys the reflected formula. If the jump cell has both a preceding and a following cell, the total variation is
\[
V_{\rm inner}(t)=|A(t)|+6t(1-t)+|1-B(t)|
=\begin{cases}
1+4t-6t^2,&0<t\le1/3,\\
12t(1-t)-1,&1/3\le t\le2/3,\\
-1+8t-6t^2,&2/3\le t<1.
\end{cases}
\]
The outer branches have maxima \(5/3\), while the middle branch has unique maximum \(2\) at \(t=1/2\). A jump exactly at a mesh knot is already in \(\mathcal V_{\mathcal T}\) and has variation \(1\) after projection. Therefore the global sharp one-jump bound is \(3/2\) for \(N=1\), \(16/9\) for \(N=2\), and \(2\) for \(N\ge3\), using any interior cell for the final case.

**Step 3: arbitrary signed \(BV\) inputs.** For the signed Radon measure \(\mu=Df\), the standard one-dimensional jump representation, holding almost everywhere up to an additive constant, is
\[
f(x)=c+\int_{(a,b)}H_s(x)\,d\mu(s).
\]
As \(P_{\mathcal T}\) is linear, bounded on \(L^2\), and fixes constants, the projected integral is a finite-dimensional Bochner integral. By the triangle inequality for the full distributional-variation seminorm,
\[
\operatorname{Var}(P_{\mathcal T}f)
\le\int_{(a,b)}\operatorname{Var}(P_{\mathcal T}H_s)\,d|\mu|(s)
\le C_N|\mu|((a,b)).
\]
This proves the inequality for every real \(BV\) function, not merely a finite collection of jumps. The explicit step locations above give equality and establish exactness. Applying linearity to \(f-g\) gives the two-input version.

## Verification

A standalone standard-library Python checker, `verify_bv_broken_affine.py`, evaluates every local trace with rational arithmetic, checks exact local normal equations and sharp witnesses, scans \(1{,}790\) rational one-jump positions on both uniform and graded meshes, and tests \(2{,}400\) additional signed multijump inputs on nonuniform meshes of one through eight cells. Its expected terminal line is `ALL_SHARP_BV_BROKEN_AFFINE_PROJECTION_CHECKS_PASS`. These are supplementary finite checks; the universal result follows from the analytic three-step proof above. Run using `python3 verify_bv_broken_affine.py`.

## Relationship to prior work

Wang (2011) uses discontinuous first-degree Galerkin spaces and explicitly defines interface jumps for one-dimensional total-variation inpainting; it analyzes a coupled penalized differential-equation scheme, not the uncoupled cellwise \(L^2\) orthoprojector or its sharp \(BV\) norm. Nochetto and Salgado (2012) construct a continuous \(Q_1\) total-variation-diminishing interpolation operator, with a different definition and an upper coefficient of one rather than the above sharp discontinuous-projection coefficients. Herrmann and coauthors (2018) analyze total-variation functionals for globally discontinuous elements, but their discrete-TV and optimization results do not give the present exact cell-count transition. Bartels (2012) considers TV-minimization methods involving continuous affine and piecewise constant finite elements, not this projector. The distinct treatment of mesh-interface jumps is essential; omitting them would give another norm.

## Limitations

The result is one-dimensional and concerns the **cellwise** \(L^2\) projection onto **discontinuous** affine elements, not a continuous spline orthoprojector, not a DG elliptic solution operator, and not a projection preserving prescribed boundary values. It uses unweighted arclength measure for least squares and the full (interior jump-inclusive) distributional variation. The result does not claim higher-degree, multidimensional or weighted-measure constants. The literature comparison cannot exclude every unindexed historical equivalent, and independent verification is not claimed.

## References

1. X. Wang, *Discontinuous Galerkin Method for Total Variation Minimization on one-dimensional Inpainting Problem*, arXiv:1107.3903v1, 20 July 2011. https://arxiv.org/abs/1107.3903
2. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, 5 November 2012. https://arxiv.org/abs/1211.1069
3. M. Herrmann, R. Herzog, S. Schmidt, J. Vidal-Núñez and G. Wachsmuth, *Discrete Total Variation with Finite Elements and Applications to Imaging*, arXiv:1804.07477, 20 April 2018. https://arxiv.org/abs/1804.07477
4. S. Bartels, *Total Variation Minimization with Finite Elements: Convergence and Iterative Solution*, SIAM J. Numer. Anal. 50 (2012), 1162–1180. https://doi.org/10.1137/11083277X
