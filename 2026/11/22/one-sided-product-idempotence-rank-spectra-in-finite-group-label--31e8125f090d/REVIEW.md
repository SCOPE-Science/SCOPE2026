# Review

## Correctness — PASS

The composition convention is fixed explicitly: \(H\circ E\) acts first by \(E\). For the partition \(R\cap S=A\), \(R\setminus S=B\), \(S\setminus R=C\), the product image is \(A\cup T\), \(T=h(B)\cap C\). Product idempotence is exactly one independent requirement \(f(x)\in h^{-1}(x)\cap B\) for each \(x\in T\). A marked-preimage double count yields \((b)_t(a+t)^{b-t}\), and the group equations \(k_{f(x)}g_x=1_G\) supply exactly \(t\) independent constraints, even for nonabelian groups. This establishes the full polynomial and its bounds. The leading group-order degree is attained only by the two rank-one base maps with common fixed point, giving the probability limit \(1/n\). Direct enumeration matches every joint-rank cell for all base pairs through four positions and directly multiplied cyclic and nonabelian group-labelled transformations. See `verification/verify.py` and its captured output. No finite test substitutes for the proof.

## Originality — PASS, with residual priority risks

Published literature establishes the wreath-product/end-of-free-\(G\)-act framework and the individual-idempotent count; neither is claimed new. Full text of the archive work by Dolinka, Gould and Yang and the relevant thesis chapter was inspected for this particular question. Two particularly close published research results were inspected in full: one computes joint ranks for ordinary total transformations (trivial group labels); the other treats pairwise-*commuting* idempotents for general group labels. Their statements do not imply the noncommuting one-sided product-idempotence rank spectrum or the extra lift exponent depending on \(t\). Searches using group-labelled transformations, skew pairs, noncommuting products, aliases and one-sided idempotence located no dominating universal group-labelled formula. Blyth–Almeida Santos (2006) concerns skew pairs in transformation semigroups; only the accessible catalog/abstract could be checked, so a hidden stronger statement cannot be ruled out. Novelty is bounded to the complete general finite-group weighted rank law and group-order invariance, not the existing base or commuting cases.

## Mathematical value — PASS

This is an exact all-dimensional distribution in the natural endomorphism monoids of homogeneous free finite group-sets; it distinguishes three independent image ranks and counts noncommuting one-sided idempotent products, which commuting-only enumerations cannot detect. The universality across arbitrary finite and nonabelian groups and the fixed-rank group-order asymptotic supply structural information beyond small enumerations or a mere specialization of a known base count. The precise rank polynomial supports further study of biordered structures and product statistics, without claiming a new general semigroup structure theorem.

## Independent check and limitations

A separate independent mathematical audit has not been carried out. This proof assumes invertible group labels; the lifting equation cannot simply be transferred to non-group labels. The limit fixes the number of orbits \(n\) while \(|G|\) grows. Historical priority is provisional, especially because the full 2006 skew-pair paper was inaccessible.

Self-review: passed. Independent audit: not yet performed.
