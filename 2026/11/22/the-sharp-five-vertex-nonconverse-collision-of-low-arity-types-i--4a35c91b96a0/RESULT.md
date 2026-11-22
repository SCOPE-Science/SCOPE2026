# The sharp five-vertex nonconverse collision of low-arity types in the generic transitive-triangle-free oriented graph

## Finding
Let \(M\) be the Fraïssé limit of finite loopless oriented graphs omitting the transitive three-vertex tournament \(T_3\). For a finite pointwise named induced base \(G\subset M\), write \(t_r(G)\) for the number of complete types of ordered \(r\)-tuples of distinct new vertices over \(G\), and let \(G^{\mathrm{op}}\) reverse all arcs. Define the low-arity signature \(\sigma(G)=(t_1(G),t_2(G))\).

**Sharp classification.** For each fixed \(n\le4\), any two \(n\)-vertex bases having equal \(\sigma\) are isomorphic or converse-isomorphic. Among five-vertex bases there is precisely one fiber of \(\sigma\) containing more than one isomorphism/converse-isomorphism class. It has exactly two classes, with \(t_1=44\) and \(t_2=3882\), represented by the following arc sets on vertex labels \(0,1,2,3,4\):

\[
\begin{aligned}
E(G_A)&=\{1\to0,0\to2,0\to3,3\to1,4\to2,4\to3\},\\
E(G_B)&=\{2\to0,0\to3,1\to2,3\to1,4\to2,4\to3\}.
\end{aligned}
\]

The underlying undirected graph of \(G_A\) contains a triangle, whereas that of \(G_B\) is \(K_{2,3}\). Their three-point type counts are unequal:
\[
 t_3(G_A)=653452,\qquad t_3(G_B)=658282.
\]
Thus the third arity separates the unique first nonconverse collision of the first two type counts.

## Assumptions and scope
An oriented graph permits, for every unordered pair, either one arc in one direction or no arc, never both. \(T_3\) is the transitive tournament on three vertices; every fully oriented triple in a valid finite graph must therefore be a cyclic triangle. The finite age is a free-amalgamation class (a forbidden triangle is complete and cannot cross a free amalgam); its homogeneous limit realizes every finite admissible extension of the named base. A complete nonalgebraic tuple type is determined by the finite induced diagram with its pairwise distinct new vertices.

The comparison relation used in the classification is **unlabelled isomorphism or simultaneous reversal of all arcs**. The finite base is pointwise named when its types are counted; the isomorphism/converse comparison is between bases. Converse identification is essential: globally reversing all arcs preserves every scalar \(t_r\) while need not preserve the graph's orientation-isomorphism class.

## Proof
**One- and two-point reduction.** Code the relation of one new point \(x\) to an old vertex \(i\) by \(p_i\in\{-1,0,+1\}\), with \(+1\) meaning \(x\to i\), \(-1\) meaning \(i\to x\). If the old graph has an arc \(i\to j\), and both \(p_i,p_j\) are nonzero, the only valid choice is \((p_i,p_j)=(+1,-1)\); it makes the triple cyclic. Reverse the signs for a reverse old arc. Let \(P(G)\) be the set of allowed sign vectors and \(q=|P(G)|\). Then \(t_1(G)=q\).

