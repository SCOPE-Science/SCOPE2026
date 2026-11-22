# Sharp four-moment recovery frontier for signed two-atom measures

## Finding
Let \(-1<a<b<1\) and \(\alpha,\beta>0\), and set \(\mu=\alpha\delta_a-\beta\delta_b\). Among all finite **real signed Borel measures** \(\nu\) on \([-1,1]\) having the four moments
\[
\int_{-1}^1 t^j\,d\nu(t)=\alpha a^j-\beta b^j,\qquad j=0,1,2,3,
\]
consider minimization of the total-variation norm \(\|\nu\|_{\mathrm{TV}}\). Then \(\mu\) is its **unique** minimizer if and only if
\[
\boxed{\ b-a\ge 1+\frac{|a+b|}{2}\ }.
\]
If the inequality fails, there is a feasible real signed measure with strictly smaller total variation than \(\alpha+\beta\). The criterion does not depend on either positive amplitude. On the transition frontier equality still gives uniqueness. In particular, for symmetric sites \(a=-s,b=s\), recovery holds exactly when \(s\ge1/2\); if the midpoint has magnitude greater than \(1/3\), no admissible two-atom placement with that midpoint can be recovered from four moments. For two independent uniform locations on \([-1,1]\) subsequently sorted, the exact proportion of location pairs satisfying the criterion is \(1/6\).

## Assumptions and scope
All measures are finite real signed Borel measures on the **closed** interval \([-1,1]\). The atoms \(a,b\) are strictly interior, distinct and ordered; both masses are nonzero with opposite signs, oriented positive at \(a\) and negative at \(b\). The observations comprise the ordinary monomial moments of degrees zero through three (equivalently, observations against any basis of the degree-at-most-three polynomial space). The optimization is over all signed measures, without an atomicity, sparsity, sign-count or support constraint.

## Proof
Set \(\Delta=b-a>0\), \(\ell=a+1>0\) and \(r=1-b>0\). The moment map from finite real measures to \(\mathbb R^4\) is continuous for the weak-star topology. Its image of the measure total-variation unit ball is compact, convex and symmetric; finite-dimensional gauge duality therefore gives the attained equality
\[
\inf_{A\nu=A\mu}\|\nu\|_{\mathrm{TV}}=
\max_{p\in\mathcal P_3,\ \|p\|_{\infty,[-1,1]}\le1}
\int p\,d\mu.
\]
Indeed, this follows directly by separating a point from a scaled copy of the compact moment image; a feasible primal minimizer exists by weak-star compactness. Consequently, \(\mu\) minimizes total variation precisely if there is a real polynomial \(p\) of degree at most three with \(\|p\|_\infty\le1\), \(p(a)=1\), and \(p(b)=-1\): since \(\alpha,\beta>0\), equality in \(\alpha p(a)-\beta p(b)\le\alpha+\beta\) forces both interpolation values.

Because \(a,b\) lie strictly inside the interval, each is a local extremum of a bounded interpolating polynomial, so \(p'(a)=p'(b)=0\). A polynomial of degree at most two could not satisfy these distinct critical-point conditions and the opposite values. For degree three, its derivative must be \(K(t-a)(t-b)\); normalization forces \(K=12/\Delta^3\). There is exactly one possible certificate:
\[
p_{a,b}(t)=1+\frac{12}{\Delta^3}\left(\frac{(t-a)^3}{3}-\frac{\Delta(t-a)^2}{2}\right).
\]
It increases on \([-1,a]\), decreases on \([a,b]\), and increases on \([b,1]\). Thus \(\|p_{a,b}\|_\infty\le1\) is equivalent to the two endpoint inequalities \(p_{a,b}(-1)\ge-1\) and \(p_{a,b}(1)\le1\). Direct exact factorization gives
\[
p_{a,b}(-1)+1=\frac{2(\Delta-2\ell)(\Delta+\ell)^2}{\Delta^3},\qquad
1-p_{a,b}(1)=\frac{2(\Delta-2r)(\Delta+r)^2}{\Delta^3}.
\]
Since the squared factors are strictly positive, the two endpoint tests reduce exactly to \(\Delta\ge 2\ell\) and \(\Delta\ge2r\). With \(c=(a+b)/2\), these become \(\Delta\ge1+|c|\). This proves necessity and sufficiency for optimality. When the criterion fails, finite-dimensional strong duality implies the optimum is strictly below \(\alpha+\beta\), and primal attainment supplies a strictly better competitor.

