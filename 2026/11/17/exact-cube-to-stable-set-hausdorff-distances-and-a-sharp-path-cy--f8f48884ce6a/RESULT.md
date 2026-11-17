# Exact cube-to-stable-set Hausdorff distances and a sharp path–cycle parity jump

## Finding
For a finite simple graph \(G=(V,E)\) on \(n\ge1\) labeled vertices, define the (integral) stable-set polytope
\[
S(G)=\operatorname{conv}\{\mathbf1_I\in\mathbb R^n:I\subseteq V\text{ is an independent set}\}
\]
and the full coordinate cube \(Q_n=[0,1]^n\). All distances use the usual Euclidean norm in the same ambient \(\mathbb R^n\), and \(\alpha(G)\) is the maximum independent-set cardinality.

**General graph bridge.** For every \(G\),
\[
\boxed{d_H(Q_n,S(G))=\operatorname{dist}(\mathbf1,S(G))\ge\frac{n-\alpha(G)}{\sqrt n}.}
\]
The lower bound is attained precisely when \((\alpha(G)/n)\mathbf1\in S(G)\), equivalently when the maximum independent sets admit a probability distribution in which each vertex has the same inclusion probability \(\alpha(G)/n\). All vertex-transitive graphs have this property.

**Exact path and cycle metric.** For each path graph \(P_n\), \(n\ge2\),
\[
\boxed{d_H(Q_n,S(P_n))^2=\begin{cases}
 n/4,&n\text{ even},\\
 (n^2-1)/(4n),&n\text{ odd}.
\end{cases}}
\]
For each cycle graph \(C_n\), \(n\ge3\),
\[
\boxed{d_H(Q_n,S(C_n))^2=\begin{cases}
 n/4,&n\text{ even},\\
 (n+1)^2/(4n),&n\text{ odd}.
\end{cases}}
\]
In **every** path and cycle case, the all-ones cube vertex is the **unique** farthest point of the cube from the stable-set polytope, not merely one maximizer. The unique nearest point to it is explicit: on an even path it is constant \(1/2\); on an odd path \(n=2m+1\), the odd-position entries equal \((m+1)/n\) and the even-position entries equal \(m/n\); on a cycle every entry equals \(\lfloor n/2\rfloor/n\).

**Exact closing-edge rigidity.** For \(n\ge3\), adding the edge connecting the two endpoints of \(P_n\) creates \(C_n\) and increases the *squared* Euclidean Hausdorff distance by exactly
\[
\boxed{d_H(Q_n,S(C_n))^2-d_H(Q_n,S(P_n))^2
=\begin{cases}0,&n\text{ even},\\(n+1)/(2n),&n\text{ odd}.\end{cases}}
\]
Thus the closing edge is invisible to this global Euclidean metric at every even order, but incurs a strictly positive penalty at every odd order, tending to \(1/2\) as odd \(n\to\infty\).

## Assumptions and scope
The graph is finite, undirected, simple and unweighted; graph vertices index the ordinary Boolean coordinate embedding. The path and cycle have, respectively, \(n-1\) and \(n\) edges, with the specified lower bounds on \(n\). The Hausdorff metric is **Euclidean**, not the polytope one-skeleton metric, lattice-point distance, or an intrinsic geodesic metric. Since \(S(G)\subseteq Q_n\), one directed Hausdorff term is zero. The all-ones uniqueness assertion concerns paths and cycles (or other graphs whose nearest point to \(\mathbf1\) has no coordinate equal to one), not arbitrary edgeless graphs. For a general graph, no explicit closed-form distance in terms of the independence number alone is asserted when the equality condition fails.

## Proof
**1. The farthest cube point is always the all-ones vector.** The stable-set polytope is a down-set within the nonnegative coordinate order. Indeed, if \(x\in S(G)\) is the marginal vector of a random independent set, any \(0\le y\le x\) is represented by thinning each included vertex independently with retention probability \(y_i/x_i\) when \(x_i>0\), and never including it when \(x_i=0\). Every thinned set is still independent; hence \(y\in S(G)\).

