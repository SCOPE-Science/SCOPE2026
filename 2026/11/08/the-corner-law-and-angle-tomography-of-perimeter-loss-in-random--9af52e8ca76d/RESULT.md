# The corner law and angle tomography of perimeter loss in random inscribed polygons

## Finding

Let \(Q\subset\mathbb R^2\) be a fixed convex Euclidean polygon with \(m\ge3\) genuine vertices and no collinear consecutive sides, perimeter \(P>0\), and exterior turning angles \(\theta_1,\ldots,\theta_m\in(0,\pi)\). Choose \(N\ge3\) independent points uniformly by arclength on the whole boundary and write \(Q_N\) for their convex hull. Define its scaled perimeter deficit by
\[
Z_N=N\bigl(P-\operatorname{per}(Q_N)\bigr).
\]
For independent unit-rate exponential random variables \(E_i,F_i\), with all \(2m\) variables mutually independent, put
\[
G_\theta(u,v)=u+v-\sqrt{u^2+v^2+2uv\cos\theta},
\qquad Z_Q=P\sum_{i=1}^{m}G_{\theta_i}(E_i,F_i).
\]
Then \(Z_N\) converges in distribution **and in every fixed positive moment** to \(Z_Q\). The corner summands are independent, positive almost surely, and depend only on exterior angles. In particular the limiting law is independent of the individual side lengths once \(P\) and the unordered turning-angle multiset are fixed.

The law has an explicit Laplace transform. Define, for \(0<\theta<\pi\),
\[
a_\theta(r)=1-\sqrt{1-4\sin^2(\theta/2)r(1-r)},\qquad 0\le r\le1.
\]
Then for every \(s\ge0\),
\[
\boxed{\mathbb E e^{-s Z_Q}=\prod_{i=1}^{m}\int_0^1(1+sP a_{\theta_i}(r))^{-2}\,dr.}
\]
Consequently
\[
\boxed{\lim_{N\to\infty}N\,\mathbb E[P-\operatorname{per}(Q_N)]
=P\sum_{i=1}^{m}\Phi(\theta_i),}
\]
where
\[
\Phi(\theta)=1-\frac{\cos^2(\theta/2)}{\sin(\theta/2)}\operatorname{arsinh}\bigl(\tan(\theta/2)\bigr).
\]

The small-deficit tail is sharp:
\[
\boxed{\mathbb P(Z_Q\le z)\sim
\frac{2^m z^m}{m!P^m\prod_{i=1}^{m}(1-\cos\theta_i)}\quad(z\downarrow0).}
\]
Thus the complete limiting law determines the number of vertices from its order of vanishing at zero. **If \(P\) is known, the same law uniquely determines the unordered multiset of exterior turning angles**: the largest angle is read off from the moment-generating-function threshold, and all other angles are recovered by repeatedly removing its known Laplace factor. For a triangle, these data determine the triangle up to congruence. By contrast, all non-square rectangles of a given perimeter and the square of that perimeter share the *same* limiting law, so the full original shape is not identifiable for arbitrary polygons.

## Assumptions and scope

The polygon is fixed as \(N\to\infty\), is convex and has no collinear consecutive edges; hence every exterior turning angle lies strictly between zero and \(\pi\). Samples are independent and uniform with respect to Euclidean arclength along the **whole** boundary. All assertions concern this exact sampling model; there is no assumption of equal sampling weights for individual edges. The perimeter of a finite point hull is its ordinary Euclidean boundary length. The number \(m\) can be unknown when reading off the small-tail exponent; knowledge of \(P\) is required for the stated angle tomography. Recovered angles are an unordered multiset, not the cyclic order and not individual side lengths.

## Proof

**1. Exact finite-sample corner decomposition.** Number the vertices counterclockwise. On the event \(A_N\) that every edge contains at least one sampled point, let \(U_i\) be the distance from vertex \(i\) to the nearest sample along its incoming edge and \(V_i\) the analogous distance along its outgoing edge. The hull includes the segment of sampled points on each original side between its extreme samples, together with the chord between the two extreme points around each original vertex. This description is exact: each such chord joins the two intersections of a line with adjacent edges of the convex polygon, so every other boundary sample lies on its inward side. Hence
\[
P-\operatorname{per}(Q_N)
=\sum_{i=1}^{m}\left(U_i+V_i-\sqrt{U_i^2+V_i^2+2U_iV_i\cos\theta_i}\right)
\qquad\text{on }A_N.
\]
The squared chord length follows from the Euclidean cosine law, because the interior angle at vertex \(i\) is \(\pi-\theta_i\). Since every original edge has strictly positive length, \(\mathbb P(A_N^c)\le\sum_i(1-\ell_i/P)^N\) decays exponentially.

