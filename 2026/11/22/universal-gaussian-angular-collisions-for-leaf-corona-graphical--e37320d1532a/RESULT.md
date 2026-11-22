# Universal Gaussian angular collisions for leaf-corona graphical zonotopes

## Finding

Let \(H\) be any fixed finite simple graph on \(k\ge3\) labeled vertices, connected or disconnected. Form \(G_n(H)\) by attaching exactly \(n\) private pendant leaves to each vertex of \(H\). Let \(Z_n(H)\) be its canonical Euclidean graphical zonotope. Write \(C_n(H)\) for the probability that two independent isotropic Gaussian linear objectives expose the **same vertex** of \(Z_n(H)\).

For a finite graph \(F\), let \(q(F)\) be the probability that two independent uniformly random total orders of its vertex set induce identical orientations of every edge. Equivalently, if \(L_F(\omega)\) is the number of linear extensions of the acyclic orientation \(\omega\), then
\[
q(F)=\frac{1}{(|V(F)|!)^2}\sum_{\omega\in\operatorname{AO}(F)}L_F(\omega)^2,
\qquad q(\varnothing)=1.
\]
Then the sharp Gaussian vertex-collision law is
\[
\boxed{\lim_{n\to\infty} n^{2k}C_n(H)
=\kappa(H):=\sum_{S\subseteq V(H)}q(H[S])q(H[V(H)\setminus S]).}
\tag{1}
\]
The leading constant is **strictly decreasing under every addition of a previously absent core edge**. Consequently, for each \(k\ge3\),
\[
\boxed{\frac{1}{k!}\binom{2k}{k}\le\kappa(H)\le2^k,}
\tag{2}
\]
with equality on the left precisely for the complete core and on the right precisely for the edgeless core. In particular, the three-vertex path and triangle give distinct coefficients:
\[
\boxed{\kappa(P_3)=\frac{41}{9},\qquad\kappa(K_3)=\frac{10}{3}.}
\tag{3}
\]

There is also a conditional localization law. Conditional on the collision event, for every fixed \(0<\delta<1/2\), with probability tending to one each core vertex's *two* independent uniform-quantile objective coordinates both belong to \([0,\delta]\) or both belong to \([1-\delta,1]\). Label the former type \(0\), the latter type \(1\). The resulting random subset \(S\) of type-\(0\) core vertices converges to
\[
\boxed{\Pr(S=T\mid\text{same exposed vertex})
\longrightarrow\frac{q(H[T])q(H[V(H)\setminus T])}{\kappa(H)},}
\qquad T\subseteq V(H).
\tag{4}
\]
The limiting distribution thus records the actual core graph, not just the number of attached leaves.

## Assumptions and scope

Let \(N=k(n+1)\). Work in \(\mathbb R^N\) with its standard coordinate inner product, and define the centered graphical zonotope
\[
Z_n(H)=\sum_{\{a,b\}\in E(G_n(H))}
\left[-\tfrac12(e_a-e_b),\tfrac12(e_a-e_b)\right].
\]
For disconnected \(G_n(H)\), its intrinsic direction space is the direct sum of the coordinate-sum-zero spaces of its components. Projecting a standard \(N\)-dimensional Gaussian orthogonally onto that space is an isotropic intrinsic Gaussian. Every edge-root comparison is unaffected by projection, so one can use independent standard Gaussian coordinates on all graph vertices. Maximizers are unique almost surely. The result is about this **fixed Euclidean realization** and does not assert invariance under arbitrary affine transformations. The core size \(k\) and its edges are fixed while the common pendant count \(n\) tends to infinity.

## Proof

**Step 1: vertex equality equals agreement of all edge comparisons.** The support function of a Minkowski sum of edge segments is the sum of their support functions, and the maximizing endpoint of a segment \([-(e_a-e_b)/2,(e_a-e_b)/2]\) is determined by the sign of \(g_a-g_b\). The normal fan of a graphical zonotope is the graphical arrangement fan: its maximal cones, hence exposed vertices, are in bijection with acyclic edge orientations. Thus two generic objectives expose the same vertex if and only if their induced comparisons agree on *every* graph edge. Replacing Gaussian coordinates by their standard-normal distribution-function quantiles makes all coordinates independent \(U(0,1)\) without changing comparisons.

