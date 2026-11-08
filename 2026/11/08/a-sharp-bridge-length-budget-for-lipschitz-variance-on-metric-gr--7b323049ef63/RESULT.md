# A sharp bridge-length budget for Lipschitz variance on metric graphs

## Finding

For each finite connected metric graph \(G\) with positive edge lengths, let \(L\) be the total arclength and \(B\) the total length of its bridge edges (edges whose deletion disconnects the graph). Equip \(G\) with normalized arclength probability \(\mu\). Then every real-valued one-Lipschitz map \(f:G\to\mathbb R\) satisfies

\[
\operatorname{Var}_{\mu}(f)\le \frac{(L+B)^3-4B^3}{48L}.
\]

The bound is sharp **for every** prescribed \(L>0\) and \(0\le B\le L\). For \(0<B<L\), it is attained by a balanced barbell: two cycles each of length \((L-B)/2\), joined by a bridge of length \(B\), with a unit-slope function increasing from the antipode of the first attachment, across the bridge, to the antipode of the second attachment. For \(B=0\), a circle is sharp, and for \(B=L\), a path is sharp. In particular the sharp universal constant interpolates continuously between \(L^2/48\) and \(L^2/12\).

At equality, the law of \(f(X)\), where \(X\sim\mu\), is uniquely determined up to a translation. For \(0<B<L\), it has density \(2/L\) on each of two outer intervals of length \((L-B)/4\), and density \(1/L\) on the intervening interval of length \(B\). This equality-law statement does **not** assert a classification of all metric graphs attaining the bound.

Equivalently, the squared norm of the canonical centered map from \(\operatorname{Lip}(G)/\mathbb R\), with its Lipschitz seminorm, to \(L^2(G,\mu)\) obeys the same sharp envelope in the pair \((L,B)\).

## Assumptions and scope

A finite metric graph is the geometric realization of a finite connected combinatorial graph with every edge replaced by a closed interval of positive finite length, with the induced shortest-path distance. Subdivision of an edge does not change the graph or its total bridge length. Vertices have zero mass; \(\mu\) is arclength divided by \(L\). A *bridge* is an edge whose interior-point deletion disconnects the geometric realization; equivalently its combinatorial deletion disconnects the graph. Thus \(0\le B\le L\). The function \(f\) is real-valued, continuous, and globally one-Lipschitz. The assertion applies to all finite graph topologies, all positive edge lengths, and all such \(f\), without assuming piecewise-affinity or monotonicity.

## Proof

**1. The one-crossing levels occupy at most the bridge budget.** Let \(m=\min_G f\), \(M=\max_G f\), and suppose \(m<M\). For almost every \(y\in(m,M)\), the one-dimensional area formula on the finite edge intervals counts \(N(y)\), the finite number of preimages at nonzero metric derivative, with multiplicities. Every intermediate level has at least one crossing; any level with exactly one crossing must cross the interior of a bridge. Indeed, if such a point lay on a nonbridge edge, deleting the point would leave the graph connected, so a path avoiding it between a point below and a point above \(y\) would contradict continuity. These assertions remain true outside a null set of critical values, by the one-dimensional area formula and absolute continuity of \(f\) on each edge.

Let \(E\subset(m,M)\) consist of levels with only one crossing. The image of any bridge edge has Lebesgue length at most that edge's length, hence

\[|E|\le\sum_{e\,\mathrm{bridge}}|f(e)|\le B.\]

The pushforward probability \(\nu=f_*\mu\) dominates \(N(y)\,dy/L\): at regular values each crossing contributes the reciprocal of the local speed, at least one. Thus its absolutely continuous density is at least \(1/L\) on the whole intermediate range and at least \(2/L\) outside \(E\). Any additional singular or atomic mass strengthens these inequalities.

