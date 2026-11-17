# A sharp convex-order envelope for arclength Lipschitz functions on bridgeless metric graphs

## Finding
Let \(G\) be any finite connected metric graph in which every edge has strictly positive length and no edge is a bridge. Write \(L\) for the sum of the edge lengths, and let \(\mu\) be normalized arclength measure. For every real function \(f:G\to\mathbb R\) with Lipschitz constant at most one, its centered law satisfies
\[
 f_\#\mu-\int_G f\,d\mu\ \preceq_{\mathrm{cx}}\ \operatorname{Unif}[-L/4,L/4].
\]
Here convex order means that every finite convex function \(\Phi:\mathbb R\to\mathbb R\) has no larger expectation under the law on the left. In particular,
\[
 \operatorname{Var}_\mu(f)\le\frac{L^2}{48},\qquad
 \int_G e^{t(f-\int f\,d\mu)}\,d\mu\le\frac{\sinh(tL/4)}{tL/4}\quad(t\ne0),
\]
with the right-hand side interpreted as one when \(t=0\), and for every \(p\ge1\),
\[
 \int_G\left|f-\int_Gf\,d\mu\right|^p\,d\mu\le\frac{(L/4)^p}{p+1}.
\]

The following are equivalent: (a) some nonconstant one-Lipschitz function attains equality for one strictly convex \(\Phi\); (b) \(\operatorname{diam}(G)=L/2\); (c) there exist two edge-disjoint length-\(L/2\) geodesics with common endpoints whose union is the whole graph. If these conditions hold, *every* maximizer for any strictly convex \(\Phi\), up to an additive constant, is the distance-to-a-point function \(z\mapsto d_G(a,z)\) at a diametral point \(a\). Such functions have exactly the uniform centered law above. If the diameter is strictly less than \(L/2\), the convex-order envelope is strict for every strictly convex \(\Phi\) and every one-Lipschitz \(f\).

## Assumptions and scope
A finite metric graph is a finite connected graph realized as a compact length space by assigning positive lengths to its edges; parallel edges are permitted and interior points of edges are included. Its shortest-path distance is denoted \(d_G\). Subdividing an edge does not change the metric graph or its arclength. The absence of a bridge means removing any open edge leaves its endpoints connected by another route. A compact metric graph has finite total length \(L>0\); normalized arclength gives total probability one and has no atoms. Quantifiers include every number of edges, every positive length profile, every one-Lipschitz real function, and every finite real convex test function. All expectations are taken with respect to normalized arclength, *not* uniform mass on graph vertices.

## Proof
**1. Two routes imply a lower bound on intermediate-level mass.** Let \(m=\min_G f\) and \(M=\max_G f\). The case \(m=M\) is immediate. Choose points \(a,b\) with \(f(a)=m\) and \(f(b)=M\). Subdivide the edges if necessary so that these points are vertices. In a connected bridgeless multigraph there are two edge-disjoint routes from \(a\) to \(b\): otherwise a one-edge cut would separate them and its edge would be a bridge. For any \(m<u<v<M\), the continuous image on either route contains \([u,v]\). Since \(f\) is one-Lipschitz, the arclength on each route where \(u<f<v\) is at least \(v-u\) (apply the one-dimensional Lipschitz image-length inequality to the preimage of \((u,v)\)). The routes have disjoint open edges, hence
\[
 \mu\{z:u<f(z)<v\}\ge\frac{2(v-u)}{L}. \tag{1}
\]