**Step 2: exact finite integral.** For each core vertex \(i\), let \(u_i,v_i\) be its quantiles in the two independent objective directions. Conditional on them, one private leaf at \(i\) has agreeing edge directions with probability
\[
h(u_i,v_i)=u_iv_i+(1-u_i)(1-v_i)=1-u_i-v_i+2u_iv_i.
\]
Its \(n\) private leaves are conditionally independent. The core edges agree precisely on the event
\[
A_H(\mathbf u,\mathbf v)
:=\bigcap_{\{i,j\}\in E(H)}\{(u_i-u_j)(v_i-v_j)>0\}.
\]
Consequently the exact identity
\[
C_n(H)=\int_{[0,1]^{2k}}\mathbf 1_{A_H(\mathbf u,\mathbf v)}
\prod_{i=1}^{k}h(u_i,v_i)^n\,d\mathbf u\,d\mathbf v
\tag{5}
\]
holds for every positive integer \(n\), without any asymptotic approximation.

**Step 3: localization at two corners.** The function \(h\) satisfies \(0\le h\le1\), with equality \(h=1\) only at \((0,0)\) and \((1,1)\). Fix \(0<\delta<1/4\), and split each coordinate pair into the two squares of side \(\delta\) adjoining these corners and their complement. On the complement \(h\le1-\eta_\delta\) for some \(\eta_\delta>0\), so the total complementary contribution to (5), multiplied by \(n^{2k}\), tends to zero. On the zero-corner square write \((u_i,v_i)=(X_i/n,Y_i/n)\), while on the one-corner square write \((u_i,v_i)=(1-X_i/n,1-Y_i/n)\). In either case, for fixed nonnegative \(X_i,Y_i\),
\[
h(u_i,v_i)^n=\left(1-\frac{X_i+Y_i}{n}+\frac{2X_iY_i}{n^2}\right)^n
\longrightarrow e^{-X_i-Y_i}.
\]
For \(u_i,v_i\le\delta\), \(1-h(u_i,v_i)=u_i+v_i-2u_iv_i\ge(1-\delta)(u_i+v_i)\). The same inequality holds in one-corner deficit coordinates. Therefore the rescaled integrand is dominated by \(\exp(-(1-\delta)\sum_i(X_i+Y_i))\), an integrable function on the positive orthant. Dominated convergence applies on every fixed corner-pattern sector.

**Step 4: induced-subgraph partition function.** Associate to a corner pattern the set \(S\subseteq V(H)\) of zero-corner vertices. If \(i\in S\) and \(j\notin S\), their core-edge comparison is automatically the same in the two objectives for sufficiently large \(n\) on bounded rescaled regions: a zero-corner quantile is below a one-corner quantile in both objectives. If both endpoints lie in \(S\), comparison agreement becomes \((X_i-X_j)(Y_i-Y_j)>0\). If both lie in the complement, simultaneous reversal of both comparisons gives the same condition. Outside a set of zero limiting measure there are no ties.

Under the limiting product density \(\exp(-\sum_i(X_i+Y_i))\), the \(X_i\) and \(Y_i\) are independent unit exponentials, whose relative orderings within any fixed subset are independent uniform permutations. Consequently the corner sector indexed by \(S\) contributes exactly \(q(H[S])q(H[V(H)\setminus S])\) to the scaled integral. Summing the \(2^k\) sectors proves (1). The same joint sector convergence, divided by the positive total limit \(\kappa(H)\), proves the conditional localization and weights in (4).

