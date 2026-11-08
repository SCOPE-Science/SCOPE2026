# Mathematical review: golden-mean first-order limit spectrum

## Correctness

**PASS.** The finite ensemble is specified without ambiguity: equally weighted length-\(n\) binary words avoiding \(11\), interpreted in \(\mathrm{FO}[<,P]\). The Fibonacci completion ratios produce the exact one-sided limiting Markov law and independent geometric zero-runs following successive \(1\)'s. The marker code uses a unique initial gap \(k+1\) and a permutation of \(1,\ldots,k\); consequently distinct candidate patterns have equal positive probability and cannot overlap, proving uniformity of the first successful label. Every such finite-pattern/earliest-occurrence test is definable by one fixed first-order sentence. The rational mixtures of two prefix-end classes are exact Fibonacci identities, with conditional rational probabilities tending to the desired interior field value.

For the upper bound, the aperiodic syntactic monoid and the primitive no-\(11\) base automaton imply that each component with maximal Perron root is closed under all legal transitions and contains a one-cycle. Dominant components cannot occur sequentially. Rational generating-function residues therefore give a convergent first-order probability in \(\mathbb Q(\sqrt5)\). The checker exhaustively validates several finite consequences; the proof, not the finite data, establishes the infinite statements.

## Originality

**PASS relative to compared literature and indexed claims.** Markström–Räty (arXiv:2610.22218, 2026-10-15) supplies an automata and first-order framework, including a relevant spectral-radius lemma, but its stated limit law concerns small permutation classes and does not classify the uniform no-adjacent-ones word ensemble. Falgas-Ravry–Markström–Räty–Skerman (arXiv:2610.34328, 2026-10-25) establishes a dense spectrum for exponentially growing small permutation classes, not an exact quadratic-field spectrum for these words. Sin'ya (arXiv:1505.03343) treats zero-one densities of ordinary regular languages, rather than all probabilities under Fibonacci conditioning. A related calculation for unrestricted binary word models yields a rational spectrum on a different probability space, so it does not imply the irrational values here. No matching exact golden-mean FO spectrum was found in the searches described in the accompanying structured review.

Residual risk is that a wider published theorem on aperiodic-language densities under primitive Markov sources may already imply the result, even if the source-specific statement is not indexed. These searches and comparisons do not establish absolute historical priority.

## Value

**PASS.** The golden-mean language is a canonical mixing regular constraint, and exact limiting-probability spectra measure the expressive power of first-order logic on a natural random-structure ensemble. The result replaces qualitative convergence or density by the complete arithmetic classification \(\mathbb Q(\sqrt5)\cap[0,1]\); notably, local forbidden factors allow irrational first-order limiting probabilities, whereas unrestricted fair binary words yield rational ones. The fair-renewal selector offers a reusable mechanism for constructing exact values without arithmetic predicates.

## Scope and limitations

The proof covers ordinary first-order sentences only, fixed formula independent of length, and uniform selection from no-\(11\) words. It makes no assertion about all regular or monadic second-order properties or arbitrary finite-state sources. The marker selection is asymptotic, not guaranteed to terminate at finite length. The independent audit status below refers to independent scientific assessment, not to reproducibility of the finite tests.

Self-review: passed. Independent audit: not yet performed.
