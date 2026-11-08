# Parity obstructions and random rarity of balanced EF1 in two-sparse group sharing

## Finding

Fix two nonempty groups of agents, one group indexed by the vertices of a finite loopless Eulerian multigraph \(G\), and a second group of agents indifferent to every valued good. Each edge is one indivisible good worth one to its two endpoints and zero to all other agents. Write \(m=|E(G)|\), and let \(r\) denote the number of connected components containing an odd number of edges (isolated vertices are not counted). In a complete allocation, let \(X\subseteq E(G)\) be the goods assigned to the first group. Then

\[
\min_{\mathrm{EF1}}|X|=\frac{m+r}{2},\qquad
\min_{\mathrm{EF1}}\bigl||X|-(m-|X|)\bigr|=r.
\]

A cardinality-balanced EF1 allocation (bundle-size difference at most one) exists if and only if \(r\le1\). If \(h\ge0\) completely unvalued extra goods are added, the minimum possible cardinality difference becomes

\[
\max\{(m+h)\bmod 2,\ r-h\},
\]

and a cardinality-balanced EF1 allocation exists exactly when \(h\ge\max\{0,r-1\}\).

For the subcase that \(G\) is a simple 2-regular graph, write \(e\) for its number of even cycles and \(\mathcal O\) for its set of odd cycles. The number of EF1 allocations attaining \(\min|X|\) is exactly

\[
2^e\prod_{C\in\mathcal O}|V(C)|.
\]

For a uniformly random labeled simple 2-regular graph \(G_n\) on \(n\ge3\) vertices, let \(P_n\) be the probability that a balanced EF1 allocation exists. Define

\[
E(z)=e^{-z^2/4}(1-z^2)^{-1/4},\quad
O(z)=\tfrac12(\operatorname{artanh}z-z),\quad
D(z)=e^{-z/2-z^2/4}(1-z)^{-1/2}.
\]

Then an exact finite formula and sharp parity-dependent asymptotics are

\[
P_n=\frac{[z^n]E(z)(1+O(z))}{[z^n]D(z)},\qquad
C=\frac{e^{1/2}2^{3/4}\sqrt\pi}{\Gamma(1/4)},
\]

\[
P_n\sim Cn^{-1/4}\quad(n\to\infty\text{ through even integers}),
\qquad
P_n\sim\frac C4n^{-1/4}\log n\quad(n\to\infty\text{ through odd integers}).
\]

## Assumptions and scope

There are exactly two *fixed* nonempty groups. Every agent in the second group assigns value zero to every good. An agent corresponding to a vertex in the first group values exactly its incident edges at one each, with additive utilities. The graph has no loops; parallel edges are permitted in the deterministic statement; every vertex has even degree (including zero). Edges are distinct goods, and no disposal is allowed. An allocation is EF1 if, for each agent \(i\), either its group bundle has at least as much utility as the other group bundle or there is a single good in the *other* bundle whose removal eliminates its envy. Cardinality balance concerns the number of goods, not agents or utility. For the probability theorem, the graph is simple, all vertices have degree two, and is drawn uniformly from the finite set of labeled 2-regular graphs; the extra unvalued-goods parameter is then zero.

## Proof

**1. Characterizing EF1.** Denote a first-group vertex's degree by \(d_v\), and the count of its incident edges in \(X\) by \(x_v\). Since the vertex values its first-group bundle at \(x_v\) and the other group's bundle at \(d_v-x_v\), its EF1 constraint is precisely \(x_v\ge d_v-x_v-1\). As \(d_v\) is even, integer rounding makes this equivalent to \(x_v\ge d_v/2\). Agents in the second group never envy. Thus these vertex inequalities are necessary and sufficient for group EF1.

**2. Exact minimum.** For a nontrivial connected component \(H\) with \(t\) edges, sum the vertex inequalities. Every selected edge contributes two to the left-hand sum and \(2t\) to the degree sum, giving \(|X\cap E(H)|\ge\lceil t/2\rceil\). Since \(H\) is connected and Eulerian, choose a closed Euler tour. Color its successive edges alternately for the two groups. If \(t\) is even, every vertex has equally many incident edges of both colors (including the start vertex). If \(t\) is odd, start and end with the first color: all vertices except the start have equal color degrees, and the start has an excess of two first-color edges. In either case the first-group count is exactly \(\lceil t/2\rceil\) and all EF1 inequalities hold. Summing over components proves \(|X|\ge(m+r)/2\) with equality attained. Moving any edge from the second to the first group never violates the inequalities; hence every integer first-group count between \((m+r)/2\) and \(m\) can be attained.

**3. Null goods and balance.** With \(h\) extra goods having utility zero for all agents, any subset of the null goods can go to either group without changing EF1. Consequently all integer first-group bundle sizes from \((m+r)/2\) to \(m+h\) are attainable. Their closest distance from half the total \(m+h\) is exactly \(\max\{(m+h)\bmod 2,r-h\}\); this yields both the minimum imbalance and the required and sufficient null-good budget. Taking \(h=0\) yields the initial statements.