**Step 5: strict edge monotonicity and sharp bounds.** If \(F'\) is obtained from \(F\) by adding an edge \(ij\), then the event of comparison agreement on \(F'\) is contained in the event of agreement on \(F\). The inclusion is strict in probability: choose one total order in which \(i,j\) are consecutive, and a second order obtained by swapping that adjacent pair. Every old edge comparison agrees, since \(ij\notin E(F)\), but the new comparison differs. This pair of orders occurs with strictly positive probability. Therefore \(q(F')<q(F)\). In the sum defining \(\kappa(H)\), every term is nonincreasing upon adding a core edge, and at least one strictly decreases because one may choose a subset containing both endpoints. This gives strict graph-edge monotonicity.

For the edgeless graph on \(k\) vertices, every induced subgraph has \(q=1\), hence \(\kappa=2^k\). For the complete graph on \(s\) vertices, only identical total orders agree on all edges, so \(q(K_s)=1/s!\). Thus
\[
\kappa(K_k)=\sum_{s=0}^k\binom{k}{s}\frac{1}{s!(k-s)!}
=\frac1{k!}\sum_{s=0}^k\binom{k}{s}^2
=\frac1{k!}\binom{2k}{k}.
\]
Strict edge monotonicity gives precisely the equality cases in (2). For the three-vertex path, two independent orders agree on the two edges with probability \(q(P_3)=5/18\) (the four orientation-class sizes among the six total orders are \(1,1,2,2\)). The two all-one-color sectors contribute \(2(5/18)\); four mixed sectors contain an adjacent two-vertex edge and contribute \(4(1/2)\); two mixed sectors place the path endpoints together, contributing \(2\). This sums to \(41/9\), and the complete-core value is \(\binom63/3!=10/3\), proving (3).

## Verification

The standalone `CHECK.py` (Python standard library only) independently enumerates all pairs of uniform rank-order orientation classes for induced graphs of size at most four, verifies the exact rational coefficients \(\kappa\), and checks strict monotonicity under every possible edge addition on every labeled graph of size at most four. It also enumerates every ranking of the full leaf-corona graph for four small finite cases and computes the resulting collision probabilities directly as sums of squared orientation-class frequencies. Run `python CHECK.py`. The verified exact finite cases include a two-core edge with one and two leaves per core (probabilities \(11/72\) and \(859/16200\)), and the three-core path and triangle with one leaf per core (probabilities \(89/1800\) and \(13/400\)). These finite enumerations corroborate the probabilistic orientation model; they are **not** used as an infinite-dimensional proof. The all-graph, all-\(n\) identity (5) and the limits and equality cases rely on the analytic argument above.

## Relationship to prior work

Padrol, Pilaud and Poullot (arXiv:2111.12422) establish the graphical-zonotope and normal-fan framework. Iriarte (arXiv:1405.4880), particularly Sections 1 and 5, relates acyclic orientations, linear extensions, and spherical fractions of graphical-arrangement chambers. Those results provide the standard permutation interpretation of cone angles, but do not give the fixed-core pendant-blowup scaling law or the new graph-extremal partition coefficient. Stinson, Gleich and Constantine (arXiv:1602.06620) provide the general Gaussian normal-cone sampling principle.

The published *Gaussian angular collisions on double-star graphical zonotopes* (2026-10-18, at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-gaussian-angular-collisions-on-double-star-graphical-zonotopes--75406421a74c) establishes a sharp two-hub limit \(C_{n,n}\sim3/n^4\). That is the \(k=2\), single-edge specialization of (1), and is **explicitly excluded from the new claim**. The published *Two critical Rényi windows in the angular spectra of star-graph polytopes* gives the one-hub angular law and is likewise credited as known. The contribution assessed here is the arbitrary fixed-core \(k\ge3\) limiting partition formula, its full conditional core-color law, and the sharp strict graph-edge extremal theorem, not previously known special cases or the general acyclic-orientation bijection.

## Limitations

The theorem assumes a fixed finite core and exactly \(n\) private leaves per core vertex; it does not quantify uniformity when the core itself grows, and gives no rate of convergence. It requires independent isotropic Gaussian objectives in the specified intrinsic Euclidean metric. Formula (5) is an exact integral but is not claimed to yield a fast algorithm for general finite core size. Bibliographic searches cannot exclude an unindexed equivalent random-order formulation. This mathematical result has received only self-review, not independent mathematical validation.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422v1, first publicly posted 2021-11-24. https://arxiv.org/abs/2111.12422
2. B. Iriarte, *Graph Orientations and Linear Extensions*, arXiv:1405.4880 (2014), Sections 1 and 5. https://arxiv.org/abs/1405.4880
3. K. Stinson, D. F. Gleich, P. G. Constantine, *A randomized algorithm for enumerating zonotope vertices*, arXiv:1602.06620 (2016). https://arxiv.org/abs/1602.06620
4. *Gaussian angular collisions on double-star graphical zonotopes*, publicly indexed 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-gaussian-angular-collisions-on-double-star-graphical-zonotopes--75406421a74c
5. *Two critical Rényi windows in the angular spectra of star-graph polytopes*, publicly indexed 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-critical-r-nyi-windows-in-the-angular-spectra-of-star-graph--e1b409771cb8
