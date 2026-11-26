# Likelihood-ratio domination through ten vertices in subcubic parking graphs

## Finding
Let \(G\) be a finite, simple, connected graph with \(1\le |V(G)|\le10\) and maximum degree at most three. Let \(U_G\) be the size of a uniformly chosen maximal independent set, and let \(S_G\) be the size obtained by sequential parking: repeatedly select an available vertex uniformly, occupy it, and exclude its closed neighborhood. Write \(u_G(k)=\Pr(U_G=k)\) and \(s_G(k)=\Pr(S_G=k)\).

**Theorem (finite exhaustive likelihood-ratio order).** For every such \(G\) and every pair \(k<\ell\) in the common support,
\[
s_G(k)u_G(\ell)\le s_G(\ell)u_G(k).
\]
Equivalently, \(s_G(k)/u_G(k)\) is nondecreasing on that support. In particular, \(U_G\le_{\mathrm{st}}S_G\). The exact check covers all 2,571 connected subcubic isomorphism classes through order ten. At order ten the size distributions differ in 1,687 classes and coincide in 46. The numbers of graph classes themselves agree with the previously tabulated sequence A243393 [3]; the result concerns their parking size laws, not a new graph count or a new finite range for first-order stochastic dominance.

## Assumptions and scope
The graphs are unweighted and loopless. Selection is uniform over the still-available vertices, without early stopping. Maximal independent sets are independent dominating sets. Every greedy outcome is maximal, and every maximal independent set has positive sequential probability because a priority ordering that puts its vertices first realizes it. Consequently the two size laws have exactly the same support. The likelihood-ratio theorem does not cover disconnected graphs or orders above ten.

## Proof
**1. Complete inductive graph enumeration.** A connected graph with at least two vertices has a non-cut vertex: take a leaf of any spanning tree, whose deletion leaves a connected spanning subtree. Deleting such a vertex from a connected subcubic graph leaves a smaller connected subcubic graph. To reverse the deletion, attach a new vertex to one, two, or three different vertices whose current degree is at most two. Starting with the unique one-vertex graph thus generates all desired classes. The program `verify_census.py` does this recursively; equivalent base representatives have equivalent sets of extensions. Degree profiles, neighbor-degree profiles and color refinement are used only as isomorphism invariants for bucketing. Duplicates are discarded only using an exact search for a bijection preserving both adjacency and nonadjacency. This gives one representative per isomorphism class.

**2. Exact size laws.** For the available vertex subset \(A\), let \(f_A(k)\) be the probability of occupying \(k\) additional vertices. At \(A=\varnothing\) this is the point mass at zero. Otherwise, conditioning on the uniformly selected next vertex gives
\[
f_A(k)=\frac1{|A|}\sum_{v\in A} f_{A\setminus N_G[v]}(k-1).
\]
The program memoizes this recurrence using vertex bitmasks and exact rational arithmetic. Separately, it counts each independent subset that meets every closed neighborhood. These subsets are exactly the maximal independent sets, so dividing the size-resolved counts by their total gives the static law.

**3. Exhaustive test.** For every generated class, the program compares consecutive ratios \(s_G(k)/u_G(k)\) on the increasing common support using exact fractions. Adjacent inequalities imply the inequalities for every pair. The results are:

| \(|V(G)|\) | Connected subcubic classes | Different size laws | Equal size laws | Likelihood-ratio failures |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 0 |
| 2 | 1 | 0 | 1 | 0 |
| 3 | 2 | 1 | 1 | 0 |
| 4 | 6 | 3 | 3 | 0 |
| 5 | 10 | 5 | 5 | 0 |
| 6 | 29 | 20 | 9 | 0 |
| 7 | 64 | 55 | 9 | 0 |
| 8 | 194 | 172 | 22 | 0 |
| 9 | 531 | 508 | 23 | 0 |
| 10 | 1733 | 1687 | 46 | 0 |

The first-order consequence follows because the ratio has mean one under \(u_G\), and its conditional mean on a lower tail cannot exceed its mean over the support. This is a finite computer-assisted proof, not an extrapolation to all subcubic graphs.

## Verification
Run `python3 verify_census.py 10` using a standard-library Python installation with assertions enabled. It regenerates the graph classes and checks the inequalities with exact fractions; see `census_output.txt`. The companion `python3 verify_orders.py` compares the law obtained from every priority permutation to a separately written first-choice calculation on the 49 classes through order six; see `orders_output.txt`. This second check shares the graph generator but uses a different probability calculation. The scripts need no network access or external graph catalogue.

## Relationship to prior work
Higuita-Diaz, López and Roldán-Correa [1] study these same models and prove first-order stochastic dominance on paths and cycles. Version 2, dated 18 November 2026, §5.4 reports an exhaustive **first-order** dominance computation for connected subcubic graphs through order twelve (27,525 classes). It therefore already covers the entire order range here in the weaker order. The class counts, including 194, 531 and 1,733 at orders eight, nine and ten, are also tabulated independently in OEIS A243393 [3]. The contribution here is the exact **likelihood-ratio** comparison through order ten, not extension of the earlier first-order census. A cumulative-probability inequality does not imply monotonicity of point-mass ratios; for example, on a three-point ordered support, \((1/6,1/2,1/3)\) dominates the uniform law in first-order stochastic order but has ratios \((1/2,3/2,1)\). The inspected first-order result does not assert the stronger comparisons. Its cited computation [2] may contain additional information; its exact scope beyond what is stated in the paper is not established here. A related result [4] gives a six-vertex likelihood-ratio failure without the degree bound, so the stronger order is not automatic even for very small graphs.

## Limitations
No likelihood-ratio assertion is made above order ten. In particular, the computation does not prove the all-orders first-order stochastic dominance conjecture. The conclusion concerns sizes, not uniformity over individual maximal independent sets. The certificate relies on exact finite code and exhaustive generation; the priority-permutation cross-check covers only orders through six. Historical priority of the likelihood-ratio comparison is bounded by the examined statements and available computational material.

## References
1. R. Higuita-Diaz, L. López and A. Roldán-Correa, *Random Sequential Adsorption versus the Uniform Ensemble of Jammed Configurations: Stochastic Dominance on Graphs*, arXiv:2611.14718v2 (18 November 2026), https://arxiv.org/html/2611.14718v2, especially §5.4. Version 1 appeared as *Stochastic Dominance in Discrete Parking Processes on Graphs*.
2. L. López, accompanying *Stochastic Dominance DPP Graphs* repository, https://github.com/lykoslopezrivera-blip/Stochastic_Dominance_DPP_Graphs.
3. The On-Line Encyclopedia of Integer Sequences, [A243393](https://oeis.org/A243393), connected trivalent graphs with semi-edges; see the comment identifying the equivalent count of connected simple subcubic graphs.
4. [*Sharp six-vertex failure of likelihood-ratio domination in graph parking*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-six-vertex-failure-of-likelihood-ratio-domination-in-graph--2fafc168a061), related result for unrestricted degree.
