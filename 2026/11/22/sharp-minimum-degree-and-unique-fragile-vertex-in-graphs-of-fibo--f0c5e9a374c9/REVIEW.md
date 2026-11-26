# Independent mathematical audit

## correctness

PASS

For any one-run of length b, its last min(b,q) flips to zero are legal: any newly tested suffix has fewer than q ones, and a preceding run constraint can only weaken. Thus at least q flips are legal with at least q ones. With at most q-2 ones all flips are legal; with q-1 ones a first-zero flip is legal in addition to deleting any one (it shortens the first zero-run or makes or extends an unrestricted prefix, including when a singleton zero is removed). The all-one word has exactly q neighbors for n>q, and n<=q gives the cube. At n=q+1 only 01^q is deleted; at n=q+2 exactly three words are deleted and the unique distance-two pair, 01^(q+1) and 101^q, has the two stated surviving common neighbors. At n>=q+3 and q-1 ones, there is at most one illegal addition because the only forbidden word with q ones is 01^q followed by zeros. At q ones a first-zero flip works for a split run, or a suitable endpoint zero can be flipped for a single run: a leading run of at least three zeros can lose its first zero, or two leading zeros permit extending q ones to q+1 into a trailing zero. An initial one-run can always extend. Above q ones multiple runs already give q+1 deletions; a single noninitial run admits one extra deletion at its first one, and a non-full initial run admits extension. These cover q=2 as well as all larger q. Independent replay `python /workspace/branches/independent_replay.py 1` checks 83 full induced graphs, totaling 48289 admissible vertices, and verifies the full extremizer sets in the noncube cases.

## originality

PASS

Earlier work defines these words, counts them, and lists them with Gray bounds. The nearest degree-sequence results instead use other graph definitions. No inspected result gives or implies the exact one-coordinate minimum and attained multiplicities for this graph.

## value

PASS

For single-coordinate generation on a known constrained family, minimum degree and its minimizing words locate the states with the fewest legal next moves. The exact universal transition from the cube through two boundary strata to a unique bottleneck is a useful structural invariant, especially because other equinumerous languages behave differently. This is local degree information, not a claim about connectivity, Hamiltonicity, or generation complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
