# Sharp John-ellipsoid saturation at a one-vertex simplex truncation

## Finding
Fix an integer \(n\ge2\) and real \(0<h\le n\). Define the truncated simplex
\[
K_{n,h}=\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad\sum_{i=1}^n x_i\le n,\quad x_1\le h\}.
\]
Set the residual barycentric coordinate vector \(y=(n-\sum_i x_i,x_2,\ldots,x_n)\in\mathbb R^n\), and its centered component \(u=y-\frac{n-x_1}{n}\mathbf1_n\), which belongs to \(\mathbf1_n^\perp\). Let
\[
\alpha=\frac n{n+1},\qquad h_*=\frac{2n}{n+1},\qquad \kappa_n=\frac{\pi^{n/2}}{\Gamma(n/2+1)}.
\]
The unique maximum-Euclidean-volume ellipsoid contained in \(K_{n,h}\) is
\[
E_{n,h}=\left\{x:\frac{(x_1-c)^2}{s^2}+\frac{\|u\|_2^2}{\rho^2}\le1\right\},
\]
with explicit parameters
\[
\boxed{(c,s,\rho^2)=\begin{cases}
(h/2,h/2,(n-h)/(n-1)),&0<h\le h_*,\\
(\alpha,\alpha,\alpha),&h_*\le h\le n.
\end{cases}}
\]
The parameter values agree at \(h=h_*\). Its ambient Euclidean volume equals
\[
\boxed{J_n(h)=\frac{\kappa_n}{\sqrt n}\,s\,\rho^{n-1}.}
\]
The function \(J_n\) increases strictly on \((0,h_*)\), equals the uncut-simplex John volume on \([h_*,n]\), and is \(C^1\) but not \(C^2\) at \(h_*\). Every original simplex facet is tangent throughout. The extra truncating hyperplane \(x_1=h\) is tangent exactly for \(h\le h_*\), where all \(n+2\) facets are in contact; it is strictly separated thereafter. At \(h=n\), that inequality is redundant.

In particular, the one-capped arbor polytope \(Q_{n,1}=K_{n,1}\) has \(c=s=1/2\), \(\rho^2=1\) and John volume \(\kappa_n/(2\sqrt n)\) in every dimension \(n\ge2\).

## Assumptions and scope
The parameter \(h\) measures the retained coordinate length along the vertex \(ne_1\). This is an \(n\)-dimensional convex body, and ellipsoid volume uses the standard Euclidean metric in the original \(x\)-coordinates. A purported ellipsoid expressed in \((x_1,u)\) coordinates must include the nonunit Jacobian when computing volume. No claim about general oblique truncations or multiple simultaneously capped vertices is made.

## Proof
**1. Affine symmetry and ellipsoid coordinates.** There are \(n\) residual barycentric coordinates \(y_j\), namely the slack \(n-\sum_i x_i\) and the \(n-1\) entries \(x_2,\ldots,x_n\). All are nonnegative and sum to \(n-x_1\). Each permutation of these \(n\) coordinates induces an affine symmetry of \(K_{n,h}\). The John ellipsoid of a full-dimensional convex body exists and is unique and is equivariant under invertible affine transformations. Thus the optimizer is invariant under the full permutation action. The representation splits into the fixed \(x_1\)-axis and the irreducible \((n-1)\)-dimensional standard representation \(\mathbf1_n^\perp\). An invariant ellipsoid consequently has center \((c,0)\) and separate circular radii \(s,\rho>0\) in these subspaces, with no mixed term; the displayed form \(E(c,s,\rho)\) is exhaustive.

**2. Exact support constraints.** For the ellipse \(E(c,s,\rho)\), the \(x_1\)-range is \([c-s,c+s]\), so the two end constraints are \(s\le c\) and \(s\le h-c\). Every residual coordinate has center \((n-c)/n\). Its linear-functional support radius satisfies
\[
\sup_{E(c,s,\rho)}\left|y_j-\frac{n-c}{n}\right|
=\sqrt{\frac{s^2}{n^2}+\frac{n-1}{n}\rho^2}.
\]
The equality follows by orthogonally projecting the \(j\)-th coordinate vector onto \(\mathbf1_n^\perp\), whose squared norm is \((n-1)/n\), and observing that the \(x_1\)-coefficient of \(y_j\) is \(-1/n\). Consequently, the ellipsoid lies in \(K_{n,h}\) if and only if
\[
0<s\le\min(c,h-c),\quad0<c<h,\quad
s^2+n(n-1)\rho^2\le(n-c)^2.\tag{1}
\]
All defining facets have been tested, so these conditions are both necessary and sufficient.

**3. Determinant and the complete constrained optimization.** Choose an orthonormal basis for the \(u\)-space and let its \(n-1\) coordinates be \(z\). The affine map \((x_1,z)\mapsto x\) has absolute Jacobian \(1/\sqrt n\): its \(z\)-columns are the last \(n-1\) coordinate restrictions of an orthonormal basis of the zero-sum hyperplane, with Gram determinant \(1/n\). The ellipse therefore has Euclidean volume \(\kappa_n s\rho^{n-1}/\sqrt n\). At a fixed center \(c\) and axial radius \(s\), maximizing volume forces equality in the last inequality of (1), leaving the scalar objective
\[
F(c,s)=s\big[(n-c)^2-s^2\big]^{(n-1)/2},\qquad0<s\le\min(c,h-c).
\]
Its unconstrained maximizing radius at fixed \(c\) is \(s=(n-c)/\sqrt n\). When \(0<h\le h_*=2n/(n+1)\), the inequality
\[
\min(c,h-c)\le\frac{n-c}{\sqrt n}\qquad(0<c<h)
\]
holds: for \(c\le h/2\) it follows from \(c\le h/2\le n/(1+\sqrt n)\), and for \(c\ge h/2\) its worst case is the same junction \(c=h/2\). Thus throughout this range the optimum \(s\) is \(\min(c,h-c)\).