For uniqueness, let \(\nu\) be any minimizer with the same moments when the criterion holds. Equality in the certificate bound forces \(\nu\) to be supported on \(E=\{t:\lvert p_{a,b}(t)\rvert=1\}\). Strict monotonicity in each of the three open subintervals \((-1,a)\), \((a,b)\), \((b,1)\) shows \(E\subseteq\{-1,a,b,1\}\), even at either or both endpoint equalities. The monomial moment map through degree three is injective on signed measures supported on at most four distinct nodes (its Vandermonde matrix has full column rank). Hence \(\nu=\mu\).

For the location probability, set \(h=(b-a)/2\) and \(c=(a+b)/2\). Ordered interior sites satisfy \(0<h<1-|c|\), whereas recovery is equivalent to \(h\ge(1+|c|)/2\). The recovered region therefore has \(|c|\le1/3\), and the Jacobian of \((c,h)\mapsto(a,b)\) is two. Its area in the \((a,b)\) plane is
\[
\int_{-1/3}^{1/3}2\left(1-|c|-\frac{1+|c|}{2}\right)\,dc=\frac13.
\]
The ordered-pair region \(-1<a<b<1\) has area two, giving probability \((1/3)/2=1/6\). The frontier has zero area.

## Verification
The accompanying standalone `check_cubic.py` performs independent symbolic checks of the cubic interpolation, derivative and endpoint factorizations, classifies 253 ordered rational location pairs exactly, checks the Chebyshev boundary case \(p_{-1/2,1/2}(t)=4t^3-3t\), and uses optional finite-grid linear programming to probe feasible optimal and nonoptimal pairs. Successful checks do not replace the duality and uniqueness proof above; discrete grids are not exhaustive over arbitrary measures. Run from the embedded directory with `python check_cubic.py` (Python 3 with SymPy; SciPy and NumPy are optional for diagnostic LP tests).

## Relationship to prior work
De Castro and Gamboa (public preprint dated March 25, 2011) establish the generalized minimal-extrapolation and dual-polynomial framework for real signed measures and identify special Chebyshev-support families; that framework is used rather than claimed as new. Bendory, Dekel and Feuer (public preprint December 19, 2014) obtain a general high-degree sufficient separation condition for algebraic-polynomial moments, applicable only at degree at least 128. The present claim is specifically the **complete sharp necessary-and-sufficient location criterion at degree three for an oppositely signed interior pair**, with uniqueness at the endpoint-contact frontier, failure on its complement and exact phase-region area. This classification is not stated in the inspected primary sources; related general dual results motivate but do not by themselves give the explicit two-variable frontier.

## Limitations
The theorem is for real measures and exactly four moments; no statement is made about complex amplitudes, noisy stability, arbitrary numbers of atoms, degrees four and above, or unconstrained sparse inversion by Prony's method. Failure means failure of **total-variation minimization**, not non-identifiability within the restricted class of two-atomic measures. The certificate uses established gauge duality; the new calculation is the exhaustive cubic feasibility classification. A separately unindexed explicit formulation of this low-degree case remains possible, and independent assessment has not been performed.

## References
1. Y. de Castro and F. Gamboa, *Exact Reconstruction using Beurling Minimal Extrapolation*, first publicly posted March 25, 2011, arXiv:1103.4951, https://arxiv.org/abs/1103.4951 . Sections 1 and 3 were inspected, including generalized dual certificates and Chebyshev families.
2. T. Bendory, S. Dekel and A. Feuer, *Exact recovery of non-uniform splines from the projection onto spaces of algebraic polynomials*, first publicly posted December 19, 2014, arXiv:1412.6254, https://arxiv.org/abs/1412.6254 . Sections 1–3 were inspected, including the degree-128 separation hypotheses and dual interpolation principle.
3. E. J. Candès and C. Fernandez-Granda, *Towards a Mathematical Theory of Super-resolution*, https://arxiv.org/abs/1203.5871 . Background for bounded dual polynomials; not used to establish the sharp cubic location boundary.
