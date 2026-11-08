# Scientific review

## Correctness — PASS

The exact scope is nonempty binary words with pairwise distinct complete zero-gap lengths; the theorem covers zero, one, two, three, four, and at least five occurrences of the marked symbol. Every permissible symmetric period is accounted for by its border. Distinct complete gaps exclude borders with two marked symbols. A zero-only border changes only the closing circular gap, through the exact closed integer interval bounded by the two external zero-runs. A one-marker border exists only for the explicit prefix/suffix inequalities and leaves all circular gaps of the shorter period distinct. The dihedral symmetry analysis is exhaustive for three and four markers, and impossible with five or more. The literal-definition checker matched all 19,530 admissible words through length 18 and 600 randomized examples. No finite test is used as an infinite proof.

## Originality — PASS, qualified

The source most directly supplying definitions and the symmetric-word-period lemma is Fici, Shallit, and Simpson (arXiv:2407.10564, materially read as full arXiv text and full 2025 HTML), which discusses Sturmian, trapezoidal, automatic, and extremal-count questions, not pairwise unequal zero-gap boundary conditions. Simpson (arXiv:2402.05381, materially read) studies palindrome-center constructions and multiple periods, not this finite gap-spectrum classification. Borchert and Rampersad (arXiv:1509.05396, materially read) analyze two-palindrome products, rich families, and minimal non-pairs, not a complete criterion for *symmetric word-periods* in gap-distinct words. The closest accessible previous finite-gap findings address closed factors, Lie complexity, minimal absence, and circular BWT, which use different predicates and do not imply the present test. Relevant search variants for gap-distinct, run-length, circular reflection, and palindrome-periodic factors returned no precise coverage. This does not exclude unknown or unindexed sources.

## Mathematical value — PASS

The theorem replaces a general search over all periods and palindrome splits with an exact constant-size arithmetic test on the boundary gaps once the natural distinct-gap condition is verified. Its sharp four-marker ceiling is structural and holds for *arbitrarily ordered*, not just increasing, internal gaps. It separates one-marker overlap periods from zero-only overlap periods, which is essential: retaining only the symmetric whole-word case would miss some three-marker examples. It is a complete nontrivial classification of a natural subclass of a recently studied invariant, not a routine finite tabulation.

## Risks and limitations

Novelty is qualified by incomplete indexing of all earlier literature; the classification is not proposed as a general theorem for repeated gaps. The counted checks have a finite word-length cutoff. No independent expert evaluation has been performed.

Self-review: passed. Independent audit: not yet performed.
