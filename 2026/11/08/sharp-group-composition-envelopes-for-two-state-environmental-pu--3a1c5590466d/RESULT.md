# Sharp group-composition envelopes for two-state environmental public-goods games

## Finding

Freeze the cooperative/defective strategies in a uniform public-goods hypergraph, and retain the state-dependent game-transition law of Wei et al. with sensitivity exponents \(\alpha_1=1\) and \(\alpha_2=2\). A group with cooperator fraction \(p\) remains high-value with probability \(p\) if already high-value, and becomes high-value with probability \(p^2\) if low-value. The stationary high-value probability is
\[
h(p)=\frac{p^2}{1-p+p^2}.
\]
For every integer group size \(g\ge2\), write \(a=\lfloor g/2\rfloor\), \(u=a/g\), and \(h_j=h(j/g)\). Let \(L_g:[0,1]\to[0,1]\) be the continuous polygonal function joining consecutively \((j/g,h_j)\) for \(j=0,\ldots,a\), then joining \((u,h_a)\) directly to \((1,1)\). Thus, for \(j=0,\ldots,a-1\) and \(j/g\le m\le(j+1)/g\),
\[
L_g(m)=(j+1-gm)h_j+(gm-j)h_{j+1},
\]
and for \(u\le m\le1\),
\[
L_g(m)=1-\frac{1-m}{1-u+u^2}.
\]

**Sharp occupancy envelope.** For any probability distribution \((w_0,\ldots,w_g)\) of cooperator counts in groups, define mean cooperator fraction \(m=\sum_{j=0}^g w_jj/g\) and stationary high-value fraction \(B=\sum_{j=0}^g w_jh_j\). Then
\[
\boxed{\quad L_g(m)\le B\le m.\quad}
\]
Both functions are the exact extremal bounds over all such distributions: every point on each bound is achievable with at most two supported group-composition values. The upper-bound equality distributions have support in \(\{0,g\}\). For \(m>u\), lower-bound equality distributions have support in \(\{a,g\}\) when \(g\) is even, or \(\{a,a+1,g\}\) when \(g\) is odd; two supported values suffice to achieve any specified \(m\). Below \(u\), lower extrema use adjacent cooperator counts. For odd \(g\), the points at \((a+1)/g\), \(a/g\), and \(1\) lie on a single supporting line. This is an exact group-size/parity-dependent phase transition in the minimizers.

For four-person groups at mean fraction \(m=3/4\), four homogeneous groups with three cooperators each have \(B=9/13\). Redistributing the same 12 cooperators among four disjoint groups as \((2,2,4,4)\) gives \(B=2/3\), while \((0,4,4,4)\) gives \(B=3/4\). Thus, at fixed aggregate cooperation, both an improvement and a deterioration of stationary high-value game abundance relative to homogeneous composition are possible; the entire attainable range has been classified above.

## Assumptions and scope

There are \(g\ge2\) players in each hyperedge and exactly two game states, high-value \(H\) and low-value \(L\). Strategies are frozen during the environmental equilibration measurement. A hyperedge with \(j\) cooperators has \(p=j/g\) and, whenever its game state is refreshed, obeys
\[
\Pr(H\mid H,p)=p,\qquad \Pr(H\mid L,p)=p^2.
\]
Every hyperedge is refreshed infinitely often; for convergence claims below, it is enough that each is selected independently of its current state with a fixed positive probability per time step. Simultaneous or overlapping-edge state updates may be correlated; the one-edge marginal law and its expected average do not require independence between edges. In a finite hypergraph, \(w_j\) is the empirical fraction of edges with \(j\) cooperators. In the sharpness assertion, arbitrary probability weights \(w_j\) are allowed; rational weights can be realized exactly by finitely many disjoint uniform hyperedges, and general weights by limits.

Only the environmental transition subsystem is analyzed, not the coevolving imitation dynamics of the motivating model. The bounds apply to any fixed uniform hypergraph but need not be exactly attainable within a fixed connected topology or a fixed specified number of edges. The high-value game may have any greater synergy than the low-value game; the probability bound is unaffected by the synergy magnitudes.

## Proof

**1. Stationarity and convergence.** Let \(q\) be a single hyperedge's high-value probability immediately before an update. Conditional on an update,
\[
q'=pq+(1-q)p^2=p^2+(p-p^2)q.
\]
Its unique fixed point is \(q=h(p)\), since \(1-p+p^2\ge3/4\). At the endpoints it is \(h(0)=0\) and \(h(1)=1\), with absorbing low and high states respectively. A Bernoulli refresh of probability \(\rho\in(0,1]\) replaces the recurrence multiplier by \(1-\rho(1-p+p^2)\in[0,1)\), so the marginal converges to \(h(p)\). Linearity of expectation gives \(B=\sum_jw_jh_j\), even if state updates between overlapping hyperedges are dependent.

**2. Universal upper bound.** Put \(D(p)=1-p+p^2\). The factorization
\[
p-h(p)=\frac{p(1-p)^2}{D(p)}\ge0
\]
is strict for \(0<p<1\). Averaging yields \(B\le m\). Conversely, assign mass \(1-m\) to groups with no cooperators and mass \(m\) to all-cooperator groups: this achieves \(B=m\). The strictness establishes the claimed upper equality support for \(0<m<1\).

