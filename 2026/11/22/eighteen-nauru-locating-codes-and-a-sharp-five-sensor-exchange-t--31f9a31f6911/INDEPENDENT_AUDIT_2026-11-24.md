# Independent mathematical audit

## correctness

PASS

For a locating-dominating k-set in this cubic graph, at most k omitted vertices can have singleton traces. Thus there are at least 2(24-k)-k selected-to-omitted incidences and at most 3k; k is at least eight. Equality forces independence and eight traces of each of sizes one and two. The independent reconstruction in /workspace/branches/04d64270-7057-441c-acf6-b444e60cb810/independent_nauru_check.py tested all 1,271,626 subsets of size at most eight and recovered exactly the eighteen displayed sets. It checked shore balance, the two double-cover incidence 8-cycles, and the permutation taking A_0 to B_{0,1}; rotations and reflections are transitive within each family. Direct comparison recovered intersection multiplicities 27, 36, 72, 18 at 0, 2, 3, 4. For distinct codes the exchange cost is exactly eight minus the intersection size. The resulting graphs are edgeless through budget three, three six-cycles at four, and 10-regular with 90 edges and every eccentricity two at five. The search is exhaustive for this one graph, not evidence for a generalized Petersen family. Supplied scripts were inspected, not executed.

## originality

PASS

The general lower bound is known. No independent earlier statement or stronger result furnishing the exact eighteen ordinary optima, their structure or their batch-exchange graphs was established in the inspected evidence. Credit the finite classification and sharp transition, not the lower bound or general move rule.

## value

PASS

This natural cubic graph provides a concrete exact benchmark for minimum locating-domination mobility: all optima are frozen under single moves, budget four retains three cyclic components, and adding one replacement gives diameter two. The complete census, automorphism orbit and overlap data explain rather than merely report the threshold, and are useful for testing structural or algorithmic predictions about constrained reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
