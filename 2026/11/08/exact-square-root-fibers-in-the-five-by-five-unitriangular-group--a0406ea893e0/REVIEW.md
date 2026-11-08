# Review of the five-by-five unitriangular square-root fiber theorem

## Correctness (PASS)

The characteristic-two identity \( (I+N)^2=I+N^2 \) gives six explicit output coordinates. The two necessary implications are independently shown sufficient by an exhaustive constructive division into \(v\ne0\), \(v=0,u\ne0\), \(v=0,w\ne0\), and \(u=v=w=0\). These constructions do not assume algebraic closure or a finite field. For finite fields the proof partitions input matrices according to the first-superdiagonal coordinates and solves the remaining linear and product equations. The target-root counts sum to \(q^{10}\), and a literal matrix-product implementation independently verifies all target fibers over \(\mathbb F_2\) and \(\mathbb F_4\). Finite enumeration is corroboration, not a proof of the general assertion.

## Originality (PASS, provisional)

Sosnovsky (arXiv:1201.6513, Theorem 1) determines verbal widths for triangular groups, rather than the pointwise square-image membership and prescribed-element root counts for \(\operatorname{UT}_5\). Bier (DOI 10.1142/S0218196712500191, Theorem 3 and arguments on power-word width) already proves the width-two threshold: it is excluded from the new claim. Dolfi--Singh--Yadav (arXiv:1905.04244, Proposition 3.4, Theorem A, Section 3 table) give group-theoretic estimates and previously published small-field square-image sizes 52 and 3376: these values are explicitly credited. Neither source inspected supplies the all-field six-coordinate criterion or the seven-stratum pointwise root-fiber formula for every binary field. Historical priority is provisional; an unidentified general word-map or character-theoretic formula may imply this specialization.

## Value (PASS)

The individual-square set, unlike the subgroup it generates, is a natural invariant of a finite unipotent group and its power word map. The exact criterion specifies which elements are powers, and the full fiber distribution measures the number of roots of each such element. The fact that two deep target coordinates produce different fiber sizes, even within one derived-subgroup layer, is meaningful information not determined by width or the known small-field cardinalities. The all-field membership criterion and uniform all-extension-field fiber theorem provide a reusable baseline for larger power-word images.

## Limitations

The theorem does not address larger matrix sizes, odd characteristic, or alternative power words. The finite checks cover two field sizes only. Originality has been compared with the cited primary texts and mathematical records, but independent historical and mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
