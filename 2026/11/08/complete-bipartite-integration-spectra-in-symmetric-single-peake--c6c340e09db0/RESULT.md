# Complete bipartite integration spectra in symmetric single-peaked swap Schelling games

## Finding
Consider the fully occupied two-color swap Schelling game with a symmetric single-peaked utility maximized at an own-color closed-neighborhood fraction of \(1/2\). Every coloring of every complete multipartite graph is a swap equilibrium. In particular, for the complete bipartite graph \(K_{a,b}\) with \(a,b\ge1\), \(n=a+b\), and exactly \(k\) agents of the minority color, where \(1\le k\le\lfloor n/2\rfloor\), the **entire integration spectrum with multiplicities** is
\[
 F_{a,b,k}(t)=\sum_{x=\max(0,k-b)}^{\min(a,k)}\binom ax\binom b{k-x}\,t^{D(x)},
\]
where \(y=k-x\) and
\[
 D(x)=x\mathbf1_{y<b}+(a-x)\mathbf1_{y>0}+y\mathbf1_{x<a}+(b-y)\mathbf1_{x>0}.
\]
Here \(D(x)\) is the number of agents having at least one differently colored neighbor. In particular, the smallest and largest degrees of integration among equilibria are
\[
 D_{\min}=k+\min(a,b),\qquad
 D_{\max}=\begin{cases}
 n-k+1&\min(a,b)=1,\\
 1+\max(a,b)&a,b\ge2,\ k=1,\\
 n&a,b\ge2,\ k\ge2.
 \end{cases}
\]
Thus the price of stability is exactly \(1\), and the price of anarchy is the explicit ratio \(D_{\max}/(k+\min(a,b))\). For \(K_{2,t}\), \(t\ge2\), and \(k=2\), this is \((t+2)/4\), which grows without bound. The polynomial counts occupied-node colorings, not label-distinguishing agent permutations.

## Assumptions and scope
A complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) has \(r\ge2\) parts of positive integer sizes, with all edges between different parts and no edges within a part. Exactly two colors occur; every vertex is occupied by one agent. Each agent at vertex \(v\) evaluates the own-color fraction
\[
 f(v)=\frac{1+|\{u\in N(v):\text{color}(u)=\text{color}(v)\}|}{1+|N(v)|}
\]
(including the evaluating agent). Its utility is \(p(f(v))\), where a common \(p:[0,1]\to[0,1]\) satisfies \(p(t)=p(1-t)\), is strictly increasing on \([0,1/2]\), and has its maximum at \(1/2\) (normalized to \(p(1/2)=1\)). Agents may exchange their locations only when **both** strictly increase their own utilities. An equilibrium has no such mutually beneficial swap. The integration measure counts occupied vertices with at least one opposite-color neighbor, independently of the utility magnitude. Define price of anarchy (PoA) as optimal degree of integration divided by its minimum among equilibria, and price of stability (PoS) by the corresponding maximum among equilibria. The theorem concerns two-color fully occupied graphs, symmetric utilities and strict bilateral improvement; it makes no claim for vacancies, more colors, asymmetric preferences, or unilateral moves.

## Proof
**Multipartite freezing.** Let blue agent \(i\) at vertex \(u\) and red agent \(j\) at \(v\) contemplate a swap. If \(u,v\) are in the same part, they have the same external neighborhood and interchanging the colors leaves every agent's own-color count at its destination unchanged. Neither moving agent improves.

If \(u,v\) are in distinct parts, they are adjacent. Write \(d_u=|N(u)|\) and \(c_u\) for the number of blue neighbors of \(u\) before the swap; the initially blue agent's fraction is \((1+c_u)/(1+d_u)\). After exchange, \(u\) houses red, and the red count among its neighbors is \(d_u-c_u-1\), since the neighbor \(v\) changed from red to blue. The new fraction at \(u\) is therefore \((d_u-c_u)/(1+d_u)=1-(1+c_u)/(1+d_u)\). By symmetry of \(p\), the new utility **at the vertex** \(u\) equals the original blue utility there. The same argument at \(v\) shows its new utility equals the old red utility there. Therefore the moving blue and red agents exchange their old utility levels: if the old levels are \(U_i,U_j\), their new levels are \(U_j,U_i\). Both cannot strictly improve. All configurations are equilibria. This adjacent-swap complement identity is consistent with the general swapping identity in Bilò et al. (2022, Section 2); the additional complete-multipartite observation accounts for the same-part case.

