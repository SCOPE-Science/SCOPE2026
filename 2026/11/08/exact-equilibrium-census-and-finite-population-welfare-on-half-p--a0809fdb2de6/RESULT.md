# Exact equilibrium census and finite-population welfare on half-peaked Schelling rings

## Finding

Consider a ring with \(n=b+r\ge3\) **labeled vertices**, with \(1\le b\le r\) blue and red occupants, respectively. Every vertex is occupied. Utility is a common symmetric single-peaked function of the fraction of own-type agents in the **closed** neighborhood, with its unique maximum at \(1/2\). Two unlike agents may swap positions only if both strictly improve. A configuration is a swap equilibrium if no such move is possible. Let integration be the number of vertices with at least one opposite-type neighbor.

**Exact structural criterion.** A configuration is a swap equilibrium if and only if at least one of the two colors has no monochromatic run of three consecutive vertices. Equivalently, all monochromatic runs of at least one color have length at most two.

**Exact welfare and equilibrium count.** Put \(m=\lceil b/2\rceil\). Among all color configurations, the maximum integration, and among all swap equilibria, the minimum integration, are respectively

\[
I^*(b,r)=\min\{b+r,3b\},\qquad I_{\min}^{\mathrm{SE}}(b,r)=b+\min\{r,m+1\}.
\]

Consequently the exact degree-of-integration price of anarchy is

\[
\operatorname{PoA}(C_{b+r};b,r,1/2)=
\frac{\min\{b+r,3b\}}{b+\min\{r,\lceil b/2\rceil+1\}}.
\]

For nonnegative integers \(a,t\), let \(\binom at=0\) when \(t>a\). Define

\[
F(x,y)= (x+y)\sum_{k=1}^{\min(x,y)}\frac1k
  \binom{k}{x-k}\binom{y-1}{k-1},
\quad
H(b,r)=(b+r)\sum_{k=1}^{b}\frac1k
 \binom{k}{b-k}\binom{k}{r-k}.
\]

Then the number of swap equilibria **as colorings of the labeled ring** is exactly

\[
N(b,r)=F(b,r)+F(r,b)-H(b,r).
\]

If each of the \(b\) blue and \(r\) red agents is individually labeled, the number of complete agent placements inducing swap equilibria is \(b!r!\,N(b,r)\). No rotational or reflection quotient is taken.

For example, \((b,r)=(4,8)\) has exactly \(399\) stable colorings, optimal integration \(12\), and worst equilibrium integration \(7\), so the exact price of anarchy is \(12/7\). For even \(b=2h\) with \(r\ge2b\), it equals \(6h/(3h+1)\), approaching the upper bound \(2\) from below with an explicit finite-population correction.

## Assumptions and scope

The graph is the simple cycle \(C_n\) for \(n\ge3\). Two colors are present and the count \(b\) denotes the smaller color class. Every vertex has degree two, there are no vacancies, and swaps can be between any pair of unlike-color agents (not only adjacent ones). The value of an agent with own-type closed-neighborhood fraction \(z\) is \(p(z)\), where \(p:[0,1]\to[0,1]\) is strictly increasing on \([0,1/2]\), satisfies \(p(0)=p(1)=0\), \(p(1/2)=1\), and \(p(z)=p(1-z)\). These are the half-peak assumptions of the original single-peaked swap model; there is **no additional tie breaking** between the fractions \(1/3\) and \(2/3\).

An agent is integrated if at least one of the two neighboring vertices has the other color. Integration, not the sum of the agents' utilities, is the welfare measure. All extrema and counts are over **all** configurations with the specified population counts. The numerical verifier samples no real-valued functions \(p\), because the theorem's comparisons depend only on the three achievable neighborhood fractions and are independent of the particular admissible \(p\).

## Proof

**1. Reduction of profitable swaps.** Every agent's own-type fraction in its three-element closed neighborhood belongs to \(\{1/3,2/3,1\}\). By symmetry of the peak, \(p(1/3)=p(2/3)>0\), while \(p(1)=0\). Thus an agent can strictly improve only when both neighbors currently have its own color; in this case its current utility is zero. A profitable swap requires both moving agents to have zero utility and hence to be of opposite colors and each the middle of a monochromatic triple. Such vertices are necessarily nonadjacent. After the exchange, each moving agent has neighbors of the opposite color, giving fraction \(1/3\) and strictly positive utility. The condition is therefore both necessary and sufficient. In run language, such a centered triple exists in a given color precisely when one of its maximal monochromatic runs has length at least three.

**2. The count of stable configurations.** Every nonconstant cyclic two-coloring has \(k\) blue runs alternating with \(k\) red runs, where \(1\le k\le\min(b,r)\). The number of ordered positive length compositions of \(b\) into \(k\) blue runs, each of length at most two, is \(\binom{k}{b-k}\): choose which runs have length two. The number of unrestricted ordered positive compositions of \(r\) into \(k\) red runs is \(\binom{r-1}{k-1}\).

