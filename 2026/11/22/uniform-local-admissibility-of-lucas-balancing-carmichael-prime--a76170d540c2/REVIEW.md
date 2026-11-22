# Review: Uniform local admissibility of Lucas-balancing Carmichael prime triples

## Correctness — PASS

The proof fixes the sequence normalization, derives the norm identity \(AD-B^2=8\) and the mod-\(48\) cycle, then treats **every prime**: parity, primes dividing the middle term, primes dividing the outer product, and remaining primes. The exceptional local residues \(1,-1/6,-6\) do not vanish because all prime divisors of \(AD\) exceed \(3\). The direct Korselt calculation is independent of the numerical example. The infinity assertion is explicitly conditional on Dickson's conjecture. The standalone script checks \(17\) even indices against \(37\) primes each, plus a verified prime-factor example; this is supporting finite evidence only.

## Originality — PASS, with residual risks

Bensella (arXiv:2611.02054v1, 2026-11-01) characterizes the Korselt parameters but explicitly does **not** assert infinite prime triples or establish the all-index no-local-obstruction result. Wright (2019), summarizing Chernick's use of Dickson, establishes conditional results with different linear forms. The closest indexed Lucas–Carmichael and positive-shift claims use different divisibilities. The reviewed local-admissibility claim is not implied by the inspected prior results. Some database entries were readable only as scientific summaries and an unindexed equivalent could remain.

## Mathematical value — PASS

The all-index admissibility calculation resolves the concrete local existence obstruction for the newly parametrized Carmichael product family. It is a structural theorem with an immediate Dickson-conditional infinitude consequence for **each** even index, rather than an arbitrary special case or an additional isolated numeric example. It does not claim an unconditional result about infinitely many prime triples.

Self-review: passed. Independent audit: not yet performed.
