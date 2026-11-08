# Scientific review: a sharp eight-cycle threshold on wheels

## Correctness

PASS. The update identities reduce the rim map to alternating Boolean OR and AND operations controlled by one hub bit. The explicit all-even witness has a cyclic interval of \(n/2-4\) ones and a verified eight-step expansion/contraction history, returning at time eight with a different hub at time four. All interval size bounds are checked for \(n\ge12\). For odd rim sizes, the hub becomes a strict anti-threshold updater; Theorem 10 of Haslegrave–Cannings applies to the simple loopless graph and forbids period eight. The only remaining even sizes, \(4,6,8,10\), are exhaustively excluded by two independently implemented transition checkers. Both complete algorithms count \(288\) primitive-eight configurations at the first possible size \(n=12\). Reproducible code and outputs are provided, not merely reported checksums.

## Originality

PASS under the accessible-literature comparison, with explicit priority uncertainty. Haslegrave–Cannings (2016), read in its first-version full text, proves period restrictions for a strict anti-threshold nonconformist but not the inertial tie-retaining hub: at even rim sizes the latter rule depends on the hub's previous opinion at a tie. Its permissive results for more general rules on other graphs do not supply a wheel-specific sharp existence threshold or the first-size census. Cannings (2009) considers majority/minority behavior on complete graphs, hypercubes and selected cubic graphs in the accessible abstract; its full text was not reviewed. Goles–Olivos (1980) is relevant to homogeneous threshold periodicity but does not imply this mixed-rule result from its accessible abstract. Searches for equivalent wheel/contrarian/tie variants and indexed results found no demonstrated covering implication. An unindexed or inaccessible equivalent remains possible.

## Value

PASS. The condition \(n\in2\mathbb Z\), \(n\ge12\) identifies a sharp qualitative change in possible primitive periods caused solely by the interaction of a minority hub and inertial ties. It refines a natural boundary of an established nonconformist-period theorem, provides explicit period-eight waves on an infinite family of simple loopless graphs, and gives the nontrivial first admissible finite population and orbit count. This is structural periodic behavior, not a parameter rename or an isolated experimental example.

## Limits and verification

The result is not a complete recurrent-state census at every wheel length; no general eight-cycle count is asserted. Earlier source access is imperfect and publication priority is not certified. Enumeration is exhaustive for the stated small cases but cannot substitute for the infinite construction or the odd-case theorem.

Self-review: passed. Independent audit: not yet performed.
