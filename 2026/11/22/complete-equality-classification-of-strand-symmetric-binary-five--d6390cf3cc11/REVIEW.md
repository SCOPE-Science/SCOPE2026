# Independent mathematical audit

## correctness

PASS

Independent exact enumeration in checks/binary_avoidance.py covered all 14893 unions of at most six of the 16 reverse-complement orbits. For each candidate, repeatedly take the allowable starts of a walk with one extra vertex, intersecting with retained vertices. A nonempty fixed point has walks of arbitrarily large length and hence a cycle; reaching empty yields the exact maximum length in vertices of the retained DAG. No candidate of fewer than six orbits survived. Independently counted avoiding strings of each length m+4 to evaluate the tail sum of the first-hit time: P(T≥m) is the count divided by 2^(m+4), since the first m five-words must all avoid the selected set. Compared every orbit-label/length/exact-fraction tuple against the frozen table, and checked the complementation involution directly for each of the ten sets. All rows match, the involution has no fixed points, and path counts are 6:4, 8:4, 10:2. In a DAG each retained walk is a path, so the sharp guaranteed-hit windows have lengths L+5. Replay: python3 checks/binary_avoidance.py; output in checks/binary_avoidance.out. No conclusions beyond the binary five-word graph and stipulated uniform model.

## originality

PASS

The ten-set equality classification, five complement pairs and full path/first-hit profile are the supported contribution. Minimum cardinality 12 and short optimized examples are credited to Marçais–Elder–Kingsford. Their lawful preprint was inspected, including its actual Table 3 and single-solution ILP formulation. The parity reference points to a genuine Hexagon paper; the prefix arXiv in the frozen reference is wrong. The correct paper proves a weaker odd-order obstruction, not this exact classification.

## value

PASS

This is the complete equality layer of a previously posed symmetric feedback-vertex optimization problem. It quantifies which worst-case and fair-bit first-hit behaviors are possible at the fixed minimum cardinality, including the spread of exact guarantees and differences among sets with the same longest path. This is a natural finite benchmark, not a biological estimate or an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