**3. The lower supporting line.** The polynomial \(D(p)=(p-1/2)^2+3/4\) is minimal over the lattice \(\{0,1/g,\ldots,1\}\) at \(p=u\), and also at \(p=1-u\) if \(g\) is odd. The identity
\[
h(p)=1-\frac{1-p}{D(p)}
\]
therefore implies, at every lattice point,
\[
h(p)\ge 1-\frac{1-p}{D(u)}=:\ell_u(p).
\]
Equality holds at \(p=1\), at \(p=u\), and also at \(p=1-u=(a+1)/g\) when \(g\) is odd. The line \(\ell_u\) joins \((u,h(u))\) to \((1,1)\).

**4. Convex polygon.** Direct differentiation gives
\[
h'(p)=\frac{p(2-p)}{D(p)^2},\qquad
h''(p)=\frac{2(p^3-3p^2+1)}{D(p)^3}.
\]
The numerator of \(h''\) decreases on \([0,1/2]\) and is \(3/8\) at \(p=1/2\); thus \(h\) is strictly convex on \([0,1/2]\). Consequently the successive secant slopes between the lattice points \(0,1/g,\ldots,u\) are strictly increasing. The final segment has slope \(1/D(u)\), which satisfies
\[
\frac1{D(u)}-h'(u)
=\frac{(u-1)(2u-1)}{D(u)^2}\ge0
\]
because \(0<u\le1/2\). Hence \(L_g\) is convex. Moreover, it equals \(h\) at its early polygon vertices and equals \(\ell_u\) from \(u\) onward. By step 3, \(L_g(j/g)\le h_j\) at every lattice point.

**5. Sharp lower bound and equality.** Since \(L_g\) is convex,
\[
B=\sum_jw_jh_j\ge\sum_jw_jL_g(j/g)
\ge L_g\!\left(\sum_jw_jj/g\right)=L_g(m).
\]
On each of the segments defining \(L_g\), a mixture of the two endpoint group counts realizes every point exactly. Thus no larger pointwise lower bound is possible. Strict convexity on the early vertices implies that, below \(u\), lower-bound equality uses the two adjacent counts bounding the mean (or the single count at a vertex). On the final supporting segment the only contact counts are \(a,g\) when \(g\) is even and \(a,a+1,g\) when \(g\) is odd. These are exactly the stated high-mean equality restrictions. This proves the theorem.

## Verification

`check_envelope.py` uses exact rational arithmetic to verify the stationary identity, upper/lower lattice inequalities and convex polygon slopes for all group sizes \(2\le g\le80\) (3318 lattice points). It exhaustively checks 4970 unordered finite group-composition profiles for \(2\le g\le8\) and one through five groups. It also checks exact four-person witnesses \(2/3<9/13<3/4\). Run `python check_envelope.py` with Python 3.8 or newer; it has no third-party dependencies. These finite checks supplement, rather than prove, the all-\(g\) statement established above.

## Relationship to prior work

Wei, Xiong, Li, Feng and Szolnoki (2026, arXiv:2603.22967) introduce the uniform-hypergraph game-transition rule and study the full asynchronous coevolution of strategies and game states numerically. Their equations (6)–(7), with \(\alpha_1=1\), \(\alpha_2=2\), yield the exact two-state kernel here. Their analysis concerns dynamic cooperation levels and environmental-state quality/scale, not the fixed-cooperator-count extremal envelope derived above.

Su, McAvoy, Wang and Nowak (2019) study game transitions and cooperation under weak evolutionary selection. Pi, Feng, Deng, Chen and Szolnoki (2026, arXiv:2603.20603) optimize distributions of variable games in a pairwise selection framework. Neither comparison supplies, in the material inspected, the discrete \(g\)-dependent convex-envelope profile for the frozen-strategy hypergraph environmental chain. The generic stationary distribution of a two-state chain and the convexification/Jensen method are standard; novelty is asserted only for the exact model-specific envelope, parity contacts and the arrangement-reversal witnesses.

## Limitations

The result is an exact statement about stationary high-value game *abundance*, not average player welfare, evolutionary fixation, imitation-equilibrium stability, or the full coevolving process. A fixed finite edge count adds arithmetic restrictions on allowable mixing weights; a fixed connected hypergraph may restrict realizable group-count distributions even further. The two sensitivity exponents are fixed at \(1\) and \(2\); arbitrary exponent pairs need not obey this polygonal profile. No theorem is claimed for exponents outside those assumptions or for temporally changing cooperator strategies. Wider distributional convexification principles are already established; an unindexed instance of the particular sharp envelope remains possible.

## References

- N. Wei, X. Xiong, Q. Li, M. Feng and A. Szolnoki, *Cooperation in Public Goods Games over Uniform Random Hypergraphs with Game Transitions*, arXiv:2603.22967, first posted 2026-03-24. https://arxiv.org/abs/2603.22967 ; *J. R. Soc. Interface* **23** (2026), 20251319. https://doi.org/10.1098/rsif.2025.1319
- Q. Su, A. McAvoy, L. Wang and M. A. Nowak, *Evolutionary dynamics with game transitions*, arXiv:1905.10269, *PNAS* **116** (2019), 25398–25404. https://arxiv.org/abs/1905.10269
- B. Pi, M. Feng, L.-J. Deng, X. Chen and A. Szolnoki, *Evolutionary Dynamics of Variable Games in Structured Populations*, arXiv:2603.20603, first posted 2026-03-21; *IEEE Trans. Cybernetics* **56** (2026), 4559–4571. https://arxiv.org/abs/2603.20603
- Y. Zhang, M. Feng, Q. Li, M. Perc and A. Szolnoki, *Effects of Stochastic Games on Evolutionary Dynamics in Structured Populations*, arXiv:2602.07877, first posted 2026-02-08; *Communications Physics* **9** (2026), 101. https://arxiv.org/abs/2602.07877
