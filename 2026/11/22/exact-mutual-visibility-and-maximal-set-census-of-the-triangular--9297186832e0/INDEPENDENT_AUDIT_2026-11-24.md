# Independent mathematical audit

## correctness

PASS

In the Cartesian product, a geodesic follows a shortest cyclic arc and uses zero triangle steps for equal rows, otherwise exactly one. Both directions at antipodal columns and all positions of that step must be included. Checking existence of an interior mask disjoint from the selected set for each selected pair is therefore equivalent to ordinary mutual visibility. Heredity gives one increasing-order path per feasible set and makes maximality equivalent to failure of every one-vertex extension, including vertices smaller than the last inserted ID. Both supplied programs and their logs were inspected without executing them. An independently written BFS/distance-descent replay reproduced all labeled coefficients: from size 0 through 9, feasible [1,24,276,1952,8808,24720,40256,33000,9960,928], maximal [0,0,0,0,0,0,0,4608,4656,928], with totals 119925 and 10192. There were no larger feasible sets. Replay and saved output: /workspace/branches/7eb8e17e-a688-4029-8a64-ddcabd18ae17/independent_census.py and independent_width8.txt in the same directory. The seven-vertex witness also has a direct check: the pair of complete columns 0 and 4 can use the arc avoiding (1,0), and (1,0) can reach either complete column visibly by choosing when to change row. A new vertex on columns 5–7 is separated from (1,0) by the filled columns; on columns 1–3 its geodesics to (0,0) either use (1,0) or reach column 0 in another selected row. This verifies maximality of that witness independently of the counts.

## originality

PASS

The upper cardinality nine follows from published work and is explicitly credited. The minimum size among inclusion-maximal ordinary visible sets on this even torus, and the exact labeled census, are not supplied by the checked maximum-size theorem, the general lower-invariant paper, or the odd-width result. The exact catalog match is the frozen record itself.

## value

PASS

The lower invariant on Cartesian tori is a published problem, and the two antipodal shortest arcs make even widths a different case from the known odd-width value. Here the precise gap between the smallest inclusion-maximal size seven and the known maximum nine, together with the labeled distribution of maximal sizes, is a concrete benchmark for proposed even-width classifications and for testing maximal-set algorithms. This is not just a recomputation of the known maximum, and implies no general even-width theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