**Counting integrated vertices.** In \(K_{a,b}\), put \(x\) blue vertices in the first part, \(y=k-x\) in the second. A blue vertex in the first part has a red neighbor exactly when \(y<b\), while a red vertex in the first part has a blue neighbor exactly when \(y>0\). Likewise, blue and red vertices of the second part contribute precisely when \(x<a\) and \(x>0\), respectively. Summing these four mutually exclusive vertex classes gives \(D(x)\). There are \(\binom ax\binom by\) such colorings; the allowable integer interval for \(x\) is exactly \(\max(0,k-b)\le x\le\min(a,k)\), proving the polynomial. Setting \(t=1\) yields \(F_{a,b,k}(1)=\binom nk\) by Vandermonde's identity, an independent count check.

**Extrema.** When both parts contain both colors (\(0<x<a\), \(0<y<b\)), every vertex is integrated, so \(D=n\). At a boundary, the exact values are \(D(0)=k+a\), \(D(k)=k+b\), \(D(a)=n-k+a\), and \(D(k-b)=n-k+b\), whenever the respective boundary is feasible; coincident boundaries give the same value. Since \(k\le n/2\), every such value is at least \(k+\min(a,b)\). This lower bound is attained by placing all \(k\) blue agents in the larger part (possible because \(k\le n/2\le\max(a,b)\)). If \(a,b\ge2\) and \(k\ge2\), choose \(1\le x<a\) and \(1\le y<b\), with \(x+y=k\), possible because \(2\le k\le n/2\le n-2\); hence \(D_{\max}=n\). For \(k=1\), the blue vertex has exactly the vertices of the other part as opposite-color neighbors, so the maximum is \(1+\max(a,b)\). Finally, if one part is a singleton, every coloring either puts no blue there, giving \(D=k+1\), or puts a blue there, giving \(D=n-k+1\); because \(n\ge2k\), the latter is maximal. The stated extrema and efficiency ratios follow because **all colorings are equilibria**.

## Verification
Run `python3 verify.py` using the standalone Python 3 file accompanying this result. This checker enumerates all nonconstant binary colorings and all opposite-color swaps across 85 complete multipartite graph structures (up to eight vertices). For the biclique portion it enumerates all node colorings of \(K_{a,b}\) for \(1\le a,b\le7\) and \(1\le k\le\lfloor(a+b)/2\rfloor\) (184 parameter configurations), and compares the directly computed histogram with the polynomial and both extrema. The checker uses exact rational utilities for the representative symmetric peak \(p(t)=\min(t,1-t)\). These finite checks do **not** establish the all-order theorem; the preceding elementary proof does.

## Relationship to prior work
Bilò, Bilò, Lenzner and Molitor (2022, arXiv:2204.12599) introduce the symmetric single-peaked closed-neighborhood swap model, the degree-of-integration objective, a general adjacent-swap identity, bipartite equilibrium existence and generic bounds on PoA and PoS. Their adjacent-swap identity substantially overlaps the freezing argument, so the no-cross-part-profitable-swap step is **not claimed as a new general principle**. The present contribution is a full all-size **integration distribution with multiplicities** for bicliques, its sharp extremal welfare and PoA/PoS formulas, coupled to the explicit stability classification. These statements are not supplied by the source's general existence and efficiency bounds. Agarwal et al. (2019, arXiv:1909.02421) analyze an earlier, monotone, typically open-neighborhood fraction model; its conclusions do not imply the symmetric single-peaked closed-neighborhood spectrum here. The separate 2023 single-peaked jump model permits vacant sites and is not equivalent to this swap model.

## Limitations
Originality is assessed relative to accessible published source texts and research-record searches, not as a proof of worldwide priority. The adjacent complement identity was already present in the initiating literature; the independent part is the joint full integration distribution and sharp efficiency classification. Complete multipartite network structure, two colors, identical symmetric single-peaked utilities and strict bilateral swaps are all essential to the stated proof. Integration counts agents with any opposite-color neighbor and is not equivalent to average preference satisfaction. No external independent validation has been performed.

## References
1. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (first publicly submitted 2022-04-26), https://arxiv.org/abs/2204.12599 and https://arxiv.org/html/2204.12599v2.
2. A. Agarwal, E. Elkind, J. Gan and A. A. Voudouris, *Swap Stability in Schelling Games on Graphs*, arXiv:1909.02421 (2019), https://arxiv.org/html/1909.02421v3.
3. T. Friedrich, P. Lenzner, L. Molitor and L. Seifert, *Single-Peaked Jump Schelling Games* (2023), cited solely to distinguish the vacancy/jump mechanism, https://hpi.de/friedrich/people/pascal-lenzner.html.
