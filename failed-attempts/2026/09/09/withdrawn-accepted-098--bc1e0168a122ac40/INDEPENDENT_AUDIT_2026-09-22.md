# Independent audit — SCOPE-20260909-098

## Scope
Independent review of `2026/09/09/098` at tree `57e3384b0e387c1c18703f1ce860fe8ce73bea3b`.

## Correctness
**PARTIAL PASS / MATERIAL OVERCLAIM.** The finite census itself is correct. Multiplication by 13 modulo 157 has one fixed point and 26 six-cycles, so a 13-set fixed by multiplication by 13 and containing 0 is exactly `{0}+O_i+O_j`, giving 325 cases. An independent implementation reproduces zero difference sets and the published distributions of covered nonzero differences and maximum multiplicities.

However, the record's “code-transfer” wording overreaches when it suggests that the circulant rank of the translate code for one subset excludes that subset from being a block of an arbitrary symmetric `2-(157,13,1)` design. That inference requires the cyclic translate development to be the design; it does not hold for an unrelated symmetric design with the same labeled point set.

## Originality
**FAIL.** The main cyclic-difference-set exclusion is already a direct consequence of the classical multiplier theorem, and in fact a stronger statement is immediate. A planar abelian difference set has every divisor of `n=k-lambda=12` as a numerical multiplier; in particular 2 is a multiplier. A suitable translate is therefore fixed by multiplication by 2. But `ord_157(2)=52`, so multiplication by 2 has orbit sizes `1,52,52,52`; no union of these orbits has size 13. Hence there is no cyclic `(157,13,1)` difference set at all, not merely no set fixed by multiplication by 13.

## Scientific value
**FAIL as a validated finding.** The 325-case census is a correct computational cross-check of a subcase already excluded by a much shorter classical theorem, and the additional arbitrary-design code-transfer statement is not valid as written. That combination does not meet the audit's originality/value bar for an accepted scientific finding.

## Reproducibility
An independent implementation reproduced exactly: 27 multiplication-by-13 orbits with nonzero orbit size 6; 325 candidate unions; zero survivors; distinct-nonzero coverage histogram `{42:26,48:26,60:78,66:26,72:169}`; maximum-multiplicity histogram `{4:273,6:26,8:26}`. It also recomputed `ord_157(2)=52`.

## Literature checked
- Hall/Ryser first multiplier theorem for difference sets; see standard multiplier-theorem statements and expositions.
- Qiu Weisheng, *On the Multiplier Conjecture*, Acta Math. Sinica 10 (1994), DOI 10.1007/BF02561547.
- K. Akiyama, C. Suetake, M. Tanaka, *Projective planes of order 12 do not have a collineation group of order 4*, J. Combin. Designs 31 (2023), DOI 10.1002/jcd.21869, for modern order-12 context.

## Conclusion
Relocate the complete package to the assigned failed path. Preserve it as a reproducible negative computation, but do not present it as an original validated finding.
