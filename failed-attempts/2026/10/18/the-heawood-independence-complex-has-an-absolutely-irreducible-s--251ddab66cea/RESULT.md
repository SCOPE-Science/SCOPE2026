# The Heawood independence complex has an absolutely irreducible six-dimensional full-symmetry homology representation

## Finding

Let \(H\) be the bipartite point-line incidence graph of the seven-point Fano plane. Put \(K=\operatorname{Ind}(H)\), the simplicial complex of all independent vertex sets. The natural action of the entire \(336\)-element graph-automorphism group \(\Gamma=\operatorname{Aut}(H)\) on \(V=\widetilde H_3(K;\mathbb Q)\) is absolutely irreducible, and \(\dim_{\mathbb Q}V=6\). All other reduced rational homology vanishes.

Write \(G=\operatorname{GL}(3,\mathbb F_2)\) for the \(168\)-element subgroup preserving point and line vertices separately. The complete character of \(V\) is

\[
\chi(g)=\begin{cases}6&g\in G,\ \operatorname{ord}(g)=1,\\-2&g\in G,\ \operatorname{ord}(g)=2,\\0&g\in G,\ \operatorname{ord}(g)=3,\\2&g\in G,\ \operatorname{ord}(g)=4,\\-1&g\in G,\ \operatorname{ord}(g)=7,\\0&g\notin G.\end{cases}
\]

In particular, the restriction of \(V\otimes\mathbb C\) to \(G\) splits as the two complex-conjugate three-dimensional irreducibles, whereas its extension to the full symmetry group is irreducible.

## Assumptions and scope

Identify the seven points with nonzero triples \(p\in\mathbb F_2^3\) and the seven lines with nonzero triples \(\ell\in\mathbb F_2^3\); incidence means \(p\cdot\ell=0\) in \(\mathbb F_2\). The Heawood graph has 14 vertices and 21 incidence edges. An independent set contains no incident point-line pair. The group \(G\) acts by \(p\mapsto Ap\) and \(\ell\mapsto A^{-T}\ell\), for \(A\in\operatorname{GL}(3,\mathbb F_2)\). The involution \(\tau\) interchanges a point \(p\) and the line indexed by the same \(p\). These maps preserve incidence; as the connected graph has a unique bipartition and every incidence-preserving permutation of points is induced by an invertible linear transformation, they yield its full group of order \(2\cdot168=336\).

The claim is about rational homology as an actual representation, not the integral representation lattice or equivariant homotopy type.

## Proof

**Concentration of homology.** List the 14 vertices as points \(1,\dots,7\) followed by lines \(1,\dots,7\). The complete family of independent sets, including the empty face, has degree-by-degree counts

\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(1,14,70,154,147,56,14,2).
\]

The standalone verifier includes both a \(2^{14}\)-mask enumeration and an independent recursive enumeration and confirms equality of their face lists. Apply the stated successive-vertex toggle matching in the fixed order \((8,10,5,9,3,11,13,2,6,0,1,7,12,4)\), indexed from zero. Each pass pairs an as-yet unpaired face not containing the pivot with its union with the pivot, when both exist. The resulting matching has \(226\) pairs and precisely six unmatched faces, all of dimension three. The verifier enumerates all \(1582\) Hasse incidences, reverses every matched incidence, and topologically sorts the full oriented graph; every face is visited, proving acyclicity rather than relying on a heuristic. The augmented empty face is matched with a vertex. Deleting that pair yields an ordinary acyclic matching with one critical vertex and six critical three-faces. Forman's discrete Morse theorem therefore gives \(K\simeq\bigvee^6S^3\). In particular \(V\cong\mathbb Q^6\) is the only nonzero reduced rational homology group.

**Signed equivariant Lefschetz calculation.** For any graph automorphism \(g\), list each \(g\)-invariant independent face \(F\), including the empty face, and let \(\epsilon(g,F)\in\{1,-1\}\) be the sign of the induced permutation of its ordered vertices. Because the only reduced homology is in degree three, the simplicial Hopf trace formula yields

