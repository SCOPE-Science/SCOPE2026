# Sharp quadrant and distribution-function total-positivity transitions in geometric–FGM copulas

## Finding
Fix a geometric parameter \(0<p\le1\), write \(q=1-p\), and let \(-1\le\theta\le1\). For the Farlie–Gumbel–Morgenstern (FGM) copula \(C_\theta(x,y)=xy[1+\theta(1-x)(1-y)]\), let \(g_p(s)=ps/(1-qs)\) be the geometric probability-generating function and define its geometric-PGF transform
\[
K_{p,\theta}(u,v)=g_p\big(C_\theta(g_p^{-1}(u),g_p^{-1}(v))\big).
\]
This is the geometric–FGM copula family. Its *exact global dependence phase diagram* is as follows:

1. Positive quadrant dependence (PQD), meaning \(K_{p,\theta}(u,v)\ge uv\) for every \(u,v\), holds **if and only if** \(\theta\ge-(1-p)\).
2. Negative quadrant dependence (NQD), meaning the reverse pointwise inequality, holds **if and only if** \(\theta\le-(1-p)/p\).
3. When \(\theta=-t\), with \(0<t\le1\), a genuine neither-PQD-nor-NQD region exists **if and only if**
\[
1-t<p<\frac1{1+t}.
\]
The interval has exact width \(t^2/(1+t)\). Inside it the dependence discrepancy changes sign *once* as a function of the joint lower-tail coordinate \(z=(1-x)(1-y)\), where \(x=g_p^{-1}(u)\), \(y=g_p^{-1}(v)\): its zero contour is \(z=z_*=(q+p\theta)/(-q\theta)\), with a negative discrepancy above \(z_*\) and a positive one below.

Moreover, the *copula distribution function*, not necessarily its density, is totally positive of order two (CDF-TP\(2\)) **if and only if** either \(\theta\ge0\), or \(-1<\theta<0\) and
\[
\boxed{(1-p)(1+\theta)^3\ge-\theta.}
\]
Writing \(t=-\theta\in(0,1)\), a positive geometric parameter satisfying CDF-TP\(2\) exists precisely for \(t<t_*\), where \(t_*\) is the unique root of \((1-t)^3=t\) in \((0,1)\), numerically \(t_*\approx0.31767219617198067\). For such \(t\), the exact range is \(0<p\le1-t/(1-t)^3\), strictly smaller than the PQD range \(0<p\le1-t\). Thus geometric compounding can turn an FGM copula with *negative* dependence into one with CDF-TP\(2\), while also producing a distinct PQD-but-not-TP\(2\) region.

## Assumptions and scope
The sample space is \([0,1]^2\). The baseline FGM parameter satisfies \(-1\le\theta\le1\), ensuring a genuine copula; \(0<p\le1\), with \(p=1\) corresponding to no compounding. All comparisons concern the fully transformed copula, with pointwise inequalities on the entire closed square; strict claims concern its interior. The geometric PGF here is \(ps/(1-(1-p)s)\), corresponding to a count on \(\{1,2,\ldots\}\). The inverse map is \(g_p^{-1}(u)=u/(p+qu)\). CDF-TP\(2\) means \(K(u_1,v_1)K(u_2,v_2)\ge K(u_1,v_2)K(u_2,v_1)\) whenever \(u_1\le u_2\), \(v_1\le v_2\); it is **not** the distinct property of total positivity of its copula density.

## Proof
Because \(g_p\) is an increasing bijection of \([0,1]\), write \(x=g_p^{-1}(u)\), \(y=g_p^{-1}(v)\), \(z=(1-x)(1-y)\), and \(F=xy(1+\theta z)\). Then \(u=g_p(x)\), \(v=g_p(y)\). Straight rational common-denominator calculation gives the exact identity
\[
\boxed{K_{p,\theta}(u,v)-uv=\frac{p\,xy\,z\,[q+p\theta+q\theta z]}{(1-qF)(1-qx)(1-qy)}.}
\]
All denominators are positive for \(0<p\le1\); the numerator factor \(p xyz\) is positive in the interior. Thus its sign equals that of the affine function \(L(z)=q+p\theta+q\theta z\), where \(0<z<1\). If \(\theta\ge0\), both endpoints \(L(0)=q+p\theta\) and \(L(1)=q+\theta\) are nonnegative, so PQD. If \(\theta=-t<0\), \(L\) decreases, and \(L(1)=q-t\), \(L(0)=q-pt\). Hence PQD exactly when \(q\ge t\), i.e. \(p\le1-t\), and NQD exactly when \(q\le pt\), i.e. \(p\ge1/(1+t)\). Equality cases are included by continuity; at \(p=1,\theta=0\), the product copula is both. The two thresholds are strictly ordered when \(t>0\), with difference \(t^2/(1+t)\). Between them, \(L(0)>0>L(1)\), so the unique sign-change coordinate is \(z_*=L(0)/(qt)\in(0,1)\), with the stated orientation. Each \(z\in(0,1)\) is attained by an interior pair, so this proves necessity as well as sufficiency. When \(t=1\), the PQD region is empty for admissible \(p>0\); the same general formulas still hold.

