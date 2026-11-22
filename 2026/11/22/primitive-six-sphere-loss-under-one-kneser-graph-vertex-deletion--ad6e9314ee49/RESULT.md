# Primitive six-sphere loss under one Kneser-graph vertex deletion

## Finding
Let \(G=\mathrm{KG}(6,2)\) have as vertices the fifteen two-element subsets of \(\{1,2,3,4,5,6\}\), with two vertices adjacent exactly when disjoint. For any graph vertex \(v\), let \(G-v\) be the graph with that vertex deleted, and let \(\mathcal N(H)\) be the **open Lovász neighborhood complex** of \(H\): a nonempty collection of graph vertices is a face precisely when those vertices have a common adjacent graph vertex. Then, integrally,
\[
\mathcal N(G-v)\simeq\bigvee^{13}S^2,
\qquad \mathcal N(G)\simeq\bigvee^{19}S^2.
\]
Moreover the natural simplicial inclusion \(i:\mathcal N(G-v)\hookrightarrow\mathcal N(G)\) induces a split injection
\[
0\longrightarrow\mathbb Z^{13}\xrightarrow{i_*}\mathbb Z^{19}
\longrightarrow\mathbb Z^6\longrightarrow0
\]
in degree-two integral homology. Thus six primitive sphere classes are lost when one Kneser vertex is removed, and there is no torsion in any of these homology groups.

## Assumptions and scope
The result concerns this specific fifteen-vertex Kneser graph and deletion of **one graph vertex**, not deletion of a simplex vertex from the already-formed neighborhood complex and not removal of one graph edge. The same answer holds for any deleted graph vertex because permutations of the six ground-set labels act transitively on two-element subsets. It uses ordinary integral homotopy and singular/simplicial homology, without a group-equivariant splitting assertion. The **first public source** defining the relevant Kneser neighborhood-complex family and proving the intact-complex classification is Nilakantan and Singh (2018-02-16).

To specify a finite certificate, label the ground set \(\{0,1,2,3,4,5\}\), order its fifteen duads lexicographically, and delete the duad \(\{0,1\}\). Use the original fifteen labels for both complexes, so a simplex is always a sorted tuple of original labels. The empty simplex is included for combinatorial bookkeeping but is not a chain generator in ordinary homology.

## Proof
**1. Exact finite face description.** Every facet of the full neighborhood complex is contained in the open neighborhood of a duad, namely the six duads disjoint from that center. For the punctured graph the potential centers and face vertices both exclude \(\{0,1\}\). Taking all subsets of all these neighborhood simplices is an exhaustive construction, not a partial search. The face vectors in dimensions zero through five are respectively
\[
(15,105,260,225,90,15)\quad\text{and}\quad(14,88,192,150,54,8).
\]
The second complex is a simplicial subcomplex of the first.

**2. Exact simplicial collapses.** The embedded `verify.py` constructs both complete face sets, and, in the deterministic lexicographic order specified there, removes elementary free-face/coface pairs. Every removal is checked against all active cofaces, so it preserves simple homotopy type. The full complex undergoes 290 valid elementary collapses to a two-dimensional simplicial complex with \(15\) vertices, \(55\) edges and \(60\) triangles; the punctured complex undergoes 202 such collapses to one with \(14\) vertices, \(44\) edges and \(44\) triangles. All ordered pairs are stored in `certificate.json` and are regenerated and compared on replay.

**3. Fundamental groups.** For each resulting connected two-complex, take the lexicographically breadth-first spanning tree of its one-skeleton. Contracting that tree gives a free fundamental-group presentation with one generator per non-tree edge and one triangular boundary relator per remaining triangle. The full complex has 41 generators and 60 relators; the punctured one has 31 generators and 44 relators. The exact Tietze elimination in `verify.py` finds, at every stage, a relator containing one generator exactly once, solves it for that generator, substitutes into every other relator and freely/cyclically reduces. It removes every generator (41 or 31) and leaves only trivial relators (19 or 13). These are group-presentation equivalences, not an inference from abelian homology, so **both spaces are simply connected**.

