# The sharp three-cut shellability threshold for fourth powers of cycles

## Finding
Let \(C_n^4\) be the graph on the cyclic vertex set \(\mathbb Z/n\mathbb Z\), where distinct vertices at cyclic distance at most four are adjacent, and let \(\Delta_n=\Delta_3(C_n^4)\) be its **ordinary** three-cut complex. For every integer \(n\ge 11\),
\[
\boxed{\Delta_n\text{ is shellable if and only if }n\ge17.}
\]
Moreover, for all integers \(n\ge17\),
\[
\boxed{|\Delta_n|\simeq \bigvee^{\binom{n-8}{2}-35}S^{n-4}.}
\]
The four previously unproved shellable values have explicit complete facet orders:

| \(n\) | Number of facets | Spanning facets | Integral homotopy type |
|---|---:|---:|---|
| 17 | 408 | 1 | \(S^{13}\) |
| 18 | 528 | 10 | \(\bigvee^{10}S^{14}\) |
| 19 | 665 | 20 | \(\bigvee^{20}S^{15}\) |
| 20 | 820 | 31 | \(\bigvee^{31}S^{16}\) |

For \(n\le10\), the complex has no facets and is void; the shellability equivalence is intentionally stated only for the nonvoid range.

## Assumptions and scope
The underlying graphs are finite, simple, unweighted cycle powers. The *ordinary* three-cut complex has as facets all subsets \(V\setminus T\), where \(T\subseteq V\) has three vertices and the induced graph \(C_n^4[T]\) is disconnected. This is not the total cut complex, whose complementary triples would have to be independent.

Each facet has \(n-3\) vertices, hence when nonvoid the complex is pure of dimension \(n-4\). Three vertices induce a disconnected graph precisely when their three possible edges number at most one.

## Proof
**1. The four missing positive cases.** For each \(n\in\{17,18,19,20\}\), the attached `p4_nNN_order.txt` is a complete ordered list of the disconnected triples \(T_1,\ldots,T_m\). The corresponding ordered facets are \(F_i=V\setminus T_i\). Each triple is a strictly increasing three-element list of labels between zero and \(n-1\). Completeness and uniqueness are checked against an independent connected-component enumeration.

For each \(i>1\), let
\[
R_i=\{v\in V\setminus T_i:\text{some }j<i\text{ has }T_j\setminus T_i=\{v\}\}.
\]
For any earlier facet \(F_j\), a previously present codimension-one face of \(F_i\) contains its intersection \(F_i\cap F_j\) **if and only if** some \(v\in (T_j\setminus T_i)\cap R_i\) exists. To see this, an old ridge of \(F_i\) has the form \(F_i\setminus\{v\}=F_i\cap F_h\) for an earlier facet \(F_h\) whose complementary triple differs from \(T_i\) only by adding \(v\). Inclusion \(F_i\cap F_j\subseteq F_i\setminus\{v\}\) is exactly the condition \(v\in T_j\setminus T_i\). Thus the condition
\[
R_i\ne\varnothing,\qquad (T_j\setminus T_i)\cap R_i\ne\varnothing\quad\text{for all }j<i
\]
is **equivalent** to every noninitial facet having a pure codimension-one intersection with the preceding union: the standard pure shelling criterion.

The executable `verify.py` directly checks this criterion for **every** preceding pair of facets in the four complete supplied orders, without trusting their construction. All four pass; hence the complexes at these four values are shellable.

**2. The infinite positive range.** Chauhan and Shukla, arXiv:2603.23155v1, Theorem 1.4, already prove shellability and the stated sphere-wedge count for every \(p\ge2\) and \(n\ge6p-3\). Taking \(p=4\) covers \(n\ge21\). The four newly supplied certificates cover exactly \(17\le n\le20\), with no gap. In a pure shelling, a facet contributes a top-dimensional sphere exactly when all its ridges are already present. The verifier counts such spanning facets by checking \(|R_i|=n-3\); the counts are \(1,10,20,31\), agreeing with \(\binom{n-8}{2}-35\). A pure shellable complex has the homotopy type of a wedge of top-dimensional spheres, giving the complete formula.

