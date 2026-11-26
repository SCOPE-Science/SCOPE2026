# Independent mathematical audit

## correctness

PASS

Every rectangle is counted once by the two columns belonging to its row-pair/color slot. Each column contributes at least four slot incidences, with equality at weights two and three. Pairwise balancing of integer loads proves R≥20 binom(q,2)+4qr at b=5q+r. When b=5q is odd, an unbalanced column adds at least two incidences and hence at least 2q to this bound. Otherwise the sum of deviations from q is zero and the defect is one-half the sum of their squares. An independent form of the parity argument: let e_i be the parity of ones in row i; then the number s_ij of same-color agreements is odd precisely when e_i=e_j, since b is odd. At least four of the ten pairs are within the two parity classes (the minimum is the 2+3 split). Each odd pair forces at least one nonzero integer deviation, so defect ≥2. Independently recomputed the B, C, W slot histograms as {2:20}, {0:4,1:16}, {0:2,1:16,2:2}. In B the two-one masks form a 5-cycle and the two-zero masks its complement; regularity explains the uniform loads. C is a subset of B with no repeated slot. W has exactly two rectangles, from mask pairs (24,12) and (24,18). Add copies of B, append a prefix of C or remove it from the next copy, or append W at residue five; the corresponding distributions give the stated equality and exceptional defect for all widths, including b<5. Independent direct counts through width 120 are supporting checks rather than the universal proof.

## originality

PASS

The counting identity, convexity lower bound, and several small exact widths are known. The inspected closest primary source explicitly poses the broader exact evaluation and equality problem and notes the 5×5 exception. The new content supported by the comparison is the symbolic evaluation for every width at height five, including the precise odd-multiple obstruction and matching constructions.

## value

PASS

This gives a complete one-parameter solution of a natural small-height case of a published exact-minimum and sharpness question. The bounded parity effect is not an isolated improvement: it characterizes exactly an infinite congruence class where the otherwise sharp convexity bound fails, and comes with portable finite constructions certifying all other widths as well.

The dated certificate retains the supplied scientific assessment, sources and limitations.