Mark the first vertex of one blue run and its labeled position on the ring. There are \(n\) possibilities for that position, followed by the two ordered run compositions. Each coloring with \(k\) blue runs is thereby counted exactly \(k\) times. Division by \(k\) yields \(F(b,r)\), counting colorings with no blue run of length three; exchanging color names gives \(F(r,b)\). Requiring both colors to have runs of length at most two instead gives \(\binom{k}{b-k}\binom{k}{r-k}\) ordered pairs of compositions, and the same marking argument gives \(H(b,r)\). The stability criterion and inclusion-exclusion prove the formula \(N=F(b,r)+F(r,b)-H(b,r)\).

**3. Maximum integration.** A monochromatic run of length \(\ell\ge1\) contributes exactly \(\min\{\ell,2\}\) integrated vertices: its one or two boundary vertices. Hence all \(b\) blue vertices and at most \(2b\) red vertices can be integrated, so integration is at most \(\min\{n,3b\}\). To attain it, place the blue vertices as singletons separated by \(b\) nonempty red runs (possible since \(r\ge b\)). If \(r\le2b\), choose all red run lengths in \(\{1,2\}\), integrating everyone. If \(r>2b\), choose each red run of length at least two, integrating exactly \(2b\) red and all \(b\) blue vertices.

**4. Minimum equilibrium integration.** Suppose first that an equilibrium has no blue run of length at least three. If it has \(k\) blue runs then \(k\ge\lceil b/2\rceil=m\), all \(b\) blue agents are integrated, and its \(k\) red runs contribute at least \(\min\{r,k+1\}\) integrated vertices. Indeed, when \(r=k\) every red run is a singleton; otherwise at least one run contributes two and all others at least one. Thus the integration is at least \(b+\min\{r,m+1\}\). Equality is attainable by choosing \(k=m\) blue runs of lengths one or two summing to \(b\), \(m-1\) singleton red runs, and one remaining red run of length \(r-m+1\).

If instead an equilibrium has no red run of length at least three, it has at least \(\lceil r/2\rceil\) red runs, giving integration at least \(r+\min\{b,\lceil r/2\rceil+1\}\). This cannot be lower than the preceding bound: for \(b\ge2\), \(m+1\le b\le r\) and \(\lceil r/2\rceil\ge m\), hence the latter bound is at least \(r+m+1\ge b+m+1\). For \(b=1\) it is at least \(r+1\ge 1+\min\{r,2\}\). The displayed construction is stable, so the lower bound is exact. Division of the optimum by the attained minimum yields the price-of-anarchy formula.

## Verification

The included `verify_cycle.py` enumerates each choice of the blue vertices for every integer \(3\le n\le15\) and \(1\le b\le\lfloor n/2\rfloor\). It independently checks strict improvement by performing every unlike-color pairwise swap and evaluating the two moving agents' utilities after the move, then compares stable membership, exact counts, and extrema against the proved formulas. Executing `python verify_cycle.py` prints:

```
PASS: 55 population instances, 35103 distinct fixed-count cyclic color profiles, 19506 equilibria.
Exact swap condition, stable census, minimum and maximum degree of integration verified through n=15.
```

All arithmetic for the counting formulas is exact, with binomial coefficients and rational fractions. The finite enumeration independently tests the derivation for small sizes but is not used as a proof of the universal claims; Steps 1–4 are the general proof.

## Relationship to prior work

Bilò, Bilò, Lenzner and Molitor introduced the single-peaked swap model with the same closed-neighborhood convention. Their Lemma 5 proves the general necessary condition that segregated agents of opposite colors cannot coexist in a swap equilibrium, Theorem 1 proves convergence on almost regular graphs for the tolerant half-peak regime, and Theorem 8 exhibits a family of rings with price of anarchy approaching two. The present result gives the **if-and-only-if ring condition**, a complete fixed-population equilibrium count, and the exact finite-population maximum and minimum integration. The general bound and asymptotic witness are respected and refined rather than contradicted.

The earlier work *Topological Influence and Locality in Swap Schelling Games* obtains an exact cycle price-of-anarchy formula for the **monotone, own-type-preferring** Schelling model, with its own welfare definition. Its cycle Theorem 12 does not yield the half-peaked, closed-neighborhood integration formula here: the underlying payoff orderings are different. The *Single-Peaked Jump Schelling Games* literature admits empty vertices and unilateral jumps rather than two-agent swaps, so its ring results address different deviations and states. These comparisons do not establish that an equivalent result is absent from all literature.

## Limitations

The formulas depend on a degree-two ring, two colors, full occupancy, symmetric peak at one half, strict improvement by **both** agents, and full freedom to swap distant seats. They are not asserted for non-cycle graphs, jump dynamics, adjacent-only swaps, different peak values, or utilities with asymmetrically resolved ties. The count is for labeled vertices and unlabeled agents within each color, with the explicit factorial conversion for fully labeled agents. Independent external review and a comprehensive proof of publication priority have not been performed.

## References

1. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (first public version April 26, 2022), IJCAI 2022, DOI 10.24963/ijcai.2022/12. https://arxiv.org/abs/2204.12599
2. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, Autonomous Agents and Multi-Agent Systems 36, article 47 (2022), DOI 10.1007/s10458-022-09573-7. https://link.springer.com/article/10.1007/s10458-022-09573-7
3. T. Friedrich, P. Lenzner, L. Molitor, L. Seifert, *Single-Peaked Jump Schelling Games*, arXiv:2302.12107 (2023). https://arxiv.org/abs/2302.12107