**2. Independent corner process.** For arbitrary fixed nonnegative \(t_1,\ldots,t_{2m}\), the tiny boundary arcs of lengths \(t_j/N\) adjoining the \(2m\) directed edge ends are disjoint once \(N\) is sufficiently large. The probability that they all contain no sampled point is exactly
\[
\left(1-\frac{\sum_jt_j}{NP}\right)^N\longrightarrow
\exp\left(-\frac{\sum_jt_j}{P}\right).
\]
Thus the vector of the \(2m\) scaled nearest-point distances converges jointly to independent exponential variables of rate \(1/P\). By the exact decomposition, homogeneity of \(G_\theta\), continuity, and \(\mathbb P(A_N^c)\to0\), we have \(Z_N\Rightarrow Z_Q\).

**3. Uniform integrability and all positive moments.** Define each directed nearest-end distance to equal its edge length if no sample lies on that edge. If this distance is \(T_N\) along an edge of length \(\ell\), then for \(0\le t<\ell\), \(\mathbb P(T_N>t)=(1-t/P)^N\). Therefore \(\mathbb P(NT_N>x)\le e^{-x/P}\) for \(0\le x<N\ell\), and this probability is zero for \(x>N\ell\). Consequently all fixed moments of \(NT_N\) have uniform bounds. On \(A_N\), \(0\le Z_N\le N\sum_i(U_i+V_i)\); on \(A_N^c\), \(0\le Z_N\le NP\), whose fixed moments contribute at most a polynomial times an exponentially small probability. This proves uniform integrability of every fixed positive power and hence convergence of moments.

**4. Laplace transform and exact mean.** For independent unit exponentials \(U,V\), the sum \(S=U+V\) has the \(\operatorname{Gamma}(2,1)\) law and the ratio \(R=U/S\) is independent and uniform on \([0,1]\). Direct substitution shows \(G_\theta(U,V)=S a_\theta(R)\). Given \(R=r\), the gamma Laplace transform is \((1+s a_\theta(r))^{-2}\), giving the stated product formula. Because \(\mathbb E S=2\),
\[
\mathbb E G_\theta=2\int_0^1 a_\theta(r)\,dr.
\]
Writing \(q=\sin(\theta/2)\), substituting \(z=2r-1\), and integrating \(\sqrt{1-q^2+q^2z^2}\) gives
\[
2\int_0^1a_\theta(r)\,dr=1-\frac{1-q^2}{q}\operatorname{arsinh}\!\left(\frac{q}{\sqrt{1-q^2}}\right)=\Phi(\theta).
\]

**5. Small tail and number of vertices.** Set \(k_\theta=1-\cos\theta>0\). The function \(a_\theta(r)\) is positive for \(r\in(0,1)\) and satisfies \(a_\theta(r)\sim k_\theta r\) at zero and \(a_\theta(r)\sim k_\theta(1-r)\) at one. Conditional on \(S\), the length of \(\{r:S a_\theta(r)\le z\}\), divided by \(z\), converges to \(2/(S k_\theta)\). It is dominated by \(C_\theta/S\), since \(a_\theta(r)\ge c_\theta\min\{r,1-r\}\); and \(\mathbb E[1/S]=1\). Dominated convergence therefore yields
\[
\mathbb P(G_\theta(U,V)\le z)\sim\frac{2z}{1-\cos\theta}.
\]
For \(m\) independent nonnegative variables having distribution functions \(c_i z+o(z)\) at zero, iterated convolution (or the rescaled probability measures on the unit simplex) gives \(\mathbb P(\sum_i W_i\le z)\sim(\prod_i c_i)z^m/m!\). Applying this to \(Z_Q/P\) proves the asserted small-tail constant and identifies \(m\) as \(\lim_{z\downarrow0}\log\mathbb P(Z_Q\le z)/\log z\).

