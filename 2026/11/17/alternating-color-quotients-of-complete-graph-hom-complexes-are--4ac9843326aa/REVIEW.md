# Scientific review: alternating-color complete-graph Hom quotients

## Correctness — PASS

The statement specifies all integers \(2\le m\le n\) and separates the cases \(n=m\), \(n=m+1\), and \(n\ge m+2\). The sorted-row difference coordinates give a finite product-cell model of the full-symmetric orbit space. The odd-stabilizer criterion exactly determines which cells have one or two lifts under the alternating quotient. The resulting kernel of integral cellular chains has a two-term differential with coefficients \((-1)^{n-i}\), and the columns selected by adding one to the final composition part give a triangular integral submatrix with diagonal units. Hence there can be no concealed integral torsion. The known simply-connected Hom-complex sphere-wedge theorem and Armstrong's orbit-space fundamental-group formula, with explicit fixed points for all three-cycles, permit the final Hurewicz–Whitehead step. The standalone verifier independently checks all quotient cellular boundary compositions and homology in three characteristics in fifteen cases. These finite checks corroborate, but do not replace, the unrestricted proof. The principal risk is the correctness of the quotient characteristic-map and parity-lift description; its derivation and boundary signs are stated explicitly and checked combinatorially.

## Originality — PASS relative to inspected evidence

The closest accessible complete result, *Full two-sided symmetry character of complete-graph Hom complexes*, proves the exact \(A_n\)-quotient rational Betti rank \(\binom{n-2}{m-2}\) but expressly does not determine quotient homotopy types or integral torsion. Rational homology cannot imply the new integral wedge homotopy type. Babson–Kozlov's later paper establishes the unquotiented wedge homotopy type, not the present alternating-color quotient. Their 1997 ordered-disjoint-block paper concerns a related quotient for block permutations; its full text was inaccessible and is recorded as a residual priority risk, not as a document shown not to cover the new claim. Pfeifle's related geometric comparison was checked at abstract level and likewise cannot be ruled out completely. Search comparisons included the complete-graph Hom, alternating-color, symmetric deleted-join and quotient aliases; no equivalent integral homotopy classification was identified. A failed search is not offered as a uniqueness proof.

## Mathematical value — PASS

The integral homotopy classification is a natural strengthening of already motivated rational representation computations. Symmetry quotients can create fundamental groups or torsion absent in an unquotiented space, so ruling both out for this *entire infinite family* is not a routine conversion of rational Betti ranks. The explicit two-sheeted cell geometry and primitive integral boundary explain the phenomenon and can support further analysis of related graph-coloring moduli. The statement is not a minor numerical gain or an arbitrary finite slice.

## Sources and unresolved risks

Primary source inspected in detail: Babson–Kozlov, *Complexes of graph homomorphisms* (2003), Definition 1.2 and Proposition 4.5, https://arxiv.org/html/math/0310056v4. Closest prior complete character result inspected in full: https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-full-two-sided-symmetry-character-of-complete-graph-hom-complexe--ce942485ca98/RESULT.md. Earlier Babson–Kozlov 1997 preprint and Pfeifle 2005 paper were accessible only in abstract/description; these remain publication-priority risks. Armstrong's 1965 orbit-space fundamental-group theorem is classical and used as an input. There is no independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
