# Strong odd colourings of the dodecahedral graph: a 212-partition census and a square-colouring gap

## Finding
Let \(D=\operatorname{GP}(10,2)\) be the twenty-vertex dodecahedral graph. Its **odd-independent-set polynomial** is
\[
I_D(t)=1+20t+100t^2+120t^3+90t^4+10t^6.
\]
Its strong odd chromatic number is exactly \(\chi_{\mathrm{so}}(D)=5\). With the vertices fixed and colour names forgotten, there are **exactly 212** optimal five-colour partitions. Their exhaustive block-size census is
\[
\begin{array}{c|r}
\text{sorted block sizes}&\text{number}\\ \hline
(2,3,3,6,6)&60\\
(3,3,4,4,6)&100\\
(4,4,4,4,4)&52
\end{array}
\]
Exactly **two** of the 212 optimal strong odd partitions are also proper colour partitions of the square \(D^2\), so the other 210 demonstrate a strict *colouring-level* relaxation even though \(\chi(D^2)=\chi_{\mathrm{so}}(D)=5\). The covering map \(\operatorname{GP}(10,2)\longrightarrow\operatorname{GP}(5,2)\) therefore exhibits a strict decrease from the Petersen strong odd chromatic number six, independently verified below, to five.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple. Set \(U=\{u_i:0\le i<10\}\) and \(V=\{v_i:0\le i<10\}\), with all subscripts reduced modulo ten. The edges of \(D\) are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), for each \(0\le i<10\). Computations index \(u_i\) by integer \(i\) and \(v_i\) by \(10+i\).

An **odd-independent set** \(S\subseteq V(D)\) is independent and has \(|N_D(x)\cap S|\) equal to zero or odd for every \(x\notin S\). A **strong odd colouring** is a proper vertex colouring in which every colour used in the open neighbourhood of any vertex appears an odd number of times there. Thus its nonempty colour classes are precisely a partition into odd-independent sets, where odd independence is tested in the original graph \(D\). Partitions are unlabelled in colours, but the twenty vertices are distinguished. The square \(D^2\) joins vertices of original graph distance at most two.

## Proof
**Odd-independent class enumeration.** Every vertex has degree three. Associate to a vertex subset \(S\) the twenty-bit mask \(m(S)=\sum_{x\in S}2^{\operatorname{index}(x)}\). Write \(B_x\) for the bit mask of the three neighbours of \(x\). The odd-independent condition is equivalent to the following finite, exact predicate:
\[
\text{for each }x:\quad
\bigl(x\in S\Rightarrow (m(S)\mathbin{\&}B_x)=0\bigr),
\qquad
\bigl(x\notin S\Rightarrow \operatorname{popcount}(m(S)\mathbin{\&}B_x)\ne2\bigr).
\]
There are exactly \(2^{20}\) masks, including the empty mask. Exhausting all masks by this predicate yields respectively \(1,20,100,120,90,0,10\) odd-independent sets at cardinalities \(0,1,2,3,4,5,6\), and none above six. This is exhaustive, not a sampling inference: the supplied standard-library verifier tests every twenty-bit mask, while an independent C++ verifier generates every independent set by include/exclude branching and then checks all neighbourhood parities.

**The lower bound.** In a four-class partition, if there were at most one six-vertex class, its total size would be at most \(6+3\cdot4=18\). Thus at least two six-classes would be required. Among the ten six-classes there are exactly 15 unordered disjoint pairs and **no three mutually disjoint**. For each of the 15 disjoint pairs, the eight remaining vertices contain **no** odd-independent four-set. Hence the two required residual classes cannot each have four vertices. The verified finite list therefore excludes four classes. Also, at most three classes would cover at most \(3\cdot6=18\) vertices. This proves \(\chi_{\mathrm{so}}(D)\ge5\).

**Attainment.** The following five index sets form an odd-independent partition of all vertices, each of size four:
\[
\begin{gathered}
\{0,2,5,11\},\quad\{1,8,14,15\},\quad\{3,6,10,19\},\\
\{4,12,16,17\},\quad\{7,9,13,18\}.
\end{gathered}
\]
Each block satisfies the stated exact neighbourhood predicate; their union is all twenty indices and they are disjoint. Therefore \(\chi_{\mathrm{so}}(D)=5\).

