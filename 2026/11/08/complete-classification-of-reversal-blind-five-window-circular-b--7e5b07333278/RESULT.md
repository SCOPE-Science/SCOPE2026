# Complete classification of reversal-blind five-window circular binary identifiers

## Finding

Let \(k\ge5\) be an integer and let \(w\in\{0,1\}^k\) be a circular word with indexed positions modulo \(k\). For each \(i\), write \(W_i=w_iw_{i+1}w_{i+2}w_{i+3}w_{i+4}\), interpreting subscripts modulo \(k\). An observation retains the reversal class \([W_i]=\{W_i,W_i^R\}\), but not the direction in which its five-bit arc was read. Call \(w\) *position-distinguishable* if all \(k\) observation classes are distinct. Two position-distinguishable circular identifiers can coexist exactly when their sets of observation classes are disjoint. Identifiers are considered modulo rotation, not bit complementation or reversal.

**Theorem.** Position-distinguishable circular words exist exactly for
\[
 k\in\{6,7,8,9,10,12\}.
\]
The numbers of such words modulo cyclic rotation, in the order of these six lengths, are respectively \(2,4,4,4,2,4\). There are precisely \(20\) such rotation classes in total; `CENSUS.txt` lists every canonical representative. At any common fixed length \(k\ge5\), any two position-distinguishable words share at least one observation class. Consequently, the largest possible reversal-blind five-window codebook has size
\[
 E_{\mathrm{rev}}(k)=\begin{cases}1,&k\in\{6,7,8,9,10,12\},\\0,&\text{otherwise},\end{cases}\qquad (k\ge5).
\]
The maximum length of a single position-distinguishable circular binary identifier with five-bit unoriented readings is therefore exactly \(12\), attained, for example, by `000100110111`.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\); the read length is exactly five bits; every cyclic arc of five consecutive positions is observed without noise; the receiver discards only the order of reading along the arc (reversal), not bit labels or the arc position. A palindrome is a legitimate observation and may occur once. The task is to infer the arc position, **not** the viewing direction. This is strictly different from classical orientable sequences, which prohibit palindromic windows in order to infer direction as well. A codebook uses the same circumference \(k\) for all identifiers. The observed class sets must be disjoint both within and across identifiers.

## Proof

There are \(2^5=32\) labeled binary five-bit words. Exactly \(2^3=8\) are palindromes, and the other \(24\) form \(12\) reversal pairs, so exactly \(20\) reversal classes exist. Distinctness of all \(k\) window classes therefore forces \(k\le20\). This proves that it suffices to examine the finite range \(5\le k\le20\).

Introduce the binary order-four de Bruijn state graph with vertices \(0,1,\ldots,15\), encoding four-bit strings. From state \(v\), a choice of appended bit \(b\in\{0,1\}\) gives the five-bit edge label \(e=2v+b\in\{0,\ldots,31\}\) and next state \((2v+b)\bmod16\). Give edge \(e\) the class label \(c(e)=\min\{e,\operatorname{reverse}_5(e)\}\). A cyclic word corresponds to a closed walk in this graph, with exactly its cyclic five-windows as edge labels. It is position-distinguishable exactly when no class label is reused on its walk.

For each of the \(16\) initial states, the exhaustive recursion of `verify_graph.py` follows both possible outgoing bits when their reversal class is not yet in its used-class mask. It registers a closed walk whenever the current state equals the initial state at a depth between \(5\) and \(20\). It reconstructs the first \(k\) bits from the initial four bits and the append choices, and canonically rotates the result. It stops at depth \(20\), the established upper bound. The recursion is exhaustive: every eligible closed walk has an initial four-bit state and exactly one sequence of appended bits, and the algorithm explores every such sequence until its first prohibited class reuse. Conversely, any registered walk is closed and has distinct class labels, so it gives a valid circular word. Revisiting a vertex is allowed; only reusing a reversal-class edge is forbidden.