**4. Counting cycle optimizers.** If \(G\) is 2-regular, every first-group vertex must receive at least one of its two incident edge goods, so the edges given to the second group form a matching. Minimum \(|X|\) corresponds to a maximum matching in each cycle. An even cycle has exactly two perfect matchings; an odd cycle of length \(\ell\) has exactly \(\ell\) maximum matchings. Multiply these independent component counts.

**5. Exact random model.** A labeled undirected cycle on \(\ell\ge3\) vertices has \((\ell-1)!/2\) realizations. The exponential formula for labeled disjoint unions therefore gives the 2-regular graph EGF

\[
\exp\!\left(\sum_{\ell\ge3}\frac{z^\ell}{2\ell}\right)=D(z).
\]

Even cycles alone give \(E(z)=\exp(\sum_{j\ge2}z^{2j}/(4j))\), and one marked odd cycle has EGF \(O(z)=\sum_{j\ge1}z^{2j+1}/(2(2j+1))\). By the deterministic criterion, a graph is favorable precisely if it has zero or one odd cycle. Its EGF is therefore \(E(z)(1+O(z))\), proving the exact probability formula (the common \(n!\) cancels).

**6. Asymptotic transfer.** Standard binomial-coefficient/Gamma asymptotics at the unique dominant singularity of \(D(z)\) give

\[
[z^n]D(z)\sim\frac{e^{-3/4}}{\sqrt{\pi n}}.
\]

For even \(n=2s\), only \(E(z)\) contributes and the change of variable \(w=z^2\) gives

\[
[z^{2s}]E(z)=[w^s]e^{-w/4}(1-w)^{-1/4}
\sim\frac{e^{-1/4}}{\Gamma(1/4)}s^{-3/4}.
\]

For odd \(n=2s+1\), write \(O(z)=zH(z^2)\), where

\[
H(w)=\frac{\operatorname{artanh}(\sqrt w)-\sqrt w}{2\sqrt w}
=\frac14\log\frac1{1-w}+O(1)
\quad(w\to1).
\]

The logarithmic transfer formula, equivalently differentiation of \([w^s](1-w)^{-\alpha}=\Gamma(s+\alpha)/(\Gamma(\alpha)\Gamma(s+1))\) at \(\alpha=1/4\), yields

\[
[z^{2s+1}]E(z)O(z)
\sim\frac{e^{-1/4}}{4\Gamma(1/4)}s^{-3/4}\log s.
\]

The analytic remainders are of lower logarithmic order; the square-root substitution is analytic for the power series in \(w\) away from the unit singularity. Dividing by the total EGF coefficients, and using \(s\sim n/2\), gives exactly the two asserted constants and exponents.

## Verification

The accompanying standalone Python verifier enumerates binary edge allocations of finite even-degree graphs, including parallel-edge cases. It checks 741 test instances (with null goods in the range zero to four), tests the sharp pair-of-triangles obstruction and minimum-allocation counts, and compares exact rational EGF coefficients with all 4,058 labeled simple 2-regular graphs on three to eight vertices. All checks passed. These finite checks do not establish the infinite statements; those follow from the preceding arguments and standard coefficient asymptotics. Run using `python verify_euler_fairness.py` in a standard Python 3 environment.

## Relationship to prior work

Deligkas, Eiben, Ganian, Goldsmith, Gründel and Wietheger (2026) analyze the computational complexity of EF1 allocation between fixed or variable groups under subjective valuations, including hardness for fixed groups, but do not give this Eulerian sparse-binary parity invariant or its labeled-random cycle distribution. Suksompong (2019) studies EF1 group-sharing and balanced allocations under varying assumptions on group memberships and preferences; its positive results under movable group assignments do not imply cardinality balance for the prescribed groups here. The graph-theoretic matching characterization and exponential-formula enumeration are used as proof tools, not claimed as new in isolation.

## Limitations

The deterministic equality assumes the support graph is Eulerian and the second group has zero utilities. With positive second-group values, non-Eulerian degrees, more than two groups, or subjective chores, the equivalence need not hold. The random-graph result uses uniformly labeled simple 2-regular graphs, not general Erdős–Rényi graphs or independently chosen preferences. The asymptotics are first-order along separate parity subsequences, not a uniform error estimate. The Euler-tour algorithm minimizes the *count* of first-group goods while ensuring EF1, not total social welfare under other valuation models.

## References

- A. Deligkas, E. Eiben, R. Ganian, T.-L. Goldsmith, M. Gründel, and S. Wietheger, *Subjective Valuations Make It Hard to be Fair: The Complexity of Resource Allocation to Groups of Agents*, arXiv:2610.28213v1 (first public 2026-10-20), https://arxiv.org/abs/2610.28213 .
- W. Suksompong, *Almost Envy-Freeness in Group Resource Allocation*, 2019, arXiv:1901.08463, https://arxiv.org/abs/1901.08463 .
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Chapters II and VI (labeled cycle exponential formula and singularity transfer).
