# Antipodal traces and the twenty-vertex Möbius-ladder two-independence complex

## Finding

For every integer \(n\ge 3\), let \(M_{2n}\) be the graph with vertex set \(\mathbb Z/(2n)\) and edges between residues at cyclic difference one or at difference \(n\). Write \(X_n=\operatorname{Ind}_2(M_{2n})\) for the simplicial complex of subsets inducing components of at most two vertices, and let \(\tau(i)=i+n\) be the antipodal graph involution. Then the **reduced Lefschetz number** of its simplicial action is

\[
\widetilde L(\tau\mid X_n)
= -I(C_n;-1)
= -2\cos(n\pi/3),
\]

where \(I(C_n;t)\) is the independent-set polynomial of the ordinary \(n\)-cycle (including the empty set).

In the first twenty-vertex case \(n=10\), there is the complete **integral homotopy classification**

\[
X_{10}\simeq\bigvee^{23} S^7.
\]

The antipodal action on its sole nonzero reduced rational homology group has trace \(-1\). Therefore its degree-seven rational homology representation of the order-two group decomposes into an \(11\)-dimensional \(+1\) eigenspace and a \(12\)-dimensional \(-1\) eigenspace. The homotopy equivalence is not asserted to be equivariant.

## Assumptions and scope

All graphs are finite, undirected, simple graphs. An allowed vertex subset is exactly one whose induced graph has maximum vertex degree at most one: every connected component is an isolated vertex or an isolated edge. Equivalently, no three of its vertices span the edges of a path on three vertices, even if a further edge joins the endpoints. The term two-independence complex refers to this condition, not to the ordinary independence complex or a matching complex on graph edges.

The reduced Lefschetz number uses rational augmented simplicial chains, with the empty face as a single generator in homological degree \(-1\), and thus is the alternating trace on reduced homology. The integral homotopy claim is only for \(n=10\). The character formula applies to every \(n\ge3\), without assuming a homotopy classification at other lengths.

## Proof

**1. Explicit finite integral homotopy certificate.** Identify the vertices of \(M_{20}\) with \(0,\ldots,19\). Construct the simplicial faces by testing for every chosen vertex whether it has at most one chosen neighbor. Equivalently, form the sixty forbidden three-vertex masks consisting of a central vertex and two of its neighbors and reject every vertex mask containing one. The two constructions coincide on every one of the \(2^{20}-1=1{,}048{,}575\) nonempty masks. They produce \(53{,}670\) nonempty simplices, with face vector, in dimensions zero through nine,

\[
(20,190,1080,3975,9624,15050,14340,7505,1760,126).
\]

An explicit discrete Morse matching is determined by the following ordered sequence of pivot vertices:

`(19, 7, 3, 15, 17, 9, 11, 6, 10, 18, 12, 14, 16, 1, 2, 4, 0, 8, 5, 13)`.

At each pivot \(v\), traverse all currently unmatched nonempty faces in ascending order of cardinality, then ascending integer mask. Match each available face \(F\) not containing \(v\) with \(F\cup\{v\}\) whenever the latter is also available, and remove both from subsequent consideration. The definition is finite, deterministic and includes no empty-face matching.

It gives exactly \(26{,}823\) matched pairs and leaves exactly one critical zero-simplex and twenty-three critical seven-simplices. For acyclicity, orient every face-poset covering relation from the larger to the smaller face except for the matched relations, which are reversed. There are exactly \(335{,}460\) such covering relations. The reproducible topological-sort check visits all \(53{,}670\) nonempty faces; hence there is no directed cycle. Every matched pair is an actual covering relation and each simplex occurs in at most one pair. By the integral version of discrete Morse theory, the complex is homotopy equivalent to a CW complex with exactly one zero-cell and twenty-three seven-cells and no other cells. Each higher cell attaches to a point, so this CW complex is the displayed wedge of twenty-three seven-spheres. This is an integral homotopy conclusion; no mod-two-to-integral inference is used.

**2. Antipodal fixed-face classification for all lengths.** A face invariant under \(\tau\) is a union of \(k\) opposite vertex pairs \(\{i,i+n\}\). Every such pair is one graph edge. Two selected pairs corresponding to adjacent vertices of the quotient cycle \(C_n\) create an induced path on three vertices and are forbidden. Conversely, if no two chosen quotient vertices are adjacent, there are no edges between the chosen pairs, and the induced graph is a disjoint union of \(k\) isolated edges. Thus the \(\tau\)-invariant faces are in bijection with independent sets in \(C_n\).

