# Seventy nine-clique islands in optimal contagion on Tutte's eight-cage

## Finding

Let \(T\) be the Tutte–Coxeter graph, realized as the incidence graph between the fifteen edges (duads) and fifteen perfect matchings (synthemes) of \(K_6\). Under irreversible synchronous two-neighbour activation, an initial vertex set is *contagious* if every vertex eventually activates. The minimum contagious-set size is \(8\); the new finite classification is that there are **exactly \(12{,}780\)** such labelled eight-vertex sets. Their numbers by count \(j\) of initially selected duad vertices, for \(j=0,1,\ldots,8\), are

\[
(225,720,1860,2280,2610,2280,1860,720,225).
\]

The **one-vertex-exchange graph** \(\mathcal E\) has these \(12{,}780\) optimal sets as vertices; two sets are adjacent when one selected vertex is replaced by one unselected vertex, keeping the set optimal. It is eight-regular, with exactly \(51{,}120\) edges, and its components are **seventy disjoint copies of \(K_9\)** and **one connected component on \(12{,}150\) vertices**. The seventy nine-cliques consist of fifteen containing duad-only seeds, fifteen syntheme-only, twenty in which each seed has two or three duads, and twenty in which each seed has five or six duads. In the mixed cases, the nine seeds in each component split \(3+6\) by these two duad counts.

Under the natural action of relabelling the six vertices of \(K_6\), all optimal seeds form exactly \(40\) \(S_6\)-orbits, with orbit-size multiplicities

\[
15^{[2]},\;60^{[2]},\;90^{[3]},\;120^{[4]},\;180^{[4]},\;360^{[19]},\;720^{[6]}.
\]

Here exponents in square brackets mean multiplicity, not powers. The number of optima finishing in synchronous rounds \(4,5,6,7,8,9\), respectively, is \((120,660,3360,4320,1440,2880)\). These counts refer to unordered initial vertex subsets in the explicitly labelled graph.

## Assumptions and scope

Write \(D=\binom{\{0,1,2,3,4,5\}}2\), and let \(M\) be the fifteen partitions of \(\{0,1,2,3,4,5\}\) into three unordered pairs. Index the elements of \(D\) lexicographically as vertices \(0,\ldots,14\), and list \(M\) recursively by selecting the smallest unused symbol and pairing it successively with larger unused symbols, as in `enumerate_incidence.cpp`; syntheme vertices are \(15,\ldots,29\). An edge joins duad \(d\) to syntheme \(m\) exactly when \(d\in m\). This is a simple connected cubic graph of order \(30\) and size \(45\), isomorphic to Tutte's girth-eight cage. No unlabelled quotient is used when counting seeds.

At time \(0\), exactly the selected seed vertices are active. At each integer time \(t+1\), every previously inactive vertex having at least two active neighbours at time \(t\) becomes active simultaneously and permanently. The finishing round is the first time at which all thirty vertices are active. Exchange adjacency permits replacement by any graph vertex, not necessarily an adjacent vertex.

## Proof

**Known reduction, proved for clarity.** For any cubic graph \(G\), let \(S\) be initially active and \(U=V(G)\setminus S\). A cycle in \(G[U]\) cannot start activating: each vertex on the cycle has at most one neighbour outside it. Conversely, if \(G[U]\) is a forest, some leaf of each nonempty remaining induced component has at least two neighbours outside the remaining inactive set and activates at the next round. Repeating eliminates all inactive vertices. Thus contagious sets coincide exactly with feedback vertex sets for cubic graphs. This equivalence is classical, not asserted as new.

**Sharp size and tree rigidity.** For an arbitrary set \(S\) of \(k\) vertices in \(T\), write \(e(S)\) for the number of edges induced by \(S\). Since \(T\) is cubic with \(45\) edges, the complement induces exactly \(45-3k+e(S)\) edges on \(30-k\) vertices. If \(S\) is contagious, this complement is a forest, so

\[
45-3k+e(S)\le 29-k,\qquad 2k\ge16+e(S).
\]

Hence \(k\ge8\). At \(k=8\), equality is possible only when \(e(S)=0\) and \(T[V\setminus S]\) is a single tree on \(22\) vertices. Conversely, an independent eight-set with connected complement has an induced \(22\)-vertex subgraph with exactly \(21\) edges, hence a tree and a contagious seed. The exhaustive checker below constructs explicit such sets, establishing \(8\) as the optimum. The general lower bound and stable tree/independent partition phenomenon are already known in the decycling literature; only the exact instance census and exchange topology are offered as new.

