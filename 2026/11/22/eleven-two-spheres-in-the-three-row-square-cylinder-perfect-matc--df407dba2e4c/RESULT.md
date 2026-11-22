# Eleven two-spheres in the three-row square-cylinder perfect-matching complex

## Finding

Let \(P_3\) be the path on three vertices and \(C_4\) the four-cycle. For a graph \(G\) with perfect matchings, write \(\mathcal M_p(G)\) for the simplicial complex whose vertices are edges of \(G\), and whose faces are exactly the edge subsets extendable to perfect matchings of \(G\). Then the twelve-vertex square cylinder has complete integral homotopy type

\[
\boxed{\big|\mathcal M_p(P_3\square C_4)\big|\simeq\bigvee^{11}S^2.}
\]

This is a pure five-dimensional simplicial complex with 32 facets and 1,196 nonempty faces. It is simply connected with \(\widetilde H_2\cong\mathbb Z^{11}\) and all other reduced integral homology zero, so it cannot be shellable. In contrast, the known open-boundary graph \(P_3\square P_4\) has perfect-matching complex homotopy equivalent to \(S^1\). Closing the four columns into a square cycle changes both the first nonzero homotopy dimension and its multiplicity.

## Assumptions and scope

All graphs are simple, undirected, and finite. The graph \(G=P_3\square C_4\) has vertex set \(\{(r,c):0\le r<3,\ 0\le c<4\}\), identified with the integers \(4r+c\). Its edges are the four cycle edges \((r,c)(r,c+1\bmod4)\) in each row and the eight transverse edges \((r,c)(r+1,c)\) for \(r=0,1\). In particular it has 12 vertices and exactly 20 undirected edges. Equivalently, since the four-cycle is \(C_4\cong P_2\square P_2\), this graph is the first non-cubic three-dimensional rectangular cubical box \(P_2\square P_2\square P_3\). This is a **longitudinally periodic square cylinder**; it is not the open grid \(P_3\square P_4\), the triangular-transverse cylinder \(C_3\square P_4\), or the toroidal grid \(C_4\square C_4\).

For reproducibility, order graph edges lexicographically by their sorted integer endpoint pairs, numbered \(0,\ldots,19\). A face is represented by the sum of \(2^i\) over its edge indices \(i\), including the zero mask for the empty face when a separate chain calculation uses it. The complete certificate checks every simplicial face rather than selecting illustrative matchings.

## Proof

**1. Exact facets and the full complex.** Enumerate perfect matchings by selecting the least as-yet-uncovered graph vertex and pairing it with every available neighbor, recursively. This returns exactly 32 distinct six-edge matchings. Independently, inspect every six-subset of the 20 graph edges (\(\binom{20}{6}=38{,}760\) candidates) and retain exactly those covering all twelve vertices without repetition. This second enumeration returns precisely the same 32 facets. Taking every nonempty subset of every facet gives the exact face numbers

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(20,142,392,418,192,32).
\]

Thus the complex is pure of dimension five and has 1,196 nonempty simplices. Its Euler characteristic is \(20-142+392-418+192-32=12\).

**2. An exhaustive simplicial collapse to dimension two.** The attached `certificate.json` records 526 ordered pairs of face masks \((\sigma,\tau)\). The checker reconstructs all faces independently from the graph and confirms, for each consecutive pair, that \(\sigma\subset\tau\), that \(\dim\tau=\dim\sigma+1\), and that \(\tau\) is the unique currently present codimension-one coface of \(\sigma\). Therefore each is a valid elementary simplicial collapse, and deleting all 526 pairs preserves homotopy type. The remaining complex \(Y\) is two-dimensional with 18 vertices, 66 edges and 60 triangles. All proper faces remain present, and no unverified disappearance of higher-dimensional simplices is assumed.

**3. Trivial fundamental group by an explicit triangular presentation.** Choose the breadth-first spanning tree of the one-skeleton of \(Y\), rooted at its lowest-numbered vertex and scanning edges in lexicographic order. The tree has 17 edges. Collapsing it contracts the entire connected one-skeleton to a bouquet of \(66-17=49\) loops. Each of the 60 oriented triangles yields one attaching-word relation in these 49 generators, with signs determined by the oriented triangle boundary. The accompanying certificate records 49 successive pairs consisting of one triangle mask and one loop-generator index. At each step, after deleting generators already killed, the specified triangle's word consists of **exactly one letter with exponent \(+1\) or \(-1\)**. Hence that relator kills precisely its named generator; the checker verifies the relation and updates every remaining word. All 49 generators are eliminated, and 11 empty attaching words remain. Consequently \(\pi_1(Y)=1\), with no reliance on abelianized relations alone.

