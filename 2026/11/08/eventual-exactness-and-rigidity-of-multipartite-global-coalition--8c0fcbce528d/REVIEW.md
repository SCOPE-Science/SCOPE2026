# Self-review

## Correctness — PASS

For every integer \(r\ge4\), the proof first reduces global domination of a complete multipartite graph to meeting every part. Each selected singleton from part \(i\) has a partner omitting precisely that part; partners selected from distinct singleton-bearing parts are distinct, so there are \(s\) hubs of at least \(r-1\) vertices. The excess accounting inequality charges each hub \(r-2\) and every vertex in a part without a singleton at least one-half after its \(s\) marked positions. The three integer cases \(s\le r-2\), \(s=r-1\), and \(s=r\) establish the upper bound; the disjoint hub construction attains it. At the stronger threshold, strict inequality excludes \(s<r\), and equality forces every class, proving the independent injection product. No finite test is used for the universal quantifiers. The included verifier checks exact arithmetic and independent sample partitions and constructions.

## Originality — PASS (historical priority provisional)

Anholcer, Besharati, Mojdeh, and Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386, Proposition 6, already give a construction with \(N-r(r-2)\) classes; that construction is expressly not claimed as new. Their Theorem 7 covers only up to three parts, whereas their Conjecture 54 asks for exactness in general. The present upper bound at \(m\ge3r-6\), rigidity at \(m\ge3r-4\), and product enumeration are stronger statements not implied by the cited lower bound. Semantic searches of available research findings and primary literature did not identify a covering result. A failed search does not prove absolute priority, and unindexed or later manuscripts remain a risk.

## Mathematical value — PASS

This supplies a theorem for an explicit infinite tail of a named open conjecture, for arbitrary numbers of parts and unequal sizes. The structural accounting bound and the forced form of every optimal partition are not routine substitutions into the known construction, and the exact product enumeration is a natural additional invariant.

## Limits and literature

The published conjecture remains unresolved outside the stated sufficient-size regime. The thresholds need not be sharp. The proof concerns global coalitions, not related domination polynomials, global offensive alliances, or merely the existence of domination sets. Primary inspection was of arXiv:2509.15386 (version 4), including Proposition 6, Theorem 7, and Conjecture 54; the original introductory coalition framework is Haynes et al. (2020).

Self-review: passed. Independent audit: not yet performed.
