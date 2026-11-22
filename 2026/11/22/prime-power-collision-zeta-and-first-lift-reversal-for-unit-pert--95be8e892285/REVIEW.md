# Scientific review: prime-power collision zeta for unit-perturbed biquadratics

## Correctness — PASS
For odd \(p\) and unit \(c\), the exact factorization \((x-y)(x+y)(x^2+y^2+c)\) has three smooth components with no triple crossing. Their finite-field union contains \(3p-3-\chi_p(-1)-2\chi_p(-c/2)\) points and has \(3+2\chi_p(-c/2)\) transverse double crossings. One-component residue disks have exactly \(p^{k-1}\) lifts; each double-crossing disk reduces by a Hensel coordinate isomorphism to \(uv\equiv0\pmod{p^k}\), with \(p^{k-1}(1+(k-1)(p-1))\) lifts. These facts produce the displayed all-level formula and the signed difference between coefficient classes. The attached checker passed 105 direct-histogram cases and additional independent pair/geometry checks. Its finite coverage does not substitute for the general proof.

## Originality — PASS on inspected evidence
Seraj (2023) proves a different invariant, the sum of distinct quartic outputs modulo primes, though its character-class and repeated-output analysis is relevant. Li and Xiong (2024) determine line-intersection statistics of degree-four polynomial graphs over finite **fields**. The published unit-perturbed quartic graph result concerns a four-variable additive energy only modulo prime squares; the published pure-quartic graph result concerns a different polynomial and a different additive energy. Neither full source inspected states the uniform two-variable second-fiber-moment formula for the nonfield rings \(\mathbb Z/p^k\mathbb Z\) at all \(k\), or its first-lift reversal. Standard normal-crossing lifting is acknowledged as background; implicit equivalent local-zeta calculations remain a priority risk.

## Mathematical value — PASS
The collision second moment is the simplest quantitative measure of nonuniformity among preimages of a polynomial, beyond image cardinality. The full exponent-dependent law isolates singular collision growth and proves a sharp reversal: the coefficient class with fewer collisions over the prime field has more at **every** higher precision. The leading growth coefficient switches by a factor of five, providing a natural, nonlocal-to-mod-\(p\), infinite-family invariant. This is an explicit all-precision local congruence result, not a fixed-modulus table or a substitution in a known scalar theorem.

## Closest literature and limitations
The distinction from the two published graph-energy formulas is between *two-input equality* and *four-input equality of graph sums*. Prime-field information, general Hensel lifting, and normal-crossing zeta methods are established background. The theorem addresses neither individual fiber sizes nor nonunit coefficients or characteristic two. Bibliographic priority and any unrecognized general special-case implication remain subject to independent validation.

Self-review: passed. Independent audit: not yet performed.
