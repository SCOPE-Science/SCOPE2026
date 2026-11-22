# An optimizer-collapse transition in generalized Petersen domination shattering

## Finding

Let \(G_n=\operatorname{GP}(n,2)\), for \(n\in\{8,9\}\), and let \(\mathcal H_n\) be the family of all minimum-cardinality \([1,2]\)-dominating vertex subsets, viewed as binary membership concepts on the vertices. Both graphs have \([1,2]\)-domination number six, but their optimizer counts, shattered-support complexes and online learning dimensions differ sharply:

| Invariant | \(G_8\) | \(G_9\) |
| --- | ---: | ---: |
| Number of optimal concepts | \(248\) | \(9\) |
| Shattered-support polynomial | \(1+16z+116z^2+464z^3+812z^4+32z^5\) | \(1+18z+81z^2\) |
| VC dimension | \(5\) | \(2\) |
| Littlestone dimension | \(6\) | \(2\) |

For \(G_8\), exactly \(32\) shattered five-vertex supports form two full dihedral orbits of size \(16\) each. In the labeling below, orbit representatives are \(\{u_2,u_4,u_7,v_0,v_1\}\) and \(\{u_3,u_7,v_0,v_1,v_3\}\). The shattered-support complex is nonpure, with exactly \(660\) inclusion-maximal four-vertex supports and \(32\) inclusion-maximal five-vertex supports.

For \(G_9\), the entire optimal concept class is the \(3\times3\) family
\[
S_{a,b}=\{u_i:i\equiv a\pmod3\}\cup\{v_i:i\equiv b\pmod3\},\qquad a,b\in\{0,1,2\}.
\]
Its shattered supports are precisely the empty support, all single vertices, and all cross-shore vertex pairs. Therefore its shattering complex is the graph \(K_{9,9}\), homotopy equivalent to a wedge of \(64\) circles.

## Assumptions and scope

All vertices are labeled. The graph \(G_n\) has vertices \(u_0,\ldots,u_{n-1},v_0,\ldots,v_{n-1}\), indices interpreted modulo \(n\), and undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for every \(i\). A subset \(S\) is \([1,2]\)-dominating if for every vertex \(x\notin S\), \(1\le|N(x)\cap S|\le2\). There is no requirement on the neighbors of a selected vertex, and this is *not* total domination. Each hypothesis is the characteristic function of one minimum-cardinality set \(S\). A query support \(T\) is shattered when every subset of \(T\) occurs as \(S\cap T\). The Littlestone dimension is the maximum depth of a complete binary query tree with a distinct realizable membership outcome at every internal split, allowing queries to depend on earlier outcomes.

## Proof

**Minimum cardinality and exact finite universe.** The published all-order theorem of Beggas, Turau, Haddad, and Kheddouci gives \(\gamma_{[1,2]}(G_n)=6\) at both \(n=8\) and \(n=9\). Independently, the Python certificate enumerates every vertex subset of smaller cardinality and checks the exact graph-neighborhood predicate, finding no feasible set; both certificates then enumerate all size-six subsets. There are \(\binom{16}{6}=8008\) potential subsets for \(G_8\) and \(\binom{18}{6}=18564\) for \(G_9\). Filtering with the necessary-and-sufficient vertexwise condition produces exactly \(248\) and \(9\) subsets. These finite exhaustions constitute complete proofs for the stated orders, not empirical samples.

**Static shattering.** For each support \(T\) of size \(k\), construct all binary traces \(\{S\cap T:S\in\mathcal H_n\}\). Shattering is equivalent to having exactly \(2^k\) distinct traces. The two separately implemented enumerations over every support through size six obtain the displayed polynomials, with zero six-supports at \(n=8\), and zero three-supports at \(n=9\). Since shattering is downward closed, these zero layers exclude all higher layers. In particular the VC dimensions are five and two.

For \(n=8\), an exact membership check over the complete set of shattered supports yields the facet census \(660\) at cardinality four and \(32\) at cardinality five; all smaller shattered supports extend to larger ones. Applying the graph's index rotations \(i\mapsto i+r\) and reflections \(i\mapsto r-i\) to the two displayed five-support representatives yields two disjoint sets of \(16\) supports, whose union is exactly the full five-support census.

