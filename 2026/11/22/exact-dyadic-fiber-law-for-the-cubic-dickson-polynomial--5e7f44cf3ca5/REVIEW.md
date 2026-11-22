# Scientific review

**Claim examined:** The complete target-by-target fiber law for \(D_3(X,1)=X^3-3X\) modulo \(2^k\), together with the sharp maximal fiber size and its target multiplicity for every \(k\ge1\). This review concerns only this claim; there is no broader claim for varying Dickson degree, parameter, or prime.

## Correctness: PASS

The polynomial identities at \(\pm2\) were expanded and the even-input change \(x=2t\) checked. Every odd class modulo eight is covered exactly once. The unique normalized square roots in \(1+4\mathbb Z_2\) give invertible 2-adic coordinate maps with explicitly proved difference valuations; these maps justify all modular fiber counts, including multiplicities from discarded bits. The ordinary 2-adic square-root classification gives the exact maxima and their number; the transition at exponent eight was checked separately. The standalone checker produced exact agreement on 131,070 target fibers from the 131,070 input residue classes across exponents one through sixteen, and on all square-root targets through exponent twelve. The proof, not the finite check, establishes the infinite statement. Remaining correctness risks: none identified in the stated normalization, but no independent proof assessment has occurred.

## Originality: PASS on accessible evidence

Source comparisons included Brazelton–Harrington–Litman–Wong (2021, arXiv:2103.09119, odd finite fields), Bremser–Gómez-Calderón (1991, Dickson values over Galois rings; stated main restrictions include odd residue characteristic), Yoshioka–Dainobu (2015, ordinary \(T_3\) dyadic permutation and periodicity), Iwasaki–Umeno (2016, ordinary Chebyshev orbital and degree periods), and Shang (2023, general residue-ring image-size bounds). Related public mathematical records for the monic cubic at powers of three, even-degree first-kind Dickson maps, and quartic second-kind maps do not cover the stated degree-three dyadic target-fiber theorem. The current accessible claim history has no matching statement; the nearest local Dickson claim assumes degree equal to a prime \(p\ge5\) and modulus \(p^k\). The proper comparison distinguishes algebraic equality \(D_3(X,1)=2T_3(X/2)\) from an invalid invertible dyadic substitution. Residual priority risks include unindexed prior work, imperfect transcription of the 1991 article, incomplete retrieval of other historical records, and inaccessible full public files of some nearby abstracts. No absolute novelty guarantee is asserted.

## Value: PASS

The result completely resolves a natural and classically motivated fiber question for the smallest monic odd Dickson polynomial at the singular prime. It separates an isometric Chebyshev even branch from four ramified odd branches, identifies all attained values, provides the full exact fiber formula uniformly in the modulus exponent, and gives a sharp large-fiber law with alternating extremizer counts. These are motivated structural invariants of the polynomial's local arithmetic, not a data-only statement, an arbitrary slice, or an automatic consequence of earlier image-size bounds.

## Scientific limitations and reproducibility

Only the fixed cubic at parameter one and powers of two is covered. The supplementary finite checker tests exponents at most sixteen; the proof is uniform. No external checking, certification, or infinite computation is claimed. Run `python3 verify.py` to reproduce every reported computational test.

Self-review: passed. Independent audit: not yet performed.
