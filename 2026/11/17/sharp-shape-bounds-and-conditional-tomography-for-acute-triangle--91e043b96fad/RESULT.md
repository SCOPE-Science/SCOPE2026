# Sharp shape bounds and conditional tomography for acute triangles on collapsing convex lenses

## Finding

Let \(h:[-1,1]\to[0,\infty)\) be Lipschitz and concave, with \(h(-1)=h(1)=0\) and \(h(x)>0\) for \(-1<x<1\). For each \(\varepsilon>0\), set
\[
K_\varepsilon=\{(x,y):-1\le x\le1,\ |y|\le\varepsilon h(x)\}.
\]
Take three independent points uniformly by **Euclidean arclength** on the full boundary \(\partial K_\varepsilon\), and let \(A_\varepsilon\) denote the event that their Euclidean triangle is strictly acute. Write
\[
B=\int_{-1}^{1}h(x)\,dx,\qquad Q=\int_{-1}^{1}h(x)^2\,dx.
\]
Then
\[
\boxed{\Pr(A_\varepsilon)=\frac32 Q\,\varepsilon^2\log(1/\varepsilon)+o_h(\varepsilon^2\log(1/\varepsilon)).}
\]
The sharp fixed-\(B\) envelope is
\[
\boxed{\frac34 B^2<\frac32Q\le B^2.}
\]
The upper equality holds precisely for triangular-tent height profiles (a concave function affine on each side of a single maximum); the lower bound is not attained but is approached by profiles with long nearly flat plateaus and increasingly short linear tip ramps. Neither bound is a finite-\(\varepsilon\) probability inequality.

Sort the sampled points by their horizontal positions \(X_1<X_2<X_3\). Put \(X=X_2\), \(U=X_2-X_1\), \(V=X_3-X_2\), and \(S=\operatorname{sgn}(Y_2)\). On the acute event define
\[
T_\varepsilon=\frac{\log U}{\log\varepsilon},\qquad W_\varepsilon=\frac{UV}{4\varepsilon^2h(X)^2}.
\]
The **joint conditional distribution**, in total variation, converges to independent variables with laws
\[
\boxed{X\sim h(x)^2\,dx/Q,\qquad T\sim\operatorname{Uniform}(0,2),\qquad W\sim\operatorname{Uniform}(0,1),\qquad S\sim\operatorname{Uniform}\{-1,1\}.}
\]
In particular the full rare-event location law determines \(h\) up to a positive multiplicative factor, and its probability coefficient supplies that factor: if \(\rho\) is the limiting density of \(X\), and \(C=\lim\Pr(A_\varepsilon)/(\varepsilon^2\log(1/\varepsilon))\), then \(h(x)=\sqrt{(2C/3)\rho(x)}\).

For the parabolic lens \(h(x)=1-x^2\), \(B=4/3\), \(Q=16/15\), and hence
\[
\Pr(A_\varepsilon)\sim\frac85\varepsilon^2\log(1/\varepsilon),\qquad\rho(x)=\frac{15}{16}(1-x^2)^2.
\]

## Assumptions and scope

The curves are the two graphs \(y=\pm\varepsilon h(x)\). The Lipschitz assumption ensures that normalized boundary arclength has a bounded horizontal density and that no additional vertical edge carries positive arclength at the tips. All limits hold for each **fixed** admissible \(h\); no uniform error over profiles is claimed. Strictly acute means all three Euclidean vertex angles are strictly less than \(\pi/2\); zero-area and right-angle coincidences, except impossible same-branch cases, occur with probability zero. We do not include unbounded-slope profiles such as a vertically compressed ellipse in the theorem. The parameter \(B\) is the uncompressed profile integral, and the actual lens area is \(2\varepsilon B\).

## Proof

