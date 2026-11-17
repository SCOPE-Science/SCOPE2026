# A universal half-Pareto incircle deficit in large random hyperbolic triangles

## Finding

**Theorem.** Work in the hyperbolic plane of constant curvature \(-1\). Independently sample three points uniformly by hyperbolic arclength on a geodesic circle of radius \(R>0\), and let \(r_R\) be the inradius of their geodesic triangle. Set \(r_*=\tfrac12\log 3\). Couple the triangles for different \(R\) by using the same three independent uniform polar angles. Starting at the **first labeled sampled vertex**, traverse the circle counterclockwise and let \(U,V,W\) be the three consecutive positive angular gaps divided by two, so \(U,V,W>0\) and \(U+V+W=\pi\). Define
\[
 Z_R=e^{2R}(r_*-r_R),\qquad
 Z=\frac13\bigl[(\cot U+\cot V)^2+(\cot V+\cot W)^2+(\cot W+\cot U)^2\bigr].
\]
Then \(r_R<r_*\) almost surely for each finite \(R\), and \(Z_R\to Z\) almost surely as \(R\to\infty\). In particular, the critical exponential scale is \(e^{-2R}\), and \(Z\) is finite and positive almost surely.

**Sharp tail and integrability.** The limiting variable has
\[
 \boxed{\lim_{t\to\infty}\sqrt t\,\Pr(Z>t)=\frac6\pi\sqrt{\frac23}.}
\]
For every real \(p>0\), its positive moment \(\mathbb E[Z^p]\) is finite if and only if \(p<\tfrac12\). This moment statement concerns the limiting variable and makes **no** claim about convergence of moments for the finite-radius variables.

**Marked rare-event geometry.** For each \(t>0\), let \(J\in\{1,2,3\}\) be the cyclic position of the smallest gap among \(U,V,W\) (ties have probability zero), and set
\[
 Q_t=\sqrt t\min\{U,V,W\},\qquad H_t=\frac{\text{gap immediately following the smallest gap in cyclic order}}\pi.
\]
Conditionally on \(Z>t\), the law of \((J,Q_t,H_t)\) converges in total variation, as \(t\to\infty\), to the independent product of a uniform index on \(\{1,2,3\}\), a uniform variable on \([0,\sqrt{2/3}]\), and a uniform variable on \([0,1]\).

## Assumptions and scope

The input is **exactly three** independent normalized-arclength-uniform points on a **single** centered geodesic circle in curvature \(-1\), not three volume-uniform points in its disk. Hyperbolic distances, incircles and geodesics are intrinsic. Polar angles are uniform because arclength on a fixed hyperbolic circle is a constant multiple of angle. Degenerate triangles and tied shortest gaps occur with probability zero. Conditional on the direction of the first sampled vertex, the other two relative polar directions are independent uniform angles. Their order statistics give the **anchored** gap vector a constant density \(2/\pi^2\) with respect to \(dU\,dV\) on \(U,V>0\), \(U+V<\pi\), with \(W=\pi-U-V\). For the marked theorem, the gap sequence **must** be anchored at the first labeled sampled vertex (or another uniformly chosen sampled vertex), not at the point with smallest absolute polar angle. The latter convention does not give a uniform Dirichlet law for a labeled gap vector. Relabeling the three vertices cyclically in a rotation-equivariant manner preserves the theorem. Limits in \(R\) hold at fixed sampled angles, while tail and marked limits in \(t\) refer to the **limit** random variable \(Z\). No uniform interchange of those two limits is asserted.

## Proof

**1. Exact hyperbolic inradius identity.** Let \(a,b,c>0\) be a nondegenerate hyperbolic triangle's side lengths and \(s=(a+b+c)/2\). Put \(x=s-a\), \(y=s-b\), \(z=s-c\). Hyperbolic half-angle trigonometry gives
\[
 \tan^2(A/2)=\frac{\sinh(s-b)\sinh(s-c)}{\sinh s\,\sinh(s-a)}.
\]
The right triangle at the incircle tangency point gives \(\tanh r=\sinh(s-a)\tan(A/2)\), so
\[
 \tanh^2r=\frac{\sinh x\sinh y\sinh z}{\sinh(x+y+z)}.
\]
Rewriting every hyperbolic sine exponentially yields the **exact** identity
\[
 \tanh r=\frac12\sqrt{\frac{(1-e^{-2x})(1-e^{-2y})(1-e^{-2z})}{1-e^{-2(x+y+z)}}}.
 \tag{1}
\]
All variables \(x,y,z\) are positive by the strict triangle inequality. The numerator in (1) is strictly smaller than its denominator: for \(0<A,B,C<1\), \((1-A)(1-B)(1-C)<1-ABC\), e.g. by multiplying inequalities \((1-A)(1-B)<1-AB\) and then the third factor. Thus \(\tanh r<1/2\), or \(r<\operatorname{artanh}(1/2)=\frac12\log3=r_*\). No geometric containment assumption concerning radial ideal triangles is used.

