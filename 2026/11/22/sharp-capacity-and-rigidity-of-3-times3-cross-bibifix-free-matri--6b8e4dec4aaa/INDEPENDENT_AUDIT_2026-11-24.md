# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 27–58 from the literal corner-overlap definition, including self-pairs. The observed corner sets A,B are disjoint. A two-square equality requires the prefix matrix center in B and the suffix matrix center in A; the common square is a unique component label. For sizes a,b this yields abq² disjoint complete bipartite components with side sizes bq⁴ and aq⁴, plus ab(q−a−b)q⁶ isolated vertices. A maximum takes the whole larger side (either entire side on a tie), giving ab(q−min(a,b))q⁶. With a≥b, equality in a≤q−b is necessary, and comparing the integers next to q/3 gives the unique smaller size floor((q+1)/3). This forces both large-alphabet orientations and the stated labeled count. For q=2, the four K(16,16) per orientation give sixteen choices each; only the two constant-side choices per orientation are unrestricted diagonal lifts. Inspected VERIFICATION.md and all three scripts without executing them. Their finite scope is supplementary; the exact graph argument supplies the universal upper bound and equality cases.

## originality

PASS

Best of current evidence, the claimed distinction is the unrestricted square-overlap upper bound and labeled rigidity, including the binary non-lifts. The numerical lower bound and the lift are prior; the exact capacity and classification are not established by those prior claims.

## value

PASS

Order three is the first order with both corner-symbol and proper two-square constraints. It is natural to ask whether the standard diagonal-lift construction loses capacity or misses optimizers. The exact answer distinguishes the rigidity for every q≥3 from the 28 binary non-lifts that the construction misses, supplying structural information not contained in the lower-bound construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