**1. Exact arclength coordinates.** Write \(H=\max h>0\) and \(L=\operatorname{Lip}(h)<\infty\). A boundary sample is \((X,\varepsilon\Sigma h(X))\), where \(\Sigma\) is a fair, independent sign and the horizontal density is
\[
f_\varepsilon(x)=\frac{\sqrt{1+\varepsilon^2h'(x)^2}}{J_\varepsilon},\qquad J_\varepsilon=\int_{-1}^1\sqrt{1+\varepsilon^2h'(z)^2}\,dz.
\]
The derivative exists almost everywhere; modifying it on a null set is harmless. Uniformly almost everywhere, \(f_\varepsilon(x)=1/2+O_h(\varepsilon^2)\). After sorting three independent horizontal coordinates the density is \(6 f_\varepsilon(x-u)f_\varepsilon(x)f_\varepsilon(x+v)\,dx\,du\,dv\), on \(u,v>0\) with \(x-u,x+v\in[-1,1]\). The sorted signs remain independent fair signs.

**2. Acute-angle tests and sign classes.** For the sorted vertices \(P_1,P_2,P_3\), the middle vertex's dot product is
\[
(P_1-P_2)\cdot(P_3-P_2)=-uv+\varepsilon^2(\sigma_1h(x-u)-\sigma_2h(x))(\sigma_3h(x+v)-\sigma_2h(x)).
\]
If all three signs agree this expression is negative whenever \(\varepsilon L<1\), because the second term is bounded in absolute value by \(\varepsilon^2L^2uv\). If exactly one adjacent sign agrees with the middle sign, the middle-angle condition forces the gap to the opposite-sign endpoint to be at most \(2HL\varepsilon^2\). Integrating that bounded-width strip in the bounded \((x,u,v)\) parameter box gives total probability \(O_h(\varepsilon^2)\). Thus, up to that error, acute triangles require \(\sigma_1=\sigma_3=-\sigma_2\), two of the eight equally likely sign patterns.

For those two sign patterns the exact middle-angle inequality becomes
\[
uv<\varepsilon^2\,[h(x-u)+h(x)]\,[h(x+v)+h(x)].\tag{1}
\]
The other two vertex dot products are bounded below by \(u(u+v)-2HL\varepsilon^2(u+v)\) and \(v(u+v)-2HL\varepsilon^2(u+v)\), respectively. Hence both are positive once \(u,v>2HL\varepsilon^2\), and the part where either gap is at most this threshold contributes only \(O_h(\varepsilon^2)\). The right-angle boundary has measure zero.

**3. Logarithmic area lemma.** For a fixed \(x\in(-1,1)\) the area of \((u,v)\) satisfying (1), its geometric domain conditions, and the two other acute tests is
\[
8h(x)^2\varepsilon^2\log(1/\varepsilon)+o_x(\varepsilon^2\log(1/\varepsilon)).\tag{2}
\]
To prove (2), choose any \(0<\delta<1\). In the logarithmic bulk \(\varepsilon^{2-\delta}\le u\le\varepsilon^\delta\), the inequality (1) restricts \(v\) to order \(\varepsilon^2/u\), so uniformly in that bulk, \(u,v\to0\); consequently the right-hand factor is \(4h(x)^2+o_x(1)\). Both outer angle tests are automatically positive. The bulk integral is
\[
\bigl[4h(x)^2+o_x(1)\bigr]\varepsilon^2(2-2\delta)\log(1/\varepsilon).
\]
Outside this bulk, the global bound \(uv\le4H^2\varepsilon^2\) shows that the logarithmically normalized excluded area is at most a constant times \(\delta\) (with an additional \(O_h(\varepsilon^2)\) contribution at the ends \(u\asymp\varepsilon^2\) and \(u\asymp1\)). Letting \(\delta\downarrow0\) proves (2). The same global product bound controls the area at every \(x\), by \(O_h(\varepsilon^2[1+\log(1/\varepsilon)])\), so dominated convergence allows integration of (2) over \(x\in[-1,1]\).

**4. Probability constant.** The sign probability in step 2 is \(2/8=1/4\); combining it with the sorted-coordinate factor 6, the marginal limit \(f_\varepsilon^3\to1/8\), and (2), yields
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(A_\varepsilon)}{\varepsilon^2\log(1/\varepsilon)}
=\frac64\cdot\frac18\int_{-1}^1 8h(x)^2\,dx=\frac32Q.
\]
The other sign patterns and the short-gap exceptions are of lower order, as shown above.

**5. Joint marked limit in total variation.** In the two contributing sign patterns use the exact change of variables
\[
u=\varepsilon^t,\quad v=4\varepsilon^2h(x)^2w/u,\quad \left|\frac{\partial(u,v)}{\partial(t,w)}\right|=4\varepsilon^2h(x)^2\log(1/\varepsilon).
\]
For each fixed interior \(x\), each \(0<t<2\) and \(w>0\), the transformed acute-event indicator tends to \(\mathbf 1_{0<w<1}\), while the boundary densities tend to \(1/2\). On each compact set where \(x\) stays away from the tips and \(t\) stays away from 0 and 2, the limiting density convergence holds in \(L^1\), including the \(w\)-coordinate (which is bounded there by (1)). The global hyperbolic-area bound in step 3 controls the discarded \(x\)-tip strips and the \(t\)-endpoint strips; their normalized masses vanish as the strips shrink. Thus the transformed *unnormalized* finite measures converge in \(L^1\) to the measure with density proportional to \(h(x)^2\mathbf1_{0<t<2}\mathbf1_{0<w<1}\) and equal mass on the two signs. Division by their converging positive total mass proves total-variation convergence to the product law stated above. The reconstruction formula follows by squaring \(\rho=h^2/Q\) and using \(C=3Q/2\).

