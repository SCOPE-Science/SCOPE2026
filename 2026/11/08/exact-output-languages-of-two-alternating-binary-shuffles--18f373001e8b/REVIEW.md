# Scientific review: alternating-source shuffle output languages

## Correctness (C): PASS

The source-prefix excess gives the necessary height conditions. The converse for equal-phase inputs is a constructive two-stream allocation with completed-pair counts differing by at most one; for opposite-phase inputs the two synchronization states and independent boundary bits prove that every allowed two-letter block string is realizable by exactly balanced sources. Even-boundary encoding yields the two exact counts; the height conditions force the intersection singleton. The independent exhaustive mask generator in `checker.py` agrees with both characterizations for each integer parameter from one through five. Finite checks alone do not establish the infinite claim; the constructions do.

## Originality (O): PASS within available evidence

The recent insertion-degree source by Ma, Zhang and Hughes (arXiv:2610.39941v1, October 29, 2026) studies masks, exchanges, and insertion degrees, not distinct-output language characterization for the two periodic source pairs. Grytczuk, Pawlik and Ruciński (arXiv:2503.22043) consider general binary shuffle-square recognition, which is not a prescribed alternating-root output count; their constrained-run criteria do not imply the opposite-phase classification or the singleton intersection. OEIS A191755 tabulates the count of all binary shuffle squares at each length, and A331850 the maximum count across all possible roots, not the specific roots here. Search comparisons for exact formulas, bounded-height/ballot equivalences, shuffle products, and the opposite-phase pair-block language did not identify a published identical or stronger statement. A possible implicit classical shuffle-product derivation remains; the text of Datko and Pawlik's relevant 2025 article could not be fetched in full due to HTTP 429, though indexed passages were considered. Lack of a matching search hit alone is not a proof of priority.

## Value (V): PASS

The exact output languages and their overlap resolve a natural, tightly parameterized ambiguity problem for periodic shuffles, not merely the numbers of masks. The two source pairs have identical length and letter multiplicities, yet an opposite phase doubles the distinct-output count; the output families meet in exactly one word. This gives a complete infinite classification with a constructive membership witness and a transparent connection between source-phase synchronization and constrained lattice paths. The exact fixed-root counts and contrast are not supplied by the compared general shuffle-square counting tables.

## Limits and review status

Historical priority remains subject to further checks, particularly in older shuffle-product and automata literature. This review is not independent mathematical validation. The theorem says nothing about arbitrary roots, source multiplicities, or mask multiplicity.

Self-review: passed. Independent audit: not yet performed.
