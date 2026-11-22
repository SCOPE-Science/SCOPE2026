# A single edge activates primitive-three parallel chip-firing on triangular books

## Finding
For every integer \(n\ge2\), let \(B_n=K_2\vee\overline K_n\) be the triangular book: two adjacent labelled hubs, each adjacent to all \(n\) labelled independent leaves. In the synchronous degree-threshold chip-firing map \(U\), each vertex with at least its degree in chips simultaneously sends one chip to each neighbor. Define the mass-resolved *initially primitive-three* polynomial
\[
H_n(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{n+2}\\U^3x=x,\ Ux\ne x}}z^{\sum_vx(v)}.
\]
The exact formula is
\[
\boxed{H_n(z)=6\sum_{j=0}^{n-1}\left(\sum_{k=0}^{j}\binom nk\right)\left(z^{2n+1+j}+z^{5n+1-j}\right).}
\]
Thus the complete mass support consists of the integer intervals \([2n+1,3n]_{\mathbb Z}\) and \([4n+2,5n+1]_{\mathbb Z}\), and the gap \([3n+1,4n+1]_{\mathbb Z}\) contains no initially primitive-three state. Every integer mass in both bands occurs. There are exactly \(6n\,2^n\) such labelled states and \(2n\,2^n\) distinct three-state orbits. The two end masses of each band have coefficients \(6\) and \(6(2^n-1)\), respectively, in opposite orders.

A one-edge change is decisive: the hub-edge deletion of \(B_n\) is \(K_{2,n}\), on which no period-three state exists, by the published complete-bipartite period classification [1, Theorem 3.10].

If \(M_n\) is the conserved mass of a uniformly chosen primitive-three state, then
\[
\frac{M_n}{n}\ \Longrightarrow\ \frac12\operatorname{Unif}[5/2,3]+\frac12\operatorname{Unif}[4,9/2].
\]
Here \(\operatorname{Unif}[a,b]\) denotes uniform probability measure on the indicated interval.

## Assumptions and scope
The graph is finite, simple, undirected, connected, and labelled, with integer \(n\ge2\). Both hubs have degree \(n+1\), every leaf has degree two, and chips are arbitrary nonnegative integers. Firing occurs when the chip count is *at least* the degree, with all decisions made before transfers. Only states periodic at time zero with least period three are counted; attraction basins, first-entry times, and other periods are not classified. Each temporal rotation of a three-orbit is a distinct labelled initial configuration.

## Proof
**1. Number of firings in three steps.** Write \(f_t(v)\in\{0,1\}\) for the firing indicator at update \(t\). If \(U^3x=x\), conservation at each vertex gives \(L\sum_{t=0}^2f_t=0\), where \(L\) is the ordinary graph Laplacian. Because the graph is connected, its real Laplacian kernel is the constants; every vertex fires the same number \(c\) of times. If \(c=0\) or \(c=3\), all vertices always wait or always fire, so the state is fixed. Therefore a primitive-three configuration has \(c=1\) or \(c=2\).

**2. Complementary halves.** In a periodic state of period greater than one, each vertex waits on at least one of the three updates. At that waiting time its chip count is at most its degree minus one. The interval from zero through twice the degree minus one is forward invariant at every vertex: a waiting vertex gains at most its degree, while a firing vertex loses its degree and receives at most its degree. Thus all chip counts in the periodic orbit satisfy \(0\le x(v)\le2\deg(v)-1\). On this bounded set define \(Cx(v)=2\deg(v)-1-x(v)\). It has the opposite firing indicators, and a direct substitution into the update equation gives \(U(Cx)=C(Ux)\). Hence \(C\) bijects once-firing and twice-firing primitive-three states. It reflects total chip mass about
\[
S=\sum_v(2\deg(v)-1)=2(2n+1)+3n=7n+2.
\]

**3. Every once-firing pattern.** Assign each vertex its unique firing phase in \(\{0,1,2\}\). Suppose the two hubs have equal phase. Rotating time, both fire at phase zero. Direct degree-two threshold inequalities show that every leaf would have to fire at phase one. Each hub would then have the same chip count at times zero and two, although it must fire at time zero and wait at time two: contradiction. Thus the hubs have distinct phases.

