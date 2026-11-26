# Independent mathematical audit

## correctness

PASS

For odd p, in a full p^e-block the first-order correction from lifting an e-1 block vanishes modulo p^e because sum b=p(p-1)/2, and higher corrections are divisible by p^e. Fermat gives the initial block -1, so for two indices differing by p^e times a unit, e>=1, the power-sum difference has valuation e-1. This induces bijective isometries in the rescaled variable on each index branch and p-to-one uniformity for each coordinate. On the n=-1 mod p branch, the continuous value at -1 is zero (also the limit of sums up to p^j-1 by the block congruence). Thus S_p(n) has valuation v_p((n+1)/p), strictly below that of the adjacent increment for n!=-1; both square statuses coincide including zero at finite precision. On other branches the shift is 1 modulo p, not necessarily 1 at higher precision. The unit/unit count follows from sum chi(x(x+1))=-1, or counting (2x+1-2y)(2x+1+2y)=1; at x=0 and x=-1 the possible higher-valuation coordinate is individually uniform by its own isometry. Counting square units, even-valuation squares and zero yields all four finite counts. The geometric valuation sum gives the densities; direct algebra verifies both strict signs. For arbitrary cutoffs, truncate at depth K with p^(K+1)>N and K=O(log(2N)). Each positive-valuation square stratum below K uses O_p(1) single congruence classes per branch and depth, as does the unit/unit part. The two possible high-valuation tails are supported on at most two congruence classes per branch modulo p^(K+1), giving O_p(1) error and omitted expected count; the same argument for both marginals and the joint cell proves the other cells by subtraction. Fresh replay: python3 -B /workspace/reviews/reproduce.py 1; direct integer power sums check 102601 indices in nine complete periods, both marginals, all four cells and exceptional-branch valuations and leading digits. These are bounded checks, not the proof.

## originality

PASS

Pass the unequal-branch power-sum index law, strict covariance sign reversal and cutoff bound, not the ordinary residue-ring pair-count formula, the p=3 marginal, or classical power-sum block congruences. The strongest published catalogue overlap covers the regular-branch count exactly, but is not equivalent to the index law: applying it requires proving the isometric lift behavior for the variable increment and identifying the exceptional branch with identical statuses. The same-date evidence is used for coverage, not priority.

## value

PASS

The exponent p-1 is singled out by Fermat's congruence, and adjacency joins a single exceptional same-status branch with p-1 regular branches. The equal marginals therefore hide a strict correlation sign reversal with p modulo four. The exact four-cell law at every depth and the logarithmic error for unrestricted integer cutoffs quantify how the branch structure affects integer sampling, rather than supplying only another formula for square residues on a ring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