**2. A sharp inverse-quantile derivative budget.** Let \(Q:[0,1]\to[m,M]\) be the nondecreasing generalized quantile of \(\nu\), choosing its continuous representative. The preceding density bound implies \(Q\) is absolutely continuous and \(L\)-Lipschitz; denote its almost-everywhere derivative by \(h=Q'\), where \(0\le h\le L\). At points with \(Q(u)\notin E\) and with nonzero derivative, the density lower bound gives \(h(u)\le L/2\). The substitution formula for an absolutely continuous monotone map therefore yields

\[
\int_0^1(2h(u)-L)_+\,du
\le \int_{\{h>L/2\}}h(u)\,du
\le |E|\le B.
\]

Atoms of \(\nu\), when present, give flat quantile intervals with \(h=0\), hence cannot invalidate this estimate. The case \(m=M\) is trivial.

**3. Reduce variance to a one-dimensional extremal problem.** For uniform \(U\in[0,1]\), \(Q(U)\) has law \(\nu\). Set

\[
K(s,t)=\min(s,t)-st,\qquad 0\le s,t\le1.
\]

Writing \(Q(U)=Q(0)+\int_0^1h(s)\mathbf 1_{\{U\ge s\}}\,ds\) and centering gives the identity

\[
\operatorname{Var}(Q(U))
=\int_0^1\!\int_0^1h(s)K(s,t)h(t)\,ds\,dt.\tag{1}
\]

The kernel is strictly positive in the open square and positive definite: the right side is the variance of the absolutely continuous primitive of \(h\), and vanishes only for \(h=0\) almost everywhere. Increasing \(h\) pointwise increases (1). We may replace \(h\) by \(\max\{h,L/2\}\) without changing the budget. Put \(\beta=B/L\) and \(h=(L/2)(1+z)\) with \(0\le z\le1\). The budget becomes \(\int z\le\beta\). Because the kernel is positive in the interior, maximization can be restricted to \(\int z=\beta\), with \(z\equiv0\) for \(\beta=0\) and \(z\equiv1\) for \(\beta=1\).

**4. The optimal increased-slope budget is the central interval.** For \(0<\beta<1\), consider

\[
\mathcal J(z)=\int_0^1\!\int_0^1(1+z(s))K(s,t)(1+z(t))\,ds\,dt,
\quad 0\le z\le1,\quad\int z=\beta.
\]

A maximizer exists by weak-* compactness and continuity of the quadratic form with continuous kernel. Strict positive definiteness forces each maximizer to be an indicator \(z=\mathbf1_A\) almost everywhere: on a set with fractional \(z\), two opposite nonzero zero-integral perturbations remain admissible, and strict convexity makes their average value strictly greater than the middle value. The first-order mass-exchange condition for \(A\) says it occupies the \(\beta\) highest values of

\[
H(s)=\int_0^1K(s,t)(1+\mathbf1_A(t))\,dt.
\]

In distributions, \(-H''=1+\mathbf1_A>0\), with \(H(0)=H(1)=0\). Thus \(H\) is strictly concave and its highest-value set of measure \(\beta\) must be an interior interval \(A=(a,b)\) of length \(b-a=\beta\). The boundary exchange condition \(H(a)=H(b)\) then yields, by direct integration,

\[
H(a)-H(b)=\frac{\beta(1+\beta)}2(a+b-1).
\]

Consequently \(a+b=1\), so the unique maximizer is \(A=((1-\beta)/2,(1+\beta)/2)\), modulo null sets. This establishes the rearrangement step **globally**, not merely among intervals.

**5. Integrate and attain.** The optimal quantile derivative equals \(L/2\) on the two outer probability intervals, and \(L\) on the central interval of probability length \(\beta\). Its centered distribution has density \(2/L\) on the outer value intervals of length \((L-B)/4\) each, and density \(1/L\) on a central value interval of length \(B\). Direct integration of its second centered moment gives

\[
\frac{2}{L}\left[\int_0^{B/2}x^2\,dx
+2\int_{B/2}^{B/2+(L-B)/4}x^2\,dx\right]
=\frac{(L+B)^3-4B^3}{48L}.
\]

On the balanced barbell, take the function increasing at unit slope from the antipode of the left cycle to its bridge attachment along both half-cycles, across the bridge, and similarly from the right bridge attachment to the antipode of the right cycle. It is globally one-Lipschitz since every traversed edge has speed at most one; the above density profile follows exactly from one bridge crossing and two loop crossings. The limiting cases are realized by a circle and a path. Sharpness and the claimed unique equality law follow.

## Verification

Run `python3 verify_bridge.py` from the package directory using the Python standard library. The checker separately enumerates all bang-bang quantile-slope locations on uniform meshes of sizes two through ten, symbolically evaluates the balanced-barbell second moment at 135 rational parameter pairs, and checks 16,200 rational one-Lipschitz piecewise-affine functions on sampled connected metric graphs. The final success marker is `ALL_BRIDGE_BUDGET_VARIANCE_CHECKS_OK`. This is finite corroboration; the unrestricted theorem follows from the coarea and rearrangement argument above. No external solver or downloaded data are required.

## Relationship to prior work

The graph-spread functional goes back to Alon, Boppana and Spencer and is developed for uniform **vertex** measures and random graphs by Addario-Berry, Janson and McDiarmid [1]. Dzindzalieta [2] studies sharp deviation inequalities for Lipschitz functions on general metric probability spaces, but does not establish the arclength bridge-budget variance envelope. Nakajima and Shioya [3] give isoperimetric-profile *conditional* observable-variance comparisons; a fixed total bridge length does not supply the requisite domination by a common one-dimensional isoperimetric profile, since one-ended pendant graphs and balanced barbells have different small-volume cut behavior. Mazón [4] develops Cheeger cuts and perimeter on metric graphs rather than the global, fixed-bridge-length variance extremum. The two-crossing bridgeless case is the \(B=0\) boundary of this theorem, not the new contribution. The positive-bridge interpolation, its polynomial sharp constant, and its equality distribution are the present claim. Equivalent unindexed literature remains possible.

## Limitations

The probability measure is **normalized arclength** with no vertex atoms or nonconstant edge densities; the target is real and the observables are globally one-Lipschitz. The bound is universal given \((L,B)\), but it need not be attained on any prescribed graph. The theorem specifies the output law of equality but does not classify all attaining graph geometries. It does not assert a convex-order envelope for all centered output laws; variance alone is optimized. Different upper-tail objectives can favor different positions of the one-crossing levels. No independent proof review is claimed.

## References

[1] L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first submitted 2009-02-06), https://arxiv.org/html/0902.1156v2.

[2] D. Dzindzalieta, *Extremal Lipschitz functions in the deviation inequalities from the mean*, arXiv:1205.6300 (first submitted 2012-05-29), https://arxiv.org/abs/1205.6300.

[3] H. Nakajima, T. Shioya, *Isoperimetric rigidity and distributions of 1-Lipschitz functions*, arXiv:1801.01302 (first submitted 2018-01-04), https://arxiv.org/abs/1801.01302.

[4] J. M. Mazón, *The Cheeger cut and Cheeger problem in metric graphs*, Analysis and Mathematical Physics 12 (2022), article 117, https://doi.org/10.1007/s13324-022-00729-y.
