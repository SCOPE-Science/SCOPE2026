# Independent mathematical audit

## correctness

PASS

The proof uses zero-based starts, overlapping windows, and a one-ended finite prefix. For same-parity coverage of length sixteen, at most one letter per window has index divisible by 16; the others depend only on index mod 32. The seven representatives at each residue fit in P8 and realize both values of the exceptional letter (alternation on odd arguments, or two odd arguments two apart after division by 2). The independent finite replay matched the disjoint 12/16 parity sets of length seven, the length-sixteen multiplicities (3:16,4:47,5:1), and the three base pairs of starts at lengths 5,9,17. For longer factors, if the first retained odd-position letter occurs at global position 2j+1, the projected factor starts at j. Its parity fixes all reinserted filler bits. The start is either 2j or 2j+1, both legal on the left; on the right only a final filler after the last retained letter can fail to fit. A shorter projected suffix has at least three occurrences, so losing one preserves nonuniqueness. A lifted suffix ends at an odd position and loses none, maintaining the stronger suffix invariant. At length 2d−1 the even-start factors project to length d−1 and cannot be unique; odd-start factors project to length d with no loss. Iteration gives the claimed length and both starts.

## originality

PASS

The exact finite-prefix minimum and two minimizer locations are supported as distinct to the best of current knowledge. Prior work includes length-seven parity rigidity, infinite distinct-factor counts, and general algorithms for this invariant, all distinct from the evaluated finite-prefix theorem.

## value

PASS

The automatic word and its canonical dyadic prefixes are natural, and the global shortest-unique invariant measures finite-prefix distinguishability not captured by ordinary factor complexity. The result gives both a sharp threshold and a complete location classification for an unbounded family. Its suffix invariant addresses a genuine boundary defect in naive desubstitution and is useful for exact prefix occurrence calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