**4. Integral homotopy type.** Since \(Y\) is connected and simply connected, \(H_1(Y;\mathbb Z)=0\). Since it is a finite two-dimensional CW complex, \(H_2(Y;\mathbb Z)\) is a subgroup of a free cellular chain group and is therefore free abelian. The Euler characteristic of \(Y\), also equal to \(18-66+60=12\), gives \(\operatorname{rank}H_2=11\). The Hurewicz isomorphism supplies 11 maps of two-spheres representing an integral homology basis. Their wedge produces a homology equivalence \(\bigvee^{11}S^2\to Y\) between simply connected CW complexes; Whitehead's homology theorem upgrades it to a homotopy equivalence. The preceding elementary collapses then yield the asserted homotopy type of the original complex.

The complex is pure of dimension five but has nonzero reduced homology in dimension two. A pure shellable simplicial complex has reduced homology concentrated in its top dimension; hence this complex is not shellable.

## Verification

Run `python3 verify.py` with `certificate.json` in the same directory, using only the Python standard library. It (i) constructs the cylindrical graph; (ii) enumerates the perfect matchings by both recursive vertex pairing and independent six-subset testing; (iii) constructs all simplicial faces; (iv) independently replays all 526 elementary collapses, verifying unique cofaces at each step; (v) constructs and checks the 17-edge spanning tree; (vi) checks the 49 exact single-letter fundamental-group eliminations; and (vii) independently calculates the rank 49 of the residual simplicial two-boundary over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\). The recorded execution output is `check_output.txt`; its final success line is `HOMOTOPY_TYPE_WEDGE_11_S2_CERTIFIED`. The modular checks corroborate the integral proof but do not substitute for the verified fundamental-group eliminations.

Both the collapse list and loop-relation elimination list are explicitly included as data, so the conclusion is not inferred from a finite sample, a failed search, or numerical Betti ranks alone. A checker option `--make-certificate` reconstructs the data deterministically, but the default checks the accompanying saved certificate.

## Relationship to prior work

Chandrakar, Chau, Goyal, Karki, and Subhash [1] proved in November 2026 that the open rectangular three-row grid \(P_3\square P_{2n}\) has a wedge-of-spheres perfect-matching complex; their Theorem 3.5 assumes the open, nonperiodic column edges. At four columns, their formula yields \(S^1\), not the square cylinder considered here. The full text's definitions, theorem and proof concern the open boundary; it contains no longitudinal cycle classification.

The previously published exact collapse of \(\mathcal M_p(P_3\square P_4)\) [2] likewise gives a five-cycle and reflection action for the **open** graph. An alias search was also made under the isomorphic three-dimensional cubical-box graph \(P_2\square P_2\square P_3\); the nearest indexed three-dimensional-grid result concerns the **ordinary** matching complex of \(P_2\square P_3\square P_3\) [7], not the perfect-matching complex of this smaller box. A separately indexed \(2\times2\times3\) **honeycomb** complex [8] is also inapplicable: its dual graph has 32 vertices, while the Cartesian cubical box has 12. Another published three-row boundary comparison [3] closes the **transverse** three-vertex path to a triangle, studying \(C_3\square P_4\), not \(P_3\square C_4\). A third published calculation [4] covers the **fully periodic sixteen-vertex** graph \(C_4\square C_4\), which is not the twelve-vertex graph here. These results neither contain the same graph nor provide a natural subcomplex or homotopy equivalence that implies the present integral classification. The earlier polygonal-line-tiling work [5] treats open chains and the two-row grid, and its stated conjecture motivates examining boundary variants without supplying their exact homotopy type.

## Limitations

This is a complete finite computation and homotopy proof for the single square-cylinder graph \(P_3\square C_4\). It does not classify longer square cylinders \(P_3\square C_{2n}\), determine equivariant homology under the cylinder's automorphism group, or give an inclusion map from the open-strip complex. Matching the same numerical answer in another work might have escaped the indexed searches, so research priority is not certified. The finite certificate has been internally replayed; it has not received an independent mathematical audit.

## References

1. H. Chandrakar, T. Chau, S. Goyal, R. Karki, and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058v1, first public 2026-11-13. https://arxiv.org/abs/2611.18058
2. *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex*, public mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-five-cycle-core-and-signed-reflection-homology-for-the-three-b--521893fb03dc
3. *A boundary-sensitive eight-column classification of three-row perfect-matching complexes*, public mathematical record, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-boundary-sensitive-eight-column-classification-of-three-row-pe--c400769702b4
4. *Perfect-matching complex of the four-cube: 54 three-spheres and 21 four-spheres*, public mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perfect-matching-complex-of-the-four-cube-54-three-spheres-and-2--a4eb4065227f
5. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1, first public 2024-07-08, *Annals of Combinatorics* 29 (2025), 1211–1233. https://arxiv.org/abs/2407.05809
6. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
7. *The three-dimensional \(2\times3\times3\) grid matching complex is a wedge of 48 five-spheres*, public mathematical record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-three-dimensional-2-times3-times3-grid-matching-complex-is-a--2e1452e7c48b
8. *The \(2\times2\times3\) honeycomb perfect-matching complex is a wedge of two four-spheres*, public mathematical record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-2-times2-times3-honeycomb-perfect-matching-complex-is-a-wedg--bc0202f43949
