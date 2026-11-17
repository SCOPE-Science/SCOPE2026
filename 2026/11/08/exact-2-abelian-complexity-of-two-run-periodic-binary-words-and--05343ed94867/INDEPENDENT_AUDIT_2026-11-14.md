# Independent mathematical audit

## correctness

PASS

For each fixed cyclic starting phase, adding full period L translates counts of symbols and adjacent digrams by a constant independent of the phase, so p2(n+L)=p2(n). A length r<=L factor crosses at most two run transitions. Monochrome classes yield [r<=a]+[r<=b]; one-transition orientations with x in [max(1,r-b),min(a,r-1)] each yield T(r) distinct classes; two-transition factors yield exactly one class per middle-run orientation when r>=b+2 or r>=a+2. Letter/digram counts determine first and last letters, proving disjointness. Summing yields boxed profile; max L cap vs 2min(a,b)+2 and gap-two phase threshold follow. Independently reproduced 7875 signatures for a,b<=15 across lengths 1..2L+3, matching peak and threshold. Finite checks are not proof of arbitrary parameters.

## originality

PASS

PASS best of knowledge: foundational 2-Abelian complexity papers and 2-automatic examples do not supply the complete two-run periodic parameter profile or phase-information threshold. Prior complete multispectrum counts over all binary words and cyclic inverse-necktie k-decks address different sets of observed objects; they do not imply factor-restricted phase counts.

## value

PASS

PASS: Exact two-parameter infinite family of a standard word-combinatorics invariant, with a sharp information-loss threshold |a-b|=2. The saturation at 2min(a,b)+2 is a structural classification of local digram-statistic identifiability, rather than an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
