# Independent mathematical audit

## correctness

PASS

The odd divided difference makes the reductions bijective. F(x)−x has valuation one, so F is the identity mod 2 but swaps each parity class mod 4, forcing an even period at every finer level. Exact polynomial multiplication confirms F²(x)−x=8(x²+3x+3)(x²+4x+5), with valuations 3 and 4 on the even and odd classes respectively. All iterates of F² have derivative 1 mod 4. If an iterate H has displacement h of valuation s≥2 then H(H(x))−x=(1+H′(x))h+O(h²) has valuation s+1, since v₂(1+H′(x))=1 and 2s≥s+2. The first returning power of two for F² is the exact least period (which divides that power); doubling it gives the exact F-period at k≥2. Dividing each parity population by its period confirms the cycle counts, including k=1,2,3. The fresh checker verified the identity coefficient by coefficient and the full decompositions through k=14; the lifting proof gives unbounded k.

## originality

FAIL

Fan–Liao, arXiv:1010.5583v2, Theorem 6.7 and its type II-[s] definition directly cover the stated six-cycle census and every least period. The shifted binomial map is the one-parameter specialization of their classified odd-ball dynamics under the affine conjugacy y=2x+3, with the reduction precision shifted by exactly one. This is verified prior coverage, not a decision based on an unavailable source.

## value

FAIL

The parity split is mathematically natural, and the short proof is sound. But the claimed exact fact is a mechanical parameter substitution in the existing quadratic cycle-type classification. The record does not establish a new structural result for translated columns or a distinct valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
