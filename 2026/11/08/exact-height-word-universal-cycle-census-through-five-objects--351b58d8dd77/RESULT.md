# Exact height-word universal-cycle census through five objects

## Finding

For an integer \(n\ge 2\), let \(\mathcal W_n\) consist of all length-\(n\) words whose distinct letters are exactly \(\{0,1,\ldots,h\}\) for some \(0\le h<n\). This is the height representation of the weak orders on \(n\) labeled objects. Let \(U_n\) be the number of cyclic words which contain each member of \(\mathcal W_n\) once as a cyclic contiguous length-\(n\) factor, counting cyclic rotations of the whole word as the same cycle but **not** identifying letter permutations or reversed outputs.

The exact count through five objects is

\[
\begin{array}{c|r}
n & U_n\\ \hline
2&1\\
3&8\\
4&113192681472\\
5&6214252301172599252248681937277855126085721393995382376959963220030028306692926790213752299261892430397440
\end{array}
\]

The counting reduction works for every \(n\ge2\): all noncomplete overlap vertices have forced degree one and contract into paths between complete vertices. The resulting multigraph has exactly \(|\mathcal W_{n-1}|\) vertices; its degree-factorial contribution is explicitly

\[
P_n=\prod_{h=0}^{n-2}\big((h+1)!\big)^{(h+1)!S(n-1,h+1)},
\]

where \(S(m,j)\) denotes a Stirling number of the second kind. The remaining arborescence cofactors are evaluated exactly for \(n=2,3,4,5\). The numerical values, rather than the general applicability of standard Euler-tour theorems, are the finite enumeration asserted here.

## Assumptions and scope

The alphabet is the ordered set of nonnegative *height* labels. A word belongs to \(\mathcal W_n\) precisely when every integer between zero and its maximum occurs. The number \(|\mathcal W_n|\) is the ordered Bell number: respectively \(3,13,75,541\) for \(n=2,3,4,5\). A cyclic universal word has exactly that many positions; windows are indexed around the entire circle. No further quotient by swapping height letters, reversing direction, choosing a rank representation, or relabeling the underlying weak order is taken.

Each length-\(n\) word is an individually distinguished directed edge, even if the contracted graph has parallel arcs. The input graph includes self-loops. The convention for \(n=2\) gives one cyclic output class.

## Proof

**1. The full overlap graph.** Let \(G_n\) have the distinct length-\((n-1)\) prefixes of words in \(\mathcal W_n\) as vertices. Each \(w\in\mathcal W_n\) gives the arc \(w_1\cdots w_{n-1}\to w_2\cdots w_n\), labeled by \(w\). Because rotation preserves membership in \(\mathcal W_n\), every vertex has equal indegree and outdegree. Connectivity, and hence an Euler circuit, follows from the zero-increasing path argument of Horan and Hurlbert, Theorem 3.2 (2012). This is established prior work. Cyclic edge-distinct Euler tours and universal cyclic words correspond bijectively: reading the final letter of each successive edge recovers the output, and its consecutive length-\(n\) factors are precisely the traversed edge labels.

**2. The forced vertices.** For a vertex \(v\) of length \(n-1\), call it *complete* when its set of letters is \(\{0,\ldots,\max v\}\). If complete, exactly \(\max v+2\) letters can be appended, namely \(0,\ldots,\max v+1\). Otherwise, because \(v\) extends to an allowed length-\(n\) word, there is exactly one missing letter in its initial interval, and that letter is the **only** permitted extension. Thus every incomplete vertex has indegree and outdegree one; the complete vertices are precisely \(\mathcal W_{n-1}\), giving a core of ordered-Bell size.

**3. Forced corridors terminate.** Start at any incomplete vertex and follow its unique outgoing edge. Its associated complete length-\(n\) edge label can be cyclically rotated to put a largest letter last. The prefix of that rotated label contains every other required height, and hence is a complete vertex. Following successive forced outgoing arcs traces successive rotations of the original word until reaching a complete vertex, possibly sooner. It takes at most \(n\) edges. Therefore no directed cycle consists entirely of incomplete vertices. Maximal paths with incomplete interiors partition the original edges and produce a reduced balanced, connected, directed multigraph \(K_n\) on the complete vertices; each reduced arc retains its full labeled path, including parallel paths. Contracting a degree-one interior vertex preserves cyclic Euler tours bijectively, because its incoming arc must be followed immediately by its unique outgoing arc. The same holds along all corridors.

**4. Exact tour formula.** Write \(d_v\) for the outdegree of core vertex \(v\), \(A\) for the integer adjacency matrix of \(K_n\) counting *distinguished* parallel arcs and loops, and \(L=\operatorname{diag}(d)-A\). Delete the row and column belonging to the all-zero core vertex to obtain \(L_0\). The directed matrix–tree theorem gives the number \(t_n=\det(L_0)\) of inward arborescences, and the directed BEST theorem gives the number of cyclic edge-distinct Euler tours

\[
U_n=\det(L_0)\prod_{v\in\mathcal W_{n-1}}(d_v-1)!.
\]

This is the unrooted cyclic-tour normalization, because any tour is rooted uniquely by the edge labeled by the all-zero length-\(n\) word; no extra factor of \(|\mathcal W_n|\) or \(d_v\) is introduced. For complete words of maximum height \(h\), \(d_v=h+2\). There are \((h+1)!S(n-1,h+1)\) such words, yielding the stated all-\(n\) formula for \(P_n\).

