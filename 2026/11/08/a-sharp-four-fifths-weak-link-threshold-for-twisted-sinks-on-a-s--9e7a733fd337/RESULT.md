# A sharp four-fifths weak-link threshold for twisted sinks on a six-oscillator ring

## Finding

For the repulsive nearest-neighbour discrete phase map on a six-site cycle, weakening a single link produces a sharp and exactly soluble loss of both chiral twisted attractors. Five edges have weight one, and the closing edge has weight \(w>0\). For every \(0<h<1/\lambda_{\max}(L_w)\), the map modulo common phase has **exactly one hyperbolic sink** if \(0<w\le4/5\), and **exactly three hyperbolic sinks** if \(w>4/5\). The ever-present sink is the alternating phase-opposition state. The other two have opposite winding numbers. At the threshold the extra equilibria are nonhyperbolic and are not counted as hyperbolic sinks.

For \(w>4/5\), set \(s=\sqrt{5-4/w}\). The two chiral sinks and their companion index-one saddles are given explicitly in the attractive gauge by
\[
 y_j=\pm j\alpha_{\mathrm{sink}},\quad
 \alpha_{\mathrm{sink}}=\arccos\sqrt{\frac{3-s}{8}},
\]
\[
 y_j=\pm j\alpha_{\mathrm{saddle}},\quad
 \alpha_{\mathrm{saddle}}=\arccos\sqrt{\frac{3+s}{8}},\qquad j=0,\ldots,5.
\]
The two nontrivial branches meet at \(w=4/5\) with \(\alpha_*=\arccos\sqrt{3/8}\). At \(w=1\), the sink angles are \(\pm\pi/3\), and the saddle angles are \(\pm\pi/4\).

## Assumptions and scope

The state is \(\theta\in(\mathbb R/2\pi\mathbb Z)^6\). Edges \(j\leftrightarrow j+1\) for \(j=0,1,2,3,4\) carry weight one, and \(5\leftrightarrow0\) carries weight \(w>0\). The map is
\[
 (F_{h,w}(\theta))_j=\theta_j+h\sum_{k\sim j}a_{jk}\sin(\theta_j-\theta_k)\pmod{2\pi}.
\]
The global phase symmetry \(\theta\sim\theta+t(1,\ldots,1)\) is quotiented out. The positive weighted Laplacian \(L_w\) has diagonal weighted degrees and negative off-diagonal weights. Assume \(0<h<\lambda_{\max}(L_w)^{-1}\); this gives a gradient diffeomorphism with strictly decreasing potential away from fixed points, and all positive transverse Hessian eigenvalues yield map eigenvalues strictly in \((0,1)\). We classify **hyperbolic** sinks, not basin volumes, and not all saddles.

Because the graph is even and bipartite, \(y_j=\theta_j-\pi j\) conjugates the repulsive system to the attractive gradient step \(y\mapsto y-h\nabla V_w(y)\), with
\[
 V_w(y)=-\sum_{j=0}^{4}\cos(y_{j+1}-y_j)-w\cos(y_0-y_5).
\]

## Proof

**1. Every fixed point is stationary.** The force in coordinate \(j\) has magnitude at most its weighted degree \(d_j\), whereas \(\lambda_{\max}(L_w)\ge d_j\). Thus each lifted phase displacement has magnitude at most \(h d_j<1<2\pi\). It cannot equal a nonzero multiple of \(2\pi\). Therefore a fixed point on the torus is precisely a critical point of \(V_w\). At such a point the derivative on the phase quotient is \(I-hD^2V_w\). The bound \(\|D^2V_w\|\le\lambda_{\max}(L_w)\) shows that a critical point is a hyperbolic sink exactly when its transverse Hessian is positive definite.

**2. Current conservation and the complete necessary condition for a sink.** Orient the five strong edges in their cyclic order, and the closing edge from site five to zero. Write their angular increments as \(\delta_0,\ldots,\delta_5\), with sum zero modulo \(2\pi\). Stationarity at every vertex is equivalent to one conserved current:
\[
 \sin\delta_0=\cdots=\sin\delta_4=w\sin\delta_5=J.
\]
The five strong increments \(x_i\), \(i=0,\ldots,4\), provide local coordinates on the phase quotient; the closing increment varies as \(x_5=-\sum_i x_i\). The potential Hessian is the quadratic form
\[
 Q(x)=\sum_{i=0}^4\cos\delta_i\,x_i^2+w\cos\delta_5\left(\sum_{i=0}^4x_i\right)^2.
\]
If \(|J|=1\), all five strong-edge cosines vanish and \(Q\) has rank at most one, so it is not positive definite. If \(|J|<1\), each strong-edge cosine is \(\pm c\), with \(c=\sqrt{1-J^2}>0\). Two negative strong cosines make \(Q\) negative on their difference vector \((1,-1)\); one negative and at least one positive give a zero value on the corresponding difference vector, which is also incompatible with positive definiteness. Five negative cosines are covered by the first case. Hence every hyperbolic sink must have **all five strong cosines positive**. All strong increments therefore have one common representative \(\alpha\in(-\pi/2,\pi/2)\). Its weak closing increment is \(-5\alpha\) modulo \(2\pi\), and the conserved-current equation reduces to
\[
 \sin\alpha+w\sin5\alpha=0.
\]
This excludes *all* other possible sink configurations, not just uniform-angle solutions postulated in advance.

