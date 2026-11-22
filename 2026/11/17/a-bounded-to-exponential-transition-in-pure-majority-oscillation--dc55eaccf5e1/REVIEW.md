# Independent mathematical audit

## correctness

PASS

For strict open-neighbor majority with incumbent tie retention, F(x)=complement(x) iff each site has at most one (r=3) or two (r=4) neighbors of its current colour. Width 3 excludes monochromatic columns, forces adjacent columns to be complements and yields exactly six starting configurations for even n. Width 4 splits into alternating three-to-one columns (eight states for even n) and balanced weight-two columns. For the latter each row must avoid monochromatic triples, giving a bijection with closed walks of the explicit 36-state ordered-pair transfer matrix. Independently built this matrix from six four-bit weight-two tuples without using the repository checker, obtained precisely 90 nonzero entries, recomputed the complete 36th-degree characteristic polynomial over the integers and matched all six factors/multiplicities. Direct trace power counts n=3,4,5,6,7 are 90,98,270,1388,2940 including alternating states. The cubic has one simple root in (3,16/5), and exact Schur reductions in the package place both quartic root sets strictly within |z|<2; remaining roots are <=1, so the unique Perron contribution grows as lambda^n with error O(2^n). Finite transfer factorization plus the all-n local bijection, not finite simulation alone, establishes the law.

## originality

PASS

Foundational Goles–Olivos threshold-dynamics periodicity gives a universal period-at-most-two constraint but not the fully flipping population of this family. Turau treats trees, whereas C_n box K_r contains triangles. The closest previously indexed result counts fixed points on width-three triangular cylinders and does not enumerate pure complement two-cycles, especially for K4 columns. Same-year exact oscillation work on open triangular strips, other graph types and whiskered cycles uses non-identical graphs and often all two-cycles rather than fully flipping states. No inspected exact theorem was found to imply both stated P3/P4 counts.

## value

PASS

The same local majority rule on the consecutive natural graph widths C_n x K3 and C_n x K4 passes from at most six fully oscillating states to exponentially many with an exact algebraic entropy. This concrete structural change, alongside a reproducible full transfer factorization and analytic root separation, is a motivated population invariant, not an arbitrary finite slice of a classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