For \(0<c\le h/2\), one has
\[
F(c,c)=c\,[n(n-2c)]^{(n-1)/2},\qquad
\frac{d}{dc}\log F(c,c)=\frac1c-\frac{n-1}{n-2c}>0
\]
because \(c\le h/2\le n/(n+1)\). For \(h/2\le c<h\),
\[
F(c,h-c)=(h-c)[(n-h)(n+h-2c)]^{(n-1)/2},
\]
whose logarithmic derivative is strictly negative. Hence the unique global maximizer has \(c=s=h/2\). Substituting in (1) gives
\[
\rho^2=\frac{(n-h/2)^2-(h/2)^2}{n(n-1)}=\frac{n-h}{n-1}.
\]
At \(h=h_*\) these values equal \((c,s,\rho^2)=(\alpha,\alpha,\alpha)\).

**4. Saturation above the threshold.** The original, untruncated simplex \(K_{n,n}\) has the standard John ellipsoid \(E(\alpha,\alpha,\sqrt\alpha)\), as follows either by the same one-variable support maximization with \(x_1\le n\) redundant or by affine equivalence to the regular simplex. The largest \(x_1\)-coordinate in that ellipsoid equals \(c+s=2\alpha=h_*\). Thus it is already contained in every \(K_{n,h}\) with \(h\ge h_*\). Any ellipsoid in the truncated body is also in the full simplex, so this feasible uncut-simplex John ellipsoid remains globally maximal. Uniqueness proves the second branch.

**5. Facet contacts and differentiability.** Equality \(s=c\) holds in both branches, so \(x_1=0\) always contacts. Equation (1) is active, so each of the \(n\) residual barycentric facets \(y_j=0\) contacts. For \(h\le h_*\), \(c+s=h\) and the extra facet contacts as well; for \(h>h_*\), \(c+s=h_*<h\). These exhaust the defining hyperplanes. On the first branch,
\[
J_n(h)=\frac{\kappa_n}{\sqrt n}\frac h2\left(\frac{n-h}{n-1}\right)^{(n-1)/2}.
\]
Its logarithmic derivative is \(1/h-(n-1)/(2(n-h))\), which is strictly positive before \(h_*\) and zero there. The constant second branch therefore has the same first derivative at the transition. The left logarithmic second derivative at \(h_*\) is strictly negative, namely \(-1/h_*^2-(n-1)/(2(n-h_*)^2)\), whereas the right second derivative is zero. Thus \(J_n\) is \(C^1\) but not \(C^2\) at that point.

## Verification
The accompanying standard-library script `verify.py` checks exact-rational halfspace radii, the asserted covariance values and the saturation match over dimensions and rational truncation depths, together with finite-grid comparisons of the constrained determinant; it reports `VERIFY_OK 118736 exact/finite assertions`. An additional independent numerical nonlinear optimization tested the full three-variable constraints on dimensions \(2\) through \(12\), with maximal parameter discrepancy approximately \(2.15\times10^{-11}\). These tests corroborate the all-dimensional analytic proof; finite sampling is not used as its proof.

## Relationship to prior work
The motivating arbor-polytope paper of Chapoton introduces geometrically natural simplex truncations. The later enumeration paper of Athanasiadis, Xiao and Yan writes the one-capped arbor family as \(Q_{n,1}\), with equations identical to those above for \(h=1\), and studies lattice enumeration rather than maximal inscribed ellipsoids. A published result on one-vertex truncated simplices determines their entire Godbersen mixed-volume profile, but mixed volumes of a body and its reflection do not determine the position or dimensions of its largest inscribed ellipsoid. A separate complete result on one-rank-capped hypercubes determines John ellipsoids of a different body with coordinate upper bounds on every variable; its three-phase behavior does not imply the two-branch simplex calculation. The present statement determines the sharp point at which a truncation ceases to affect a maximal inscribed ellipsoid, the exact volume profile, and all facets in contact. This is a specific exact Euclidean-geometric calculation, not a new general John theorem.

## Limitations
Only a single parallel vertex truncation of a simplex is treated. The result is affine invariant as a statement about John ellipsoids and normalized volume but the displayed explicit radii use fixed Euclidean coordinates. An old equivalent formula under simplex frustum, truncated cone, optimal-design, or inscribed-quadric terminology remains a historical-priority risk. The literature comparisons are necessarily incomplete and no independent audit has been performed.

## References
1. F. Chapoton, *On posets and polytopes attached to arbors*, arXiv:2503.04247v1 (first publicly submitted 2025-03-06), introductory definitions and arbor-polytope construction.
2. C. Athanasiadis, X. Xiao and J. Yan, *Lattice point enumeration of some arbor polytopes*, arXiv:2603.11654v1 (2026-03-12), introduction and construction of \(Q_{n,k}\), including \(Q_{n,1}\).
3. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* (2026-10-11), published mathematical record establishing opposite-body mixed volumes on an affinely equivalent truncated-simplex family, not John-ellipsoid parameters.
4. *Three-phase John ellipsoid of a capped hypercube* (2026-10-11), published mathematical record on cube-and-rank constraints, distinct from the present simplex frusta.
5. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant*, 1948, on maximal-volume inscribed ellipsoids and uniqueness.