**2. Quantile contraction.** Let \(\nu=f_\#\mu\), let \(F\) be its distribution function, and take its nondecreasing quantile \(Q:[0,1]\to[m,M]\). Inequality (1), by approaching level endpoints and using the generalized inverse of \(F\), yields
\[
 0\le Q(t)-Q(s)\le\frac L2(t-s)\qquad(0\le s<t\le1). \tag{2}
\]
A direct justification is that (1) forces \(F(v-)-F(u)\ge2(v-u)/L\) whenever \(m<u<v<M\); inverting this inequality and taking one-sided limits proves (2), including endpoints. In particular, \(Q\) is continuous, nondecreasing, and Lipschitz.

**3. Convex-order comparison.** Set \(c=L/2\), \(q(t)=Q(t)-\int_0^1Q\), and \(b(t)=c(t-1/2)\). By (2), \(q-b\) is nonincreasing, and both \(q\) and \(b\) have mean zero. Consequently, for every \(r\in[0,1]\),
\[
 \int_r^1 q(t)\,dt\le\int_r^1 b(t)\,dt. \tag{3}
\]
For an increasing quantile \(H\), the stop-loss transform obeys
\[
 \int_0^1(H(t)-s)_+\,dt
 =\sup_{r\in[0,1]}\left\{\int_r^1H(t)\,dt-s(1-r)\right\}.
\]
Thus (3) compares all stop-loss transforms. Together with equality of the means, the stop-loss characterization of convex order gives \(q_\#\operatorname{Unif}[0,1]\preceq_{\mathrm{cx}} b_\#\operatorname{Unif}[0,1]\). The second law is precisely \(\operatorname{Unif}[-L/4,L/4]\). Integrating its squared, exponential, and absolute-power moments proves the displayed constants.

**4. Strictness and extremizers.** For any strictly convex \(\Phi\), equality in the convex-order inequality forces \(q=b\) almost everywhere. One way to see strictness is to interpolate \(q_\theta=(1-\theta)q+\theta b\). The difference \(b-q\) is nondecreasing with mean zero, while \(\Phi'(q_\theta)\) is strictly increasing when \(0<\theta<1\) (first take smooth strictly convex \(\Phi\)). Their covariance is strictly positive unless \(q=b\), so integrating the derivative of \(\int\Phi(q_\theta)\) proves the assertion. Approximation or the strict form of the convex-order theorem covers arbitrary finite strictly convex \(\Phi\). Equality therefore means that \(f\) has the uniform law on an interval of length \(L/2\), in particular \(M-m=L/2\).

**5. Geometry of equality.** For *every* pair \(a,b\) of points in a bridgeless metric graph, there are two edge-disjoint paths joining them. Each has length at least \(d_G(a,b)\), and their combined length is at most \(L\); hence \(\operatorname{diam}(G)\le L/2\). In an equality case, points where \(f\) takes its extreme values satisfy \(d_G(a,b)\ge M-m=L/2\). Hence \(\operatorname{diam}(G)=L/2\). Both edge-disjoint routes between these points must be geodesics of length \(L/2\), and together use every edge of \(G\). On each geodesic \(f\) rises by exactly its length and has Lipschitz constant at most one, so it rises with slope one along the entire path. It follows that \(f(z)=f(a)+d_G(a,z)\) everywhere.

Conversely, if \(d_G(a,b)=L/2\), the two routes just described are geodesics and exhaust the graph. The distance map \(z\mapsto d_G(a,z)\) increases linearly at unit speed on both, so normalized arclength pushes forward to the uniform law on \([0,L/2]\). Its centered version is uniform on \([-L/4,L/4]\) and attains every convex-order bound. Taking a different diametral endpoint accounts for the reversed orientation. This proves all equivalences and the claimed complete equality classification.

## Verification
The accompanying standalone `check.py` uses exact rational arithmetic on finite metric graphs. It checks stop-loss inequalities for sampled piecewise-affine one-Lipschitz potentials, evaluates continuous-edge integrals exactly, and checks equality on cycles and a figure-eight graph, strictness for a theta graph, and the necessity of the no-bridge hypothesis using a path. Its successful terminal marker is `ALL_BRIDGELESS_CONVEX_ORDER_CHECKS_OK`. Enumeration is limited to the specified finite graphs; the infinite-family and all-convex-function conclusions are established by the proof above, not by the finite checks.

## Relationship to prior work
Spread—the supremum of the variance of one-Lipschitz functions—is a standard invariant in the graph-spread literature, particularly Addario-Berry, Janson and McDiarmid. Their graph measures are uniform vertex laws, and their random-graph spread bounds do not give this arclength convex-order envelope. Barthe and O'Connell solve a Lipschitz-variance problem for Gaussian and Euclidean-ball measures, rather than continuous length measures on bridgeless networks. Discrete-torus concentration estimates use other measures and typically provide concentration inequalities rather than the all-convex-function sharp ordering and the diameter equality classification. The present argument is an arclength two-route theorem, not an extension automatically implied by results for vertex-law spread, Gaussian concentration, or Lipschitz-free Banach-space numerical indices. Equivalence to a result in unindexed metric-measure or metric-graph literature cannot be excluded.

## Limitations
The theorem requires normalized arclength, absence of bridges, connectedness, finite total edge length and real-valued one-Lipschitz functions. Arbitrary vertex atoms, arbitrary nonuniform edge densities, graphs with bridges, higher-dimensional length spaces and nonlinear target spaces are not covered. While the uniform law gives a sharp *universal envelope*, it need not be attainable on a particular bridgeless graph: the precise attainment criterion is diameter \(L/2\). The checker is corroborating finite evidence, not a proof certificate. Independent expert verification has not been performed.

## References
1. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first posted 2009-02-06. https://arxiv.org/abs/0902.1156
2. F. Barthe and N. O'Connell, *Matchings and the variance of Lipschitz functions*, ESAIM Probability and Statistics 13 (2009), 400–408, DOI:10.1051/ps:2008018. https://www.numdam.org/article/PS_2009__13__400_0.pdf
3. M. Sammer and P. Tetali, *Concentration on the Discrete Torus Using Transportation*, 2009. Its accessible abstract concerns discrete graph transport concentration, not the arclength measure considered here.