Let \(q\) be the (unique) Euclidean projection of \(\mathbf1\) onto \(S(G)\), and take any \(z\in Q_n\). The coordinatewise minimum \(w_i=\min\{q_i,z_i\}\) lies in \(S(G)\) by the down-set property. Consequently,
\[
\operatorname{dist}(z,S(G))^2\le\|z-w\|_2^2
=\sum_{i=1}^n(z_i-q_i)_+^2
\le\sum_{i=1}^n(1-q_i)^2
=\operatorname{dist}(\mathbf1,S(G))^2.
\]
If each \(q_i<1\), then for every \(z\ne\mathbf1\) at least one summand strictly decreases; this proves uniqueness of the cube's farthest point in the cases below.

**2. The independence-number lower bound and its exact equality condition.** Every \(x\in S(G)\) satisfies \(\sum_i x_i\le\alpha(G)\). By Cauchy–Schwarz,
\[
\|\mathbf1-x\|_2^2\ge\frac{(n-\sum_i x_i)^2}{n}
\ge\frac{(n-\alpha(G))^2}{n}.
\]
Equality throughout holds exactly for \(x=(\alpha(G)/n)\mathbf1\). Such a point belongs to \(S(G)\) exactly when some convex mixture of independent-set indicators has these coordinates. Since its coordinate sum is \(\alpha(G)\), all positive mixture weights must be placed on *maximum* independent sets. Conversely, that mixture gives equality. For a vertex-transitive graph, average the orbit of any maximum independent set under its automorphism group: every coordinate of the average equals \(\alpha(G)/n\), proving the assertion.

**3. Exact paths through a dual-weighted optimality certificate.** The canonical path stable-set polytope is
\[
S(P_n)=\{x\in[0,1]^n:x_i+x_{i+1}\le1\ (1\le i<n)\}.
\]
This familiar integral description follows from total unimodularity: the path is bipartite, so multiplying one bipartition's columns of its edge-vertex incidence matrix by \(-1\) makes it an oriented incidence matrix; adjoining coordinate-bound rows retains total unimodularity. The linear system has integral right-hand sides, and every Boolean feasible vertex is an independent-set indicator.

Write \(y_i=1-x_i\). The squared distance from \(\mathbf1\) is the minimum of \(\sum_i y_i^2\) subject to \(0\le y_i\le1\) and \(y_i+y_{i+1}\ge1\). For even \(n\), take \(y_i^*=1/2\) and nonnegative edge multipliers \(\lambda_i=1\) when \(i\) is odd and \(\lambda_i=0\) when \(i\) is even. For odd \(n=2m+1\), take
\[
y_i^*=\begin{cases}m/n,&i\text{ odd},\\(m+1)/n,&i\text{ even},\end{cases}
\]
and, with \(1\le j\le m\), assign
\[
\lambda_{2j-1}=\frac{2(m-j+1)}{n},\qquad
\lambda_{2j}=\frac{2j}{n}.
\]
In either case \(y_i^*+y_{i+1}^*=1\), all \(\lambda_i\ge0\), and the exact stationarity identities hold:
\[
2y_i^*=\lambda_{i-1}+\lambda_i,
\qquad \lambda_0=\lambda_n=0.
\]
For any feasible \(y\), writing \(\delta=y-y^*\),
\[
\|y\|_2^2-\|y^*\|_2^2
=\|\delta\|_2^2+2\langle y^*,\delta\rangle
=\|\delta\|_2^2+
\sum_{i=1}^{n-1}\lambda_i(\delta_i+\delta_{i+1})
\ge\|\delta\|_2^2,
\]
since \(\delta_i+\delta_{i+1}=y_i+y_{i+1}-1\ge0\). This proves global optimality, uniqueness, and the strict quantitative stability estimate without any numerical optimization. Summing squares gives \(n/4\) for even \(n\), and
\( (m+1)m^2/n^2+m(m+1)^2/n^2=m(m+1)/n=(n^2-1)/(4n)\) for odd \(n\). Since \(y_i^*>0\), every nearest-point coordinate \(x_i^*=1-y_i^*\) is strictly below one, and Step 1 gives unique cube farthest point.

**4. Exact cycles by transitive symmetry.** Each \(C_n\) is vertex-transitive and has independence number \(\alpha(C_n)=\lfloor n/2\rfloor\). By Step 2, \(q=(\lfloor n/2\rfloor/n)\mathbf1\) lies in \(S(C_n)\) and attains the sharp lower bound. Strict convexity of squared Euclidean distance gives its uniqueness as a projection. Squaring \((n-\lfloor n/2\rfloor)/\sqrt n\) produces precisely the stated even and odd formulas. Each coordinate of \(q\) is less than one, so Step 1 again gives uniqueness of the farthest cube point.

