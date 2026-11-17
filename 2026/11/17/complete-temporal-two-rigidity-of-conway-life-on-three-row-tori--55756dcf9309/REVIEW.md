# Self-review

## Correctness — PASS

The claim concerns all \(n\ge3\) for the standard eight-distinct-neighbor B3/S23 rule on \(C_3\times C_n\). For any pair of consecutive time slices, the local conditions at time zero and time one can be imposed columnwise. A closed walk of length \(n\) in the resulting 4096-vertex graph is equivalent to an indexed spatial ring configuration satisfying \(F_n^2(X)=X\), with no independent boundary assumption. The exhaustive graph certificate examines every possible local triple of temporal columns and returns 6140 edges, plus cyclic components \((30,75),(27,81),(4,4)\) (vertices, internal edges). All vertices in the first two components are phase-diagonal; the third is a single directed four-cycle with vertices 455, 504, 3640, 3591. Consequently the nonfixed part of every two-return is exactly four phases of `1100`, requiring \(4\mid n\). There are two temporal orbits. A separate program exhausts all states on n=3 through 7, with exact agreement. The universal conclusion uses the finite graph decomposition, not the bounded brute force. Residual risk is an implementation or transcription error in both implementations; source and claimed graph totals are included to allow independent reimplementation.

## Originality — PASS, qualified

The most directly relevant prior full-text source is H. V. McIntosh's chapter *Life's Still Lifes* in the 2010 Springer collection, read for its width-three de Bruijn construction, 30/27-vertex fixed-state components, and the explicit discussion that a corresponding period-two search would be harder. Those fixed components are credited. Their existence does not determine the missing two-time cyclic component or prove that all nonfixed two-return configurations are the four stripes. Reia and Kinouchi's 2014 paper concerns density and mean-field behavior rather than narrow-torus exact periodic-point enumeration; its introductory model and results were read. Searches for equivalent finite-width period-two classifications, their count sequences and row-stripe aliases did not identify a source supplying the same theorem. An indexed fixed-point census for this geometry covers \(\operatorname{Fix}(F_n)\), not the difference \(\operatorname{Fix}(F_n^2)\setminus\operatorname{Fix}(F_n)\). No absolute priority or independence claim is made. Residual risk: obscure historical Life pattern catalogues or unpublished classifications may contain an equivalent complete census.

## Value — PASS

The smallest simple Moore torus height has unexpectedly rigid temporal-two dynamics: at every circumference there are either zero or exactly two temporal two-orbits, regardless of how large the ring is, even while the fixed-point families grow exponentially. Every genuine period-two configuration uses full occupied/empty columns and is nonlocalized. This is a natural complete classification, not a selected sample or narrow arbitrary invariant. McIntosh's historic de Bruijn work emphasizes why temporal-two analysis was substantially harder than enumerating still lifes, motivating a checkable global classification. A remaining limitation is that the method does not constrain longer periods or the basins of attraction.

## Closest literature and limitations

H. V. McIntosh, *Life's Still Lifes*, in *Game of Life Cellular Automata* (Springer, 2010), Chapter 4, especially pp. 46–49, gives the two fixed-state components but not the asserted two-time rigidity. Reia and Kinouchi (arXiv:1407.1006, 2014) analyze bulk mean-field density and not this torus invariant. The theorem has only self-review and independently executable finite-state certificates, not third-party mathematical validation.

Self-review: passed. Independent audit: not yet performed.
