# The sharp first geodesic detour in prefix-normal word-chain generators

## Finding

For each integer \(n\ge 1\), let \(G_n\) have as vertices the permutations \(\pi\) of \(\{1,\ldots,n\}\) for which flipping the bits of \(1^n\) from one to zero in the order \(\pi(1),\ldots,\pi(n)\) leaves a prefix-normal word after every flip. Two vertices are adjacent if their permutations differ by one swap of neighboring entries. Let \(d_n\) be graph distance, and let \(K\) be the unrestricted Kendall adjacent-swap distance.

**Theorem.** For \(1\le n\le6\), every pair of vertices satisfies \(d_n(\pi,\rho)=K(\pi,\rho)\). At \(n=7\), there are exactly \(220\) vertices and exactly \(20\) unordered vertex pairs for which equality fails; for all of those pairs \(d_7=K+2\). Their joint \((K,d_7)\)-frequency spectrum is

\[
(4,6):4,\quad(5,7):6,\quad(6,8):4,\quad(7,9):3,\quad(8,10):2,\quad(9,11):1.
\]

For every \(n\ge7\), some pair of vertices in \(G_n\) has unrestricted distance four but induced distance six. Thus seven is the sharp first order at which the prefix-normal generator graph ceases to embed isometrically in the adjacent-transposition permutahedron.

## Assumptions and scope

A binary word \(w\) of length \(n\) is *prefix normal* if every contiguous factor of every length \(\ell\in\{1,\ldots,n\}\) has at most as many ones as the length-\(\ell\) prefix. The graph has only admissible generator permutations as vertices; edges swap consecutive **entries of the permutation**, not adjacent bits in one intermediate word. Paths are required to remain in this graph. The theorem concerns all \(n\ge1\) and makes no assertion about the graph's diameter or the maximum detour at orders above seven.

## Proof

**1. Exact finite boundary.** The accompanying independently implemented programs `check_a.py` and `check_b.py` each enumerate every permutation of \(\{1,\ldots,n\}\) that passes the defining prefix-normal test at every intermediate bitmask. The first uses a direct full-permutation scan; the second constructs the same words by a recursive bitmask path search. Each constructs all adjacent-transposition edges, computes every connected-component graph distance by breadth-first search, and compares it with the exact Kendall inversion distance, defined as the number of unordered label pairs with different relative orders in the endpoints. Since every length-\(n\) permutation is included in the direct scan, and each bitmask and all factor intervals are checked literally, these finite tests are exhaustive, rather than samples. The independently matching outputs establish the stated vertex counts \(1,1,2,4,14,44,220\), no exceptional pairs for \(n\le6\), and exactly the six displayed exceptional distance classes at \(n=7\). The scripts are short standalone certificates and their loops make the finite enumeration reproducible without unlisted software or data.

**2. A concrete sharp obstruction.** At length seven take

\[
P=(6,4,3,7,2,5,1),\qquad Q=(6,4,2,5,3,7,1).
\]

Both are admissible. A path through admissible vertices of length six is

\[
\begin{aligned}
&(6,4,3,7,2,5,1),\ (6,4,7,3,2,5,1),\\
&(6,4,7,2,3,5,1),\ (6,4,2,7,3,5,1),\\
&(6,4,2,7,5,3,1),\ (6,4,2,5,7,3,1),\\
&(6,4,2,5,3,7,1).
\end{aligned}
\]

Here consecutive permutations differ by exactly one adjacent transposition. Their admissibility follows directly from the defining test and is independently checked by the accompanying code. Between \(P\) and \(Q\), only the relative orders of the four cross pairs \(\{3,7\}\times\{2,5\}\) change, hence \(K(P,Q)=4\). Any unrestricted four-swap route must begin by interchanging the adjacent entries \(7,2\): all other neighboring pairs already have their target order, and swapping such a pair would require undoing it and exceed the four-swap budget. That forced first move yields \(P'=(6,4,3,2,7,5,1)\), which is not admissible: after the first four flips the word is `1000101`; its length-three prefix `100` has one one while the factor `101` at positions five through seven has two. Hence no four-step path exists. Every adjacent transposition changes permutation parity, so every possible path has even length; combined with the displayed six-step path, \(d_7(P,Q)=6\).

**3. Uniform infinite extension.** If \(\pi\) is an admissible generator of length \(m\), then \((m+1,\pi(1),\ldots,\pi(m))\) is admissible at length \(m+1\): after the first flip of its rightmost bit, every remaining intermediate word has the form \(w0\) for an intermediate prefix-normal word \(w\) of length \(m\). Appending zero preserves prefix normality, because any factor of \(w0\) that is not a factor of \(w\) is a suffix ending in zero, and deleting that final zero yields a factor of \(w\) of length one shorter, bounded by the corresponding prefix (which contains no fewer ones than the shorter prefix).

Apply this insertion repeatedly to each vertex of the displayed six-step path. For every \(n\ge7\) this supplies a legal six-step path between \(P_n=(n,n-1,\ldots,8,P)\) and \(Q_n=(n,n-1,\ldots,8,Q)\), with the leading block omitted for \(n=7\). The unrestricted distance remains four: the new common leading labels preserve their relative orders against all labels. In any four-swap route, only initially reversed label pairs can be swapped, so the common leading block never moves; the old forced forbidden \(7,2\) move remains the only first move. Therefore distance four is impossible. Parity excludes five, hence \(d_n(P_n,Q_n)=6\) for every \(n\ge7\).

## Verification

Run `python3 check_a.py` and `python3 check_b.py` with Python 3.8 or later. Their recorded exact outputs are included as `check_a.out` and `check_b.out`. Both methods independently construct the same complete graphs and the same exceptional spectra through length seven. The first also directly verifies every vertex of the six-swap witness and its finite lifts through length twelve. The mathematical insertion argument, rather than these finite lift tests, proves the infinite extension.

## Relationship to prior work

Adamson, Dudey, Fleischmann and Huch introduced the prefix-normal word-chain generator framework in 2025 and proved that swapping an increasing adjacent pair of generator entries preserves admissibility. They study the connectedness question for the resulting swap graphs, but their proved monotone swap lemma does not imply that admissible shortest paths attain the unrestricted Kendall distance. Indeed, it gives connectivity via paths to the decreasing permutation but does not guarantee geodesic convexity. The present result answers a different metric question: it identifies the exact first failure of unrestricted shortest-path preservation, counts every minimal-order failure, and constructs witnesses at every higher order.

Separately, published work on adjacent swaps of \(132\)-avoiding permutations finds detours in a distinct permutation class. Its hypotheses neither contain nor characterize the prefix-normal-generator condition; no implication of this specific metric spectrum follows from the indexed statement.

## Limitations

The \(20\)-pair result is an **exact finite enumeration** at length seven, not a closed all-length formula. The uniform extension establishes existence of a two-step detour for every higher length, but not maximality of two there. The novelty conclusion is based on the inspected primary manuscript and actual indexed searches; unpublished, unindexed, or indirectly equivalent earlier arguments may exist. No independent external mathematical audit has been performed.

## References

1. D. Adamson, M. Dudey, P. Fleischmann, A. Huch, *Word Chain Generators for Prefix Normal Words*, arXiv:2508.19619v1, first posted 2025-08-27, https://arxiv.org/html/2508.19619v1 .
2. G. Fici and Zs. Lipták, *On Prefix Normal Words* (2011), underlying definition and jumbled-pattern-matching motivation; cited in reference 1.
3. *Quadratic adjacent-swap detours among 132-avoiding permutations* (2026), a distinct restricted-permutation metric problem.
