# Review of the exact successive-run law

## Correctness

**PASS.** The four-symbol two-uniform substitution is established for the indexed Rudin–Shapiro word. Its primitivity yields all finite factor frequencies. The eight hidden length-two frequencies each equal \(1/8\), and the explicit even/odd-start recurrence determines every relevant factor frequency rationally. Reproducing all thirty-two run-pair frequencies through length ten verifies the entire displayed matrix, including zero entries, while five-equal-sign patterns are absent. The run normalization and exact entropy calculation then follow algebraically. A separately constructed prefix is checked against the binary-digit definition. The infinite proof does not depend on extrapolating from that finite prefix.

## Originality

**PASS, qualified.** The closest material is OEIS A203531, which records the full run-length sequence, and Hendel (2025), Section 8, on maximal run lengths and selected locations. Schaeffer–Shallit (2015) provides the substitution and other finite-factor classifications; Lü–Chen–Wen–Wu (2016) treats abelian factor complexity. The inspected texts and the available published-research comparisons do not explicitly evaluate the sign-resolved adjacent-run matrix, the nine allowed transitions, or the derived mutual information. A prior equivalent computation in unindexed run-length literature remains a risk; a failure to locate it is not proof of historical uniqueness. The published substitution is credited as a fundamental prerequisite, not claimed as new.

## Value

**PASS.** The run-length encoding of a classical low-autocorrelation automatic sequence is a natural observable. A full joint transition law, rather than merely a maximum run length or examples, identifies exact forbidden transitions, asymmetries such as forced length-one successors of length-two runs, and an information-theoretic dependence of \(\frac18+\frac{3}{16}\log_2 3\) bits. This dependence persists even though adjacent signs themselves have uniform independent pair frequencies. It is a reusable exact local structural statistic, not an arbitrary parameter slice or isolated numerical experiment.

## Limitations

This concerns adjacent, complete runs and limiting frequencies only. It does not assert that the run sequence is Markov, nor claim an independent or external audit. Historical priority remains qualified as explained above.

Self-review: passed. Independent audit: not yet performed.
