# Review of the substitution-scale Abelian-complexity formula

## Correctness — PASS

The theorem concerns every integer base \(b\ge3\) and every substitution depth \(k\ge0\). The proof explicitly establishes the signed block total \((b-2)^k\), derives exact maximum/minimum prefix sums of the complementing block, and characterizes all factor sums from adjacent parent-letter pairs. Both parent-pair orientations occur. A maximizing prefix at the explicit offset \(r_k\) yields both extreme one-counts; the sliding-window increment bound fills the intervening integer interval. Thus the complexity count and the base-three/base-four-plus growth dichotomy follow with no unproved asymptotic step. The standalone `verify.py` performs independent finite block-window and extremal-prefix comparisons; it is diagnostic, not the proof.

## Originality — PASS, with stated bibliographic risks

The closest fully inspectable paper, Popoli–Shallit–Stipulanti (2024), develops additive complexity and presents other morphic examples, but the relevant example and theorem sections do not give this complementary-binary-family formula. Rigo–Stipulanti–Whiteland (2024) treats rank-one Parikh-collinear morphisms; the present incidence matrix has rank two for every admitted base. Chen–Wen (2018/2019) treats the cyclic, larger-alphabet digit-sum-modulo-base word, not the binary digit-\((b-1)\)-count-parity word; its eventually periodic result cannot imply the unbounded complexity here. The general binary-uniform algorithm of Blanchet-Sadri–Seita–Wise (2016) and Whiteland's asymptotic classification (2019) are materially relevant but were accessible only through metadata/abstracts rather than full text. Their possible specific examples remain residual risks; neither accessible statement establishes the explicit exact formula for all bases and powers. Mathematical-record searches and recoverable earlier claims revealed no statement implying it.

## Mathematical value — PASS

Lengths \(b^k\) are the intrinsic substitution scales, not an arbitrary computational slice. The classification determines the exact set of binary Parikh vectors at each such scale, sharp balance defects, and explicit factors attaining the endpoints. It identifies a genuine parameter-dependent change from logarithmic factor-length growth when \(b=3\) to power-law growth \(L^{\log_b(b-2)}\) for \(b\ge4\). This supplies a concrete contrast between rank-one bounded-complexity criteria and this rank-two automatic family. No formula at other lengths, downstream application or independent confirmation is claimed.

## Limits and closest sources

The scope is the stated complementary substitution family, bases \(b\ge3\), and lengths \(b^k\). The relevant primary comparisons are arXiv:2410.02409, arXiv:2405.18032 and arXiv:1809.06554, with the 2016 binary-uniform algorithm and 2019 asymptotic paper identified as non-exhaustively inspected risks. The finite verifier covers only the explicitly stated bounded test instances; no formal or independent certification is asserted.

Self-review: passed. Independent audit: not yet performed.
