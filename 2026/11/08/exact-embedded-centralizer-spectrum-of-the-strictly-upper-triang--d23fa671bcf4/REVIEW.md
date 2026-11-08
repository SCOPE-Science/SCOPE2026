# Scientific review of the embedded-centralizer spectrum

## Correctness

PASS. The associative commutator calculation reduces equality of element centralizers to equality of three-row linear subspaces in a fixed five-dimensional coordinate space. Four exhaustive parameter cases give canonical representatives or projective lines, prove uniqueness and disjointness of the rowspaces, and count every fiber. The algebra-group corollary follows exactly from the identity \((1+X)(1+Y)=(1+Y)(1+X)\iff XY=YX\). The direct finite-field enumeration in `verify.py` independently reconstructs matrix products and agrees for five fields, including a nonprime field. The infinite statement rests on the proof, not on the enumeration.

## Originality

PASS relative to the inspected sources and accessible records, with provisional publication priority. Dutta–Basnet–Nath count ring centralizers in other small-number cases, not this six-dimensional algebra. Kundu–Naik–Singh's two-breadth hypothesis excludes the present four-breadth spectrum. Majeed–Ramkumar's 2026 work on \(UT_4(p)\) explicitly provides the commutation equations and the *orders* of element centralizers; these are not claimed as new. Its clique analysis also supplies partial relevant structure (notably a count of certain large cliques). It does not state the complete **number of distinct embedded centralizer subgroups** or the equality/fiber classification, and its setting is prime rather than general prime-power fields. Anil Kumar–Prajapati already count equality classes on a substantial subset in the same UT4 group (Lemma 22), and provide a partial regular-superdiagonal count; only the complete whole-group equality-and-fiber classification is claimed here. Bhunia's centralizer conjugacy equivalence is coarser than equality of embedded subgroups and assumes a different group/field setting. No directly covering statement was identified in the inspected literature, but absence of a search hit does not prove novelty.

## Mathematical value

PASS. Distinct centralizer number is a natural invariant of finite noncommutative rings and algebra groups. Centralizer-size distributions alone cannot distinguish kernels or calculate this invariant. The result supplies the full count and a fine equality classification, exposing a unique atypical codimension-two centralizer with a substantially larger fiber; it works in all finite characteristics and yields a matched group-theoretic count. This is a complete invariant calculation for a canonical nilpotent matrix algebra, not merely a small isolated numeric table.

## Closest literature and limitations

A 2015 same-group paper (Anil Kumar–Prajapati) already defines equality of centralizers and counts the \(q^2(q-1)\) classes on its \(N_2\) subset, and a 2026 group-graph study already describes the possible centralizer *orders* and basic commuting equations, so originality is restricted to **equality classification, distinct counts, fibers, and prime-power uniformity**. The theorem does not classify larger upper-unitriangular groups or centralizers up to conjugacy. Independent audit and worldwide priority verification are outstanding.

Self-review: passed. Independent audit: not yet performed.
