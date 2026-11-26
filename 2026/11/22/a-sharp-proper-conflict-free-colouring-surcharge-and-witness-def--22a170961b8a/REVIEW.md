# Independent mathematical audit

## correctness

PASS

An intersecting class of edges is a subset of a star or a full triangle. Choosing centres for the star classes, including a centre for any singleton, cannot yield a shared centre in an ordinary optimum, since those classes could be merged. In an (n-2)-class partition with t triangles there are t+2 noncentres, so binom(t+2,2)<=3t forces t=1 or 2. Equality for t=2 would force two edge-disjoint triangles partitioning K_4, which is impossible. The single triangle is on the three noncentres T; every other centre has all three of its T-edges, so centres are now intrinsic, and every edge within S=[n] minus T independently chooses one of its two endpoint stars. This is a bijection with named colourings after specifying the triangle set, a tournament oriented toward the receiving star, and the palette bijection. For e contained in S, every present colour has at least three incident neighbours (three triangle edges or the three T-edges of a star outside e); for e meeting T in one point exactly one triangle edge avoids e; for e contained in T a star at v supplies exactly 1+indeg(v) disjoint edges. So precisely binom(s,2) witness failures are forced, with three extra iff no vertex has indegree zero. Such a vertex is unique when it exists, giving s*2^binom(s-1,2) source-containing tournaments and the asserted counts after the palette factor. Both bins occur for n>=6 (orient a 3-cycle to dominate the rest for a source-free tournament); only the first occurs at n=5. The forced failures exclude n-2 colours. The minimum-endpoint rule with n-1 colours is proper and every pair e has a unique disjoint edge in a colour n-1, n-2 or n-3 class: choose respectively the largest class index not ruled out by e among those last three indices according to RESULT.md §3. Equivalently, among the last four ground points, choose the smaller of the two greatest points not in e; its colour class has exactly the larger of those points available as the other end. This also verifies all terminal-pair cases. The stated small graphs are correct. Inspected VERIFICATION.md and verify.py without executing it; the finite backtracking histograms use unlabelled partitions and don't prove unrestricted n.

## originality

PASS

The optimal proper-colouring normal form is known and is not credited as new; its full triangle-and-stars version predates the cited Daneshpajouh theorem and is already restated in arXiv:2001.00221. The distinct findings are the exact proper open-neighbourhood surcharge for all n>=5 and the witness-defect distribution of the ordinary optima. The strongest same-family and same-condition sources examined do not provide those assertions or a dominating implication. This is not a historical-priority certification.

## value

PASS

The ordinary and proper conflict-free numbers differ by exactly one for an entire classical family. More importantly, the defect census explains the obstruction for every ordinary optimum: all pairs among centres fail, while the three triangle pairs fail simultaneously exactly when its assignment tournament is source-free. The sharp palette result alone would not describe this obstruction or its distribution. The theorem has natural parameters and a reusable neighbourhood statistic, beyond counting known optimal partitions or checking small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
