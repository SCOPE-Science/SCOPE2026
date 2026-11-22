# Self-review

## Correctness — PASS

For \(q\ge2\), the \(2N-1\) spanning-edge requirement and \((q+1)\)-regularity prove \(|D|\ge2q+1\). The plane incidence axioms imply the exact connectivity criterion: both shore domination conditions plus a selected incidence. At the lower-bound cardinality each shore must have at least \(q\) selected vertices; the \(q\) selected lines must attain their maximal \(q^2+1\)-point union, forcing concurrency, and the other shore is its \(q\) uncovered points plus one covered point. Duality is exhaustive; the extra point has exactly \(q^2+1\) choices, with incidences \(e_D=q\) or \(e_D=1\). The edge-count formula gives cycle rank \(q-e_D\). Two independent standalone \(q\in\{2,3\}\) enumerators constructed from distinct coordinate systems and graph algorithms agree with every computed coefficient; they corroborate but do not replace the all-plane proof.

The argument explicitly treats the boundary order \(q=2\), finite projective planes without coordinates, the two distinct shore allocations, uniqueness of the omitted pencil line and the selected-incidence edge count. The Python and C++ checkers produced the same 210 and 1,040 optimum counts; their counts split into 168/42 and 936/104 by retained-subgraph cycle rank. They were run from the package artifact paths.

## Originality — PASS

Searched the same definition under weakly induced graph, closed stars and spanning-star-tree terminology, as well as the exact finite-plane count and low-order aliases; compared implications of primary full texts and indexed related findings. Existing generic bounds and regular spanning-star-tree existence theorems do not yield the full incidence-pencil optimizer classification or cyclic branch. One plausible 1997 paper remains inaccessible in full and absolute priority is not independently established.

In particular, the 1997 weakly connected domination source provides the parameter, while the 2009 random-regular and 2013 surface-bound papers provide general context only. The older spanning-star-tree results apply a stronger acyclicity requirement: the present \(e_D=q\) subfamily meets it, but the \(q^2\)-times larger \(e_D=1\) branch does not. The primary theorem is the dual, all-optimum geometric characterization and enumeration, not a claim to originate weak connectedness or the general spanning-tree bound.

**Closest literature and remaining limitations.** The 1997 Grossman paper on spanning star trees was inspected only at abstract level, so its unobserved special cases remain a genuine priority risk. Other indexed mathematical findings about connected domination and incidence geometry were compared on their mathematical properties and do not by themselves imply this weakly connected optimization result. No comprehensive publication priority or independent external validation is claimed.

## Value — PASS

The exact optimum geometry and count hold uniformly for all finite projective planes (including non-Desarguesian planes) and reveal a natural duality. The sharp edge-count threshold produces a structural, not only numerical, split between 2N(q+1) spanning-star-tree optima and 2N(q+1)q^2 connected cyclic optima. The finding gives a complete classifier useful for extremal network-coverage design on highly symmetric incidence networks; it is more informative than a minimum number or a finite table.

The exact class includes every finite plane of order at least two that exists, not just the Desarguesian examples tested. The dichotomy between tree and cyclic weak-star networks separates genuine shapes at a sharp coverage threshold. The full enumeration supplies concrete optimizer multiplicities, not an arbitrary parameter substitution.

Self-review: passed. Independent audit: not yet performed.
