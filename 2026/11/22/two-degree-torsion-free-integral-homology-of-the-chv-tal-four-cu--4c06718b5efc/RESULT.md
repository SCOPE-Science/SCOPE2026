# Two-degree torsion-free integral homology of the Chvátal four-cut complex

## Finding
Let \(C\) be the standard twelve-vertex Chvátal graph with the twenty-four undirected edges specified explicitly in `verify.py`. Its **ordinary four-cut complex** \(\Delta_4(C)\) has complete reduced integral homology
\[
\widetilde H_j(\Delta_4(C);\mathbb Z)\cong
\begin{cases}
\mathbb Z^8,&j=6,7,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is pure of dimension seven but is not shellable, because its sixth reduced homology does not vanish. This contrasts with the previously established integral two-torsion of the *three-cut* complex of the same graph; the present result does not assert any natural map or persistence between different cut parameters.

## Assumptions and scope
The graph has vertex set \(\{0,\dots,11\}\), with the exact graph edges listed in `verify.py` and identifiable with the Chvátal graph of the standard NetworkX catalog. An ordinary \(k\)-cut complex has facets \(V(C)\setminus T\) over the \(k\)-vertex subsets \(T\) inducing disconnected graphs. The Alexander dual is taken on the full twelve-element ground set. All homology groups are reduced integral simplicial homology. No claim is made for arbitrary four-regular graphs or other cut parameters.

## Proof
**1. The complete dual.** Let \(D=\Delta_4(C)^\vee\), with \(\sigma\subseteq V(C)\) a face precisely when it does **not** contain a disconnected four-element subset. An exhaustive, deterministic enumeration of all \(\binom{12}{4}=495\) quadruples finds exactly \(282\) disconnected induced quadruples, so \(\Delta_4(C)\) has exactly \(282\) facets of dimension seven. Examining each of the \(2^{12}-1=4095\) nonempty subsets against this explicit forbidden-family predicate gives the complete dual face vector, by dimension zero through four,
\[
(f_0,f_1,f_2,f_3,f_4)=(12,66,220,213,48),
\]
with no higher-dimensional faces. Every face is included, not a sample.

**2. Certified elementary collapses.** Perform greedy free-face removals, processing lower faces by increasing (cardinality, bitmask) at each targeted dimension, first targeting dimension four and then dimension three. A proposed pair \((\sigma,\tau)\) is removed only after verifying that \(\sigma\) has exactly one surviving immediate coface, \(\tau\), and that \(\tau\) is maximal. The reproducible code replays these conditions at every step and yields exactly \(48\) elementary four-to-three collapses and \(77\) three-to-two collapses. No lower-dimensional pair is found. The remaining complex \(D'\) has face vector
\[
(12,66,143,88)
\]
in dimensions zero through three. Each move is a genuine elementary simplicial collapse, hence \(D\simeq D'\) and the integral homology is preserved.

**3. Signed integer boundaries and invariant factors.** Orient each simplex by ascending vertex labels. The code constructs the entire signed boundary matrices of \(D'\), checks consecutive compositions vanish, and computes their **exact Smith normal forms over \(\mathbb Z\)**, not merely ranks modulo primes. The boundary ranks in degrees one, two and three are respectively \(11,55,80\). Every nonzero Smith invariant factor of all three boundary matrices is exactly \(1\). Consequently the corresponding cokernels are torsion-free. With \(143\) two-faces and \(88\) three-faces, reduced homology has ranks
\[
\widetilde\beta_2(D')=143-55-80=8,\qquad
\widetilde\beta_3(D')=88-80=8,
\]
and is zero in all other degrees. In particular, the Smith invariants of the degree-three boundary exclude torsion in \(\widetilde H_2\); free chain groups exclude torsion in top homology. The degree-one boundary has rank \(11\), verifying connectedness and vanishing reduced degree-zero homology.

**4. Integral Alexander duality.** For a complex on \(12\) vertices, combinatorial Alexander duality yields
\[
\widetilde H_j(\Delta_4(C);\mathbb Z)
\cong \widetilde H^{9-j}(D;\mathbb Z).
\]
The universal coefficient theorem, applied to the established *torsion-free* homology of \(D\), gives free cohomology of rank eight in degrees two and three only. Hence the four-cut complex has exactly \(\mathbb Z^8\) in degrees seven and six respectively and no other reduced integral homology.

**5. Shellability obstruction.** Every facet of \(\Delta_4(C)\) is the complement of one disconnected quadruple, hence has eight vertices. The complex is pure seven-dimensional. A pure shellable seven-complex has the homotopy type of a wedge of seven-spheres (or is contractible); nonzero sixth integral homology therefore precludes shellability.

## Verification
Run `python3 verify.py` with Python 3.10 or newer and SymPy (tested with the installed version). The checker uses a hard-coded twenty-four-edge list, enumerates every quad and all \(4095\) nonempty vertex subsets, replays each free-face removal, checks downward face closure of the remainder, forms the *actual* signed integer boundary matrices, verifies both zero boundary compositions, and demands the full Smith invariant factors rather than just finite-field ranks. It independently computes ranks of the original uncollapsed dual over \(\mathbb F_2\) and \(\mathbb F_3\), both giving \((11,55,157,48)\) in boundary degrees one through four. The extracted `verify_output.txt` is the recorded successful execution. The exhaustive finite calculation is a complete proof of this **fixed finite graph** claim, not extrapolation to an infinite family.

## Relationship to prior work
Bayer and collaborators' foundational 2023 cut-complex paper introduces the invariant and general theorems for trees, cycles, complete multipartite graphs, squared cycles and prism graphs. Its full text does not classify the Chvátal four-cut complex. Its 2024 sequel studies disjoint unions, squared paths and grids, not this graph. A published computation gives \(\Delta_3(C)\simeq M(\mathbb Z/2,7)\); it has a different cut parameter, so does not imply this result. The known all-graph four-cut sphere-wedge theorem for girth at least five does not apply because \(C\) has seventeen four-cycles, including overlapping squares. Other published four-cut calculations for the Shrikhande, rook, Paley and Clebsch graphs have different underlying graphs and, in some cases, distinguish ordinary from total cut complexes. The claim is specifically this previously unreported exact four-cut integral invariant; no claim is made of a general homotopy wedge decomposition or publication priority beyond the inspected literature.

## Limitations
This is one exact finite computation with a complete reproducible integer certificate, not an infinite graph-family theorem. Smith invariant factors and ranks determine integral homology, **not** the homotopy type or an explicit homology representation. The observed contrast between cut parameters three and four does not constitute a persistence map or a monotonicity theorem. Independently published but unindexed equivalent calculations may exist; independent validation has not yet occurred.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public 2024-07-11), https://arxiv.org/abs/2407.08158.
3. *The Chvátal three-cut complex is an integral Moore space*, previously published computational theorem, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-chv-tal-three-cut-complex-is-an-integral-moore-space--bc7d229f8c3e.
4. *Homotopy classification of four-cut complexes at the pentagonal girth boundary*, previously published theorem, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-homotopy-classification-of-four-cut-complexes-at-the-pentagonal--94b36fd5471f.
5. NetworkX, `chvatal_graph` graph generator specification, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.chvatal_graph.html.
