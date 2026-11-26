# Independent mathematical audit

## correctness

PASS

For n>=3 set m=n-2. At most one adjacent input can be used because deleting both ones gives the zero word. A near or far pair [i,j] can lose either one by starting the burst at i or j-1; the remaining positions are j-2 and i, coincident exactly at gap two. An adjacent pair has at least one external neighboring zero and hence consumes at least one of the m singleton outputs as well. Near starts two apart collide on a weight-two output, so their starts lie in independent sets on two parity paths. For m=4q+r the path bound is 2q plus 0,1,2,2 for r=0,1,2,3. Combining the singleton budget with this bound and the one-adjacent limit gives the claimed floor. In the stated construction singleton positions separate; zero-only bursts act before, between, or after the ones and give the eight distinct residue-pair types listed, with distinct absolute coordinates within each translated type. The boundary sizes and the three additional pairs per four positions check out. At n=2 there is one possible input. The supplied scripts were inspected, not run; the all-length proof is sufficient.

## originality

FAIL

A distinct indexed Resultary finding demonstrably already covers the exact mathematical statement, its boundary case, and the explicit optimal family. This is a duplicate-coverage decision, not a claim that the matching indexed record was chronologically first or that the mathematics is false.

## value

FAIL

The exact optimum of the sparse binary burst channel is a motivated invariant, but this record supplies neither a remaining unknown fact nor a materially different construction or obstruction after the exact indexed overlap is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