**Universal exchange lemma.** Let a cubic graph have an independent set \(S\) whose complement is an induced tree \(H\). Fix \(s\in S\) with its three neighbours \(a,b,c\) in \(H\). There is a unique vertex \(m\in H\) lying simultaneously on the three simple paths \(P_H(a,b),P_H(a,c),P_H(b,c)\): the tree median. The median has degree three in \(H+s\): if it equals one of \(a,b,c\), two of these edges lie in \(H\) and one joins it to \(s\); otherwise all three lie in \(H\). Cubicity therefore ensures that \(m\) has no neighbour in \(S\setminus\{s\}\). Replacing \(s\) by \(m\) preserves independence, and the new complement \(H-m+s\) is a tree: deleting the median from the theta subgraph \(H+s\) cuts both of its independent cycles while preserving connectivity. The deletion leaves two or three branches of \(H\), according as \(m\) equals one of \(a,b,c\) or not, and \(s\) reconnects those branches without a cycle. Conversely, any replacement making the new complement a tree must destroy both independent cycles in \(H+s\), requiring removal of a vertex on all three paths, thus uniquely \(m\). Therefore every optimum of \(T\) admits **exactly one exchange per seed**, proving eight-regularity without relying on a degree census.

**Finite exhaustive classification.** The deterministic complete incidence enumeration processes each of the \(\binom{30}{8}=5{,}852{,}925\) labelled eight-subsets. It independently checks the contagion process and whether the twenty-two-vertex complement is an induced tree. Both tests accept the same \(12{,}780\) sets; their bipartition sizes and finishing rounds give the displayed distributions. It emits their integer bitmasks. The separate `orbit_exchange.py` program tests every valid single-vertex exchange from all these masks, computes all connected components, verifies the \(70K_9\) and \(12{,}150\)-component decomposition, enumerates all \(720\) six-symbol permutations, and partitions the entire optimum family into forty orbits of the displayed sizes. This is a complete finite exhaustion: no heuristic orbit extrapolation is used.

## Verification

Build `enumerate_incidence.cpp` with a C++17 compiler and run it to generate `optima.txt`. Then run the two supplied Python 3 scripts from the same directory. For example:

```sh
g++ -O3 -std=c++17 enumerate_incidence.cpp -o enumerate
./enumerate optima.txt
python3 verify_symplectic.py
python3 orbit_exchange.py
```

`verify_symplectic.py` **independently constructs** the same graph as the incidence graph of nonzero vectors and totally isotropic two-subspaces of the four-dimensional symplectic space over \(\mathbb F_2\). It enumerates all independent eight-sets via backtracking, checks connectivity of their complement, performs the synchronous infection process, and independently determines the exchange degree, component sizes, and nine-clique profiles. Both implementations agree: there are \(111{,}225\) independent eight-sets and exactly \(12{,}780\) among them whose complements induce trees. This supplies a mathematically distinct finite check for the counts and exchange structure.

The S6 orbit program uses the explicit six-symbol incidence model; its forty orbits are under this **specified subgroup** rather than an assertion about an unchecked larger automorphism group. All checks use only the three included source files and ordinary language compilers/interpreters; no external datasets are necessary.

## Relationship to prior work

Irreversible two-conversion was studied before this computation. The cubic-graph equivalence to feedback vertex sets appears explicitly in Takaoka and Ueno (2015), in turn citing earlier work. Classical theorems of Payan and Sakarovitch, discussed and strengthened by Nedela, Seifrtová and Škoviera (2023), establish the sharp decycling bound and existence of coherent partitions for suitable cubic graphs; hence neither the lower bound \(8\), the tree/independent form, nor the general exchange reduction is presented as a priority claim. The 2009 work of Rapaport and collaborators treats dissemination in cubic graph classes rather than this exact enumeration. The contribution is the **complete Tutte–Coxeter optimum multiplicity, six-symbol orbit census, synchronous finishing-time law, and disconnected exchange-component classification**. Related finite computations for other graphs, including Pappus and Desargues configurations, do not imply this instance's exact values.

## Limitations

The findings concern only the explicitly constructed Tutte–Coxeter graph, not every cubic graph of girth eight or every generalized quadrangle. The \(12{,}150\)-vertex component is proved connected by exhaustive graph search; no closed-form description of its graph structure, diameter, or independent mathematical publication is claimed. Exhaustive finite computation supplies the exact counts, while the lower-bound, tree equivalence and exchange-degree arguments are conceptual proofs. The searches and inspections recorded in the accompanying review do not rule out unindexed earlier enumerations. No independent scholarly validation has been performed.

## References

1. Rapaport, I., Suchan, K., Todinca, I., and Verstraete, J., *On Dissemination Thresholds in Regular and Irregular Graph Classes*, Algorithmica 59, 16–34; first public online 21 April 2009. https://doi.org/10.1007/s00453-009-9309-0
2. Takaoka, A., and Ueno, S., *A Note on Irreversible 2-Conversion Sets in Subcubic Graphs*, IEICE Transactions E98-D, 1589–1591 (2015); manuscript publicized 14 May 2015. https://doi.org/10.1587/transinf.2015EDL8021
3. Nedela, R., Seifrtová, M., and Škoviera, M., *Decycling cubic graphs*, arXiv:2309.11606, 20 September 2023. https://arxiv.org/abs/2309.11606
4. Payan, C., and Sakarovitch, M., classical cyclically-four-edge-connected cubic decycling theorem, as cited and precisely stated in Reference 3.
