# Scientific review: two-block type spectra in the dense local order

## Correctness — PASS

The source circular representation, proved by Brouwer, is used only for its precisely stated bijection between labelled locally transitive tournaments and cyclic antipodal orders. The formula's proof fixes the old block, places the first new vertex into one of its \(2n\) gaps, and represents all remaining new vertices by one weak composition across the \(n+1\) gaps before its antipode. Each named cross arc receives the correct integer exponent. Palindromicity follows from a half-turn of the new block; the total follows from stars and bars. The finite first-failure classification uses exact integer arithmetic, independently cross-checked by enumerating **every** cross orientation for every positive \((n,r)\) with \(n+r\le8\). Both implementations agree coefficient by coefficient for all 28 ordered pairs. The independent graph-orientation check explicitly rejects precisely those orientations containing a directed triangle in a vertex's in- or out-neighborhood. The checks completed with `VERIFY_OK`. Finite checks do not replace the infinite symbolic proof.

## Originality — PASS (provisional historical comparison)

The unary specialization \(r=1\) agrees with the existing one-point score polynomial and is not counted as new. Brouwer's 1980 report contains the general antipodal representation and a census of unlabelled tournaments, whereas the retained result is the finite-base **labelled two-block type polynomial**, a coefficientwise weighted enumeration with a sharp unimodality threshold. Babai–Cameron (2000) gives switching-class enumeration and local-order characterizations, not this cross-block polynomial. Coregliano's 2015 preprint studies asymptotic tournament sequences, not the finite coefficient spectrum. A separately reported result concerning feasibility of cyclic triangles among *three unary* types and a published six-point unary score reconstruction result do not imply the new weighted ordered-block result; the distinction between existence of a profile and counts by \(k\) cross edges is essential. An equivalent hidden coefficient enumeration remains a plausible priority risk, and the review does not certify global novelty.

## Mathematical value — PASS

The cross-arc count is an intrinsic finite-base extension statistic, rather than a combinatorially arbitrary parameter. The all-order formula controls every coefficient for all positive block sizes and thus gives a reusable calculation of multi-point logical type spectra. Its sharp first nonunimodality at a total of eight individually named vertices demonstrates a genuine information-distribution feature invisible from the unweighted total and from the one-point spectrum. This is more than a routine relabeling of the prior unlabelled count.

## Limits and closest literature

The result treats only two prescribed transitive blocks and does not classify higher-arity extensions with an arbitrary induced new block. The unimodality cutoff is proved through total order eight only, with no global classification beyond. Originality comparisons relied on full relevant sections of Brouwer (1980), Babai–Cameron (2000), and Coregliano (2015); indexed summaries did not always supply the full paper text. See the structured source comparisons for residual risks. Independent mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
