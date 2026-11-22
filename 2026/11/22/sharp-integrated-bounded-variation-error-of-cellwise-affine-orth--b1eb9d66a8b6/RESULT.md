# Sharp integrated bounded-variation error of cellwise affine orthogonal projection

## Finding
Let \(a=x_0<x_1<\cdots<x_N=b\) be any finite partition of a real interval, with \(h=\max_i(x_i-x_{i-1})\). Let \(P_{\mathcal T}\) denote the unweighted cellwise \(L^2\)-orthogonal projection onto functions affine on each open cell, without continuity constraints across cell boundaries. Then the **sharp, attained** error seminorm is
\[
\sup_{f\in BV(a,b),\ |Df|(a,b)>0}
\frac{\|f-P_{\mathcal T}f\|_{L^1(a,b)}}{h\,|Df|(a,b)}
=\kappa
=\frac{t_*(6t_*^2-9t_*+4)^2}{6(1-t_*)}
=0.251497656507972\ldots,
\]
where \(t_*\) is the **unique root in** \((0,1/3)\) of
\[
24t^3-48t^2+27t-4=0,
\qquad t_*=0.234328086180391\ldots.
\]
For any longest cell, a unit step with its jump at relative position \(t_*\) or \(1-t_*\) attains the norm. For a step with a jump strictly inside one cell, these are the only two maximizing relative positions. In particular, the worst jump is **off centre**, and the constant depends on the mesh only through its longest cell. Both the full space of distributional \(BV\) inputs and one-cell single-jump extremizers are covered.

## Assumptions and scope
The interval is finite; all cells have positive length; \(N\ge1\). The input is a real \(L^1\)-equivalence class \(f\in BV(a,b)\), with distributional variation \(|Df|(a,b)\). No point values at mesh nodes are required. Since a one-dimensional \(BV\) input is bounded modulo constants, its cellwise \(L^2\) projection is well-defined. The \(L^1\) norm uses Lebesgue measure, and the projection uses unweighted Lebesgue \(L^2\). The estimate reads \(\|f-P_{\mathcal T}f\|_1\le\kappa h|Df|(a,b)\). No variation is artificially assigned at the endpoints \(a,b\). Jumps at interior mesh nodes lie in \(Df\) but contribute zero to the projection error because the piecewise constant step is reproduced exactly there.

## Proof
**Step reduction.** Fix a representative of \(f\) and put \(\mu=Df\), a finite signed Radon measure on \((a,b)\). Up to an additive constant and almost everywhere, \(f(x)=\int_{(a,b)}\mathbf1_{\{s<x\}}\,d\mu(s)\). The map \(P_{\mathcal T}-I\) annihilates constants and is bounded from \(L^1(a,b)\) to \(L^1(a,b)\) for each fixed finite mesh. Hence Fubini, the finite-dimensional moment formula for the projector, and the triangle inequality give
\[
\|f-P_{\mathcal T}f\|_1
\le\int_{(a,b)}\|H_s-P_{\mathcal T}H_s\|_1\,d|\mu|(s),
\qquad H_s(x)=\mathbf1_{\{s<x\}}.
\]
For a jump at a mesh node, the integrand is zero. For a jump in cell \(I_i=(x_{i-1},x_i)\) with relative coordinate \(t=(s-x_{i-1})/h_i\), the error vanishes outside \(I_i\) because constants are reproduced; after affine rescaling it equals \(h_i E(t)\), where \(E\) is the error for a unit jump at \(t\) on \((0,1)\). Consequently the sharp global coefficient is the maximum of \(E(t)\), multiplied by \(h\), provided the maximum is attained by a unit step.

**Local moment solution.** For \(0<t<1\), the projection of \(H_t\) onto \(\operatorname{span}\{1,x\}\subset L^2(0,1)\) is
\[
 g_t(x)=1-t+6t(1-t)(x-1/2),
\]
as follows from preservation of the zeroth and first moments. Therefore
\[
E(t)=\int_0^t|g_t(x)|\,dx+\int_t^1|g_t(x)-1|\,dx,
\qquad E(t)=E(1-t).
\]
It suffices to examine \(0\le t\le1/2\), with \(E(0)=0\). The sign-change point of \(g_t-1\) is \(r_t=(4-3t)/(6(1-t))\). For \(0<t\le1/3\), \(g_t\ge0\) on \([0,t]\), while \(g_t-1\) changes from negative to positive at \(r_t\in[t,1]\). Exact integration gives
\[
E(t)=\frac{t(6t^2-9t+4)^2}{6(1-t)},\qquad 0\le t\le1/3. \tag{1}
\]
For \(1/3\le t\le1/2\), \(g_t\) also crosses zero inside \([0,t]\), at \(v_t=(3t-1)/(6t)\), and \(g_t-1\) still crosses at \(r_t\). Integrating these four signed affine pieces gives
\[
E(t)=\frac{(2t^2-2t+1)(18t^4-36t^3+24t^2-6t+1)}{6t(1-t)}.
\tag{2}
\]
Both formulas equal \(25/108\) at \(t=1/3\). Equation (2) equals \(5/24\) at \(t=1/2\). The stated sign regions follow directly from \(g_t(0)=(1-t)(1-3t)\), \(g_t(t)=(1-t)(1-3t+6t^2)\in(0,1)\), and \(g_t(1)=1+t(2-3t)>1\) throughout the relevant ranges.

