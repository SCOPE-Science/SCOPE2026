# Mathematical review

## Correctness: PASS
The vertex and edge definitions are explicit and periodic in both coordinates. The executable proof exhaustively constructs all \(96{,}433\) independent faces, all \(623{,}476\) covering relations, and complete matchings. Acyclicity is checked on every edge of the full oriented Hasse graph; the first matching leaves a vertex, two critical five-cells and one critical six-cell. Its exact signed recursive Morse boundary is \((0,0)\). Hurewicz identifies the two attaching degrees with the homotopy class because the five-skeleton is four-connected, proving the integral wedge. The independent second matching gives a primitive rank-three boundary and the same Betti numbers. Remaining computational risk is implementation error in the enumeration or reduction; readable source, redundant matching, and exact integer arithmetic mitigate but do not establish independent certification.

## Originality: PASS relative to inspected evidence
Jonsson 2006 treats the exact doubly periodic graph class but supplies Euler-characteristic information, not its full homotopy type. Bousquet-Mélou–Linusson–Nevo 2007 treat open/cylindrical grids, and Adamaszek 2012 and Okura 2019 likewise do not provide this exact toric classification. Other explicitly published square-torus cases concern \(4\)-by-\(4\), \(5\)-by-\(5\), or \(5\)-by-\(6\), not \(4\)-by-\(7\); a seven-cycle categorical product is mathematically different from the Cartesian torus graph. No inspected full text or accessible published exact-match record implies the two fifth spheres and one sixth sphere. An unindexed or otherwise inaccessible equivalent classification remains a publication-priority risk; no claim of exhaustive global novelty is made.

## Mathematical value: PASS
The coprime \(4,7\) torus is a natural test case for the classical negative-activity hard-square problem. Its classical alternating independent-set count \(\widetilde\chi=-1\) conceals three independent homology classes in two dimensions; an integral homotopy classification is strictly stronger than that index. The mixed-dimensional answer gives a concrete boundary to any inference from the coprime alternating-count phenomenon to a single-sphere homotopy type, and distinguishes this case from previously studied neighboring square-torus examples. No general infinite-family theorem is claimed or required for the exact natural finite object.

## Closest literature and limits
Primary sources are Jonsson (2006), Bousquet-Mélou–Linusson–Nevo (2007), Adamaszek (2012), and Okura (2019); their exact scope is compared in `RESULT.md`. All proofs apply only to the stated finite graph. Publication priority and independent validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