**2. Large-circle side expansion and fixed-configuration limit.** The hyperbolic cosine rule at the circle center gives, for a pair of vertices separated by polar angle \(2u\),
\[
 \sinh(d_R(2u)/2)=\sinh R\sin u,\qquad
 d_R(2u)=2R+2\log(\sin u)+o(1)
 \quad(R\to\infty)
\]
for fixed \(u\in(0,\pi)\). Assigning the three hyperbolic side lengths to half-gaps \(U,V,W\) in any order, their semiperimeter deficits obey
\[
 x=R+\log\frac{\sin V\sin W}{\sin U}+o(1),\quad
 y=R+\log\frac{\sin W\sin U}{\sin V}+o(1),\quad
 z=R+\log\frac{\sin U\sin V}{\sin W}+o(1).
\]
Hence
\[
 e^{2R}(e^{-2x},e^{-2y},e^{-2z})\to
 \left(\frac{\sin^2U}{\sin^2V\sin^2W},
 \frac{\sin^2V}{\sin^2W\sin^2U},
 \frac{\sin^2W}{\sin^2U\sin^2V}\right),
\]
while \(e^{-2(x+y+z)}=o(e^{-2R})\). Expanding (1) and using the derivative \((\operatorname{artanh})'(1/2)=4/3\) proves
\[
 e^{2R}(r_*-r_R)\to\frac13\left(
 \frac{\sin^2U}{\sin^2V\sin^2W}+
 \frac{\sin^2V}{\sin^2W\sin^2U}+
 \frac{\sin^2W}{\sin^2U\sin^2V}\right).
 \tag{2}
\]
Because \(U+V+W=\pi\), the identity \(\sin U=\sin(V+W)\) transforms each quotient into \((\cot V+\cot W)^2\), giving \(Z\). At least one such sum is nonzero, since three nonzero sine ratios appear in (2); thus \(Z>0\) almost surely.

**3. A globally valid small-gap restriction.** Put \(m=\min(U,V,W)\). Every gap belongs to \([m,\pi-2m]\), and \(|\cot v|\le 1/\min(v,\pi-v)\le 1/m\). Each of the three squared sums defining \(Z\) is at most \(4/m^2\), hence
\[
 Z\le 4/m^2. \tag{3}
\]
In particular, \(Z>t\) forces \(m<2/\sqrt t\). Such events occur only in shrinking neighborhoods of the three sides of the simplex. The regions where **two** gaps are simultaneously of order \(t^{-1/2}\) have probability \(O(t^{-1})\), negligible relative to the eventual leading \(t^{-1/2}\) probability.

**4. Boundary blow-up and the exact tail constant.** Partition by the unique shortest gap. On the chart where \(U\) is shortest, write \(U=q/\sqrt t\), \(V=\pi h\), \(W=\pi-\pi h-q/\sqrt t\). At each fixed \(q>0\), \(0<h<1\),
\[
 \frac{Z}{t}\to\frac{2}{3q^2},
 \qquad \mathbf 1_{\{Z>t\}}\to\mathbf1_{\{0<q<\sqrt{2/3}\}}.
 \tag{4}
\]
By (3), \(0<q<2\) on the event, regardless of \(t\). The density \(2/\pi^2\) in \(dU\,dV\) becomes \((2/\pi)dq\,dh/\sqrt t\). The shortest-gap chart additionally restricts \(V,W\ge U\); its indicator converges to one at each fixed \(0<h<1\). The integrands are bounded by the constant \(2/\pi\) on \((0,2)\times(0,1)\). Dominated convergence applied to (4) gives for this chart
\[
 \sqrt t\Pr(Z>t,\ J=1)\to \frac2\pi\sqrt{\frac23}.
\]
Cyclic symmetry multiplies this by three, proving \(C=(6/\pi)\sqrt{2/3}\). The pairwise small-gap corners are automatically negligible in this dominated-convergence calculation because they occupy a set with vanishing \(h\)-width.

**5. Total-variation conditional limit and moments.** On each shortest-gap chart the unnormalized density of \((q,h)\), multiplied by \(\sqrt t\), is precisely \((2/\pi)\mathbf1_{\{U\text{ shortest},\,Z>t\}}\) in the stated coordinates. Equation (4) and dominated convergence imply convergence in \(L^1(dq\,dh)\) to \((2/\pi)\mathbf1_{0<q<\sqrt{2/3},\,0<h<1}\). Divide by the total probability asymptotic and sum the three disjoint chart densities: this is total-variation convergence to the claimed product law, not merely weak convergence. Finally, for \(p>0\), the layer-cake formula \(\mathbb E[Z^p]=p\int_0^\infty t^{p-1}\Pr(Z>t)\,dt\), combined with the positive finite tail constant, gives finiteness exactly when \(p<1/2\).

## Verification

The self-contained script `check_hyperbolic_inradius.py` checks two separately implemented finite-radius inradius calculations: (i) hyperbolic side lengths and semiperimeter identity and (ii) Lorentz-model inward-normal equidistance. It then checks fixed-angle convergence against the exact cotangent expression, and estimates the tail coefficient and marked-law means through normalized-exponential simulation of the angular-gap simplex. Run with `python check_hyperbolic_inradius.py` after installing `numpy>=1.24`. Its fixed-seed test produced `HYPERBOLIC_INCIRCLE_PARETO_GEOMETRY_CHECK_OK`: predicted tail constant approximately \(1.55939360247\), observed \(1.55626153309\) for threshold \(6000\) from \(1{,}600{,}000\) simulated triangles; the observed conditional next-gap mean was \(0.50249\) versus the limit \(1/2\). Numerical tests support but cannot establish the infinite-radius limit, sharp tail, or total-variation assertions.

## Relationship to prior work

Classical hyperbolic triangle trigonometry supplies identity (1) and the universal ideal-triangle inradius; neither is claimed to be new. Brody and Schettler [1] study hyperbolic triangles with prescribed perimeters and inradii, but do not examine random radius-growing circumcircle samples or collision tails. Biró and Powers [2] analyze a different random-hyperbolic-triangle model (uniform intrinsic angles conditioned on their sum) and a strong triangle inequality. Available exact studies of acuteness of triangles sampled on a hyperbolic circle and of inradii for Euclidean cyclic triangles concern different observables or geometries. Published large-hyperbolic-ball **volume-uniform** triangle-area deficit results involve radial Pareto factors and do not imply this fixed-radius **arclength-uniform** incircle deficit and its angular-collision tail. The new assessed contribution is specifically the cotangent-law deficit, half-Pareto exponent with explicit constant and moment threshold, and marked total-variation rare-event geometry.

## Limitations

The result is restricted to dimension two, curvature \(-1\), three independent arclength-uniform points and a growing common circle radius. The limit random variable can have infinite mean even though each finite-radius deficit is bounded after rescaling; moment convergence is not proved. The conditional marked law is for \(Z>t\), not uniform over growing \(t\) and \(R\) simultaneously. Numerical verification is finite. Historical priority is provisional: the literature search is not exhaustive and a differently formulated earlier random-incircle law could contain an equivalent statement. Independent mathematical validation has not been carried out.

## References

1. N. Brody and J. Schettler, *Rational Hyperbolic Triangles and a Quartic Model of Elliptic Curves*, arXiv:1406.0467, first publicly posted 2014-06-02. https://arxiv.org/abs/1406.0467
2. C. Biró and R. C. Powers, *A strong triangle inequality in hyperbolic geometry*, arXiv:1507.04033, first publicly posted 2015-07-14. https://arxiv.org/abs/1507.04033
3. *Exact dilogarithmic acuteness law for random triangles on hyperbolic circles*, public research record (2026), concerning the same vertex-sampling model with a different statistic.
4. *The full inradius law and two contrasting tails of random cyclic triangles*, public research record (2026), concerning Euclidean cyclic triangles.
5. *Pareto limit law and sharp moment threshold for areas of large random hyperbolic triangles*, public research record (2026), concerning volume-uniform sampling and area deficits.
