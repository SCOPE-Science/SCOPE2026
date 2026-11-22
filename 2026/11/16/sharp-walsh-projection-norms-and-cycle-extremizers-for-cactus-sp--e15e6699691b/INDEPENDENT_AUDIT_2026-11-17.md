# Independent mathematical audit

## correctness

PASS

Connected cactus spanning trees require every bridge and exactly one omitted edge independently per edge-disjoint cycle, so their Walsh sum factors as bridge signs times ∏[(∏ s_e)(Σ s_e)]. This immediately gives rank product 2^b∏(2^ell−1_{even} binom(ell,ell/2)), invertibility iff cycles odd, min nonzero multiplier 2^{#even cycles}, and inverse 2-norm when no zeros. Endpoint norm of Fourier projection onto this specific spanning-tree frequency set is its kernel's normalized L1 mass =∏ E|Σ_{ell} ε_i| =∏ α_floor((ell−1)/2). The central-binomial telescoping identity α_m=(2m+1)binom(2m,m)/4^m was independently computed for ell3..9, including parity plateaus. For N vertices, Σ m_j≤K=floor((N−1)/2), α_1=3/2 and α_{m+1}/α_m=(2m+3)/(2m+2) decreasing, hence global max (3/2)^K and equality only all m_j=1 with the specified one-edge parity budget; at fixed r balancing all m_j via these decreasing ratios gives stated α_a^(r−u)α_(a+1)^u. Independent integer configuration enumeration checked global maxima for N=3..17. The proof, not finite enumeration, establishes all N and cactus topologies.

## originality

PASS

Bounded semantic Resultary search plus primary-literature comparison finds no earlier theorem dominating the precise full stated claim. Explicit equivalences and narrower covered portions are identified. This is best-of-knowledge, not a guarantee of global novelty. The previously known ingredients and different domains of related results are not claimed new.

## value

PASS

This evaluates an exact Fourier projection and sharp cactus extremizers across all connected cactus graphs, a natural family where cycle-block combinatorics produces an operator-theoretic invariant. The extremizer and refined fixed-cycle-count classification are meaningful structural optimization, beyond generic matrix-tree enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
