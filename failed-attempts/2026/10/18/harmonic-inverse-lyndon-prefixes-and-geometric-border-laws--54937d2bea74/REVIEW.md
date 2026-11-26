# Independent mathematical audit

## correctness

PASS

Bonizzoni et al. Proposition 7.21 characterizes inverse Lyndon words as strict sesquipowers of anti-Lyndon words, which is equivalent to the frozen periodic-prefix formulation with root length at most k. An unbordered root of length m is the least period of its length-k extension: a smaller period would restrict to a smaller period of the root and supply a nonempty border. The root is then forced by the initial m letters. Counting primitive necklaces gives the two exact counts including m=k and m=1. The Möbius formula gives L_q(m)=q^m/m+O_q(q^{m/2}); in its sum, writing m=k−b and expanding 1/(k−b)=1/k+O(b/k²) for b≤k/2, with the remainder of the sum exponentially small relative to q^k/k, gives the stated C_q(k). The geometric limit follows at each fixed b. The first moment is justified separately: probabilities are bounded by a constant times q^(−b) up to k/2, and the weighted tail above k/2 is O_q(k²q^(−k/2)). Prefix closure gives exactly the marginal tail at each position with at least k symbols remaining. Summing tails and using linearity (without independence between entries) proves both expectation claims and their remainders. The frozen script and finite output were inspected without execution; the uniform-in-k asymptotics and convergence of the mean are analytical.

## originality

FAIL

The prior strict-sesquipower characterization and classical necklace enumeration together determine the full least-period/border histogram directly. The remaining conditional and array laws are elementary asymptotic and tail-sum consequences of those counts and the known prefix closure. The reviewed formulas are not asserted to appear verbatim in the earlier array papers; the failure is the demonstrated implication, not an unsuccessful attempt to find an exact table.

## value

FAIL

The border and array statistics are natural, and the expected total is not an algorithmic running time. However, the exact counts are direct consequences of the known periodic-root description, and rewriting them as marginal tails, then summing, adds only standard asymptotic estimates. The finding does not resolve a nonroutine probabilistic question about joint array structure or any comparably independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
