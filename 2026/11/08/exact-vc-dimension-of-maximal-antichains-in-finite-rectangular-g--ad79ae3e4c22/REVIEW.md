# Independent mathematical audit

## correctness

PASS

For coordinatewise weak order [m]×[n], every shattered membership support must be an antichain, size k<=min(m,n). Omitting a marked point while retaining others requires a comparable blocking point and hence at least one adjacent slack row/column coordinate; with at most two marked positions served by each spare coordinate level, m+n-2k>=ceil(k/2), hence k<=floor(2(m+n)/5). All labels are realized by explicit maximal-antichain gadgets in 2×3 and 1×2 rectangles and transposes, arranged anti-diagonally; an extension to a global maximal antichain cannot reinsert a negatively tested point already blocked by its local witness. The proof handles 1×1 and all rectangular boundaries. Independent brute-force membership-shattering for 25 rectangles with 1<=m,n<=5 gives the exact formula, including the 5×5 case with 83 maximal antichains and VC=4.

## originality

PASS

PASS best-of-knowledge. Bouyssou–Marchant–Pirlot 2024 systematically enumerates maximal antichains of products of two chains, gives bijections and e.g. count 817 on 7×7, but the inspected full relevant sections do not determine VC membership-shattering of the maximal-antichain FAMILY. Tsai studies the strict-coordinate product order (different comparability) and Cambie et al. lattice-valued shattering differs from binary membership. No stronger theorem implying min(m,n,floor(2(m+n)/5)) was found in actual comparisons; the inability to exclude obscure equivalent combinatorics remains a residual risk.

## value

PASS

A natural poset-class learning invariant is sharply smaller than its width for square grids, with a nontrivial resource-obstruction bound and explicit rectangular gadgets. Full-width shattering exactly when n>=ceil(3m/2) for m<=n is a meaningful structural threshold; it is not simply counting maximal antichains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
