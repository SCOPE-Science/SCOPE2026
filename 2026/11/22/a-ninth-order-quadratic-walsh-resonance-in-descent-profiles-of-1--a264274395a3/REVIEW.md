# Scientific review: positional descent-profile Fourier cancellation

## Correctness — PASS

The precise claim is the identity for the two Walsh characters supported at \(\{1,2\}\) and \(\{1,3\}\) for every \(n\ge4\), the iff-ninth-order zero, and the exhaustive two-character census through \(n=9\). The unique maximum-element decomposition of a \(132\)-avoider gives four explicitly displayed formal power-series recurrences. Substitution into \(C(z)=1+zC(z)^2\) yields \(D(z)-A(z)=z^3\) and the Catalan-coefficient identity. The rational expression factors as \((n-2)(n-9)\), establishing the exact zero domain. `checker.py` uses independent factorial enumeration and independent Catalan recursion and compares every character through order nine; the finite census is exhaustive within its stated scope. No unproved extension to all quadratic frequencies at larger orders is claimed.

## Originality — PASS with residual priority risk

The nearest structural theorem is Reifegerste's 2002 descent-set/excedance-set preserving bijection; it transfers the problem but does not state or calculate either of the two fixed-position signed moments or the first quadratic-band cancellation. The inspected 2004 Mansour paper concerns positional extrema and inversion-sign statistics; the 2010 Barnabei–Bonetti–Silimbani paper identifies the \(132\)-descent Narayana distribution but studies aggregate \(123\)-avoidance descents. Published Fourier computations for the same avoidance class use inversion-incidence coordinates, not descent-position coordinates. Published quadratic sampling for stack-sortable permutations studies injectivity of an observation map, not signed descent-profile convolution. An unindexed derivation in the language of \(321\)-avoiding excedance sets or Dyck valley positions could nonetheless subsume this identity, so historical priority is provisional rather than guaranteed.

## Value — PASS

The equality of two geometrically different coordinate pairs is an exact all-length signed correlation identity on a canonical Catalan family. Its factorization selects the isolated natural order \(n=9\), where exactly four quadratic Fourier characters become invisible while all linear characters remain visible. This resolves a concrete low-degree recovery boundary, not merely an arbitrary recomputation of Catalan numbers. The finite four-mode list and the infinite two-mode statement are intentionally distinguished.

## Limitations

The finding gives neither the full convolution rank at length nine nor quadratic-band zero classifications at lengths exceeding nine. Inference of full-spectrum invertibility from low-degree characters is expressly excluded. The independent audit channel has not been used.

Self-review: passed. Independent audit: not yet performed.