**3. Exact bifurcation threshold.** The solution \(\alpha=0\) gives the synchronized attractive sink (and thus the alternating repulsive sink), for every \(w>0\). Nonzero roots come in opposite pairs. For \(\alpha>0\), the current equation and \(0<\alpha<\pi/2\) require \(\pi/5<\alpha<2\pi/5\). Dividing by \(\sin\alpha\) gives
\[
 \frac1w=-\frac{\sin5\alpha}{\sin\alpha}=-U_4(\cos\alpha),\quad U_4(t)=16t^4-12t^2+1.
\]
The exact square identity
\[
 U_4(t)+\frac54=\frac{(8t^2-3)^2}{4}
\]
shows that the minimum of \(U_4\) on this interval is \(-5/4\), achieved uniquely at \(t^2=3/8\). The ratio takes value zero at both interval endpoints. Therefore there are no nonzero solutions when \(w<4/5\), two symmetric fold solutions at equality, and exactly two positive roots (hence four signed points) when \(w>4/5\). Solving the quadratic equation in \(\cos^2\alpha\) yields the formulas above.

**4. Which branch is attracting?** For a solution with five positive strong cosines, \(c=\cos\alpha>0\), the Hessian quadratic form is
\[
 Q(x)=c\sum_i x_i^2+w\cos5\alpha\left(\sum_i x_i\right)^2.
\]
Its matrix in edge-increment coordinates has eigenvalues \(c\) with multiplicity four and \(c+5w\cos5\alpha\) with multiplicity one. Their signs give its inertia; this is an invertible coordinate change from phase variables modulo rotation, although the numerical eigenvalues in the two coordinate systems need not agree. Along the equilibrium curve \(w(\alpha)=-\sin\alpha/\sin5\alpha\), differentiating gives
\[
 \frac{dw}{d\alpha}=-\frac{\cos\alpha+5w\cos5\alpha}{\sin5\alpha}.
\]
Since \(\sin5\alpha<0\) on the allowable interval, the final Hessian sign is that of \(dw/d\alpha\). The larger-angle root \(\alpha_{\mathrm{sink}}\) lies on the increasing branch and has positive-definite Hessian, so it is a hyperbolic sink. The smaller-angle root \(\alpha_{\mathrm{saddle}}\) has exactly one negative transverse Hessian direction and is an index-one saddle. At the fold the final eigenvalue vanishes; hence these points are nonhyperbolic. The antipodal branches have the same indices by reflection.

**5. Exhaustiveness and step-size independence.** Step 2 proved that every hyperbolic sink lies among the roots now classified; Step 4 proved that precisely the claimed roots are sinks. Since \(0<h<1/\lambda_{\max}(L_w)\), the signs of all transverse Hessian eigenvalues determine the stable/unstable map multipliers without additional step-size bifurcations. The sink count therefore holds for *every* allowed \(h\), not merely a limit as \(h\to0\).

## Verification

The standalone `VERIFY.py` checks the exact degree-four Chebyshev square identity and the algebraic threshold, the two explicit branches at representative weights on both sides of one, the signs of the reduced Hessians and full six-by-six Hessian spectra, exact fixed-point force balance, and the two-dimensional nullspace (including common rotation) at the fold. Execute with Python 3 plus SymPy and NumPy: `python VERIFY.py`. It is a finite cross-check; the theorem for every positive \(w\) and every admissible \(h\) follows from the preceding inequalities.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (2026) establish the discrete Huygens gradient structure, sharp Laplacian-based step interval, and observe that cycle constraints yield twisted local minima. Their discussion does not give a heterogeneous single-link bifurcation threshold or an exhaustive all-step sink count for a six-cycle. Delabays, Coletta and Jacquod (2016; first preprint 2015) establish loop-current/winding-number classifications and an upper bound of three stable phases for a six-node uniform-nearest-neighbor ring. Their general upper bound does not imply the specific weight threshold, precise branch angles, or the exact transition with a single weakened edge. The present result uses those established principles but derives a new sharp special-weight classification; no priority beyond the inspected literature is asserted.

## Limitations

The conclusion concerns exactly six identical sinusoidally coupled nodes, five equal edge weights and one positive distinguished weight. It counts fixed-point hyperbolic sinks modulo global phase for admissible step sizes. It does not classify all nonhyperbolic stationary points or all saddles, assert basin sizes or strong global attraction, or extend the threshold to other ring sizes, heterogeneous intrinsic frequencies, arbitrary phase laws or inadmissibly large steps. The absence of an exact matching statement in the inspected literature is not a proof of historical uniqueness; independent audit has not been performed.

## References

Buescu, J., D'Aniello, E., and Oliveira, H. M., *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public October 7, 2026), sections 2, 3, 5.5. https://arxiv.org/html/2610.10993v1

Delabays, R., Coletta, T., and Jacquod, P., *Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks*, arXiv:1512.04266v2 (first public December 14, 2015; journal 2016), sections II–IV. https://arxiv.org/html/1512.04266v2
