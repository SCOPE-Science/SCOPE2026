# Review of the sixty-line boundary and complement

## Correctness — PASS

Rams--Schuett's model and sixty lines give a well-defined reduced divisor. The finite-field verifier independently lists all 120 coordinate permutations, obtains sixty distinct line spans, and enumerates all 1020 pairs (line, rational point on that line) over \(\mathbb F_{16}\). The 1020 incidences comprise exactly 510 distinct points, each on two lines. Since any geometric meeting of two F16-defined lines is itself F16-rational, this is exhaustive over an algebraic closure. No triple point is possible. All intersections are transverse on the smooth K3 surface. The thirty conjugate line pairs are skew, and therefore boundary points occur only in even extension degrees. Inclusion--exclusion gives \(60\cdot4^m-450\) boundary points for even \(m\) and zero for odd \(m\). The already established projective-surface zeta is independently recomputed from the line-class Gram ranks and exhaustive projective point counts, and division by the newly proven boundary zeta proves the all-extension open-surface formula. A finite experiment is used only for finite enumerations, not for infinitary extrapolation.

## Originality — PASS, provisional priority

Rams--Schuett (arXiv:1512.01358) already construct the surface and its sixty lines; Degtyarev (arXiv:1604.05836), Degtyarev--Itenberg--Sertoz (arXiv:1601.04238) and Veniani (arXiv:1606.02135) give relevant geometric classifications. A previous exact calculation of this *same* surface already determines its complete projective zeta function, arithmetic Picard rank and Frobenius line orbits. Another earlier computation already determines the exact 60-line graph with 510 intersecting *pairs*, adjacency spectrum, and skew Frobenius-conjugate pairs. These substantially stronger antecedents are not asserted as new here.

The new and logically distinct assertion is that the 510 pairwise intersections are 510 **distinct** points, without any triple concurrency, and exhaust each line's 17 F16-rational points. The line-graph edge census does not imply this: graph triangles may represent three distinct nodes or a single triple crossing. The projective surface zeta does not determine the line-union zeta or the open-surface zeta. The compared primary full-text passages and published mathematical-record searches did not identify this boundary point scheme or complement zeta. Priority remains provisional against specialist arithmetic studies and unindexed tables.

## Mathematical value — PASS

The union of all 60 lines is a geometrically natural divisor on a record-setting quartic K3, not an arbitrary cutout. Its 510-node decomposition and absence of points over all odd-degree extensions determine a concrete, previously unforced arithmetic invariant of the associated *open* K3 surface. The boundary is unexpectedly saturated by intersections over F16, a useful exact input for its log geometry, finite-field rational-point analysis, and divisorial arithmetic. Although the already established zeta of the projective K3 is used, the zeta of its complement cannot be computed from it without the separate scheme-theoretic boundary incidence theorem. The claim is narrow but substantive.

## Limits and evidence

This is the specified F4 model and reduced line divisor only; no statement about other twists, unknown automorphisms or all K3 line arrangements. Finite checks and their precise logical use are described in `VERIFICATION.md`. The source Picard rank is assumed rather than independently proved. A later discovery of a directly covering boundary count would change the originality verdict. Independent scientific validation was not performed.

Self-review: passed. Independent audit: not yet performed.
