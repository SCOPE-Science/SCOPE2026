# Mathematical review

## Correctness

**PASS.** The two exact prefix–suffix tests account for all possible starts, including zero gaps and periodic words. The four-gap indicator identity is checked algebraically against a finite exhaustive partition of all 75 weak orders, each carrying an exact unrestricted integer generating function. The exact numerator calculations yield the claimed four rational series; an independent direct word-level program tests all length-\(n\) binary weight-four words for \(4\le n\le20\). The infinite theorem follows from the border classification and a finite covering identity, not merely observed coefficients. Risk: code is useful as a reproducible integer certificate, but implementation review is still part of the self-review.

## Originality

**PASS, qualified.** Harju–Nowotka (2004) studies general border correlations; Holub–Müller (2015) characterizes binary words with exactly two unbordered conjugates; OEIS A321162 tabulates the unrestricted maximum. Each addresses a different or partially overlapping assertion. The present theorem classifies every fixed-four-one fiber and gives the exact joint generating series, including the three- and four-conjugate families and a nonlocal opposite-gap law. Related fixed-three-one results do not cover the four-one enumeration. Searches for fixed weight-four unbordered conjugates, gap formulas, and exact enumerators located no statement proving this full theorem. Residual risk: historical or unindexed source containing the same census, especially an enumeration derivable from the existing exactly-two classification.

## Value

**PASS.** Binary border correlation is a standard periodic word invariant; fixed four-one composition is the next natural case after the known three-one local-gap phenomenon. The exact distinction between local and nonlocal gap conditions is structural, and the simultaneous all-length enumeration of every fiber supplies a motivated benchmark beyond a finite table. The result also quantifies typical four-rotation behavior with explicit exceptional families. No broader arbitrary-weight theorem is claimed.

## Verification limits

Two standalone standard-library implementations accompany the proof. Tests are not a substitute for mathematical reasoning. Literary priority and an independent proof audit remain open.

Self-review: passed. Independent audit: not yet performed.
