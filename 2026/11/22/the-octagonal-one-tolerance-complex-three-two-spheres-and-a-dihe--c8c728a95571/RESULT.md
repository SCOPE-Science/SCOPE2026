# The octagonal one-tolerance complex: three two-spheres and a dihedral reflection split

## Finding

Let \(G=C_8^2\) be the square of the cycle on \(V=\mathbb Z/8\), with edges joining vertices of cyclic distance one or two. Let \(K=\operatorname{Cl}(G)\) be the filled clique complex; in particular its consecutive three-vertex cliques are filled two-simplices. Define the one-tolerance complex by
\[
X=\mathcal T_1(K)=\{\sigma\subseteq V:\sigma\setminus\{v\}\in K\text{ for some }v\in\sigma\}\cup\{\varnothing\}.
\]
Then
\[
|X|\simeq S^2\vee S^2\vee S^2.
\]
This is an integral homotopy classification, not just a rational homology computation.

Let \(D_8=\langle r,s:r^8=s^2=1,\ srs=r^{-1}\rangle\) act by \(r(i)=i+1\) and \(s(i)=-i\) modulo eight. Define \(\varepsilon_{-,-}\) by \(\varepsilon_{-,-}(r)=\varepsilon_{-,-}(s)=-1\), and let \(\rho_2\) be the two-dimensional dihedral representation where \(r\) rotates the plane through a quarter turn and \(s\) reflects it. The complete rational homology action is
\[
\widetilde H_2(X;\mathbb Q)\cong\varepsilon_{-,-}\oplus\rho_2.
\]
Every other reduced rational homology group is zero. The characters at \(r^a\), \(a=0,\ldots,7\), and at the reflections \(i\mapsto a-i\) are respectively
\[
(3,-1,-1,-1,3,-1,-1,-1),\qquad (-1,1,-1,1,-1,1,-1,1).
\]
In particular, the geometric quotients by all rotations and by the full dihedral group are rationally acyclic in positive degrees. Quotienting by the two nonconjugate individual reflection types produces second rational Betti numbers one and two, respectively.

## Assumptions and scope

The graph is the simple unweighted eight-cycle with graph distance-one and graph distance-two edges; the input complex is the *filled* clique complex, not the unfilled edge complex and not the robust-clique complex. The tolerance is exactly one. All homotopy and integral statements concern the ordinary geometric realization. All representation statements are over the rational field. The natural dihedral group has sixteen elements; no larger symmetry group is required for the theorem.

The order eight is a natural boundary: \(\alpha(C_n^2)=\lfloor n/3\rfloor\) for \(n\ge6\), so eight is the last cycle length with no independent triple and hence the last length for which the entire two-skeleton of the vertex simplex lies in this tolerance complex. No formula at other lengths is asserted.

## Proof

**Face classification.** Each of the eight triples of consecutive vertices is a clique of \(G\), and there is no clique with four vertices. Because an independent triple in a squared cycle needs three cyclic gaps of size at least three, no such triple exists on eight vertices. Thus every three-element subset of \(V\) contains an edge of \(G\), so every such subset is in \(X\). All singletons and pairs are also in \(X\). A four-element subset lies in \(X\) precisely when it contains a three-element graph clique. There are exactly 32 distinct such four-subsets, as certified by full finite enumeration in `check.py`. Five-element subsets cannot belong to \(X\), because they would have to contain a four-clique in \(G\). Hence the face counts in dimensions zero through three are \((8,28,56,32)\).

**Integral homotopy.** The complete two-skeleton of the simplex on eight vertices lies in \(X\). Every edge loop is nullhomotopic by its triangular two-faces, so \(X\) is simply connected. The attached file `collapse_certificate.json` gives 40 ordered pairs of faces \((\sigma,\tau)\), with \(\sigma\) a codimension-one face of \(\tau\). The standalone verifier constructs \(X\) directly from the one-tolerance definition, then checks for each successive pair that \(\tau\) is the *only strict coface* of \(\sigma\) among currently surviving simplices. Thus every pair is a genuine elementary simplicial collapse. There are 32 triangle--tetrahedron collapses and eight edge--triangle collapses, ending with a two-dimensional simplicial complex \(Y\) having face counts \((8,20,16)\). These collapses preserve homotopy type and simple connectivity. Since \(Y\) is connected and simply connected, its integral first homology is zero; since it has no cells above dimension two, its second homology is free. Its Euler characteristic is \(8-20+16=4\), so \(H_2(Y;\mathbb Z)\cong\mathbb Z^3\). A map from three two-spheres representing an integral homology basis is a homology isomorphism between simply connected CW complexes; Whitehead's theorem makes it a homotopy equivalence. This proves the claimed wedge decomposition.

