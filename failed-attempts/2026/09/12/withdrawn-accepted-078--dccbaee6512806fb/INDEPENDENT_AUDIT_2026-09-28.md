# Independent Audit — 2026/09/12/078

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e35a98c7f0cecf143e5ff536e84937c33eae536f`
- Disposition: **FAILED**

## Correctness

**FAIL** — The package internally distinguishes D4-orbits of normalized Montesinos presentations from actual knot isotopy classes, but the headline collapses those notions. RESULT.md calls 1900, 5304, and 14022 D4-orbit representatives 'distinct knots' and then forms 225,260,925 'distinct pairs'. Its own Limitations section explicitly concedes residual duplication beyond D4 (including flypes or other tangle identities) that can merge these orbits. Therefore 21,226 is not established as an exact number of distinct knot types, and the 225,260,925 pair count is not established as a count of distinct knot pairs. Even accepting the record's separate at-most-eight presentation-fiber assertion, the directly justified lower bound from the ordered-tuple counts is 19,587 knots and 191,815,491 pairs, not the headline exact knot count.

## Originality

**FAIL** — Complete prime-knot tables through 19 crossings already exist, including the full alternating populations at 17 and 18 crossings. A new subfamily census would need a certified map from the enumerated Montesinos presentations to standard knot isotopy classes, with duplicates resolved. The submitted D4 presentation-orbit statistic does not supply that identification, so it does not establish the advertised original knot census.

## Scientific value

**PASS** — The ordered-presentation enumeration and its conservative lower-bound scale estimate are potentially useful for planning a commensurability computation. The scientific value survives only after downgrading the output from an exact knot census to a presentation census/lower bound; the current headline remains invalid.

## Sources

- Regina — Supporting Data: Classical knot tables: https://regina-normal.github.io/data.html — Provides tables of all prime non-trivial knots through 19 crossings, giving an external reference universe for any claimed 16–18 crossing knot census.
- Enumerating the Prime Alternating Knots, Part II: https://doi.org/10.1142/S0218216504003056 — Reports enumeration of prime alternating knots through 19 crossings, including 17- and 18-crossing populations.

## Limitations

- The submitted enumeration scripts were not rerun in this execution; the decisive failure follows from the record's own theorem/limitations mismatch and does not depend on disputing its raw ordered-tuple counts.
- The 19,587-knot lower bound quoted above is conditional on the record's stated at-most-eight presentation-fiber bound; this audit did not independently reprove that classification bound.

GitHub was read only as evidence. No GitHub mutation, dispatcher completion call, or separate publication/report action was performed by this audit chat.
