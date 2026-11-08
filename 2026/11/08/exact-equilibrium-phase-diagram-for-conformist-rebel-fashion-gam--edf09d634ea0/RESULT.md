# Exact equilibrium phase diagram for conformist–rebel fashion games on wheels

## Finding
Let \(W_{n+1}=K_1\vee C_n\), \(n\ge3\), have a hub and \(n\) labeled rim vertices in cyclic order. Each vertex chooses one of two actions and is either a conformist (prefers matching neighbors) or a rebel (prefers disagreeing with neighbors). Consider either a wholly rebel rim or a rim with precisely one conformist; independently, let the hub be conformist or rebel.

Define the Perrin sequence by \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\). Define \(c_t\) as the number of ordered compositions of \(t\) into parts of sizes \(2\) and \(3\), taking \(c_0=1\) and \(c_t=0\) for \(t<0\). For each \(n\ge3\), the exact numbers of pure Nash equilibria are:

| Hub type | All-rebel rim | One-conformist rim |
|---|---:|---:|
| Conformist | \(4\) if \(n\) is even, \(0\) if \(n\) is odd | \(0\) |
| Rebel | \(2P_n\) | \(2c_{n-4}\) |

The corresponding numbers of **strict** pure Nash equilibria are:

| Hub type | All-rebel rim | One-conformist rim |
|---|---:|---:|
| Conformist | \(0\) | \(0\) |
| Rebel | \(2P_n-4\mathbf{1}_{2\mid n}\) | \(2c_{n-4}\) |

In particular, on every wheel with even rim size, replacing one rebel by a conformist destroys all four Nash equilibria when the hub is conformist. When the hub is a rebel, all equilibria in the one-defect class are strict, and their exact multiplicities follow the two-/three-step composition sequence instead of the Perrin sequence.

## Assumptions and scope
A wheel here is the **simple undirected** graph \(K_1\vee C_n\), with \(n\ge3\). All vertices play simultaneously and have action set \(\{0,1\}\). For conformist \(i\), utility is the number of neighbors \(j\) with \(x_j=x_i\); for rebel \(i\), utility is the number with \(x_j\ne x_i\). Each edge has unit weight and every player maximizes its own utility. Pure Nash equilibrium means no player can strictly increase utility by switching its bit; an equilibrium is *strict* when every such unilateral switch strictly decreases utility. Ties count as best responses.

The two rim-type classes are (i) all vertices rebel and (ii) exactly one conformist, located at vertex \(0\) by cyclic symmetry. The hub may be either type. The table does not classify arbitrary rim-type configurations, weighted networks, more than two actions, mixed equilibria, or best-response dynamics. Counts are for **labeled strategy profiles** on this fixed labeled graph, not for symmetry orbits.

## Proof
**1. Reduction by action complement.** The utility rules are invariant under simultaneously interchanging action \(0\) and action \(1\). Therefore every equilibrium comes in a distinct pair of complementary profiles. It suffices to fix the hub's action to \(0\), count legal rim words, and double. A rim vertex has degree three, hence no tie is possible in its binary best response; only the hub can be indifferent.

**2. All-rebel rim.** Fix the hub at \(0\). A rebel rim vertex \(i\) best responds with \(x_i=0\) exactly when both cyclic rim neighbors choose \(1\), since the hub already supplies a neighbor playing \(0\). Otherwise it chooses \(1\). Thus the positions bearing \(0\) form an independent set of \(C_n\), and each position bearing \(1\) has a \(0\)-neighbor. Equivalently the zero positions form a *maximal independent set* of the cycle. Conversely every such set gives a valid best-response rim profile.

Let \(z\) be the number of zero positions. Since zero positions are nonadjacent, \(z\le \lfloor n/2\rfloor\); maximality additionally excludes three consecutive ones. Consequently consecutive zero positions are separated, cyclically, by distances \(2\) or \(3\). This yields the exact enumeration
\[
\#\mathrm{MIS}(C_n)=\sum_{z=\lceil n/3\rceil}^{\lfloor n/2\rfloor}\frac nz\binom z{n-2z}=P_n.
\]
For clarity, the Perrin identity also follows directly from the three-state transition matrix on allowable consecutive bit-pairs \((01),(10),(11)\):
\[
T=\begin{pmatrix}0&1&1\\1&0&0\\0&1&0\end{pmatrix}.
\]
A cyclic best-response word is exactly a closed state walk of length \(n\), and hence the count is \(\operatorname{tr}(T^n)\). The characteristic polynomial \(\lambda^3-\lambda-1\) gives the recurrence \(P_n=P_{n-2}+P_{n-3}\), with initial traces \(3,0,2\). This is also the classical cycle maximal-independent-set/Perrin correspondence, not a claim of new combinatorial enumeration in isolation.

The hub sees \(z\) zero actions and \(n-z\) one actions. If conformist, playing \(0\) is a best response precisely when \(z\ge n/2\); since \(z\le n/2\), equality is necessary. This occurs only for even \(n\) and yields exactly the two alternating rim words. These give \(4\) equilibria after complementing the hub, none strict because the hub ties. If the hub is a rebel, playing \(0\) is a best response whenever \(z\le n/2\), which holds for all \(P_n\) rim words. It is strict except in the two alternating even-cycle words. Thus the totals are \(2P_n\) and \(2P_n-4\mathbf{1}_{2\mid n}\), respectively.

