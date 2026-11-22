# Eight-step relaxation and unequal five-wave basins in four-state pentagonal-prism excitation

## Finding

Let \(G=C_5\square K_2=GP(5,1)\) be the ten-vertex pentagonal prism. For synchronous threshold-one, four-state Greenberg–Hastings excitation, all \(4^{10}=1{,}048{,}576\) labelled states eventually have least period one, four or five. There are exactly **one fixed point**, **530 primitive four-cycle orbits**, and **six primitive five-cycle orbits**. Their full attraction-basin populations, including recurrent states, are respectively \(436{,}846\), \(579{,}750\), and \(31{,}980\).

Every trajectory reaches its eventual cycle within a sharp eight updates, equivalently
\[
F^{28}=F^8,\qquad F^{27}\ne F^7.
\]
Exactly twenty states require all eight updates; every one reaches a five-cycle, and the twenty states constitute one orbit under the full twenty-element graph automorphism group.

The 530 temporal four-cycle orbits form 32 geometric classes: eleven of size ten and twenty-one of size twenty. The six temporal five-cycle orbits form **two** geometric classes, with respectively two and four temporal orbits. Each of the two orbits in the first class attracts exactly \(1{,}280\) initial states; each of the four orbits in the second class attracts exactly \(7{,}355\). Thus the two geometrically distinct kinds of five-wave have markedly unequal attraction basins despite identical temporal period.

The complete first-periodic-entry census is below. An entry is the number of labelled initial states \(x\) whose least entry time is \(t\) and whose eventual least period is \(p\).

| First entry \(t\) | Period 1 | Period 4 | Period 5 |
|---:|---:|---:|---:|
| 0 | 1 | 2,120 | 30 |
| 1 | 1,023 | 6,790 | 450 |
| 2 | 58,025 | 41,650 | 3,840 |
| 3 | 169,385 | 99,440 | 9,760 |
| 4 | 140,002 | 203,220 | 11,160 |
| 5 | 55,310 | 150,150 | 4,760 |
| 6 | 12,340 | 63,220 | 1,440 |
| 7 | 760 | 13,160 | 520 |
| 8 | 0 | 0 | 20 |
| **Total** | **436,846** | **579,750** | **31,980** |

## Assumptions and scope

The vertex set is \(\{u_i,v_i:i\in\mathbb Z/5\mathbb Z\}\). Its edges are \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\), where subscripts are cyclic. The label order for computation is \(u_0,\ldots,u_4,v_0,\ldots,v_4\). A state is a map \(x:V(G)\longrightarrow\{0,1,2,3\}\). With \(N(v)\) the three graph neighbors of \(v\), the synchronous map is exactly
\[
F(x)(v)=\begin{cases}
1,&x(v)=0\text{ and there is }u\in N(v)\text{ with }x(u)=1,\\
0,&x(v)=0\text{ and no such }u\text{ exists},\\
2,&x(v)=1,\\
3,&x(v)=2,\\
0,&x(v)=3.
\end{cases}
\]
The first periodic-entry time \(T(x)\) is the smallest nonnegative integer for which \(F^{T(x)}(x)\) lies on a directed cycle, and \(P(x)\) is its eventual least temporal period. A *primitive temporal orbit* identifies its different time phases, but not distinct graph labellings. A *geometric class* is an orbit of primitive temporal orbits under the entire graph automorphism group. The attraction basin of a temporal orbit includes every initial state whose trajectory eventually enters that particular orbit. No claim concerns other graphs, other numbers of colors, or other thresholds.

## Proof

**Exact finite encoding.** Associate with each state the integer
\[
s(x)=\sum_{j=0}^{9}x(v_j)4^j\in\{0,\ldots,4^{10}-1\},
\]
where \(v_j\) denotes the displayed vertex order. This is a bijection; thus visiting every such integer is a complete proof by finite exhaustion. Both embedded programs construct the prism graph and compute the update at every vertex without lookup tables or inferred transitions.

**Functional-graph completeness.** Every function from a finite set to itself has a disjoint union of directed cycles with directed in-trees attached. Removing every state of indegree zero, repeatedly, leaves exactly the cycle states: no cycle vertex can be removed, and a noncyclic retained in-tree would contain an indegree-zero leaf. An attached state inherits its eventual period from its forward neighbor, and its first-entry time is one more than that neighbor's time. Conversely, a state on a cycle has first-entry time zero. Therefore indegree pruning, explicit cycle traversal, and reverse propagation compute all \((T,P)\) pairs exactly, without any guessed time bound.

`verification/verify_prism_indegree.cpp` independently constructs all ten degree-three neighborhoods, evaluates the transition for every one of the \(1{,}048{,}576\) encoded states, and performs the indegree-pruning classification. It asserts that the only temporal cycle lengths are one, four and five, with respective orbit multiplicities one, 530 and six. It independently checks every displayed table cell, the basin totals and the sharp eight-update bound. It also evaluates both iterates on **every** encoded state to prove \(F^{28}(x)=F^8(x)\), and reports exactly twenty states where \(F^{27}(x)\ne F^7(x)\). The former identity follows as well from the computed entry cutoff and the fact that both nontrivial periods divide twenty; the latter makes the cutoff sharp.

