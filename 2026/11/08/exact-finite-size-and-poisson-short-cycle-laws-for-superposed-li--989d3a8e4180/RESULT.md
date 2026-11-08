# Exact finite-size and Poisson short-cycle laws for superposed linear-order successors

## Finding

Let \(r\ge 1\) be fixed. Independently and uniformly choose \(r\) linear orders of \([n]=\{1,\ldots,n\}\), take their immediate-successor relations \(S_1,\ldots,S_r\), and forget the individual relations in favor of the simple directed union \(U=\bigcup_{i=1}^r S_i\). For \(2\le k\le n\), let \(C_{n,k}\) count directed simple \(k\)-cycles in \(U\), modulo cyclic rotation (but **not** reversal).

Write \((n)_h=n(n-1)\cdots(n-h+1)\), with \((n)_0=1\), and define
\[
 b_{n,k}(j)=\sum_{h=0}^{\min(j,k-1)}\frac{(-1)^h\binom jh}{(n)_h}\qquad(0\le j\le k).
\]
Then the following **finite-size identity** holds for all integers \(n\ge k\ge2\) and \(r\ge1\):
\[
 \boxed{\mathbb E C_{n,k}=\frac{(n)_k}{k}\sum_{j=0}^{k}(-1)^j\binom kj b_{n,k}(j)^r.}
\]
Furthermore, for any fixed integer \(K\ge2\), as \(n\to\infty\),
\[
 \boxed{(C_{n,2},\ldots,C_{n,K})\xrightarrow{d}(P_2,\ldots,P_K),\qquad
 P_k\text{ independent},\quad P_k\sim\operatorname{Poisson}\!\left(\frac{r^k-r}{k}\right).}
\]
In particular, if \(r\ge2\), the first-order sentence asserting a directed \(k\)-cycle in \(U\) has limiting probability \(1-\exp(-(r^k-r)/k)\). The probability of **no** directed cycle of any length \(2,\ldots,K\) tends to
\[
\boxed{\exp\!\left(-\sum_{k=2}^{K}\frac{r^k-r}{k}\right).}
\]
The directed girth therefore converges to a proper integer-valued law, with \(\Pr(G=k)=e^{-\sum_{j=2}^{k-1}(r^j-r)/j}(1-e^{-(r^k-r)/k})\), for \(r\ge2\); a directed cycle exists with probability tending to one. For \(r=1\), every union is a path and all counts vanish identically.

## Assumptions and scope

Orders are independent uniform permutations of the **same labelled carrier**. Each \(S_i\) consists of the \(n-1\) successive directed arcs in its order, with no closing arc, and is globally acyclic. The union \(U\) has only one arc per ordered pair even if several orders share it. Both loops and length-one cycles are excluded. A cycle of length two is the pair of opposing arcs on two distinct vertices. All limits take \(r,K\) fixed before \(n\to\infty\). The displayed finite-size expectation also covers \(k=n\).

The first-order signature contains just \(U\), no successor-color predicates and no underlying order predicates. For \(k\ge2\), the cycle-existence sentence is
\[
\psi_k:=\exists x_1\cdots\exists x_k\left(\bigwedge_{i<j}x_i\ne x_j\ \land\ \bigwedge_{i=1}^k U(x_i,x_{i+1})\right),\qquad x_{k+1}:=x_1.
\]
Every finite Boolean combination of bounded cycle-count events can likewise be represented by a first-order sentence; no first-order limit law is asserted for **all** sentences in the reduct.

## Proof

**1. Block-counting lemma.** Fix a directed \(k\)-cycle with arc set \(E\), where \(2\le k\le n\). Every proper subset \(F\subsetneq E\) with \(|F|=h\) is a vertex-disjoint union of directed paths (isolated vertices are permitted). Collapsing each required directed path into a linearly ordered block leaves \(n-h\) blocks, hence exactly \((n-h)!\) permutations realize every arc of \(F\) as an immediate successor. Thus
\[
\Pr(F\subseteq S_i)=\frac{(n-h)!}{n!}=\frac{1}{(n)_h}.
\]
For \(F=E\), this probability is zero: a linear order cannot contain a directed cycle.

**2. Exact expectation.** Select any \(j\) of the \(k\) cycle arcs. Inclusion–exclusion and the block-counting lemma show that the probability that none of these \(j\) arcs belongs to one uniform successor relation is exactly \(b_{n,k}(j)\). The upper limit \(k-1\) is essential when \(j=k\), since the complete directed cycle cannot lie in one order. Independence of the \(r\) orders makes the probability that all \(j\) arcs are absent from \(U\) equal to \(b_{n,k}(j)^r\). A second inclusion–exclusion, over the arcs required to be present in \(U\), gives the inner alternating sum in the claimed formula. There are exactly \((n)_k/k\) directed simple \(k\)-cycles on the labelled carrier. Linearity of expectation completes the exact identity.

**3. Probability of a fixed finite disjoint cycle family.** Consider fixed pairwise vertex-disjoint directed cycles of lengths \(k_1,\ldots,k_s\), and let \(L=\sum_i k_i\). Assign to every required arc one of the \(r\) orders meant to realize it. An assignment is impossible if it colors all arcs of any one of the cycles identically, because that order would then contain an entire directed cycle. Every other assignment gives, in each order, a disjoint union of directed paths, and therefore has probability
\[
\prod_{c=1}^r (n)_{h_c}^{-1}=n^{-L}(1+O(n^{-1})),
\]
where \(h_c\) is the number of arcs assigned color \(c\). There are exactly \(\prod_{i=1}^s(r^{k_i}-r)\) feasible color assignments. The assignment-events can overlap only if some required arc appears in at least two orders. For fixed \(L,r\), the total probability of such multiply assigned covers is \(O(n^{-L-1})\), again by the block-counting lemma (or zero when a color creates a full cycle). Hence
\[
\Pr(\text{all prescribed cycles lie in }U)
=n^{-L}\prod_{i=1}^s(r^{k_i}-r)+O(n^{-L-1}).
\]
The constants depend on the fixed pattern and on \(r\), not on its distinct vertex labels.