**4. Absolute homotopy.** The collapsed complexes have no cells above dimension two. Their Euler characteristics are respectively \(15-55+60=20\) and \(14-44+44=14\). Connectedness and simple connectivity imply \(H_1=0\), while \(H_2\) is a subgroup of a free integral two-chain group and is therefore free. Euler characteristic gives \(H_2\cong\mathbb Z^{19}\) and \(\mathbb Z^{13}\), respectively. By Hurewicz, choose representatives of integral second-homology bases as maps of two-spheres. Their wedges induce homology equivalences from \(\bigvee^{19}S^2\) and \(\bigvee^{13}S^2\); the simply connected homology Whitehead theorem makes them homotopy equivalences.

**5. Primitive inclusion map.** Consider the relative integral simplicial chain complex \(C_*(\mathcal N(G),\mathcal N(G-v);\mathbb Z)\). Its chain-group ranks in degrees zero through five are
\[
(1,17,68,75,36,7).
\]
The embedded exact integer reduction repeatedly selects a boundary entry \(+1\) or \(-1\), changes integral bases by unimodular operations, and cancels the corresponding adjacent-dimensional chain generators. It checks \(\partial^2=0\) after every cancellation. Precisely 99 unit pivots remain available, with numbers by pivot degree \((1,16,46,29,7)\) for degrees one through five. The final relative chain complex has six degree-two generators, no others, and zero differential. Thus
\[
H_j(\mathcal N(G),\mathcal N(G-v);\mathbb Z)=
\begin{cases}\mathbb Z^6,&j=2,\\0,&j\ne2.\end{cases}
\]
In the long exact sequence of this pair, relative \(H_3=0\) proves injectivity on \(H_2\), and absolute \(H_1(\mathcal N(G-v))=0\) proves surjectivity onto relative \(H_2\). Its free quotient \(\mathbb Z^6\) makes the injection primitive and split as a map of free abelian groups. This completes the claim.

## Verification
Run `python3 verify.py certificate.json` from a directory containing the two embedded files. Python's standard library suffices. The script reconstructs every face from the graph, validates all 492 elementary collapse pairs, proves the two fundamental groups trivial by 72 exact generator eliminations, and verifies the 99 primitive integral relative-chain cancellations and each chain identity. It compares the regenerated ordered certificates byte-semantically with `certificate.json` and asserts the displayed face vectors and final chain ranks. The relative reduction is genuinely integral: checking mod-two Betti numbers alone would not establish this result.

## Relationship to prior work
Nilakantan and Singh proved the **intact** family theorem \(\mathcal N(\mathrm{KG}(k+4,2))\simeq\bigvee^{k^2+5k+5}S^k\), whose \(k=2\) case gives the already-known nineteen two-spheres. That intact classification is credited rather than reclaimed. The published rational \(\mathfrak S_6\)-representation calculation for \(\mathcal N(\mathrm{KG}(6,2))\) refines its unpunctured rank and character but does not determine the graph-vertex-deleted complex or its integral inclusion map. Other published neighborhood-complex vertex-deletion theorems concern hypercubes and Hamming graphs, not the Kneser disjointness graph. The new content is the thirteen-sphere punctured type **and primitive integral six-class loss**, a direct robustness calculation for the smallest two-dimensional nontrivial case of this Kneser neighborhood family.

## Limitations
The result is restricted to \(\mathrm{KG}(6,2)\) and single-vertex deletion. It asserts neither a uniform formula for all Kneser parameters nor an equivariant decomposition, nor a classification of multiple deletions. The group and integral-chain certificates establish the stated finite homotopy and inclusion properties; they are not independent external certification. Bibliographic search cannot exclude all unindexed equivalents.

## References
1. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(\mathrm{KG}_{2,k}\)*, arXiv:1802.05848v1, first public 2018-02-16, Theorem 1.3 and Section 5. https://arxiv.org/abs/1802.05848
2. *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rational-symmetry-decomposition-of-the-kneser-neighborhood-compl--6890383e239b
3. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory, Series A 25 (1978), 319–324. https://doi.org/10.1016/0097-3165(78)90022-5
4. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, 2012. https://arxiv.org/abs/1210.2803