**Second exhaustive reconstruction.** `verification/verify_prism_stdlib.py` constructs the same graph separately and uses path marking, identification of repeated states, and backward recursion, rather than indegree peeling. Its independent complete functional-graph census matches the C++ result for each entry time and period. Both programs calculate integers, with no random input or floating-point threshold. The generated output records are included; the programs are the repeatable exhaustive certificates, not just those output records.

**Geometric classes and basin sizes.** The only pentagonal cycles in the prism graph are the two rail pentagons. Every automorphism therefore permutes those rails and acts on each by the same dihedral rotation or reflection, since matching spokes must remain matched. Conversely, these actions are automorphisms. Thus the full automorphism group is \(D_5\times C_2\), of size twenty. The standard-library verifier enumerates all twenty actions explicitly as
\[
u_i\mapsto u_{\varepsilon i+j},\quad v_i\mapsto v_{\varepsilon i+j},
\]
with independent rail swap allowed, where \(\varepsilon\in\{-1,1\}\) and \(j\in\mathbb Z/5\mathbb Z\). Each action commutes with \(F\). It maps the minimum-state representative of every temporal orbit to the canonical minimum of its image orbit, partitions all 537 temporal orbits, and checks that the class multiplicities sum to their respective exhaustive totals. Period-four classes have sizes ten (eleven classes) and twenty (twenty-one classes); the two period-five classes have sizes two and four. Canonical period-five representative state integers are 27,675 and 27,756, with equal attraction-basin sizes \(1{,}280\) and \(7{,}355\) across the members of the respective geometric classes. The sums \(2\cdot1{,}280=2{,}560\) and \(4\cdot7{,}355=29{,}420\) recover the complete period-five basin count \(31{,}980\).

Finally, the verifier identifies all twenty states with entry time eight, checks their eventual period is five, and proves they form exactly the orbit of the concrete initial state with encoded integer 28,081 under the twenty automorphisms. Its destination belongs to the larger-basin four-orbit five-wave class. This proves both sharpness and the claimed spatial type of every maximally delayed configuration.

## Verification

The embedded programs require Python 3 standard library and a C++17 compiler. From the package root run:

```sh
python3 verification/verify_prism_stdlib.py
c++ -std=c++17 -O2 verification/verify_prism_indegree.cpp -o /tmp/verify_prism_indegree
/tmp/verify_prism_indegree
```

The generated stdout should equal `verification/python_results.txt` and `verification/cpp_results.txt` respectively, apart from environment-neutral whitespace. These two algorithms exhaustively enumerate all \(4^{10}\) configurations, independently reconstruct the functional graph, and compute the complete joint \((T,P)\) census. The Python proof additionally computes the complete orbit-level symmetry and basin census. The C++ proof independently confirms the sharp global iterate identity. All assertions and input sizes are explicit; no random sampling, partial enumeration, or floating-point approximation is used.

## Relationship to prior work

Fisch, Gravner and Griffeath introduced a multi-color, threshold-parametrized Greenberg–Hastings formulation and investigated travelling patterns on planar lattices; the full inspected 1991 paper does not enumerate dynamics on this finite prism. Gravner, Lyu and Sivakoff treat three-color excitation on arbitrary graphs and provide qualitative synchronization and long-run activity results, not this four-color attraction-basin and entry-time table. Earlier exact research on the same pentagonal prism with **three** colors has periods one, three, four, five and seven and six primitive period-five orbits; its occurrence of five-cycles does not imply their multiplicities, basins or sharp transient profile at four colors. Earlier exact research with **four** colors on the Petersen graph \(GP(5,2)\) counts ninety primitive four-cycles and thirty primitive five-cycles with an eleven-step entry bound, a distinct graph and a different census. Neither result states or implies the eight-step prism census and unequal five-wave basin sizes here. Results on complete bipartite and tripartite graphs likewise require different adjacency structures. Published exact comparative records and their full result statements were inspected, not inferred from matching titles alone.

## Limitations

This is an exact, self-contained finite computational theorem about the specified ten-vertex prism. It does not establish an infinite-family formula, a universal law on cubic graphs, or an analytic closed form for the eight-step clock. Historical priority outside the inspected literature is not certified: the original 1978 Greenberg–Hastings article was accessible as an abstract/bibliographic record, not in full; unindexed prior computations could exist. The available precisely day-dated archival supporting source was public on 1993-03-22, while the original model is older; the stated archival date is not an origin date for the model. An external independent validation has not been performed.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523, https://doi.org/10.1137/0134040 (abstract and bibliographic record).
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39, https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf (full text inspected).
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint dated 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 (abstract and archival date).
4. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, submitted 2016-10-24, https://arxiv.org/html/1610.07320v1 (full text inspected).
5. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, public exact three-color comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-recurrence-and-basins-on-the-two-ten-vertex-generalized-pe--7d4c1d4df82a (full result statement inspected).
6. *Five-cycle survival and two four-cycle symmetry types in four-state Petersen excitation*, public exact four-color comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-five-cycle-survival-and-two-four-cycle-symmetry-types-in-four-st--9ac3197a4c9b (full result statement inspected).
