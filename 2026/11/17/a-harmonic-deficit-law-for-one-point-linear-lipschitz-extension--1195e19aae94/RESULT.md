# A harmonic-deficit law for one-point linear Lipschitz extension over clustered metrics

## Finding
Let \(X=C_1\sqcup\cdots\sqcup C_k\) consist of \(k\ge2\) nonempty equilateral clusters, with \(m_j=|C_j|\ge1\). Distinct points in \(C_j\) have distance \(t_j\in(0,1]\), and points in different clusters have distance \(1\). Adjoin a point \(o\) at the common distance \(R\ge1/2\) from all points of \(X\), obtaining a metric space \(Y\). Define
\[
\beta_j=1-t_j\left(1-\frac1{m_j}\right),\qquad
H=\sum_{j=1}^{k}\beta_j^{-1},\qquad
D=1-H^{-1}.
\]
For real-linear simultaneous extension operators \(E:\operatorname{Lip}_0(X)\to\operatorname{Lip}_0(Y)\), fixing each input function on \(X\), the exact minimum operator norm is
\[
\boxed{\inf_E\|E\|=\max\{1,D/R\}.}
\]
One optimal extension assigns to the new point the probability-weighted cluster mean
\[
\boxed{(Ef)(o)=\sum_{j=1}^{k}\frac{1}{H\beta_j m_j}\sum_{x\in C_j}f(x).}
\]
The new-point functional minimizes its largest Lipschitz dual distance to a point evaluation **uniquely**, even if arbitrary signed coefficients are admitted. Consequently, among *all* linear extension operators, the optimum itself is unique if \(1/2\le R\le D\), whereas it is attained by a continuum of distinct operators whenever \(R>D\). In particular, a norm-one linear simultaneous extension exists exactly when \(R\ge D\).

For \(k\) clusters of equal size \(m\) and equal within-cluster radius \(t\), the threshold is
\[
D=1-\frac{1-t+t/m}{k}.
\]
At any fixed \(R<1\), taking enough such clusters forces every linear extension to have norm greater than one, although each individual real-valued Lipschitz function admits a (nonlinear-in-the-data) norm-preserving extension.

## Assumptions and scope
All scalars and linear maps are real. The spaces of functions vanishing at a fixed basepoint \(x_0\in X\) have norms \(\|f\|_{\operatorname{Lip}_0(X)}=\max_{x\ne y\in X}|f(x)-f(y)|/d(x,y)\), and similarly on \(Y\). The basepoint is the same in both spaces. Since all between-cluster distances are one and all within-cluster distances are in \((0,1]\), \(d|_X\) is a metric. The common apex distance produces a metric on \(Y\) precisely when \(R\ge1/2\). The theorem includes singleton clusters and the endpoint \(t_j=1\); for a singleton its parameter is immaterial. Each \(\beta_j\) is strictly positive. The new point is distinct from \(X\), and \(|X|\ge2\).

## Proof
**1. Every extension is an affine-weight functional.** Since an extension fixes all values on \(X\), it is determined by a linear functional \(L(f)=(Ef)(o)\). Any \(f\in\operatorname{Lip}_0(X)\) can be represented uniquely as arbitrary values on \(X\) with \(f(x_0)=0\). Thus there are real numbers \((c_x)_{x\in X}\) summing to one such that \(L(f)=\sum_x c_x f(x)\). Conversely, every coefficient family with sum one defines such a linear extension; changing \(c_{x_0}\) to enforce the sum does not change the functional on basepoint-zero functions. The restriction of \(E\) to pairs in \(X\) has norm one, and hence
\[
\|E\|=\max\left\{1,\frac{K(c)}{R}\right\},\quad
K(c)=\sup_{\|f\|_{\operatorname{Lip}_0(X)}\le1}\max_{i\in X}\left|\sum_xc_xf(x)-f(i)\right|.
\]

**2. Distance-potential lower bound for arbitrary signed coefficients.** For \(i\in X\), the function \(\varphi_i(x)=d(i,x)-d(i,x_0)\) belongs to the Lipschitz unit ball. Put \(w_j=\sum_{x\in C_j}c_x\). For \(i\in C_j\), evaluating the functional on \(\varphi_i\) gives
\[
A_{j,i}=\sum_xc_xd(i,x)-d(i,i)=1-w_j+t_j(w_j-c_i).
\]
The average of these \(m_j\) numbers is \(1-\beta_jw_j\). Because \(K(c)\ge\max_i|A_{j,i}|\), it follows that
\[
K(c)\ge\max_j\{1-\beta_jw_j\}.
\]
Since \(\sum_jw_j=1\), at least one index satisfies \(\beta_jw_j\le1/H\) (otherwise \(\sum_jw_j>\sum_j1/(H\beta_j)=1\)). Thus \(K(c)\ge D\) for *every* linear extension, with no positivity or symmetry assumption.

**3. The exact sharp candidate.** Choose \(c_x^*=1/(H\beta_jm_j)\) for \(x\in C_j\). These coefficients are nonnegative and sum to one. For every \(i\in C_j\),
\[
\sum_{x\in X}c_x^*d(i,x)=1-\beta_j\frac1{H\beta_j}=D.
\]
For every one-Lipschitz \(f\), positivity and the triangle inequality imply
\[
\left|\sum_xc_x^*f(x)-f(i)\right|
\le\sum_xc_x^*d(x,i)=D.
\]
The distance potential \(\varphi_i\) attains equality, proving \(K(c^*)=D\). Together with Step 2 this proves the exact infimum \(\max\{1,D/R\}\) and its attained formula.

