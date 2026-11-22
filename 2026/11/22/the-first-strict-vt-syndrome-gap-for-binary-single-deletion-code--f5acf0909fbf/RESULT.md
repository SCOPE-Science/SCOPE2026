# The first strict VT-syndrome gap for binary single-deletion codes with run ceiling two

## Finding
Let \(\mathcal R_n\) be the set of indexed length-\(n\) binary words that contain neither `000` nor `111` as a contiguous factor. Let \(M(n)\) be the largest size of a set \(C\subseteq\mathcal R_n\) for which the sets of words obtainable by **exactly one arbitrary deletion** from distinct codewords are disjoint. Then
\[
(M(1),M(2),\ldots,M(9))=(1,2,2,3,3,6,6,10,13).
\]
For the conventional Varshamov–Tenengolts syndrome classes
\[
V_a(n)=\left\{w\in\{0,1\}^n:\sum_{i=1}^n i w_i\equiv a\pmod{n+1}\right\},
\]
the maximum intersection \(\max_a|\mathcal R_n\cap V_a(n)|\) equals \(M(n)\) for every \(1\le n\le8\), but equals \(12\), strictly smaller than \(M(9)=13\), for \(n=9\). Thus length nine is the first length at which no single conventional VT syndrome class, restricted to the run-ceiling-two source, attains the constrained deletion-correcting capacity.

## Assumptions and scope
The run constraint concerns **both symbols** and includes the endpoints: no run of equal bits may exceed length two. There is no prescribed starting/ending symbol, no constant-weight condition and no cyclic wraparound. The deletion channel removes one symbol at an unknown position; received words are **not** assumed to obey the run constraint. Words are indexed linear words. Codes are sets, with no restriction on systematic encoding or linearity. Only lengths \(1\) through \(9\) are asserted; there is no asymptotic conclusion.

## Proof
For any word \(w=w_1\cdots w_n\), define its deletion shadow
\[
D(w)=\{w_1\cdots w_{i-1}w_{i+1}\cdots w_n:1\le i\le n\}.
\]
Repeated descendants caused by deletion inside a constant run are counted just once. Define an undirected compatibility graph \(G_n\) with vertex set \(\mathcal R_n\), joining two **distinct** vertices precisely when their deletion shadows are disjoint. A one-deletion-correcting code is exactly a clique of \(G_n\). Hence \(M(n)=\omega(G_n)\), without any relaxation.

The standalone `verify_exact.py` enumerates every allowed vertex and every deletion shadow. It then computes \(\omega(G_n)\) for each integer \(1\le n\le9\) by an exhaustive integer-bitset branching algorithm. The algorithm assigns proper greedy colors to each current candidate induced subgraph. Every clique uses at most one vertex per color, so the number of used colors is a rigorous upper bound; whenever this bound cannot improve the best verified clique, the entire branch is discarded. Otherwise the algorithm branches on each candidate vertex, reducing the next candidate set to its neighbors. By induction on the number of candidate vertices this covers every possible clique, and no pruning discards a potentially larger clique. The complete search returns the values displayed under **Finding**, with 14,968 recursive nodes at length nine. The length-nine graph has exactly 110 candidate words. The program also independently rechecks disjoint deletion shadows of each returned clique.

One explicit length-nine code of size thirteen is

```
001001011 001010100 001101101 010011010 010110011
011001001 011010110 100100110 101010101 101101100
110010100 110011011 110110010
```

Every word meets the run constraint. Computing its thirteen distinct deletion shadows and testing each pair confirms that all these shadows are disjoint. Together with the exhaustive clique upper bound, this proves \(M(9)=13\). The earlier eight maxima follow from the same exact exhaustive method; no inference from a finite trend is used.

For each \(n\), enumerate the ordinary VT syndrome \(\sum i w_i\pmod{n+1}\) over \(\mathcal R_n\). The maximum class sizes for lengths one through nine are respectively
\[
(1,2,2,3,3,6,6,10,12).
\]
More explicitly, at length nine the ten residue sizes \(a=0,1,\ldots,9\) are
\[
(11,10,12,12,10,11,10,12,12,10).
\]
Each VT class corrects one deletion by the classical VT property, and the exact graph maxima above show that these intersections are optimal through length eight. Since no length-nine residue has thirteen allowed words, the asserted first strict gap follows.

## Verification
Run `python3 verify_exact.py` in the directory containing this document. This uses only the Python standard library, constructs the compatibility graphs from definitions and checks all nine optima, syndrome sizes and deletion-disjoint witnesses. Its output is reproduced in `VERIFICATION.md`.

As an independent numerical cross-check, `python3 verify_milp.py` uses SciPy to rebuild an input-output incidence matrix directly from the deletion channel and solves the resulting binary packing integer program for lengths seven, eight and nine, recovering \(6\), \(10\) and \(13\). This solver check is corroborative only; the exhaustive integer-bitset search supplies the mathematical finite certificate and has no numerical dependence.

## Relationship to prior work
Kulkarni and Kiyavash's 2012 preprint introduces the deletion-shadow hypergraph optimization viewpoint and analyzes a distinct, guarded \((d,k)\) recording constraint; the exact source here instead forbids `000` and `111` with unrestricted endpoints. Schoeny, Wachter-Zeh, Gabrys and Yaakobi (2017), Section V-B, explicitly define maximum-run-limited binary words, intersect such sources with VT classes and use that technique for burst-deletion constructions; their result does not state the nine-bit constrained optimum or this first strict inequality. Takemoto and Nozaki (2020), Section IV-E, compare efficiently encodable maximum-run-limited single-indel constructions with general redundancy bounds, without an exact length-nine extremal classification. The present finite finding therefore goes beyond the inspected implications of these constructions and bounds; it does not challenge the ordinary unrestricted optimality of VT codes at length nine.

## Limitations
This is a finite exact statement for the particular run ceiling two, not a formula for arbitrary length, alphabets or run ceilings. The exhaustive proof assumes that the provided standard-Python implementation is executed as written; the correctness of its recursion and pruning is explained above, and a separate integer-programming formulation checks the larger cases. No independent human verification or external formal proof has been performed. A matching unindexed historical computation remains possible.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, first posted 2012-11-13. https://arxiv.org/abs/1211.3128
2. C. Schoeny, A. Wachter-Zeh, R. Gabrys and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, IEEE Transactions on Information Theory **63** (2017), 1971–1985. https://doi.org/10.1109/TIT.2017.2661747
3. R. Takemoto and T. Nozaki, *Construction and Encoding Algorithm for Maximum Run-Length Limited Single Insertion/Deletion Correcting Code*, arXiv:2012.13536, first posted 2020-12-25. https://arxiv.org/abs/2012.13536
