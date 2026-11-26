# Independent mathematical audit

## correctness

PASS

Index the starting four-bit state by fixed cycle labels. The overlaps of a rooted closed walk recover one indexed cyclic word, even at shorter period, and every appended bit is counted exactly once; the transition omits the central bit, testing exactly the four distinct neighbors for n≥5. For ordinary total domination a feasible cyclic gap list has each gap ≤5 and no two consecutive gaps ≥3, and these properties suffice by checking interior and selected sites separately. With L long gaps this gives n≤2k+3L≤2k+3⌊k/2⌋. Inverting yields the stated seven cases; the listed short/long constructions meet them, and separation by at least two precludes three neighbors since any three of the four neighbor sites contain an adjacent pair. The q=0 cases n=5,6 use just two selections. Equality forces alternating (2,5) at residue zero, giving seven distinct rotations, and forces one short-short junction with no deficit at residue two, giving n. At residue six the alternation has one unit of deficit, either a short 1 or a long 4, and the uniquely located defect of each type gives n sets. A shortened short between long gaps of length five cannot cause a third selected neighbor: any forbidden triple would use its adjacent selected pair, and the next selection is too far away. At residue one the q long gaps and q+1 shorts have one short-short junction and one unit of deficit. The junction fixes the label and gives 2q+1 defect choices; only the two shorts at this junction, producing gaps (1,2) or (2,1), overfill an open neighborhood. All other defects respect the cap, giving (2q−1)n and excluding exactly 2n. Independently reconstructed direct counts and polynomial-walk counts agree coefficient by coefficient for 5≤n≤18; the finite check corroborates rather than proves the all-order argument.

## originality

PASS

The standard transfer-matrix method, ordinary total domination on this family, and overlapping ordinary extremal data are antecedents. The new content supported by the comparison is the load-capped cardinality enumeration and the exact description and count of ordinary minima rejected by the cap at n≡1 mod 7. Neither the ordinary polynomial nor membership-dependent regular-set classification covers those claims. No distinct exact covering record was located; this is a bounded statement, not proof of priority.

## value

PASS

On the canonical quartic circulant family, cardinality counts answer a natural placement question not settled by the minimum size. The distinction from ordinary total domination is substantial: a complete all-size capped enumerator plus a structural theorem that the cap removes exactly two choices per labelled junction from a quadratically growing ordinary optimum family. This quantifies how an upper load constraint changes feasible optimal placements rather than merely applying a standard transfer method to reproduce a known scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