\[
\chi(g)=-\sum_{F:gF=F}(-1)^{\dim F}\epsilon(g,F).
\]

The verifier explicitly constructs every one of the \(168\) invertible three-by-three binary matrices and its fourteen-vertex incidence permutation. The respective element-order populations in \(G\) are \(1,21,56,42,48\) for orders \(1,2,3,4,7\). The signed face formula gives constant character values \(6,-2,0,2,-1\) on those respective order classes. Separately, it computes the independence polynomial at \(-1\) of the permutation-orbit compatibility graph, giving the same values without orientation bookkeeping. For each of the other \(168\) automorphisms \(g\tau\), both independent calculations give exactly zero. They have orders \(2,6,8\) with multiplicities \(28,56,84\).

**Irreducibility.** The squared character norm over all \(336\) elements equals

\[
\frac{1}{336}\bigl(1\cdot6^2+21\cdot(-2)^2+56\cdot0^2+42\cdot2^2+48\cdot(-1)^2+168\cdot0^2\bigr)=1.
\]

By irreducible-character orthogonality, the complexified homology representation is irreducible. As the representation itself is defined over \(\mathbb Q\), this establishes absolute irreducibility. Comparing the restricted character with the standard \(\operatorname{PSL}(2,7)\cong G\) table identifies the two conjugate three-dimensional summands on \(G\): their sum has the displayed inner-group character.

## Verification

Execute `python3 verify.py` with Python 3.9+ and no third-party modules. The program checks 458 faces by two constructions, the precise face-count vector, all 226 pairs and 1582 Hasse incidences, the complete acyclicity topological sort, all 336 group actions, edge preservation for color-swapping actions, and agreement of two independent finite character enumerations for all 336 automorphisms. It prints `VERIFY_OK` only if every assertion passes. It also validates the exact rational character norm calculation. The finite automorphism group and complete finite simplicial complex are both exhausted; the calculation is an exact finite proof certificate rather than a sample or an asymptotic extrapolation.

## Relationship to prior work

A public October 4, 2026 determination of \(\operatorname{Ind}(H)\simeq\bigvee^6S^3\) gives the nonequivariant input and matches the independent Morse certificate above; that homotopy type alone does not determine the action of any nonidentity graph symmetry on homology. Tsukuda's 2017 *Independence complexes and incidence graphs* establishes general homotopy relationships for incidence graphs, but its duality statement does not specify the full \(336\)-element rational homology character or imply the displayed irreducibility decomposition without a separate action-sensitive calculation. The ordinary matching complex of the Heawood graph concerns a different simplicial complex and does not imply this statement.

The complete character was compared with records for Heawood incidence, Fano-plane complexes, equivariant independence homology, and the six-dimensional representations of \(\operatorname{PSL}(2,7)\). No equivalent full-graph-automorphism character calculation was identified in accessible material; this is a qualified novelty assessment, not proof of global uniqueness.

## Limitations

The original October 2026 public record was accessible as its indexed title and summary, not as its full supplemental text. An unindexed equivariant refinement there or in another unavailable source remains a genuine overlap risk. The standard finite-group character table is used only to name the two constituents of the restriction; absolute irreducibility follows directly from the enumerated norm. The finding does not classify integral representations, point-set equivariant homotopy types, or complexes for other projective planes. The proof certificate establishes an exhaustive result for this exact finite object, not a general-order formula.

## References

1. Public mathematical record, *The Heawood independence complex is \(\bigvee^6 S^3\)* (2026-10-04), identifier `dbd95019d1e2`, published source `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2`.
2. Shuichi Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), doi:10.55016/ojs/cdm.v12i1.62277.
3. Character table of \(\operatorname{PSL}(2,7)\), `https://en.wikipedia.org/wiki/PSL%282%2C7%29` (used to identify the restricted constituent pair).
4. Robin Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145 (acyclic-matching theorem).
