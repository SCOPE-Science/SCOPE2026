# Independent mathematical audit

## correctness

PASS

A failed signature or equality of signatures after erasure is equivalent to deleting every selected witness of a closed neighborhood or symmetric difference. Closed neighborhoods are antipodal transversals. In axis coordinates, the north closed neighborhood is 0^6; the five upper ones differ in the two consecutive axes i+2,i+3 mod 5, and the other six are their complements. This proves distances 2,4,6 between signatures at graph distances 1,2,3 (reduce to the north vertex by transitivity). Adjacent-pair differences give all pairs of axes: pole-to-upper edges give consecutive pairs, upper-pentagon edges give nonconsecutive pairs, and cross-ring edges give the pole with one cyclic axis; each occurs twice. The pair occupancies therefore force the lower bounds 5,6,11,12. With five detectors, omitting any axis projects the twelve signatures to distinct words, forbidding exactly twelve of 32 choices; separation is automatic. At size six, the occupancy inequalities force a transversal. Relative to the zero and cycle-edge words, admissible choices have (pole bit, cyclic weight) (1,1), (0,2), (1,3), (0,4); the five choices in each class are respectively singleton, independent pair, vertex cover of size three, and complement of a singleton. Each admissible word is even, so deleting one detector cannot give a 5-set shared by two admissible words. Each face yields the claimed induced triangle with one pendant leaf at each triangle vertex; face transitivity, the checked representative, and the unique triangle in each such induced graph give twenty distinct optima. At eleven detectors, deleting one vertex of the full graph loses at most one witness from any requirement of size at least four. At twelve every requirement holds to level four, and a four-element pair witness rules out level five and above.

## originality

PASS

The ordinary model and general redundancy criterion are prior. A materially overlapping volume census even classifies the same optimal six-sets as one of its classes, but does not identify them by detector properties, prove their minimality as robust codes, or give the multilevel or extension results. No inspected statement covers the joint detector hierarchy and unique completion. The originality pass is for those detector results and their structural characterization, not for discovering the previously classifiable 20-element cohort as a set of point configurations divorced from its identifying-code property.

## value

PASS

The fixed icosahedral graph is a canonical tightly symmetric test for robust identification. The main return is structural: a triangle-and-leaves optimum for one loss, a unique extension for every smallest ordinary code, and a sharp jump from six detectors to eleven for one more tolerated failure. This relates exact configurations across levels rather than simply reporting an exhaustive-program count, and gives a benchmark against graphs with similar antipodal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