**Exhaustive optimum census.** Let \(\mathcal A\) be the complete family of nonempty odd-independent masks. For a set of still-uncovered indices \(W\), let \(F(W,k)\) be the polynomial counting partitions of \(W\) into exactly \(k\) blocks from \(\mathcal A\), with one formal variable \(z_j\) recording every block of size \(j\). If \(a\) is the least index in nonempty \(W\), use
\[
F(W,k)=\sum_{\substack{S\in\mathcal A\\ a\in S\subseteq W}}
 z_{|S|}F(W\setminus S,k-1),\qquad F(\varnothing,0)=1,
\]
with all other empty or impossible cases zero. Choosing the least uncovered index removes every permutation of the blocks and counts each unlabelled partition exactly once. Evaluating the recurrence at the full twenty-vertex set and \(k=5\) gives precisely
\[
F(V(D),5)=60z_2z_3^2z_6^2+100z_3^2z_4^2z_6+52z_4^5.
\]
In particular there are 212 optimal partitions, with exactly the three stated size profiles. The same method with colour classes required independent in \(D^2\) returns exactly two five-block partitions. The supplied verifiers compute all these values by separate mask generation and search orders; their code and the graph definition are included.

**Covering comparison.** Reducing every subscript modulo five gives a graph covering map \(\operatorname{GP}(10,2)\to\operatorname{GP}(5,2)\) because the neighbours of each vertex map bijectively onto its image's three neighbours. Pulling back any strong odd colouring through a covering preserves every local neighbour-colour multiplicity. Kwon and Park exhibit a six-colour strong odd colouring of the Petersen graph. For the exact lower bound, `verify_petersen.py` enumerates all ten-vertex subsets of \(\operatorname{GP}(5,2)\): the only nonempty odd-independent sets are ten singletons and ten triples; no three eligible triples are pairwise disjoint, so four colours cannot cover ten vertices, while fifteen pairs of disjoint triples yield six-colour partitions using four singletons each. Every colour class has odd cardinality, ruling out five colours by parity. Thus \(\chi_{\mathrm{so}}(\operatorname{GP}(5,2))=6\), and the present five-colour dodecahedral value demonstrates strictness of the covering inequality.

## Verification
With Python 3, run `python3 verify_exact_cover.py`. With a C++17 compiler, run `g++ -O2 -std=c++17 verify_independent.cpp -o verify_bin` followed by `./verify_bin`. Both independently construct the dodecahedral graph, evaluate every relevant local constraint, rule out four classes, verify all 212 optimum partitions and their three size profiles, and count exactly two square-colouring partitions. The supplemental `python3 verify_petersen.py` independently certifies the ten-vertex quotient has strong odd chromatic number six and exactly fifteen six-colour partitions. `CHECKS.txt` records the outputs from actual executions. Neither verifier relies on stochastic search, an optimisation-solver claim, precomputed tables, or input beyond the included source files.

## Relationship to prior work
Kwon and Park introduced strong odd colouring in arXiv:2401.11653, first posted 22 January 2024, and displayed a six-colour Petersen example; exactness of the Petersen value is independently checked in the included finite certificate. Caro, Petruševski, Škrekovski and Tuza (arXiv:2410.02336, first posted 3 October 2024) proved broad results on trees, planar graphs and graph products. These sources define the invariant and give broad upper bounds, but not the twenty-vertex dodecahedral class enumerator or the 212-partition spectrum here. Caro et al. note the well-known equality with square chromatic number for claw-free graphs; the dodecahedral graph is cubic and has an induced claw at every vertex, so that equality theorem does not directly apply. The later study by Caro et al. (arXiv:2509.20763) derives general inequalities relating odd independence and strong odd colouring but does not provide this dodecahedral census. A complete published historical-priority certification is not claimed.

## Limitations
The exact enumeration is finite and specific to the fixed twenty-vertex graph \(\operatorname{GP}(10,2)\); it makes no all-order claim for generalized Petersen graphs or for arbitrary cubic planar graphs. The proof of the enumerative counts relies on exhaustive reproducible integer checks rather than a short closed-form symmetry derivation. The two square-colouring partitions are counted but no complete automorphism-orbit classification is asserted. Independent external mathematical auditing has not been carried out.

## References
- H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first public version 2024-01-22), https://arxiv.org/abs/2401.11653 .
- Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (first public version 2024-10-03), https://arxiv.org/abs/2410.02336 .
- Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763, https://arxiv.org/abs/2509.20763 .
