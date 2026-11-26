# Independent mathematical audit

## correctness

PASS

The recurrence and initial values give (a+1)J_n=a^n−(−1)^n. Since the image of a primitive root modulo p^r generates modulo p, it is neither zero nor −1 there for p≥5; thus a+1 is a unit. The even order T is a period, and any period d must return both J_0 and J_1. Those two congruences force a^d=(−1)^d=1 modulo p^r, hence T divides d. Over the least period the even and odd exponent branches run once through square and nonsquare units respectively. Unit squareness is determined by the reduction modulo p, so their translated, invertibly scaled images give exactly the two indicator terms, with zero character contributing neither branch. To count overlap set z=(a+1)y and omit z=±1. The sums of χ_p(z+1) and χ_p(z−1) there are −χ_p(2) and −χ_p(−2). The product sum is −1 by the bijection (z−v,z+v) with reciprocal pairs when z²−v²=1, and the omitted product terms vanish. The overlap is therefore (p−1−χ_p(2)+χ_p(−2))/4 at p, giving the stated mod-8 cases; each class contributes p^{r−1} lifts. Counting targets and occurrences proves the zero-, single- and double-fiber totals. A fresh recurrence-only run tested all 236 primitive roots for p² with p in {5,7,11,13,17}, all 50,732 targets, the histogram and the period state. These finite tests are corroboration, not the proof or coverage of other moduli.

## originality

PASS

The exact recurrence, its Binet expression, prior completeness criteria and the character-correlation component are not new. The supported distinct result is the residue-by-residue prime-power multiplicity law under the full generator hypothesis, together with its period normalization and parameter-independent histogram. None of the strongest inspected statements enumerates this sequence's two affine parity images and combines them into that distribution.

## value

PASS

Completeness of modular Jacobsthal sequences is an established question. In the important generator regime where completeness fails, a count of all targets by multiplicity, or whether a specified residue occurs zero, one or twice without iterating the period, is a substantially stronger exact invariant. Identifying the two translated cosets explains both where repetitions occur and why the prime-level distribution lifts without change in proportions. The value is the modular classification, not a new character sum or standalone Binet or period formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