**3. The sharp lower obstruction.** For \(11\le n\le16\), set \(K_n=\Delta_n^{\vee}\) (simplicial Alexander dual on the full \(n\)-vertex set). Its faces are **exactly** the vertex subsets containing no disconnected triple: otherwise the complement belongs to a facet of \(\Delta_n\). The verifier enumerates every subset of the full vertex set, retains exactly these faces, builds all augmented simplicial boundary matrices over \(\mathbb F_2\), and computes their exact ranks by elimination. Its nonzero reduced homology is:

| \(n\) | Nonzero \(\widetilde H_q(K_n;\mathbb F_2)\) | Implied nonzero \(\widetilde H_{n-q-3}(\Delta_n;\mathbb F_2)\) | Top dimension of \(\Delta_n\) |
|---|---|---|---:|
| 11 | \(\widetilde H_5\cong\mathbb F_2\) | \(\widetilde H_3\) | 7 |
| 12 | \(\widetilde H_3\cong\mathbb F_2^6\) | \(\widetilde H_6\) | 8 |
| 13 | \(\widetilde H_3\cong\mathbb F_2^{40}\) | \(\widetilde H_7\) | 9 |
| 14 | \(\widetilde H_3\cong\mathbb F_2^{15}\) | \(\widetilde H_8\) | 10 |
| 15 | \(\widetilde H_3\cong\mathbb F_2\) | \(\widetilde H_9\) | 11 |
| 16 | \(\widetilde H_2\cong\mathbb F_2^3\) | \(\widetilde H_{11}\) | 12 |

The implications follow from combinatorial Alexander duality, \(\widetilde H_i(\Delta_n;\mathbb F_2)\cong\widetilde H^{n-i-3}(K_n;\mathbb F_2)\). In every case the nonzero degree is strictly **below** \(n-4\), contradicting the vanishing of lower reduced homology of a nonempty pure shellable complex. Thus none is shellable. The lower-range homology values are independently reproducible here, but were already present in the motivating literature and are **not** claimed as new results.

For \(n\le10\), each vertex of \(C_n^4\) has at most one nonneighbor; no three vertices can induce a disconnected graph, so the three-cut complex is void.

## Verification
Run `python3 verify.py` in this directory; it reads exactly the four included order files. `verify_output.txt` records the expected output from an actual successful run. The checker independently constructs the graph and its disconnected triples by depth-first search, validates every facet and every shelling intersection, and counts spanning facets. For the six lower values it exhausts the Alexander dual and performs complete binary Gaussian elimination on all boundaries, including the augmentation to the empty face. Independent Euler-characteristic identities are also checked. All checks are exact integer and binary operations; there are no random seeds or heuristics in the verifier.

The infinite range is not certified by finite enumeration: it is obtained from the cited published theorem. The new contributions requiring certificates are the four finite shellings; they are supplied in full.

## Relationship to prior work
Chauhan, Shukla and Vinayak, arXiv:2406.01979v2, Conjecture 4.2, propose the threshold \(n=4p+1\), along with a sphere-count formula. Their Table 2 already lists homology for numerous fourth-power cycle complexes (including the small values here), but a Betti table cannot establish shellability. Their theorem concerns the squared cycles, \(p=2\).

Chauhan and Shukla, arXiv:2603.23155v1, Theorem 1.4, prove the desired shellability for \(n\ge6p-3\), which is only \(n\ge21\) when \(p=4\). Their conclusion explicitly states that the sharper threshold remains conjectural. This finding proves **the complete fourth-power case** by furnishing and checking shellings precisely at \(n=17,18,19,20\), not by reasserting the published Betti numbers. An independently published classification covering these missing shellings was not identified in the material checked.

## Limitations
The result settles the shellability threshold for the fixed graph power \(p=4\) and ordinary three-cut complexes. It makes no claim for every graph power \(p\), for higher cut parameters, or for total cut complexes. The non-shellability obstruction is computed over \(\mathbb F_2\), which is sufficient for shellability but is not an integral homotopy classification below the threshold. The finite proofs are algorithmically checkable rather than short human-written shelling formulas. The result has not undergone independent external mathematical audit.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first publicly posted 2026-03-24, especially Theorem 1.4 and Section 4. https://arxiv.org/abs/2603.23155
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-cut complexes of squared cycle graphs*, arXiv:2406.01979v2 (original arXiv submission 2024-06-04), especially Table 2 and Conjecture 4.2. https://arxiv.org/abs/2406.01979
3. M. Bayer et al., *Topology of cut complexes of graphs*, SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675; background definitions and conjectures.
