# Independent mathematical audit

## correctness

PASS

A witness at two cuts crosses a marked segment iff exactly one cut puts the segment before it, giving the symmetric difference of prefixes. All cut pairs can be realized together with distinct endpoints. Two cells have the same trace iff the two strips between their cuts contain the same marked set, a common interval; each such interval gives two diagonals. The singleton-edge components are straight monotone chains: two edges meeting use consecutive top positions and consecutive ranks of the same slope. A positive full edge joins opposite corners on j−i=0, and a negative full edge on i+j=m; no corner connects to the other slope. A cycle in either line would require the entire intervening singleton chain, hence a monotone permutation. Thus in nonmonotone diagrams the 2m+2 baseline edges form a forest; for simple π they exhaust the equality edges and give (m+1)²−(2m+2). For a nonmonotone proper interval, neither of its diagonals can follow singleton edges through the interval; to be redundant its diagonal must use the corresponding full edge, with prefix and suffix following that slope. If both diagonals were redundant and a>1 the first value would have to be simultaneously 1 and m; if a=1 the two endpoints force c=1,d=m, contradicting properness. For an increasing bond at top a and lower minimum c the negative diagonal could be redundant only on i+j=m, so a+c=m and its prefix/suffix are descending extreme runs. Adjacent increasing bonds cannot both satisfy this sum, as it changes by two. For an isolated bond in that exceptional placement a descending extreme run has length at least two unless both outside parts have length one; an extreme descending bond has positive diagonal off j−i=0 for m≥4 and causes a new collapse. The leftover case is (4,2,3,1), whose initial triple is a nonmonotone interval. Lower-order reversal handles decreasing bonds by complementing all traces. Fully monotone diagrams have 1+m(m+1)/2, which is below m²−1 for m≥4. The explicit simple families have no interval inside a parity part. A block crossing the parity boundary contains 1 and 2k; in odd size it cannot contain all ranks up to 2k without also containing 2k+1 before the final 2k−1, so a crossing interval must be full in both parities. Prepending a common minimum to a simple tail adds 2m−2 traces containing it, from two chains meeting only in their endpoints, to (m−1)²−1 traces without it. This gives m²−2; the m=4 example (1,3,4,2) freshly yields 14 by enumerating the 25 cut pairs via python3 /workspace/reproductions/trace_and_commutant.py. Frozen code was inspected, not run.

## originality

PASS

The sharp unrestricted numerical capacity and sufficiency of simple extremizers are credited, as is classical common-interval theory. The supported addition is necessity of simplicity in every maximal marked representation and the sharp maximum over nonsimple ones. The closest literature and catalogue statements available do not establish these two restrictions; the unidentified earlier trace-complexity citation and inaccessible exact passages limit the comparison.

## value

PASS

An upper bound and a family of extremizers do not describe every equality configuration. Simplicity gives a representation-level certificate for extremality, and the m²−2 construction identifies the nearest possible failure of that certificate at every size. The common-interval collision argument explains why the condition is necessary; this is not a numerical recheck or a graph-isomorphism claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
