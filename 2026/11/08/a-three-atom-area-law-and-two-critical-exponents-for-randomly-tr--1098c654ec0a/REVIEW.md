# Scientific review

## Correctness

**PASS.** The proof explicitly handles the full real-radius range \(0<R<1\) and the uniform torus shift, including the below-threshold and measure-zero boundary cases. Every included lattice point lies among one fundamental square's four corners. The parallelogram identity forbids a two-point-only diagonal event, giving the exact area-indicator identity. Ordinary two-circle geometry computes the diagonal-pair event, and a direct fourfold intersection integral computes the four-corner event. Inclusion-exclusion yields the complete law; the moments and distinct onset exponents then follow by algebra and two local integrals. Independent numerical slicing and geometric enumeration in `verify.py` corroborate the analytical steps. The proof does not rely on experiments to establish an all-radius claim.

## Originality

**PASS on the inspected record, subject to historical priority risk.** The most relevant full texts, Bárány–Matoušek (2005) and Ngoc–Reitzner (first publicly posted in 2020), treat large-body expected vertices/missed area and mean width, respectively, without an exact three-atom area law for small disk radii. Baudrier–Mazo (2019) analyzes the number and structure of translated digitizations, not probabilities of hull-area values. The Huxley–Žunić (2006) abstract concerns asymptotic counts of distinct disk digitisations, but its full text was not accessible; its possible treatment of small radii remains a genuine residual historical-priority risk. This review does not take negative search results as proof of novelty.

## Mathematical value

**PASS.** The first positive-area radius and the largest simple four-corner regime are geometrically canonical, not arbitrary parameter choices. The exact three-atom distribution determines every area moment and the two-dimensional boundary-length law. The distinct onset exponents of triangular and square hulls quantify how the random lattice first produces a nondegenerate polygon, providing a precise small-radius counterpart to established large-dilation hull approximation theory. These structural facts are not implied by the previously inspected asymptotic estimates.

## Limitations and closest literature

The theorem is confined to Euclidean circular disks of radius below one lattice unit and the square lattice, with uniform translation. It neither proves an all-radius formula nor supplies independent validation. The most important unresolved comparison is the full text of the 2006 paper on displaced disk digitization patterns, which was inaccessible; its abstract does not establish a competing area law. The 2019 paper on translation digitization was text-accessible and studied in its relevant disk and combinatorial sections. Only scientific claims contained in material actually inspected are used here.

Self-review: passed. Independent audit: not yet performed.
