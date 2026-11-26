# Independent mathematical audit

## correctness

PASS

The stated conclusions hold. At radius two a sequential pair of disjoint swaps is one batch and an overlapping pair is two single-swap batches, so the metric ball equals the two-batch ball with total size at most two. Active singles and disjoint pairs have distinguishable supports of sizes two (adjacent) and four, giving 1+b+binom(b,2)-s with the center included. A triple contributes two new rotations if all distinct, one changing its separated endpoints if its endpoints differ but exactly one adjacent pair is equal, and zero otherwise. Those supports also identify the triple, giving the correction h+d. Under uniform letters p=(q-1)/q, an active edge has mean p, disjoint pairs contribute binom(n-2,2)p^2 in expectation, and the per-triple bonus is p+p(q-2)/q=2p^2. For q>=3 the simultaneous pointwise maxima of the three contributions require all adjacent pairs and all distance-two pairs to differ; choosing each symbol thereafter to avoid the preceding two gives the stated count. For binary boundary bits a_i, put N=n-1 and F=1+3b+binom(b,2)-a_1-a_N-3 sum(a_i a_{i+1}). This formula follows from h=sum|a_i-a_{i+1}|. The frozen proof has a localized false bound at N=6,z=5: with the only 1 interior, the neighboring zero-pair count C_0 is 3, not at least 4. The correct bound 3 still proves strict loss since the polynomial term vanishes. Independently, if b>=4 and a zero remains, filling it gains at least b-3>0 (at most two new neighboring one-pairs for an interior site, or one pair and one endpoint penalty). For N>=6, b<=3 gives F<=13<2+binom(N,2). For N=5, b<=2 gives F<=8; b=3 costs at least two in endpoint and adjacent-one penalties, since the only nonadjacent triple of ones is 10101, so F<=11<12. Thus only the all-one boundary pattern maximizes for N>=5. For N=4, exact evaluation by b gives value 8 precisely at 1111, 1011 and 1101; for N=3 the unique best bit pattern is 101. At N=2 all nonzero patterns tie at 3 and at N=1 only 1 attains 2. Each boundary pattern corresponds to two complement words, recovering the complete small-length lists. The singleton case is immediate. The PASS is for independently reconstructed conclusions, not for the literal N=6 intermediate bound.

## originality

FAIL

Record 4 already carries the equivalent local formula, mean and nonbinary extremum in a different triple notation. The binary rigidity and small cases materially distinguish this record from record 4, but are themselves covered by the verified distinct indexed Kendall-ball spectrum result, including explicit large-n rigidity and small-n values and multiplicities. Its pointwise formula mechanically gives the two short exact lists. This is a judgment of demonstrated overlap in the reviewed corpus, not historical anticipation by a later-dated document or an inference of order from the same-day labels.

## value

FAIL

The alternating rigidity is a meaningful coding-metric fact, and would be a valuable remainder relative to record 4 alone. But the full indexed spectrum already determines it and the small-n cases, leaving only explicit labels at two tiny lengths obtained by immediate evaluation and the trivial singleton. Fixing the proof-bound typo does not restore a distinct exact finding, so no scientific repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