**5. Determinants and products.** In ascending height-word lexicographic order, the reduced matrices have \(1,3,13,75\) rows. Their root cofactors and factorial products are

\[
\begin{array}{c|r|r}
n & t_n & P_n\\ \hline
2&1&1\\
3&2&4\\
4&37908&2985984\\
5&27571102170646823740986252600397906575360&225390057412667141559249255183922002204556655201227127499578671104
\end{array}.
\]

Taking the indicated products proves the displayed values of \(U_n\). The full deterministic construction of every cofactor entry, the exact determinant algorithms, and the labeled core-corridor certificate for \(n=5\) are supplied as standalone attachments. Neither numeric determinant is inferred from a short prefix of a sequence.

## Verification

Run `python3 verify_exact.py` and `python3 crosscheck.py` from the directory containing the attachments. Both use only the Python standard library. The first enumerates valid height words, constructs and verifies disjoint forced corridors, checks the 308-path certificate against all 541 original edges at \(n=5\), computes cofactors by exact fraction-free Bareiss elimination, and checks all four counts. The second regenerates words by surjectivity at each alphabet size and independently computes cofactors by modular Gaussian elimination and the Chinese remainder theorem, with a row-sum Hadamard bound smaller than the CRT modulus; it uses the **full uncontracted graph** for \(n\le4\), and brute-enumerates complete Euler tours at \(n=3\), obtaining eight. It performs a separately generated contraction for \(n=5\). Successful outputs are `VERIFY_OK` and `CROSSCHECK_OK`.

For \(n=5\), the original graph has 308 vertices and 541 edges. The contracted graph has 75 vertices and 308 distinguished arcs; its outdegree histogram is \(\{2:1,3:14,4:36,5:24\}\). These statistics and all counts are serialized in `counts.json`; `core_edges_n5.tsv` lists every reduced arc with its original edge-label path. The CRT modulus has 82 decimal digits and exceeds the explicit 66-digit Hadamard upper bound on the relevant determinant.

## Relationship to prior work

Horan and Hurlbert (first posted March 23, 2012, arXiv:1203.5169) introduce this height-word overlap graph and prove universal-cycle **existence**, not the complete cycle multiplicity. The directed BEST and matrix–tree theorems are classical and are explicitly acknowledged, not claimed as new. Sawada and Wong (2020) give efficient successor rules for constructing a universal cycle using both height and rank representations; their worked examples at small orders are not enumerations of *every* such cycle. Sawada, Sears, Trautrim, and Williams (2023) use concatenation trees to generate universal cycles efficiently; Section 5.3 discusses weak-order construction, not a complete count of all Euler tours. Sawada and Gabrić (first posted October 18, 2025) give a general arborescence-based method for sampling universal cycles uniformly, and explicitly explain how to generate all tours from trees (Section 2); their Section 4.2 concerns weak-order sampling and random-walk cover-time experiments, not an evaluated count at orders four or five. Thus the general enumeration mechanism is earlier work, while the evaluated exact invariant and degree-one-core certificate are the finite claim here.

The standard ordered Bell sequence OEIS A000670 counts input weak orders \(|\mathcal W_n|\), not cyclic universal output words \(U_n\). A web search also located the integer \(113192681472\) as an unrelated term of OEIS A027271; numerical coincidence alone is not mathematical coverage. Searches for weak-order universal-cycle counts, Cayley-permutation Euler tours, and the exact determinants did not identify an equivalent published enumeration. Failed searches do not prove priority; residual risk of an unindexed earlier table remains.

## Limitations

The evaluated census stops at \(n=5\); although the core reduction and tour formula apply for every \(n\ge2\), no closed form for the arborescence cofactor is established for arbitrary \(n\). The result does not enumerate rank-representation universal words, weak-order cycles modulo other symmetries, or restricted height and weight classes. The computational checks do not replace the structural reduction proof and cited standard graph theorems. Historical priority remains subject to independent literature verification.

## References

1. V. Horan and G. Hurlbert, *Universal Cycles for Weak Orders*, arXiv:1203.5169, first public version March 23, 2012. https://arxiv.org/abs/1203.5169
2. J. Sawada and D. Wong, *Efficient Universal Cycle Constructions for Weak Orders*, *Discrete Mathematics* 343 (2020), 112022. Author full text: https://www.cis.uoguelph.ca/~sawada/papers/weak.pdf
3. J. Sawada, J. Sears, A. Trautrim, and A. Williams, *Concatenation trees: A framework for efficient universal cycle and de Bruijn sequence constructions*, arXiv:2308.12405 (2023). https://arxiv.org/abs/2308.12405
4. J. Sawada and D. Gabrić, *Las Vegas algorithms to generate universal cycles and de Bruijn sequences uniformly at random*, first public version October 18, 2025, arXiv:2510.16545. https://arxiv.org/html/2510.16545v3
5. The directed BEST theorem (de Bruijn–van Aardenne-Ehrenfest–Smith–Tutte) and the directed matrix–tree theorem, classical exact counting results. https://en.wikipedia.org/wiki/BEST_theorem
6. OEIS A000670 (ordered Bell/Fubini numbers), https://oeis.org/A000670 ; OEIS A027271 (unrelated numeric coincidence), https://oeis.org/A027271
