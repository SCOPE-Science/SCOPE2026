# Independent mathematical audit

## correctness

PASS

Two wholly unseeded path interiors form an obstruction: neither terminal can make a first force into their union while both interiors remain white. A connected set with neither terminal lies in one interior and is obstructed. With one terminal, connectedness permits just end-prefixes, and at least two must be nonempty; their degree-two propagation reaches the other terminal and fills the two paths, leaving at most one final forceable path. With both terminals, connectivity requires a full path and excludes internal blue runs not touching an end. A proper nonempty end-union of size j has j+1 splits between ends, each distinct, whereas a full path counts once. Forcing is equivalent to having at least two nonempty interiors: each seeded but incomplete path propagates into its gap, after which a single empty path fills. Multiplication over paths, subtraction of configurations with no full path in the both-terminal case, and the terminal choices give the stated coefficient formula. No connected forcing set has size below three; exactly six size-three sets arise from one terminal and two adjacent interior vertices on different paths. The full set gives the monic term. All arguments allow one-vertex interiors but not direct terminal edges. Fresh fort-based enumeration (a set fails iff its complement contains a nonempty set into which every exterior vertex has either zero or at least two neighbors) agreed on every coefficient for 54 nondecreasing triples with 1≤r_i≤7 and N≤15, testing 509,994 nonempty subsets. Replay: python /workspace/replay_frozen.py 4. The packaged 68-triple pass is reported evidence; CODE/verify_theta.py was not supplied among the frozen support files. The independent proof covers all admissible lengths, not just the replay cutoff.

## originality

PASS

The supported distinct result is the complete connected polynomial for three paths with arbitrary lengths at least two, not the definition or the equal-arm minimum alone. The closest equal-arm classification gives a genuine overlap at the minimum coefficient, but the comparisons did not establish coverage of the remaining size coefficients or unequal-arm family.

## value

PASS

Three-path theta graphs form a natural simple bicyclic family for testing how induced connectivity interacts with forcing, beyond trees and cycles. A complete labelled size distribution for all three lengths distinguishes the two terminal mechanisms and provides exact counts (including the probability by initial set size), information not available from the scalar minimum or an ordinary forcing polynomial. Value rests on the complete structurally motivated classification, not on finite subset scans.

The dated certificate retains the supplied scientific assessment, sources and limitations.