**Global maximum and uniqueness.** Differentiation of (1) yields
\[
 E'(t)=-\frac{(6t^2-9t+4)(24t^3-48t^2+27t-4)}{6(1-t)^2}.
\]
The first factor is strictly positive for all real \(t\). The cubic \(p(t)=24t^3-48t^2+27t-4\) increases strictly on \([0,1/3]\), since \(p'(t)=72t^2-96t+27\ge3\) on that interval, and \(p(0)=-4\), \(p(1/3)=5/9\). Therefore (1) has exactly one strict maximum, at the claimed root \(t_*\). Differentiation of (2) gives
\[
 E'(t)=-\frac{(2t-1)Q(t)}{6t^2(1-t)^2},
\quad Q(t)=72t^6-216t^5+246t^4-132t^3+30t^2-1.
\]
For \(t=1/2-u\), with \(0\le u\le1/6\),
\[
 Q(1/2-u)=\frac{288u^6-96u^4-6u^2-1}{4}<0,
\]
because \(288u^6\le8u^4\). Thus \(E'<0\) on \((1/3,1/2)\). Combining this with reflection gives precisely the two global maximizing jump positions \(t_*,1-t_*\), and establishes the universal upper bound by step reduction. A unit step on a longest cell realizes equality. The simple rational test \(E(1/4)=289/1152>1/4\) illustrates why a sharp constant cannot be replaced by \(1/4\).

## Verification
The accompanying `check_projection_error.py` evaluates the exact affine moments, the two rational error branches, their derivatives, the endpoint identities, and finite signed-step superpositions using standard-library rational arithmetic. It also brackets \(t_*\) and checks its numerical value by bisection. The infinite-dimensional upper bound, maximum uniqueness, and sharpness are proved analytically above; finite tests are corroboration, not an infinite proof.

## Relationship to prior work
Angermann and Henke, *Interpolation, projection and hierarchical bases in discontinuous Galerkin methods* (first public version 2011-02-15), define the local orthogonal projector and provide Sobolev-space error estimates, but their cited projection results do not state the exact operator error \(BV\to L^1\) or off-centre shock extremizers. Kristensen and Rindler, *Piecewise affine approximations for functions of bounded variation* (first public version 2012-11-08), construct adaptive piecewise-affine approximants with strict convergence and trace controls; those are not the fixed cellwise orthogonal projection here. Published work on Sobolev widths and endpoint norms of continuous spline projectors addresses distinct input norms, target norms or operators. An earlier exact result on the **variation of the projected output** for this same cellwise affine operator gives coefficients \(3/2,16/9,2\) depending on the number of cells; it does not imply the present error norm of \(I-P_{\mathcal T}\), which depends only on the longest cell. No historical-priority claim beyond these inspected comparisons is made.

## Limitations
This is a one-dimensional, unweighted, discontinuous degree-one orthogonal projector on a finite partition. The result is not a best nonlinear \(BV\) approximation theorem, does not classify every possible multijump extremizer, and supplies no result for continuous finite elements, higher polynomial degrees, weighted measures, or higher dimensions. A relevant historical result in a source not indexed by the completed searches could predate the formula. Exactness and novelty have not been independently audited.

## References
- L. Angermann and C. Henke, *Interpolation, projection and hierarchical bases in discontinuous Galerkin methods*, arXiv:1102.3100, first public version 2011-02-15, https://arxiv.org/abs/1102.3100 . Relevant material: local projection definition and estimates, Section 3.
- J. Kristensen and F. Rindler, *Piecewise affine approximations for functions of bounded variation*, arXiv:1211.1792, first public version 2012-11-08, https://arxiv.org/abs/1211.1792 . Relevant material: Theorem 1, Introduction, and approximation discussion.