There are exactly six ordered pairs of distinct hub phases. By rotating the three times and optionally interchanging the two labelled hubs, it suffices to analyze hub phases zero and one. Every leaf must then fire at phase one or phase two. Its unique allowed initial chip count is respectively one or zero. Let \(k\) of the \(n\) leaves fire at phase one. The phase-one hub must have precisely \(n\) initial chips. The phase-zero hub has an integer initial chip count in exactly the interval
\[
[n+1,2n-k]_{\mathbb Z}.
\]
These conditions follow by applying the degree \(n+1\) firing and waiting thresholds at times zero, one, and two; they are also sufficient, since the derived chip trajectory realizes all assigned indicators and returns after three updates. The range contains \(n-k\) values, so \(k=n\) is impossible. The total initial chip mass is exactly one of
\[
[2n+1+k,3n]_{\mathbb Z},
\]
with one realization of each mass for every fixed selection of the \(k\) phase-one leaves. There are \(\binom nk\) such selections, and the six choices of ordered hub phases give distinct labelled states. Consequently the once-firing mass polynomial is
\[
H^{(1)}_n(z)=6\sum_{j=0}^{n-1}\left(\sum_{k=0}^{j}\binom nk\right)z^{2n+1+j}.
\]
The total once-firing population is
\[
6\sum_{k=0}^{n-1}(n-k)\binom nk=6n\,2^{n-1}.
\]
Applying the complement from step 2 yields \(H_n(z)=H^{(1)}_n(z)+z^{7n+2}H^{(1)}_n(z^{-1})\). This proves the stated polynomial, masses, and total state/orbit counts. The hub phases differ, so these configurations cannot be fixed; because the third iterate returns, their least period is three.

**4. Single-edge activation.** Removing just the hub edge gives \(K_{2,n}\). Jiang's 2010 complete-bipartite period theorem [1, Theorem 3.10] permits only least periods one, two, and four for this graph, whereas the preceding construction produces \(6n\,2^n>0\) immediate primitive-three configurations after the edge is added. This comparison does not assert monotonicity of periods under arbitrary edge additions.

**5. Normalized-mass limit.** Conditional on a once-firing state, let \(K\) be the number of phase-one leaves, and let \(J\) be the offset of the first hub's chip count from its minimum. The exact weights imply
\[
\Pr(K=k)=\frac{(n-k)\binom nk}{n2^{n-1}}=\frac{\binom{n-1}{k}}{2^{n-1}},\qquad
J\mid K=k\sim\operatorname{Unif}\{0,\ldots,n-k-1\}.
\]
Thus \(K\sim\operatorname{Bin}(n-1,1/2)\), \(K/n\to1/2\) in probability, and \(J/n\Rightarrow\operatorname{Unif}[0,1/2]\). Since \(M_n=2n+1+K+J\) in this class, its normalized mass converges to \(\operatorname{Unif}[5/2,3]\). Complementation supplies the equally numerous reflected class, converging to \(\operatorname{Unif}[4,9/2]\). This proves the stated mixture limit.

## Verification
Two independently structured standalone scripts accompany this document. Execute `python3 verify_direct.py` and `python3 verify_phase.py` using Python 3's standard library, from the folder containing them. The captured outputs are `direct_output.txt` and `phase_output.txt`.

The first script directly evolves every bounded initial configuration for \(1\le n\le6\), including \(802{,}816\) states at \(n=6\), testing the equality \(U^3x=x\ne Ux\) and each mass coefficient. The second script reconstructs the integer initial-state ranges from all \(3^{n+2}\) possible one-firing phase assignments for \(1\le n\le8\), independently of direct state iteration, and checks the once-firing coefficients. Both passed when executed in the package's construction environment. Tests are finite checks supporting, not replacing, the general proof.

## Relationship to prior work
Jiang [1] proves the common-firing-count criterion, complement symmetry, and a complete classification of *possible periods* on complete bipartite graphs, together with constructions on complete multipartite graphs (which include \(B_n=K_{n,1,1}\)). The present theorem supplies the exact population at every chip mass on this three-partite graph, a distributional limit, and the one-edge comparison; possible-period existence alone does not determine those quantities. Scully, Jiang and Zhang [2] characterize firing patterns in general and study motor constructions, but do not give this labelled book-graph mass census. The earlier general mass-exclusion results [3] constrain the feasible middle range; they do not supply the exact two bands and their coefficients here.

## Limitations
No result is asserted about eventual period-three basins, transient lengths, primitive periods other than three, or different graph operations. The normalized-mass limit is conditional on the uniformly selected immediate primitive-three class, not on uniformly random unconstrained initial chips. Historical-priority searches are non-exhaustive; inaccessible full texts and unindexed equivalent formulations remain possible. This research has not received an independent mathematical audit.

## References
[1] Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, first arXiv public submission March 4, 2010, arXiv:1003.0943, especially Proposition 2.5, Theorem 3.10 and Section 4. https://arxiv.org/abs/1003.0943

[2] Tian-Yi Jiang, Ziv Scully, Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first arXiv public submission November 29, 2012, arXiv:1211.6786; see also Scully, Jiang and Zhang, *Firing Patterns in the Parallel Chip-Firing Game*, DMTCS Proceedings, 2014. https://arxiv.org/abs/1211.6786

[3] David Ji, Michael Li, Daniel Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508 (2024). https://arxiv.org/abs/2408.10508
