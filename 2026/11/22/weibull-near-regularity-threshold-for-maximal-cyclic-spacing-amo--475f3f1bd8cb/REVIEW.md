# Independent mathematical audit

## correctness

PASS

Anchoring the labeled subset at its first point and ordering the other m−1 clockwise offsets produces the factor (m−1)! with unit gap Jacobian. Shifting by the minimum allowable gap leaves simplex mass mε; all its points differ from a rotated regular polygon by O_m(ε), giving the exact uniform probability and the Lipschitz O(ε) error in the density integral. Thus the mean differs from the claimed limiting intensity by O(n^−1). Conditional on a shared anchor, all 2m−k−1 other coordinates for a k-label overlap are independently confined to fixed arcs of total length O(ε); summation gives exponent −(m−k)/(m−1). Disjoint label sets give independence from all non-neighbors together, so the dependency-graph TV bound with mean adjustment has the stated rate. Zero count is exactly the strict survival event; at x=0 a regular selected subset has probability zero. The Fourier example follows by strict AM–GM or Jensen, and for m=3 only the paired harmonics survive integration. Independent replay: python3 /workspace/branches/independent_replay.py 2 (mpmath 1.3.0); integrates the m=2,3 Fourier densities and finite widths. The all-n claim follows from the argument, not this check or the supplied simulations.

## originality

PASS

The one-subset volume and regular-polygon density factor are prior tools, and no novelty is credited to those constants in isolation, the Poisson method, or the elementary two-point correspondence with diameter. The supported distinction is the growing-cloud arbitrary-subset minimum-gap extreme and count with a quantitative fixed-m TV bound and explicit nonuniform intensity. No inspected prior statement was found to cover that package or mechanically imply its nonsmooth m≥3 law.

## value

PASS

The minimum gap is the natural best-separation objective when selecting a fixed-size subset. The result identifies its different cusp scaling, quantifies how a nonuniform sample changes the chance of finding a well-spaced subset, and gives a finite-size error for the actual number of feasible subsets, not just the optimum. In particular the rate accounts for overlapping candidate subsets; neither a fixed-polygon calculation nor an elementary upper bound on the optimum gives this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
