# Review of the periodic-prefix antidictionary theorem

## Correctness — PASS
The precise object is a finite prefix of a primitive periodic word over a declared alphabet, including unused letters. Two primitive rotations cannot share their first \(d-1\) letters, because equal-length rotations have the same Parikh vector; hence sufficiently long factors determine phase. This proves every periodic minimal absence has length at most \(d\). All periodic factors of length at most \(d-1\) occur by prefix length \(2d-2\). Case separation at lengths \(d\) and at least \(d+1\) shows the only nonperiodic-language absence of the prefix is the phase-\((d-1)\) boundary word. Its prefix and suffix are present while it is absent. The special period-one case follows directly. Two independent algorithms passed 11,747 and 4,567 finite tests; these checks corroborate but do not replace the symbolic proof.

## Originality — PASS (qualified)
The 2009 and 2014 literature develops the general minimal-absent-word problem and algorithms. The 2017/2018 circular-word result supplies the shorter, stable periodic part but not the finite-prefix endpoint equality. A closely related publicly indexed 2026 result settles a proper subclass (distinct-letter run periods with complete repetitions) and already contains the one-changing-endpoint phenomenon there. This directly limits the new contribution to arbitrary primitive roots and the sharp uniform bound for all sufficiently long prefixes, including incomplete repetitions. No indexed general theorem with this implication was found, but the ease of deriving it from established periodic language structure and inaccessible full text are residual priority risks.

## Value — PASS
The exact description applies uniformly to *every* primitive finite period and finite alphabet, not a handpicked finite census. It converts a potentially lengthy antidictionary of any sufficiently long periodic prefix into a fixed circular part and one changing endpoint obstruction, while giving the sharp universal cutoff \(2d-2\) (with a period-one convention). This is a structural classification relevant to antidictionary compression and repetitiveness: any repeated or partly repeated text can be represented by the same stable forbidden-pattern basis and one indexed long word. The assertion of value does not require claiming improved measured performance or a new general-purpose algorithm.

## Closest sources and residual limits
- Pinho et al. (2009), DOI 10.1186/1471-2105-10-137: definitions, repeat-context characterization; no identified all-prefix periodic stability theorem.
- Barton et al. (2014), DOI 10.1186/s12859-014-0388-9: general exact algorithm, no claimed single-moving-boundary classification.
- Fici, Restivo, Rizzo, arXiv:1707.04450, Lemma 2: circular antifactorial basis from a doubled word; the finite-endpoint statement and threshold require further argument.
- *The complete minimal-absent-factor spectrum of cyclic distinct-run powers* (public indexed result, 2026): direct special-case overlap; only its indexed summary was accessible, and possible wider claims in the full package remain a residual priority risk.
- The binary example `01101` at prefix length seven rules out a uniformly smaller threshold by one, but no claim is made that each individual period needs the stated cutoff.

Self-review: passed. Independent audit: not yet performed.