For an arc \(x\to y\) between two new points, a named old vertex adjacent to both must close the cycle \(x\to y\to i\to x\). Thus the two sign vectors \(p,q'\in P(G)\) are compatible exactly when for every old coordinate \(i\), either at least one of \(p_i,q'_i\) vanishes or \((p_i,q'_i)=(-1,+1)\). Define the zero-one matrix \(A\), indexed by \(P(G)\), by this condition, and let \(R=\sum_{p,q'}A_{p,q'}\). When the new points are nonadjacent there is no additional forbidden triangle, giving \(q^2\) possibilities. The two arc directions contribute equally by reversing the roles of the new points. Hence
\[
 t_2(G)=q^2+2R.
\]
So equality of \((t_1,t_2)\) is equivalent to equality of \((q,R)\).

**Finite exhaustive classification.** Enumerate every ternary assignment to the \(\binom n2\) unordered pairs for each \(0\le n\le5\), retaining precisely those without a transitive complete triple. Enumerate the \(3^n\) sign vectors for each graph and calculate \(q,R\) by the preceding local formulas. Canonicalize each old graph under the full symmetric group on its vertices and optional simultaneous arc reversal. The standalone exact checker `verify.cpp` implements all loops explicitly; its complete results are:

| \(n\) | Admissible labelled bases | Isomorphism/converse classes | Distinct signatures | Nontrivial signature fibers |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |
| 2 | 3 | 2 | 2 | 0 |
| 3 | 21 | 5 | 5 | 0 |
| 4 | 317 | 17 | 17 | 0 |
| 5 | 9735 | 79 | 78 | 1 |

The unique nontrivial fiber at \(n=5\) is \((q,R)=(44,973)\), and its two canonical representatives have ternary arc codes `3048` and `3124`. Codes are base-three encodings, least-significant digit first, of the arc states \(-1,0,+1\) on pairs ordered lexicographically \((0,1),(0,2),\ldots,(3,4)\), stored as digits \(0,1,2\). The arc lists above decode these integers exactly. The checker enumerates every possible base diagram and every vertex permutation and converse, so this is an exhaustive finite classification rather than sampled evidence. Because \(G_A\) has an underlying triangle and \(G_B\) does not, they are not related by isomorphism or converse.

**Three-point separation.** Let \(u_p=\sum_q A_{p,q}\) and \(v_p=\sum_q A_{q,p}\) be its row and column sums. An admissible three-new-vertex diagram has zero, one, two or three arcs; if all three arcs occur they must form one of the two directed cycles. Counting these diagrams yields the exact identity
\[
\begin{aligned}
 t_3(G)={}&q^3+6qR+3\sum_p u_p^2+3\sum_p v_p^2\\
 &+6\sum_pu_pv_p+2\operatorname{tr}(A^3).
\end{aligned}
\]
The finite integer matrices of the two explicit bases yield the three-point counts stated above. As an independent check, `crosscheck.py` enumerates the \(21\) admissible orientations on the three new vertices and tests each combination of valid one-point diagrams directly, reproducing \(653452\) and \(658282\).

## Verification
Build and run `verify.cpp` using `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`, then run `python3 crosscheck.py`. The recorded output is in `verification_output.txt`. All operations use exact integers, no randomness, floating point or external databases. The exhaustive proof is limited to bases through five vertices; the identity for arbitrary \(G\) and the three-point counting formula are general finite-diagram identities.

## Relationship to prior work
Cherlin's homogeneous directed graph classification and earlier construction of free-amalgamation homogeneous directed graphs supply the existence and structural setting, not the specified five-point numerical collision. Kühn–Osthus–Townsend–Zhao study the global asymptotic structure and enumeration of \(T_3\)-free labelled oriented graphs, not finite-base extension-orbit signatures. Prior numerical type-count results for undirected Henson graphs or differently forbidden directed graph classes do not imply the present orientation-specific classification; their local admissibility constraints differ. The finite exhaustive uniqueness and ternary separation are the claims advanced here, not the general Fraïssé construction or the counting of unconstrained ternary assignments.

## Limitations
There is no reconstruction claim for arbitrary bases above five vertices, nor a claim that three-point counts always distinguish nonconverse five-vertex bases. Numerical type counts are not equivalent to first-order logic with only the same number of variables. Isomorphic and converse-isomorphic bases are identified only for the **classification**, not when counting pointwise named types. Publication priority is provisional; no independent mathematical audit has been performed.

## References
- G. Cherlin, *Infinite homogeneous directed graphs*, public author-hosted text, §2.1.4, https://sites.math.rutgers.edu/~cherlin/Paper/1992Digraph.pdf.
- G. Cherlin, *The Classification of Countable Homogeneous Directed Graphs and Countable Homogeneous n-Tournaments*, Memoirs AMS 131 (1998), no. 621, https://doi.org/10.1090/memo/0621.
- D. Kühn, D. Osthus, T. Townsend, Y. Zhao, *On the structure of oriented graphs and digraphs with forbidden tournaments or cycles*, arXiv:1404.6178, first posted 2014-04-24, https://arxiv.org/abs/1404.6178.