**6. Sharp width/area envelope.** Jensen's inequality over an interval of length two gives \(Q\ge B^2/2\), with equality only for a.e. constant \(h\). That is impossible here because continuous \(h\) vanishes at both endpoints and is positive inside, so the lower inequality is strict. The classical one-dimensional Berwald inequality for nonnegative concave functions gives
\[
\left(\frac32Q\right)^{1/2}\le B,
\]
so \(Q\le2B^2/3\). Equality in the one-dimensional Berwald comparison holds for concave tent profiles, and a direct calculation for a tent of height \(B\) proves the sharp value \(Q=2B^2/3\). Conversely equality entails the tent form in this nondegenerate setting. To approach the lower bound, take a plateau of height tending to \(B/2\) with two symmetric, linearly descending tip ramps of width tending to zero, normalized to retain integral \(B\). These are admissible profiles and have \(Q\to B^2/2\). This completes both strictness and sharpness. \(\square\)

## Verification

The included standalone Python checker `verify.py` uses independent seeded Monte Carlo sampling, with exact Euclidean-angle tests after sorting. Horizontal proposals are uniform, then importance-weighted by the exact arclength Jacobian; the latter is normalized by Gauss–Legendre quadrature. For \(\varepsilon=0.02\) and three million trials per shape, the parabolic lens produced probability \(0.00246539\) versus the leading value \(0.00250369\); the symmetric tent produced \(0.001631\) versus leading \(0.00156481\). The checker also records dominance of the opposite-middle-branch sign class. These are finite diagnostics only, not proofs of limits, sharpness, or total variation. Running `python verify.py` requires NumPy; the accompanying dependency file records the requirement.

## Relationship to prior work

The fixed thin-ellipse perimeter-sampled acute-triangle law already provides the special value \(2\varepsilon^2\log(1/\varepsilon)\) and a marked law for the ellipse height \(h(x)=\sqrt{1-x^2}\), whose endpoint slope is unbounded. Its special coefficient and marks are **not** claimed as new. The new claim concerns all Lipschitz concave lens profiles, a sharp optimization envelope over those profiles, and complete height recovery from a conditional one-coordinate law plus event rate. The prior ellipse statement neither quantifies arbitrary profiles nor implies the family-wide sharp extremizers. Related literature establishes the logarithmic acuteness law for thin rectangular boundaries and a different fifth-chord-moment coefficient under **area-uniform interior** sampling; neither covers this perimeter-sampled concave-lens classification. Edelman and Strang's general shape-theoretic treatment of random triangles studies Gaussian and other shape distributions, not the present thin-lens sampling. Classical Jensen and Berwald inequalities are used, not attributed as new results.

## Limitations

Only the leading logarithmic term is determined; no uniform remainder across lenses, second asymptotic coefficient, or convergence rate in total variation is proved. Profiles with unbounded slopes (including ellipses) require separate analysis. The extremal inequalities concern the *leading coefficient* for fixed \(B\), not finite-thickness stochastic ordering. The earlier thin-ellipse example employs a closely related logarithmic change of variables; the novelty of this extension and its broad inverse/optimization statement remains subject to independent historical review. Numerical evidence is illustrative and is not a substitute for the proof.

## References

1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, first posted 2015-01-09, arXiv:1501.03053. Complete open text inspected; primarily Gaussian and shape-space sampling.
2. G. R. Hall, *Acute triangles in the n-ball*, *Journal of Applied Probability* **19** (1982), 712–715, DOI: 10.2307/3213533. The publisher abstract concerns interior-uniform points; full paper not read.
3. *A logarithmic acute-triangle law for the boundary of a thin rectangle*, published mathematical research record at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-logarithmic-acute-triangle-law-for-the-boundary-of-a-thin-rect--f2b630dbf4b1 . Complete result text inspected; polygonal boundary model.
4. *Fifth-chord-moment law for acute triangles in thin convex bodies*, published mathematical research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-fifth-chord-moment-law-for-acute-triangles-in-thin-convex-bodies--6f181af2eba0 . Complete result text inspected; interior-area model.
5. *Weighted Berwald's Inequality*, D. Langharst and E. Putterman, first preprint arXiv:2210.04438; classical Berwald inequality and equality conditions stated and referenced.
