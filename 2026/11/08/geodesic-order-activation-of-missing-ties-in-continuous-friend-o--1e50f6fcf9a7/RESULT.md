# Geodesic-order activation of missing ties in continuous friend-of-a-friend dynamics

## Finding

In the all-interacting regime of the continuous friend-of-a-friend (FOAF) model of Nugent, Gomes, and Wolfram [1], the initial positive-edge graph determines both the exact support that appears for every positive time and the first nonzero Taylor coefficient of every new tie. For a previously absent tie between distinct vertices \(i,j\) in the same connected component of the initial graph, let \(d=d_G(i,j)\ge2\) be their initial unweighted graph distance. Define the weighted geodesic sum

\[
S_{ij}=\sum_{P\in\mathcal P_{ij}^{(d)}}\prod_{\{u,v\}\in E(P)}w_{uv}(0),
\]

where \(\mathcal P_{ij}^{(d)}\) is the set of all shortest \(i\)-to-\(j\) paths, each path counted once. Then

\[
\boxed{w_{ij}(t)=\frac{S_{ij}}{n^{d-1}}t^{d-1}+O(t^d)\quad(t\downarrow0).}
\]

In particular \(S_{ij}>0\), and the tie has strictly positive strength at every \(t>0\). Every initially positive within-component tie stays positive, and each within-component off-diagonal tie tends to one as \(t\to\infty\). Ties between initially disconnected components remain identically zero. Thus the positive-time support graph is exactly the disjoint union of cliques on the initial connected components.

For an initially absent within-component tie, its unique first crossing time \(T_{ij}(\varepsilon)\) of any level \(0<\varepsilon<1\) has the sharp small-level asymptotic

\[
\boxed{T_{ij}(\varepsilon)\sim n\left(\frac{\varepsilon}{S_{ij}}\right)^{1/(d-1)}\quad(\varepsilon\downarrow0).}
\]

Thus the length and multiplicity of shortest initial routes, together with their weights, determine a hierarchy of effective tie-formation times despite instantaneous positive-time support closure.

## Assumptions and scope

Fix an integer \(n\ge2\) and a symmetric initial matrix \(W(0)=(w_{ij}(0))\in[0,1]^{n\times n}\) with \(w_{ii}(0)=1\). Let \(G\) have vertices \(\{1,\ldots,n\}\) and the undirected edge \(\{i,j\}\), for distinct \(i,j\), exactly when \(w_{ij}(0)>0\). All positive edge weights may be arbitrary, including one; no connectedness assumption is made.

The opinion interaction is bounded-confidence with \(\phi(r)=1\) when \(r<R\). Assume initial opinions lie in \([-1,1]\) and have diameter strictly less than \(R\). The associated opinion field is a nonnegative weighted averaging field, so the minimum opinion cannot decrease and the maximum cannot increase. Therefore the strict diameter bound persists and \(\phi(|x_i(t)-x_j(t)|)=1\) for every pair and all \(t\ge0\). The edge system from [1, equations (8), (13), (14)] reduces exactly to

\[
\dot w_{ij}=\left(w_{ij}+\frac1n\sum_{k=1}^{n}w_{ik}w_{kj}\right)(1-w_{ij})\quad(i\ne j),\qquad w_{ii}=1.
\tag{1}
\]

The rate coefficient of the unscaled FOAF system in [1] is used, not an additional timescale multiplier. The theorem concerns edge weights and their support, not a claimed rate of consensus of the opinions. It does not cover pairs that cease interacting under other confidence kernels or opinion configurations.

## Proof

**Forward invariance, components, and monotonicity.** Equation (1) is a polynomial vector field on the off-diagonal weight coordinates. At \(w_{ij}=0\), its derivative is \(n^{-1}\sum_k w_{ik}w_{kj}\ge0\), and at \(w_{ij}=1\) its derivative is zero. Consequently the cube of off-diagonal weights \([0,1]^{n(n-1)}\) is invariant; the bounded solution is global and real analytic in time. Transposition preserves the system, hence symmetry persists by uniqueness. If the initial matrix is block diagonal after a simultaneous row-column permutation, every cross-block derivative vanishes whenever all such entries vanish: the block-diagonal subspace is invariant. Therefore no tie can be formed between different initial connected components. Every off-diagonal weight is nondecreasing, since the right side of (1) is nonnegative.

**Leading Taylor coefficients.** For all \(i\ne j\), write \(w_{ij}(t)=\sum_{r\ge0}c_{ij,r}t^r\) near zero; the diagonal entries are identically one. For \(d_G(i,j)=1\), \(c_{ij,0}=w_{ij}(0)>0\). We prove inductively on finite initial distance \(d\ge2\) that

\[
c_{ij,r}=0\quad(0\le r<d-1),\qquad c_{ij,d-1}=\frac{S_{ij}}{n^{d-1}}.
\tag{2}
\]

Here and below distances are within the initial component. Suppose the assertion holds at distances strictly less than \(d\). For an intermediate vertex \(k\notin\{i,j\}\), the triangle inequality gives \(d_G(i,k)+d_G(k,j)\ge d\). By induction, its contribution \(w_{ik}(t)w_{kj}(t)\) to \((W^2)_{ij}\) begins no earlier than order \(t^{d-2}\). Equality in this exponent occurs exactly when \(k\) lies internally on a shortest \(i\)-to-\(j\) path. The diagonal summands with \(k=i\) or \(k=j\) are each \(w_{ij}\), which cannot affect the leading order. A direct coefficient induction in (1) therefore forces all \(c_{ij,r}\) with \(r<d-1\) to vanish.

At order \(t^{d-2}\) in \((W^2)_{ij}\), internal vertices on a geodesic contribute