For \(n=9\), the exhaustive list of all nine size-six optima is exactly the displayed \(S_{a,b}\) family. Every two queries on the same shore either have identical values for every concept (if their indices agree modulo three) or cannot both be positive (otherwise), so no same-shore pair is shattered. For every cross-shore pair, the independent choices of \(a\) and \(b\) realize all four labels. This proves the exact complete bipartite shattering complex without further enumeration. Its first homology has rank \((9-1)(9-1)=64\), and its higher reduced homology vanishes.

**Adaptive shattering.** For a nonempty residual family \(\mathcal F\) of characteristic functions define \(R(\mathcal F)=0\) when no query gives two nonempty branches, and otherwise define
\[
R(\mathcal F)=1+\max_{x:\,\mathcal F_{x,0},\mathcal F_{x,1}\ne\varnothing}\min\{R(\mathcal F_{x,0}),R(\mathcal F_{x,1})\}.
\]
Each branch is a strictly smaller finite family, making this a well-founded exact dynamic recursion. The two independent verifiers memoize all reachable residual hypothesis sets, yielding root values \(6\) and \(2\), with respectively \(91615\) and \(49\) distinct memoized states. The Python verifier also constructs and recursively checks full mistake trees with \(64\) and \(4\) nonempty leaves. The recursion establishes upper bounds, while the constructed trees establish matching lower bounds. For \(G_9\), the structural \(3\times3\) family also gives the value two directly as the product of two three-choice singleton families.

## Verification

The self-contained files `check/verify_python.py` and `check/verify_cpp.cpp` use separately written complete searches and exact integer/bitset arithmetic. Run `python3 check/verify_python.py`, then compile `check/verify_cpp.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra` and execute the binary. Expected complete outputs are embedded in `check/python_output.txt` and `check/cpp_output.txt`. The first program enumerates all smaller candidate cardinalities and constructs adaptive witness trees. The second separately enumerates the full size-six candidate layer by integer masks, verifies every query support up to size six, and solves the exact online rank recurrence. Both were compiled or run using their actual package source contents.

## Relationship to prior work

Beggas, Turau, Haddad and Kheddouci (arXiv:1906.11966, first publicly posted 27 June 2019), Theorem 1 and Lemma 3, determine the minimum \([1,2]\)-domination numbers, including the value six at orders eight and nine. Their full publicly accessible manuscript, including its small-order cases and conclusions, concerns optimum cardinalities and does not state the optimizer counts, the trace polynomials, the dihedral orbit census, or the two online dimensions here. Chen, Ma, Shi and Zhao (2018) also determined domination numbers for generalized Petersen graphs; their publisher full text was not accessible for a complete comparison. This statement does not claim that minimum cardinalities are new. Nearby published database results study other kinds of domination, other graphs, and their shattering invariants, none of which logically implies these two exact concept families in the materials inspected.

## Limitations

These are exact finite-order results for \(n=8\) and \(n=9\), not a recurrence for arbitrary generalized Petersen order. The proof is reproducible exhaustive enumeration supplemented by the explicit \(n=9\) structural classification and an exact online-rank recurrence; it is not a hand-only orbit-by-orbit classification of every \(n=8\) optimizer. The homotopy claim concerns only the \(n=9\) complex. Database searches cannot establish absolute novelty, and full text of the related 2018 article could not be inspected. There is no independent external mathematical audit.

## References

1. F. Beggas, V. Turau, M. Haddad and H. Kheddouci, *[1,2]-Domination in Generalized Petersen Graphs*, arXiv:1906.11966 (public v1, 27 June 2019), https://arxiv.org/abs/1906.11966.
2. L. Chen, Y. Ma, Y. Shi and Y. Zhao, *On the [1,2]-domination number of generalized Petersen graphs*, Applied Mathematics and Computation **327** (2018), 1–7, https://doi.org/10.1016/j.amc.2018.01.013. Accessible abstract only; full text not inspected.
