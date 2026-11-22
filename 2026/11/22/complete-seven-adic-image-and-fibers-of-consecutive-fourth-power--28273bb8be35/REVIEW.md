# Scientific review: complete seven-adic fourth-power-sum image

## Correctness — PASS

The claim is an all-precision arithmetic classification, not a finite numerical pattern. The standard Faulhaber polynomial is exact, and its derivative \(F'(x)=x^2(x+1)^2-1/30\) gives four nonsingular residue branches, two simple critical branches and one exceptional non-simple derivative residue. On the regular branches, difference quotients have seven-adic unit leading terms. On the central branch, centering at \(-1/2\) gives an explicit scaled isometry onto \(49\mathbb Z_7\). On the other branches, Hensel lifting supplies a unique critical point and an analytic isometric Morse coordinate, giving the two translated-square images. These disjoint components yield every residue count, square-root fiber, Haar measure and least index period. The embedded independent-of-library checker passed 274,512 exact comparisons through modulus \(7^6\), but the infinite claim is proved by the displayed local identities and lifting argument, not by the checker.

## Originality — PASS, with historical-priority qualification

The most closely related accessible published work describes value-set inequalities over residue rings (Ralph 1995), finite-field value-set bounds (Mullen–Wan–Wang 2012), and fast lifting algorithms for monomial congruences (Mahmood–Ahmad 2014). A public pentatope polynomial result gives square-sheet images for a *different* polynomial, while a dyadic fourth/sixth-power and even-power sum literature concerns other maps or different quantifiers. The reviewed statements do not imply the exact seven-adic image or its central branch's additional seven preimages. The 1995 paper was available only in abstract, so an implicit stronger theorem in its complete text cannot be excluded; general local Morse theory is credited rather than claimed as new.

## Mathematical value — PASS

The prime seven is the smallest prime beyond the denominator primes of the classical consecutive fourth-power-sum formula. It is the first clean prime-power setting for the polynomial. Moreover, the centered identity \(F(x)=z^5/5-z^3/6+7z/240\) singles out seven among good primes; the derivative has both simple and repeated critical reductions; consequently the integer-sequence image is neither all units nor merely a union of full residue balls. The exact closure measure \(25/56\), complete all-depth residue count, and distinctive ninefold fibers inside \(49\mathbb Z_7\) describe specific natural representability invariants for this classical power-sum sequence. Their motivic content is a complete local-solubility classification rather than a small arbitrary calculation. No extension to other primes or global integer representations is asserted.

## Sources and limitations

Ralph (1995), DOI 10.1112/S0025579300011487, first published 1 June 1995; Mullen–Wan–Wang (2012), arXiv:1210.8119; Mahmood–Ahmad (2014), DOI 10.1155/2014/575064. The 1995 complete text was not available, and the historical-priority judgment remains qualified. All finite checker comparisons succeeded, but the work has not undergone independent external audit.

Self-review: passed. Independent audit: not yet performed.
