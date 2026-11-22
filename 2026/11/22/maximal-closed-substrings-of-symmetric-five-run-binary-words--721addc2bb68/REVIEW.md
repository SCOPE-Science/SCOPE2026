# Scientific review: maximal closed substrings of symmetric five-run binary words

## Correctness — PASS
The complete endpoint classification follows from the first-next-occurrence/longest-common-extension criterion, with four exhaustive same-letter cross-run pairs and intra-run cases. The equality boundary \(c=a\), each singleton-run case, and both \(c<a\) and \(c>a\) regimes are covered. The rational generating function and exact maximal fixed-length count follow algebraically. Direct-border checks verified 216 triples and 2,886 MCS intervals; a separately specified LCE/nearest-next implementation verified 5,832 triples and 171,774 intervals. These bounded tests do not replace the universal proof.

## Originality — PASS, subject to documented priority risk
The closest prior symbolic classification is for four-run MCS occurrences (public record dated November 8, 2026), which has no first-to-fifth-run spanning family. A five-run closed-factor enumeration (public record dated October 25, 2026) counts distinct closed values, not nonextendable occurrences. Full text of Umezaki et al.'s 2026 RLE enumeration paper and Fischer--Köppl's 2026 MCS enumeration paper was inspected, along with Faro et al.'s internal-query paper. They supply important general machinery but do not state the evaluated symmetric five-run formula, rational distribution, or fixed-length maximum. The general algorithms can compute individual cases; this is not asserted as novel. Earlier unindexed exact specializations remain a historical-priority risk.

## Value — PASS
This natural palindromically symmetric five-run class has two neighboring repeated-zero configurations plus a nontrivial long spanning border family whose size changes at the precise center-run threshold. The complete all-length endpoint formula, distributional generating function, and sharp maximum supply a reusable quantitative invariant for repetitive string instances, without claiming a general algorithmic complexity improvement.

## Limitations
Only linear binary words with five runs of lengths \(a,b,c,b,a\) are covered, and the invariant counts positional MCS occurrences. There is no independent mathematical audit or claim concerning arbitrary five-run words.

Self-review: passed. Independent audit: not yet performed.
