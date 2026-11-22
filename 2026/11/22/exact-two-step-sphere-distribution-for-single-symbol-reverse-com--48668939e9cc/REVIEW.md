# Self-review

## Correctness — PASS

The three canonical expansion families comprise all exact-two duplication histories. A left-to-right two-marker alignment identifies exactly two generating collision moves, which form an acyclic edge graph and contribute the total length of the complement-following runs. The rational distribution follows from unique constant-run factorization. The standalone `verify.py` independently tests two-step evolution, canonical expansions, collision classes, and polynomial coefficients on 35,268 sources for three alphabet sizes. The finite tests are corroboration, not the proof for all lengths.

## Originality — PASS

The model and broad capacity questions appear in Ben-Tolila–Schwartz (2021), Yohananov–Schwartz (2025), and Zabokritskiy (2026). The closest result, the indexed sharp all-odd-length two-step sphere **maximum**, covers the extremal value at duplication length one; it does not count the sphere of an arbitrary input or the full loss polynomial. The full-text sections on definitions, exact-one constructions and capacity in the first two articles, and the even-length two-error geometry in the third, do not furnish the claimed exact all-word, all-length spectrum. Semantic searches for a first-run/weighted-run distribution, aliases, sphere geometry and rational generating functions did not disclose the same theorem. The unresolved possibility of an unindexed equivalent in other literature is noted; failed searches alone are not used as proof of uniqueness.

## Value — PASS

The exact-two ambiguity under reverse-complement copying is a natural invariant for DNA-type duplication channels. The result gives a word-by-word, linear-time sphere-size formula, every possible value, and a complete enumerator for every alphabet size and length. In the four-letter length-six case it separates six distinct ambiguity classes and their population counts. Those data support finite-length sphere-packing and workload analysis where knowing only the previously established worst case is insufficient; no optimal code-size theorem is claimed.

## Limitations

The theorem concerns fixed-point-free complementation and exactly two single-letter copying errors. It does not analyze intersections between different sources, larger duplication windows, or optimal error-correcting codes. It is unconfirmed by independent review, and historical priority beyond examined literature remains uncertain.

Self-review: passed. Independent audit: not yet performed.
