# Scientific review

## Correctness — PASS

The precise domain is the set of marked-origin binary words whose bi-infinite periodic extensions avoid all antisquares of order at least two. The eight short exclusions are necessary and sufficient in the periodic setting by the cited minimal-antisquare theorem and its exceptional-factor proposition. The derived cyclic transition code has zero-runs at least two and one-runs exactly two or four, which gives a unique background bit and a short/long singleton-gap encoding. Cyclic block marking yields the two rational factors, while a separate double count gives the exact binomial coefficients and sharp support. Both small-period edge cases and nonprimitive words are covered. The included verifier returned `VERIFY_OK` with 131070 exhaustively enumerated binary words through length 16 and separate transfer checks through length 40. Finite checks do not replace the infinite combinatorial proof.

## Originality — PASS, with bibliographic risk

Baranwal et al. (2022/2023) already prove the basic forbidden patterns and the asymptotic growth rate; those are prerequisites, not claimed as new. The unweighted periodic-point zeta function and ordinary primitive-orbit census are also already known and expressly excluded from the novelty claim. The precise contribution is the bivariate length/Hamming-weight function, the full binomial distribution, and a sharp central gap in possible Hamming densities including its parity restriction. The known univariate zeta function does not imply the weight distribution. Web and research-record searches for equivalent fixed-composition or weighted circular antisquare enumeration did not reveal a covering result, but negative searches do not prove uniqueness. An unindexed equivalent or an implicit weight refinement of prior block arguments remains possible.

## Mathematical value — PASS

For this natural avoidance-defined periodic language, ordinary exponential growth hides the total absence of balanced constant-composition words. The sharp support condition gives a full determination, for every block length and Hamming weight, of whether that constrained codebook is empty; the positive classes have exact multiplicities. The boundary equality requires a period divisible by six and has exactly six marked-origin words at each extreme one-third density. This is an exact structural and enumerative answer beyond a routine recount of total words, with applications to selecting fixed-composition circular constrained words.

## Closest literature and limits

Primary source: Baranwal et al., *Antisquares and Critical Exponents*, arXiv:2209.09223, Theorem 11, Proposition 18, Section 7. Related but distinct: Currie et al., *Complement Avoidance in Binary Words*, arXiv:2209.09598, and Mousavi–Shallit, *Repetition Avoidance in Circular Factors*, arXiv:1212.0052. The theorem concerns periodic binary words and the full periodic extension only. No proof of new claims is attributed to finite experiments, and no independent external scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
