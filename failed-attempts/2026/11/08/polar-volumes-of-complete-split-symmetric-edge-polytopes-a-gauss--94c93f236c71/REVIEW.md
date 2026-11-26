# Independent mathematical audit

## correctness

PASS

For p clique coordinates, anchor at the uniquely minimal one. These p chambers have unit translation-quotient Jacobians relative to a fixed root. The maximum of the p−1 remaining coordinates has unweighted density (p−1)r^(p−2), and each of the q independent coordinates has an interval of length 2−r. Adding the clique constraints restricts r to at most one. The incomplete beta integral then gives a sum of coefficients (not just a binomial probability); the projection Gram determinant is 1/n. Below half the tail probability tends to one; above half the first coefficient times its limiting geometric sum gives p²/(p−q); in the window the standardized threshold is (p−q−1)/sqrt(n−1) and local Stirling gives the stated Gaussian coefficient. Independent checks used exact polynomial integration for 121 pairs and numerical tight-constraint hulls for (2,2), (2,3), (3,2), with rooted volumes 14/3, 15/2, 11/2 and intrinsic volumes smaller by sqrt(n). Replay: branches/b7371d9b-bb78-4bcb-ac74-2e2e8b4f7b81/independent_polar_check.py and .log. These are finite diagnostics. The frozen artifacts/verify.py was read, not executed.

## originality

FAIL

The distinct indexed complete-bipartite Mahler result does not display the split volume, but its Proof Step 3 already derives the exact polar volume density in the range of the left block, p(p−1) M^(p−2)(2−M)^q/sqrt(n) on [0,2]. Completing that block to a clique imposes exactly M<=1 and changes nothing else. Truncating this known density and using the classical beta-binomial identity gives the exact invariant. The window and side estimates are then direct binomial CLT, Stirling and geometric-tail evaluations; no different asymptotic theorem is needed. This is an implication comparison, not a claim of chronological priority between same-day records.

## value

FAIL

The volume and crossover are natural quantities, but the exact split volume is a mechanical slice of an already computed natural density. The three asymptotics package directly the standard binomial tails for that slice; no independent estimate beyond that immediate reduction survives. In particular no moderate-deviation or uniform error result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