**4. Negligible overlapping cycles.** For any fixed collection of distinct cycles whose combined directed-arc union has \(v\) vertices and \(e\) distinct arcs, the probability that all its arcs occur in \(U\) is \(O(n^{-e})\): assign each required arc one realizing order, and apply the block lemma whenever the assignment is feasible. In every collection with two cycles sharing a vertex or edge, some connected component contains two distinct cycles and has \(e>v\); all other components satisfy \(e\ge v\). The total contribution of such patterns, summed over their \(O(n^v)\) embeddings, is consequently \(O(n^{-1})\).

**5. Joint factorial moments.** In \(\mathbb E\prod_{k=2}^K(C_{n,k})_{a_k}\), for any fixed nonnegative integers \(a_k\), the dominant terms are the vertex-disjoint cycles. Counting the embeddings modulo cyclic rotations and applying Step 3 gives
\[
\lim_{n\to\infty}\mathbb E\prod_{k=2}^K(C_{n,k})_{a_k}
=\prod_{k=2}^K\left(\frac{r^k-r}{k}\right)^{a_k}.
\]
Step 4 makes all other terms negligible. These are precisely the joint factorial moments of independent Poisson variables; tightness and moment determinacy yield the claimed joint weak convergence. For \(r=1\), all counts are identically zero, as already noted.

**6. Logical and girth consequences.** Each \(\psi_k\) is true exactly when \(C_{n,k}>0\). Joint Poisson convergence gives the stated limits for any fixed finite collection of cycle-existence or bounded-count formulas. For \(r\ge2\), the partial sums \(\sum_{k=2}^K(r^k-r)/k\) tend to infinity with \(K\), so the limiting directed girth is finite almost surely. In particular \(\psi_2\) has a limit strictly between zero and one, demonstrating a failure of the zero-one law in the reduct language.

## Verification

`checker.py` is a dependency-free exact-rational finite verifier. It exhaustively enumerates every tuple of orders for the parameter pairs \((n,r)=(2,1),(3,2),(4,2),(4,3)\), constructs the uncolored union, counts every directed cycle of lengths \(2\) through \(n\) without overcounting rotations, and matches the resulting rational mean to the finite-size formula. The final line of its verified run is `ALL_EXACT_CYCLE_CHECKS_PASS`. The checker confirms the finite identity in those test cases; the all-size identity and the joint weak limit are established by the proof above, not by finite enumeration.

For orientation, when \(r=2\), the first three limiting cycle means are \(1,2,7/2\), respectively, for lengths \(2,3,4\). Thus the limiting probability of no directed cycle of length at most three is \(e^{-3}\). Under a sparse independent-arc digraph with arc probability asymptotic to \(r/n\), the corresponding mean for length \(k\) would instead be \(r^k/k\); the missing \(r/k\) is the precise effect of banning a monochromatic directed cycle within each spanning path.

## Relationship to prior work

Jeż, Michaliszyn and Witkowski (2026, arXiv:2610.19943) study finite satisfiability for first-order logic with any input-dependent number of successor relations; their primary result is a complexity and finite-model upper bound, and their cycle elimination concerns individual designated relations, not the probability of mixed cycles in their union. Michaliszyn and Witkowski (2026, arXiv:2610.09758) study satisfiability and large-model certificates for the same successor setting, also without random short-cycle laws.

Cohen, Fachini and Körner (2015, arXiv:1501.00813) analyze extremal families of Hamiltonian paths separated by cycles in pairwise unions, including a directed two-cycle separation problem; these family-size bounds do not supply this joint distribution for independent uniform paths. Classical random-permutation and random-regular-graph cycle laws provide analogous Poisson techniques but concern different probability models: a uniform permutation has monochromatic cycles, whereas each successor relation here is an acyclic spanning path. The familiar reciprocal-adjacency limit for two paths accounts for the special case \(r=2,k=2\), which is not independently claimed as new. The present contribution is the all-length, all-fixed-\(r\), finite-size-plus-joint-law statement.

## Limitations

The Poisson statement is for finitely many **fixed** short lengths and a fixed number of orders. It does not establish a full first-order convergence law for arbitrary sentences, any growing-length joint approximation, independence at finite \(n\), or behavior when \(r\) grows with \(n\). The exact finite-size formula concerns the first moment, not the full finite-size distribution. Historical priority of the short-cycle law has not been independently certified; a specialized conditioning theorem for superposed Hamiltonian paths could subsume it. Independent mathematical audit has not been performed.

## References

1. A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1, first public October 14, 2026. https://arxiv.org/abs/2610.19943
2. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first public October 7, 2026. https://arxiv.org/abs/2610.09758
3. G. Cohen, E. Fachini and J. Körner, *Path separation by short cycles*, arXiv:1501.00813 (2015). https://arxiv.org/abs/1501.00813
4. A. Frieze, *Hamilton cycles in the union of random permutations*, Random Structures & Algorithms **18** (2001), 83–94. DOI:10.1002/1098-2418(200101)18:1<83::AID-RSA6>3.0.CO;2-I.
5. B. McKay, N. Wormald and B. Wysocka, *Short cycles in random regular graphs* (2004), Australian National University research repository. https://openresearch-repository.anu.edu.au/items/4a21d4b7-d6ca-40d9-a639-b658c1f86d55