On an invariant nonempty face containing \(k\) antipodal pairs, the induced permutation of its \(2k\) vertices is a product of \(k\) transpositions; the oriented simplex trace is \((-1)^k\). Its chain degree is \(2k-1\), so its contribution to the alternating trace is \((-1)^{k+1}\). Non-invariant simplices contribute zero to the trace. The empty face contributes \(-1\) in degree \(-1\). Consequently

\[
\widetilde L(\tau\mid X_n)
=-1+\sum_{\substack{S\subseteq V(C_n)\\ S\ne\varnothing\,,\ S\ \mathrm{independent}}}
(-1)^{|S|+1}
=-I(C_n;-1).
\]

For the path independence polynomial at \(-1\), set \(p_0=1\), \(p_1=0\) and \(p_m=p_{m-1}-p_{m-2}\). Deleting a chosen vertex of the cycle gives \(I(C_n;-1)=p_{n-1}-p_{n-3}\). The recurrence has period six, and directly yields \(I(C_n;-1)=2\cos(n\pi/3)\), including \(n=3\). This proves the formula for every allowed length.

**3. The degree-seven character.** For \(n=10\), the cycle polynomial evaluates to \(I(C_{10};-1)=-1\); hence the reduced Lefschetz number equals \(+1\). By the first part, reduced homology is concentrated in degree seven and is free of rank twenty-three. The Hopf trace formula therefore gives

\[
\operatorname{tr}(\tau_*\mid\widetilde H_7(X_{10};\mathbb Q))=-1.
\]

Because \(\tau_*^2=1\) over the characteristic-zero field \(\mathbb Q\), the \(\pm1\) eigenspaces are complementary. Their dimensions sum to twenty-three and have difference minus one, giving eleven and twelve, respectively. No assertion is made that the integral homology lattice splits as the direct sum of integral eigensublattices.

## Verification

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` from the directory containing the delivered files. It independently enumerates faces by the induced-degree condition and by all forbidden length-two paths; checks every matched pair and all \(335{,}460\) directed covering relations; calculates the critical-cell profile and reduced Euler characteristic; and directly evaluates the simplicial antipodal chain trace. The recorded reference output is `verification_output.txt`. All assertions must pass and the final output line must be `ALL_MOBIUS_DISSOCIATION_CHECKS_PASS`.

The finite verification applies to \(M_{20}\). The all-length Lefschetz identity is established by the separate symbolic argument above; finite checks at selected lengths are neither offered nor needed as its proof.

## Relationship to prior work

Taylan's 2015 preprint develops matching-tree methods for devoid complexes, including forbidden-path constructions on paths, cycles and forests; it does not classify the present Möbius-ladder two-independence complex or its antipodal homology action. Deshpande and Singh's higher-independence classifications concern multipartite graphs, fully whiskered graphs, paths, cycles and rooted trees. Agarwal and Basak classify *ordinary* independence and perfect-matching complexes for Möbius ladders, whose faces and ground sets differ from the present two-independence complex. Those results do not imply the stated integral wedge decomposition or fixed-pair Lefschetz formula.

Related calculations of Möbius-ladder matching-complex homology and ordinary independence-complex dihedral characters concern other complexes. An earlier calculation of the fourteen-vertex Möbius-ladder two-independence homotopy type concerns a different finite length and does not entail either this twenty-vertex classification or the all-length antipodal formula. Agreement of graph family alone is not coverage; no stronger checked theorem was found that specializes to the exact assertions made here.

## Limitations

The exact homotopy classification is restricted to \(M_{20}\), with no classification asserted for all Möbius-ladder lengths, no equivariant homotopy splitting, and no integral diagonalization of the involution. The infinite Lefschetz formula gives only an alternating virtual trace when several homology degrees occur, not the whole homology representation. Reproducible finite exhaustive calculations certify the finite claims under the explicit graph and complex definitions; scientific priority could be affected by equivalent work not recovered by the searches, and independent mathematical verification has not been performed.

## References

- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first submitted 27 January 2015; DOI:10.1007/s11083-015-9379-3.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first submitted 15 January 2020.
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1, first submitted 31 August 2026.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