**Symmetry character.** The sixteen affine permutations \(i\mapsto a+i\) and \(i\mapsto a-i\) preserve the graph and hence \(X\). In each simplex dimension the chain trace is the sum of the signs of the vertex permutations on setwise-fixed simplices, not merely the number of such simplices. By the simplicial Lefschetz formula, the alternating sum of these chain traces equals \(1+\operatorname{tr}(g\mid H_2(X;\mathbb Q))\), since only homology degrees zero and two occur. The exact signed simplex traces for identity, half-turn, even-axis reflection and odd-axis reflection, by simplex cardinality one through four, are respectively \((8,28,56,32)\), \((0,-4,0,0)\), \((2,-2,-6,-2)\) and \((0,-4,0,2)\); all other nonidentity rotations have zero signed traces. The displayed two character lists follow. The sum of the sign character \(\varepsilon_{-,-}\) and the planar character of \(\rho_2\) equals those lists, and the dihedral irreducible characters give a unique rational decomposition.

For a finite simplicial group action, barycentric subdivision removes simplex inversions. Averaging cellular chains over \(\mathbb Q\) identifies the rational homology of the geometric quotient by a subgroup with the invariant rational homology of \(X\). Rotation invariants have rank \((3+3-6)/8=0\). Full-group invariants are consequently zero. For an involution with second-homology trace \(\tau\), its invariant rank is \((3+\tau)/2\), yielding respectively one for even-axis reflections and two for odd-axis reflections.

## Verification

Run `python3 check.py` with `collapse_certificate.json` beside it. The verifier is standard-library-only, independently enumerates all nonempty faces using the original tolerance definition, verifies all 40 sequential unique-coface conditions and the 8/20/16 residual f-vector, checks the residual second-boundary rank 13 over both \(\mathbb F_2\) and \(\mathbb F_{101}\), evaluates the signed fixed-face traces for all sixteen dihedral elements, and checks the stated two character lists and invariant dimensions. An additional integer Smith-normal-form check on the residual boundary matrix yielded thirteen unit invariant factors, consistent with the integral homotopy proof; the homotopy proof itself rests on actual elementary collapses and simple connectivity rather than a finite-field rank extrapolation. All source and certificate paths in this statement refer to files included alongside it.

## Relationship to prior work

Barik--Mondal--Mukherjee, first public 14 April 2026, construct discrete-Morse matchings for independence complexes of graphs with simplicial vertices and determine several homotopy types. Their first listed 2020 MSC code is 57Q70. This motivates explicit collapse certificates, but their theorem does not cover this one-tolerance complex, which has complete one-skeleton without being a simplex and therefore cannot be a graph independence complex on this vertex set. Selvaraja, first public 10 November 2026, studies tolerance complexes and proves Leray and collapsibility bounds, especially for chordal-graph clique complexes. Here \(G\) is not chordal: the four vertices \(\{0,2,4,6\}\) induce a chordless four-cycle. The stated general bounds do not entail our specific integral homotopy type or character. Kim--Lew developed the general theory of Leray numbers of tolerance complexes, without an exact octagonal classification. Previously published exact homotopy and dihedral-character calculations for cycle two-independence, cycle-power cut, or squared-*path* tolerance complexes involve different simplicial face rules and do not imply the present statement. A 3-robust clique complex is also different: since \(\alpha(G)=2\), the three-robust clique complex of this very graph is the full seven-simplex, whereas \(X\) is three-dimensional.

## Limitations

This result is one natural eight-vertex boundary case and supplies no general formula for arbitrary powers of cycles, higher tolerance values, or integral dihedral representation lattices. A rationally acyclic geometric quotient need not be contractible or integrally acyclic. Computational checks of additional instances cannot establish any unclaimed infinite-family formula. Priority against unindexed equivalent published results has not been exhaustively certified; the independent mathematical audit has not been performed.

## References

1. S. Barik, A. Mondal, and S. Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606, first public 14 April 2026, https://arxiv.org/abs/2604.12606.
2. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384, first public 10 November 2026, https://arxiv.org/abs/2611.14384.
3. M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030, first public 7 September 2021, https://arxiv.org/abs/2109.03030.