**3. Exactly one conformist on the rim.** Put that conformist at rim position \(0\), with the hub again playing \(0\). If \(x_0=0\), a conformist best response requires at least one of its two rim neighbors to play \(0\), because its third neighbor (the hub) already plays \(0\). But neither neighboring rebel could itself play \(0\) beside \(x_0=0\): a rebel choosing \(0\) needs both its rim neighbors to play \(1\). Contradiction. Hence \(x_0=1\).

Because the conformist chooses \(1\) while the hub chooses \(0\), its unique best response requires \(x_1=x_{n-1}=1\). Each of these two adjacent rebels then requires a zero among its rim neighbors, forcing \(x_2=x_{n-2}=0\). For \(n=3\), these conditions conflict, giving no legal rim word. For \(n=4\), the two forced zero positions coincide and give the unique legal word \((1,1,0,1)\). For \(n\ge5\), every remaining rim vertex is a rebel and the zero positions in the interval from vertex \(2\) to vertex \(n-2\) must have successive distances exactly \(2\) or \(3\), as above. The two endpoints are forced zeros, and this interval has length \(n-4\). Therefore the legal rim words are in bijection with ordered compositions of \(n-4\) into parts \(2\) and \(3\), giving \(c_{n-4}\) words (with \(c_0=1\) covering \(n=4\)).

Each legal rim word contains a special gap of length \(4\) across the vertices \(n-2,n-1,0,1,2\): the three successive rim actions \(1,1,1\) lie between zeros. All other gaps between zeros have length \(2\) or \(3\). Hence the rim contains at least two more ones than zeros. This conclusion also holds for \(n=4\), whose sole rim word contains three ones and one zero. Therefore a conformist hub playing \(0\) can never best respond, whereas a rebel hub playing \(0\) always responds *strictly* optimally. Every rim vertex also best responds strictly because it has three neighbors. After action complement, the one-conformist rim has zero equilibria with a conformist hub and exactly \(2c_{n-4}\) equilibria with a rebel hub; all the latter are strict.

This proves the complete phase tables for every integer \(n\ge3\). \(\square\)

## Verification
The accompanying standalone Python program `verify_wheel.py` enumerates all \(2^{n+1}\) action profiles for every integer \(3\le n\le15\) and all four hub/rim type configurations. It directly checks individual best responses and strictness and compares against the closed formulas. It additionally checks the maximal-independent-set/Perrin trace coefficient using exact integer and rational arithmetic. The program completed \(52\) type/size cases and \(524{,}224\) profile evaluations without mismatches. These finite tests are independent sanity checks; the universal statements rely on the proof above.

Reproduce with `python3 verify_wheel.py` using only Python's standard library.

## Relationship to prior work
Cao, Sánchez and Zhang (2026) analyze heterogeneous binary network games and formulate general equilibrium existence criteria; Pei, Cao and Zhang (2026) study multi-strategy conformist–rebel–stubborn networks with results for complete graphs, lines, rings, trees and stars. Neither inspected primary source states the four-case **wheel** equilibrium and strict-equilibrium count tables or the one-rim-vertex type-change transition. The earlier fashion-game work of Cao and Yang gives general and specific-graph existence results, while Cao, Qin, Yang and Zhang (2019) analyze best-response dynamics on lines, rings and stars. Their inspected theorems do not yield the full wheel table by a stated result. Maximal independent sets of plain cycles are classically enumerated by Perrin numbers: that component is established knowledge and supplies a building block, not a novelty claim.

The new contribution claimed here is the combined exact wheel classification with a strategically best-responding center and a single conformist rim defect, including exact strictness and extinction regimes. This is distinct from graph domination or independent-set counts absent the hub best-response and heterogeneous rim constraints. Primary papers restricted to other graph families do not imply the stated four-case table without additional analysis.

## Limitations
The result concerns a restricted but natural pair of rim-type families, binary actions and uniform edge weights; it says nothing about arbitrary heterogeneous type words or dynamical convergence. Existing literature on best-response network games or graph-independent-set transfer matrices may contain equivalent formulations not indexed by title. Full text for some potentially related paywalled graph-fashion studies (Shen and Lin, 2020; 2022) was not accessible; no whole-document exclusion is claimed for those works. Exact provenance priority would benefit from human literature verification. No independent scientific audit has been performed.

## References
1. W. Cao, Á. Sánchez, B. Zhang, *Network games with heterogeneous players*, arXiv:2607.05932, first public 7 July 2026. https://arxiv.org/abs/2607.05932
2. S. Pei, W. Cao, B. Zhang, *Network games with three types of players* (later titled *Equilibria in heterogeneous multi-strategy network games*), arXiv:2607.10997, first public 13 July 2026. https://arxiv.org/abs/2607.10997
3. Z. Cao and X. Yang, *The fashion game: Network extension of Matching Pennies*, *Theoretical Computer Science* **540–541** (2014), 169–181. https://doi.org/10.1016/j.tcs.2014.05.009
4. Z. Cao, C.-Z. Qin, X. Yang and B. Zhang, *Dynamic matching pennies on networks*, *International Journal of Game Theory* **48** (2019), 887–920. https://doi.org/10.1007/s00182-019-00665-5
5. G. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, *Journal of Integer Sequences* **11** (2008), Article 08.5.7 (classical cycle/Perrin literature).
6. Shen and Lin, *Fashion game on graphs*, *Discrete Optimization* **38** (2020), 100606. https://doi.org/10.1016/j.disopt.2020.100606
7. Shen and Lin, *Fashion Game on Planar Graphs*, *Graphs and Combinatorics* **38** (2022), Article 92.