The recursion expands exactly \(3242\) nodes and yields precisely the twenty canonical words in `CENSUS.txt`. Its counts are \(2,4,4,4,2,4\) at lengths \(6,7,8,9,10,12\) and zero at all other lengths \(5\le k\le20\). This is a fully finite exhaustive proof of the existence and classification assertions, because the recursion invariant and the upper bound establish both completeness and soundness. `verify_direct.cpp` independently enumerates all \(2^k\) indexed words for each of the sixteen possible lengths, tests the reversal classes of all cyclic five-windows directly, and gives the identical list.

For each fixed length among the six possible lengths, the scripts also form the twenty-bit observation mask of each canonical word. Every two such masks of that fixed length have nonempty intersection, checked by the exhaustive pair comparison over the complete list. Therefore no two distinct identifiers at one length can coexist. One identifier exists at each of the listed lengths by the displayed witnesses. The claimed formula for \(E_{\mathrm{rev}}(k)\) follows, with larger lengths ruled out by the initial twenty-class bound.

## Verification

From a directory containing the three supplementary files, execute `python3 verify_graph.py` and `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_direct.cpp -o direct_check && ./direct_check`. Both depend only on standard libraries. The first checks a de Bruijn state-space recursion, its exact twenty canonical words, the \(3242\)-node count, and pairwise observation-mask intersection; it terminates in `GRAPH_COMPLETE_OK expanded=3242 necklaces=20`. The second tests literal indexed words and terminates in `DIRECT_COMPLETE_OK total=20`. Both were executed successfully from the package contents. This is exact bounded enumeration with an explicit exhaustive-search argument, not extrapolation from sampled lengths.

## Relationship to prior work

Grubman, Şekercioğlu and Wood (arXiv:1502.02199, first submitted 8 February 2015, Sections 1–2) study identifying *both* position and orientation from ordered circular windows; their eBug number counts disjoint cycles in an ordinary directed de Bruijn graph. The present observation instead identifies the two directions of a read, so the available symbols are reversal classes and the optimization is different. Their Section 4.5 also relaxes the need to distinguish **position** while retaining ordered reads, which is the reverse of our modification (position is required, read direction is not). The earlier ordered five-window classification does not imply this theorem.

Dai, Martin, Robshaw and Wild, *Orientable Sequences* (1993), study identifying orientation as well as position. Their orientability condition excludes palindromic reads, unlike the present position-only model; the twelve-bit witness above has four palindromic five-windows. The 1993 conference paper was located bibliographically but its complete text was not accessible in this review, leaving a historical-priority risk.

Burris, Motta and Shipman (arXiv:1608.08480, submitted 30 August 2016, Sections 1–5) study shortest *linear covering* words containing every reversal class at least once, including repeated classes when necessary; their objective is not maximum length or capacity of distinct reversal-class closed walks. Their results do not give the complete cyclic classification here.

The closest prior exact oriented circular identifier result establishes an unrestricted-direction capacity for five-bit windows. Replacing ordered windows by reversal classes cannot be achieved by taking a numerical corollary of that result: reversing a window merges different directed de Bruijn edges, while palindromic edges are allowed under this model.

## Limitations

The theorem is specific to the binary alphabet, read length five, cyclic noiseless readings, and position-only identification under reversal. It does not identify viewing direction, deal with read noise, or give a formula for other window lengths or alphabets. Exhaustive computation is finite and justified by the twenty-class bound; no formal proof-assistant certification and no external independent audit have been performed. Historical priority against inaccessible early literature remains a residual risk.

## References

1. T. Grubman, Y. A. Şekercioğlu, D. R. Wood, *Partitioning de Bruijn Graphs into Fixed-Length Cycles for Robot Identification and Tracking*, arXiv:1502.02199 (first public version 2015-02-08), https://arxiv.org/abs/1502.02199 .
2. K. M. Martin, Z. D. Dai, M. J. B. Robshaw, P. R. Wild, *Orientable Sequences*, Proceedings of the 3rd IMA Conference on Cryptography and Coding (1993), pp. 97–115, https://pure.royalholloway.ac.uk/en/publications/orientable-sequences/ .
3. C. S. Burris, F. C. Motta, P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480 (first public version 2016-08-30), https://arxiv.org/abs/1608.08480 .