**5. A sharp parity jump from a single edge.** The stable-set polytope of a cycle is contained in that of the path obtained by removing its closing edge. Substitute the established formulas: for even \(n\), both squared distances are \(n/4\); for odd \(n\),
\[
\frac{(n+1)^2}{4n}-\frac{n^2-1}{4n}
=\frac{n+1}{2n}.
\]
No value outside these parameter ranges is asserted.

## Verification
Execute `python3 verification/verify.py` with Python 3, NumPy and SciPy. The standalone checker verifies the exact rational path KKT identities for all \(2\le n\le300\), and cycle symmetry-average identities for all \(3\le n\le300\). A separate generic constrained quadratic optimizer verifies the predicted projection and squared distance for both paths and cycles in orders \(3\le n\le14\), including the extra odd-cycle inequality; exhaustive cube-vertex comparisons at orders three through seven confirm the predicted unique farthest point. A successful run reports

`CUBE_STABLE_SET_PARITY_PASS exact_paths=299 exact_cycles=298 independent_qps=24 cube_corner_checks=486`

Finite diagnostics corroborate but are not used as proofs of the arbitrary-order claims; the analytical certificates in the preceding section supply that proof. The Python script is a reproducibility aid, not an independent audit.

## Relationship to prior work
Aliniaeifard, Benedetti, Bergeron, Li and Saliola study the exact stable-set-polytope construction and its **one-skeleton** in *Stable set polytopes and their 1-skeleta* (2018, arXiv:1804.00360). Their graph distance is not the present ambient Euclidean Hausdorff distance from the full cube. The path's stable-set-polytope realization is a classical Fibonacci-polytope construction, associated for example with Rispoli (2005), and its usual edge-inequality description is standard; neither this description nor the vertex-transitivity argument is claimed as a new standalone lemma. Bärmann and Schneider (2021, arXiv:2101.09267) describe odd-cycle stable-set convex hulls by cycle inequalities, but do not state the cube-distance formulas or optimal path projection certificates. The present joint result combines the sharp general independence-number distance bridge, both exact path and cycle metrics, strict farthest-point uniqueness, and the parity-sensitive **single-edge** metric jump.

The relevant previously published cycle stable-set-polytope covariance calculation concerns a random vertex and its Fourier spectrum, not the Hausdorff distance to a cube. A published odd-cycle *fractional-versus-integral* cap calculation concerns volumes and a conditional Euclidean distribution on a different pair of convex bodies, not this cube gap. Source details and material comparisons appear in `AUDIT.json`. These comparisons are about mathematical implication rather than matching terminology.

## Limitations
No assertion is made that the general graph distance is determined solely by the independence number if the constant maximum-set marginal is infeasible. The theorem does not compute the Hausdorff metric for weighted or directed graphs, the Euclidean distance between the *fractional* and integral stable-set polytopes, or geodesic distances on the edge graph. As in any literature-led mathematical finding, the historical priority assessment is provisional: the basic symmetry reduction and some path quadratic programs may have appeared under other terminology. In particular, only the accessible abstract of Ehrenborg's 2024 graph-polytope paper and Rispoli's older Fibonacci-polytope paper was inspected; these abstracts cannot certify noncoverage by their complete texts. Independent mathematical audit has not been performed.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. Li and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360v1, publicly posted April 2, 2018, https://arxiv.org/abs/1804.00360 ; open full text https://ar5iv.labs.arxiv.org/html/1804.00360 .
2. A. Bärmann and O. Schneider, *Set characterizations and convex extensions for geometric convex-hull proofs*, arXiv:2101.09267v1, publicly posted January 22, 2021, especially Section 3.3, https://arxiv.org/html/2101.09267v1 .
3. F. J. Rispoli, *Fibonacci Polytopes and Their Applications*, 2005, https://doi.org/10.1080/00150517.2005.12428363 .
4. R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, European Journal of Combinatorics 118 (2024), article 103906, https://doi.org/10.1016/j.ejc.2023.103906 .
5. Related published exact treatments: *Antiperiodic Brownian geometry of the odd-cycle integrality cap* and *The complete vertex-covariance spectrum of cycle stable-set polytopes*, published-finding corpus mathematics archive, 2026, full published mathematical claims inspected for implication comparison.