**6. Reconstruction of exterior turning angles.** Since \(G_\theta=S a_\theta(R)\), its moment-generating function is
\[
M_\theta(t)=\int_0^1(1-t a_\theta(r))^{-2}\,dr
\quad\text{for }0\le t<\tau(\theta),
\qquad \tau(\theta)=\frac1{1-\cos(\theta/2)}.
\]
The maximum of \(a_\theta\) occurs at \(r=1/2\), where it is \(1-\cos(\theta/2)\); at the threshold the integral diverges, and for larger \(t\) the conditional gamma moment is infinite on a positive-measure set. Since all corner summands are nonnegative and independent, the moment-generating function of \(Z_Q\) is finite exactly on \(0\le t<1/[P(1-\cos(\theta_{\max}/2))]\). The threshold therefore determines \(\theta_{\max}\) uniquely when \(P\) is given, since \(\theta\mapsto 1-\cos(\theta/2)\) is strictly increasing. Divide the **Laplace** transform of \(Z_Q\), known for all \(s\ge0\), by the strictly positive known factor \(\int_0^1(1+sP a_{\theta_{\max}}(r))^{-2}dr\). The quotient is the Laplace transform of the sum of the remaining independent corner terms, and hence uniquely defines its distribution. Repeating this argument \(m\) times reconstructs the entire unordered angle multiset, with repetitions. The small-tail result supplies \(m\) even if initially unknown. This construction does not identify side lengths for polygons with at least four vertices: equal-perimeter rectangles are a concrete counterexample.

## Verification

Run the standalone `verify.py` with Python, NumPy, SciPy, and a 2D convex-hull routine (`scipy.spatial.ConvexHull`). It independently computes the perimeter from sampled coordinates and tests the **exact finite-sample corner decomposition** for 4,800 random configurations of a triangle and two unequal rectangles. All sampled configurations visited every edge. It numerically integrates the corner-mean formula at five angles, checks three small-tail coefficients, tests admissible moment-generating parameters, and compares the finite-sample mean deficit with the limiting formula. The observed relative mean deviations in the three examples were approximately \(-0.0092\), \(0.0133\), and \(0.0213\), consistent with finite-sample variation. No finite simulation is used as a proof of infinite-dimensional, exact, or asymptotic assertions.

## Relationship to prior work

Böröczky, Fodor, and Hug (arXiv:1103.4978, first publicly posted 25 March 2011) study the boundary-sampling intrinsic-volume problem and give bounds relevant to polytopes, but their precise main asymptotic formula assumes a freely rolling ball and does not provide the perimeter-deficit distribution for a polygon. Reitzner, Schütt, and Werner (arXiv:1911.05917, posted 14 November 2019) treat the same boundary-polytope sampling model, deriving facet-number and missed-volume asymptotics; they do not state the present perimeter law or angle reconstruction. Prochno, Schütt, Sonnleitner, and Werner (arXiv:2404.02870, posted 3 April 2024) derive precise expected **Hausdorff** error for boundary-sampled polygons, a different functional from perimeter loss. Closely related corner-exponential techniques also describe missed **area**; the present nonlinear corner functional, its full Laplace law, sharp small tail, and recovery of the actual exterior angles are not consequences of an area-product law that depends on \(\sin\theta\) alone. These comparisons do not certify global historical priority.

## Limitations

The polygon and its positive side lengths are fixed as the sample count grows. There are no uniform error estimates for polygons whose number of sides grows or which develop vanishing edges or turns. The angle-reconstruction assertion requires the exact population distribution and known perimeter; numerical stability, finite-sample inference, cyclic angle order, and general side-length reconstruction are not established. The result concerns perimeter, not area deficit, Hausdorff error, or boundary sampling with nonuniform density. Literature searching cannot exclude unindexed equivalent statements.

## References

1. K. J. Böröczky, F. Fodor, D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978 (first posted 2011-03-25); *Trans. Amer. Math. Soc.* 365 (2013), 785–809. https://arxiv.org/abs/1103.4978
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first posted 2019-11-14); *Discrete Comput. Geom.* 69 (2023), 453–504. https://arxiv.org/abs/1911.05917
3. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first posted 2024-04-03). https://arxiv.org/abs/2404.02870