For the stronger CDF-TP\(2\) result, strictly increasing marginal changes of variables preserve multiplicative TP\(2\) inequalities. It therefore suffices to test the positive function \(T(x,y)=g_p(F(x,y))\) on the open square. For any positive twice continuously differentiable function, TP\(2\) on a rectangle is equivalent to \(\partial_{xy}\log T\ge0\) throughout its interior, by integration over all subrectangles. Set \(A=1+\theta z\), and
\[
B=A(1-\theta+2\theta z)+2\theta^2 xyz.
\]
Exact differentiation and simplification yield
\[
T\,T_{xy}-T_xT_y
=\frac{p^2x^2y^2}{(1-qF)^4}[\theta+qAB].
\]
For \(\theta\ge0\), one has \(A\ge1\), \(1-\theta+2\theta z\ge0\) for \(\theta\in[0,1]\), so \(B\ge0\), proving CDF-TP\(2\). For \(\theta=-t<0\), let \(0<t\le1\). The factors satisfy \(A=1-tz\ge1-t\) and
\[
B=(1-tz)(1+t-2tz)+2t^2xyz\ge(1-t)^2;
\]
indeed \(1+t-2tz\ge1-t\) and the remainder is nonnegative. It follows that \(AB\ge(1-t)^3\), and this lower bound is **sharp** as \(x,y\downarrow0\) (then \(z\uparrow1\) and \(xy\downarrow0\)). Therefore \(\theta+qAB\ge0\) everywhere if \(q(1-t)^3\ge t\). Conversely, if \(q(1-t)^3<t\), continuity produces an interior region near the origin with negative mixed log derivative, violating TP\(2\) on sufficiently small subrectangles. This proves the necessary-and-sufficient inequality, including the nonattainable \(t=1\) case.

For \(0<t<1\), rearranging gives \(p\le1-t/(1-t)^3\). Such a positive \(p\) exists exactly when \((1-t)^3>t\); the strictly decreasing function \((1-t)^3-t\) has one zero in \((0,1)\). Also \(t/(1-t)^3>t\), so the TP\(2\) range is strictly smaller than the PQD range. This completes the classification.

## Verification
Run `python verify.py` with SymPy installed. The standalone exact-arithmetic checker independently reconstructs the geometric inverse, the complete PQD factorization, the mixed-log-derivative numerator, sharp boundary identities and the exact sign classification. For \(\theta=-1/8\) it certifies all four regimes at \(p=3/4\) (CDF-TP\(2\)), \(17/20\) (PQD but not CDF-TP\(2\)), \(22/25\) (neither), and \(9/10\) (NQD). It separately tests three rational cases with \(\theta=-1/2\). Finite-grid checks are auxiliary diagnostics, not the proof of whole-domain inequalities, which follows analytically above.

## Relationship to prior work
Zachariah, Arshad and Pathak (2024) introduced the probability-generating-function copula transform and the specific geometric–FGM family, and studied concordance and various dependence preservation properties. Their results include preservation of PQD for PQD baselines and preservation of CDF-TP\(2\) for CDF-TP\(2\) baselines. The originating paper's full journal PDF was not accessible; the author's publicly available 2025 thesis reproduces the substantive chapter, including the exact geometric–FGM formula, preservation propositions and related numerical examples, which were inspected. **These existing results do not imply** the sharp converse thresholds for a *negative* FGM baseline, the neither-PQD-nor-NQD region, or recovery of CDF-TP\(2\) from a baseline without it. Alhadlaq and Alzaid (2020) provided an earlier PGF–copula construction framework, but not this two-parameter phase diagram. The distinction between CDF-TP\(2\) and density-TP\(2\) is critical; no density-TP\(2\) assertion is made here. The exact comparison therefore concerns a known family but new necessary-and-sufficient structure, not a claim of inventing the transformation.

## Limitations
The result is confined to the geometric transform of the one-parameter FGM copula, not arbitrary PGFs or baseline copulas. The CDF-TP\(2\) phase diagram does not establish the stronger density-TP\(2\) property. The research record search and author-thesis inspection cannot guarantee historical uniqueness, and institutional access to the original journal full PDF was not available. The supplied symbolic checker verifies critical identities but does not replace the continuum proof. Independent external mathematical validation has not been performed.

## References
1. S. G. Zachariah, M. Arshad and A. K. Pathak, *A new family of copulas based on probability generating functions*, Mathematica Slovaca 74 (2024), 1039–1060, https://doi.org/10.1515/ms-2024-0076 (publisher listing: 14 August 2024).
2. S. G. Zachariah, *Dependence and Uncertainty*, 2025 doctoral thesis, Chapter 3, publicly available at https://dspace.iiti.ac.in/bitstream/123456789/16598/1/TH_745_Swaroop_Georgy_Zachariah_2001241009.pdf.
3. W. Alhadlaq and A. Alzaid, *Distribution Function, Probability Generating Function and Archimedean Generator*, Symmetry 12 (2020), 2108, https://doi.org/10.3390/sym12122108.
4. S. Fuchs and M. Tschimpke, *A novel positive dependence property and its impact on a popular class of concordance measures*, Journal of Multivariate Analysis (2024), https://doi.org/10.1016/j.jmva.2023.105259.
