# Independent mathematical audit

## correctness

PASS

A vertex cannot improve exactly when at least half of its present neighbors disagree with it. If either shore has imbalance of magnitude ≥2, deleting one neighbor from a vertex's neighborhood cannot reverse that imbalance or cause a tie; best responses force both shores uniformly and oppositely colored. For even n the remaining shore sums are zero and each deleted pair must agree, giving the binomial sum and deleting no crossing edge. For odd n equal-sign shore imbalances require the majority action to occur on agreeing deleted pairs, with (n+1)/2 such pairs. For opposite imbalances, every undeleted indexed pair differs in the same orientation and every unequal deleted pair differs in that orientation too; the difference of two between the shore sums leaves exactly one unequal indexed pair in total. This gives the t=n−1 and t=n cases and their separate counting factors. The cut is (n²−XY)/2 minus the number of unequal deleted pairs, so the stated cut-size bins, threshold, and welfare ratios follow. At n=t=2 both bins coincide at the optimum and the two counts combine; this is not an inefficiency claim. An independent bitmask best-response enumeration matched all 42 histograms for 2≤n≤8 and 0≤t≤n, covering 757296 ambient action profiles. Replay: python3 /workspace/evidence/bounded_checks.py 1. The bounded enumeration corroborates the analytic classification and does not prove it for larger graphs; the packaged checker was read, not run.

## originality

PASS

The crown census for n≥6 is equivalent to an earlier indexed majority C-coloring result after flipping all actions on one shore and adding the two constant coordinated assignments. The intact biclique comparison is also covered. The supported distinct claim is the partial-matching family: the weak-Nash classification and cut histogram for 1≤t<n, including the sharp odd threshold and the exceptional t=n−1 welfare level. Neither the endpoint classification nor the closed-neighborhood dynamics supplies that core result. No priority is inferred from absence of additional hits.

## value

PASS

A matching deletion preserves dense bipartite symmetry while locally changing ties, making this a natural exact test of when inefficient equilibria appear. The sharp odd threshold, all intermediate stable-cut counts, and exceptional t=n−1 cut bin quantify how weakly stable profiles and efficiency change beyond the already known endpoints. The result is static, not an assertion about reachability or dynamic absorption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