**4. Rigidity of the minimizer of \(K\).** Suppose \(K(c)=D\). The inequalities from Step 2 force \(\beta_jw_j\ge1/H\) for all \(j\), and their weighted sum identity \(\sum_jw_j=1\) forces equality for every \(j\). Hence \(w_j=1/(H\beta_j)\). For each cluster, the numbers \(A_{j,i}\) all obey \(A_{j,i}\le D\) but average to \(D\), so every one equals \(D\). Since \(t_j>0\), the displayed expression for \(A_{j,i}\) then forces \(c_i=w_j/m_j\) for every \(i\in C_j\). This is exactly \(c^*\). Thus \(c^*\) is the *unique* minimizer of \(K\).

If \(R\le D\), any optimal extension has \(K(c)\le D\) and hence equals this unique extension. If \(R>D\), the strict inequality \(K(c^*)=D<R\) and continuity of the finite-dimensional function \(K(c)\) give an open neighborhood of \(c^*\) in the affine hyperplane \(\sum_xc_x=1\) for which \(K(c)<R\). Every such coefficient family defines a norm-one optimal extension, proving the asserted continuum and the sharp uniqueness boundary.

## Verification
The proof is analytic for arbitrary integers \(k\ge2\), arbitrary positive part sizes, all permitted radii, and all signed linear extension coefficients. The standalone exact-arithmetic checker `verify_cluster_extension.py` independently enumerates the extreme vertices of small Lipschitz unit balls via signed spanning trees. Across eight heterogeneous profiles it verifies the predicted sharp dual distances, 172 distinct extreme potentials, strict increase under numerous nontrivial signed coefficient perturbations, and the threshold formula. Run `python3 verify_cluster_extension.py` with Python 3 and its standard library. Finite checks corroborate, but do not establish, the infinite-family proof.

## Relationship to prior work
Cúth and Doucha (first public 23 April 2021, arXiv:2104.11519) give general projections induced by group actions on Lipschitz-free Banach spaces. Their invariant averaging principle does not compute the optimal weights among *several inequivalent clusters*, or prove uniqueness of a minimal one-point extension under arbitrary signed weights. Basso (first public 29 April 2021, arXiv:2104.14238) reduces finite-metric relative linear Lipschitz extension problems to projection constants and linear programming, but its stated results do not derive the present closed harmonic-deficit law.

A published result on snowflaked regular polygons with a center gives vertex averaging by a transitive cyclic isometry group, whereas the clusters here can have inequivalent sizes and radii; no transitive action forces the distinct optimal cluster weights. Another published clustered-metric projection theorem computes projection onto *within-cluster fluctuations in the original free space*, not projection from the enlarged one-point free space onto the entire original free space; its constant \(\max\{1,w_{(1)}+w_{(2)}\}\) does not imply the present reciprocal-deficit expression. A prior one-point extension theorem for complete multipartite graph metrics permits same-part distance \(2\) and apex radius at least \(1\); its parameter region is disjoint from the present strict short-cluster range, and its sharp formula and interpolation phases are different. An earlier universal equilateral-leaf-to-star extension theorem explicitly gives the known scalar Banach endpoint \(2-2/n\) for \(n\) equilateral leaves at center-to-leaf distance one and leaf distances two. This agrees with the singleton-cluster, \(R=1/2\) specialization of our formula after rescaling; that endpoint is **not** claimed as new. The new result is the sharp heterogeneous multicluster formula, signed-weight uniqueness and all-radius transition. Ambrosio and Puglisi (2016) provide a general random-projection extension framework, not an explicit inequality for the present non-transitive cluster family.

## Limitations
The theorem applies to real-linear extension of scalar-valued Lipschitz functions from finite equilateral cluster metrics to *one* uniformly distant new point. It does not claim the corresponding norm for arbitrary target Banach spaces or for asymmetric new-point distances. It does not classify the full shape of the norm-one extension polytope when \(R>D\), beyond proving that it has nonempty relative interior. No claim of exhaustive historical uniqueness is made: alternative formulations in optimal-transport or random-projection literature remain a residual priority risk. Independent mathematical audit has not been performed.

## References
- M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519 (first public 23 April 2021), https://arxiv.org/abs/2104.11519.
- G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first public 29 April 2021), https://arxiv.org/abs/2104.14238.
- L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (first public 6 September 2016), https://arxiv.org/abs/1609.01450.
- *A sharp snowflake threshold for simultaneous linear Lipschitz extensions from regular polygons*, publicly available research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-snowflake-threshold-for-simultaneous-linear-lipschitz-ex--55dc55bc9348.
- *Sharp optimal projection constants for clustered finite metric free spaces*, publicly available research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-optimal-projection-constants-for-clustered-finite-metric-f--bd13acd51aa3.
- *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions*, publicly available research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-leaf-count-transitions-in-one-point-p-banach-lipschitz-ext--b03e5cc2b3f1.