\[
\frac{1}{n^{d-2}}\sum_{\substack{k\ne i,j\\d_G(i,k)+d_G(k,j)=d}}S_{ik}S_{kj}
=\frac{d-1}{n^{d-2}}S_{ij}.
\tag{3}
\]

To justify the equality, concatenate a shortest \(i\)-to-\(k\) path with a shortest \(k\)-to-\(j\) path. Because the concatenated walk has minimum length \(d\), it is itself a shortest simple path. Conversely each shortest \(i\)-to-\(j\) path has exactly \(d-1\) internal split vertices. The products of initial weights also factor at the split, proving (3) with the displayed multiplicity.

The terms \(w_{ij}\), \(-w_{ij}^2\), and \(-n^{-1}w_{ij}(W^2)_{ij}\) on the right side of (1) have no contribution at order \(t^{d-2}\), since \(w_{ij}(0)=0\) and the just-proved lower-order coefficients vanish. Hence the \(t^{d-2}\) coefficient of \(\dot w_{ij}\) is \((d-1)S_{ij}/n^{d-1}\), yielding (2) by division by \(d-1\). The argument applies identically to all connected components and establishes the asserted expansion.

**Positive-time closure and saturation.** Every geodesic consists of initially positive edges, so \(S_{ij}>0\). Formula (2) implies that each initially absent within-component tie is strictly positive at all sufficiently small positive times. Monotonicity then makes it positive at every later time. Initially positive ties also remain positive. For any within-component tie choose \(t_0>0\) with \(w_{ij}(t_0)>0\). The factor in parentheses in (1) is at least \(w_{ij}\), so

\[
\dot w_{ij}\ge w_{ij}(1-w_{ij}).
\]

Comparison with the logistic equation shows \(\liminf_{t\to\infty}w_{ij}(t)\ge1\); since the invariant interval gives \(w_{ij}(t)\le1\), the limit is one. If a tie already equals one, it remains one. All cross-component ties remain zero, proving the closure and limit statements.

**Level-crossing asymptotic.** If the tie was initially absent, \(w_{ij}(0)=0\), the established positivity and the logistic comparison imply that \(w_{ij}\) is strictly increasing on \((0,\infty)\) until its limit one (it never reaches one in finite time from below by local uniqueness). It therefore crosses each \(\varepsilon\in(0,1)\) exactly once. Substituting the positive leading Taylor coefficient into \(w_{ij}(T_{ij}(\varepsilon))=\varepsilon\), and inverting the leading power \(d-1\), gives the stated equivalence.

## Verification

The standalone `verify.py` implements the original polynomial right-hand side (1) and computes Taylor coefficients by exact rational arithmetic without using the claimed path formula in its coefficient recursion. It compares every reachable pair's first nonzero coefficient with the appropriate entry of the initial matrix power, which at shortest distance is exactly the weighted geodesic sum. It also checks that all preceding coefficients vanish, and that coefficients for disconnected pairs vanish. Run:

```text
python verify.py
```

Expected result: `VERIFY_OK 4832 exact coefficient/vanishing/positivity identities`. The input collection includes weighted paths, cycles, cliques, disconnected graphs, and pseudorandom weighted graphs with two through seven vertices. This is a finite independent check of the algebra, not proof of the universal statement.

For illustration, a unit-weight five-vertex path has end-to-end \(w_{15}(t)=t^3/125+O(t^4)\). In a unit-weight four-cycle the two opposite vertices have two shortest two-edge routes, giving \(w_{13}(t)=t/2+O(t^2)\). The different initial distances and geodesic multiplicities directly change the leading formation law.

## Relationship to prior work

Nugent, Gomes, and Wolfram [1, Section 3.2] introduce precisely the continuous FOAF mechanism, note that its matrix-square term creates new edges through mutual friends, and use repeated triadic closure to illustrate network densification. Their bounded-confidence numerical study [1, Section 3.3] and discussion [1, Section 5] concern opinion outcomes and network evolution, but do not derive the geodesic-order Taylor law, the all-positive-time support identity, or the small-level first-crossing asymptotic given here.

Di Giovacchino, Higham, and Zygalakis [2] investigate triadic closure with stochastic binary-edge birth/death dynamics and scalar mean-field limits. Their density bistability and mean exit-time statements do not imply (2) for the continuously weighted pairwise ODE (1). The matrix-power interpretation of weighted walks and shortest paths is classical [3]; the claimed contribution is its exact appearance as the first nonzero dynamical coefficient of this specific saturated FOAF system, together with componentwise positive-time closure and sharp threshold scaling.

## Limitations

The all-interacting confidence condition is essential: an interaction switch-off can prevent the FOAF creation mechanism from acting on a pair. The theorem is finite-dimensional, deterministic, and concerns the continuous-time system (1); it does not describe stochastic edge arrival, externally imposed sparsity constraints, or a finite delay before an edge becomes mathematically positive. The small-time and small-level formulas need not approximate moderate thresholds uniformly across graph sizes or tiny initial edge weights. The source's journal version was not available for complete independent page-by-page comparison; an equivalent unindexed derivation remains a publication-priority risk. No independent external audit has been performed.

## References

[1] A. J. Nugent, S. N. Gomes, and M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, arXiv:2305.09483, first posted 2023-05-16, https://arxiv.org/abs/2305.09483 ; published in *Physica D*, DOI: 10.1016/j.physd.2023.133914.

[2] S. Di Giovacchino, D. J. Higham, and K. C. Zygalakis, *A Hierarchy of Network Models Giving Bistability Under Triadic Closure*, arXiv:2111.05715, first posted 2021-11-10, https://arxiv.org/abs/2111.05715.

[3] M. E. J. Newman, *Networks*, second edition, Oxford University Press, 2018, Sections 6.11 and 8.5 (matrix powers and shortest paths).
