# Independent mathematical audit

## correctness

PASS

The formula is true. Iterating the derivative of a constant A gives (AA*)^(2^(k-1)); the normalized trace makes the first two diagonal matrix units, scaled by N^(1/q), a copy of l_q^2. With b=epsilon/2 and a=(1-b^q)^(1/q), the pair (a,b),(a,-b) has unit norms, separation epsilon, and midpoint norm a, also at epsilon=2. The cited Corollary 4.2 gives the opposite bound, but the paper's global setup takes prime-power sizes. To justify the frozen all-N quantifier, choose a power of two M>=N and use the isometric corner map F -> (M/N)^(1/q)(F direct_sum 0). Each k-fold derivative scales by (M/N) and stays in the corner, which cancels the normalized-trace change. The lower bound thus descends to every N. This also supplies the missing explicit scope justification in the frozen citation. No numerical or formal proof certification was used.

## originality

FAIL

There is no finding of a prior literal equality statement. The issue is direct mathematical implication: the published lower bound and norm definition already determine the exact answer by restriction to two constant diagonal coordinates and the standard sign pair in l_q^2. Neither a new inequality nor a nontrivial identification of the subspace is needed. The arbitrary-size extension is likewise an immediate normalized corner restriction of the published bound.

## value

FAIL

The modulus is a natural invariant, but the precise number here is already mechanically forced by the published lower bound and the standard two-coordinate test on constants. Nothing about the geometry away from constants or the quantum subspace is resolved by that test. There is no separate surviving unknown exact invariant in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
