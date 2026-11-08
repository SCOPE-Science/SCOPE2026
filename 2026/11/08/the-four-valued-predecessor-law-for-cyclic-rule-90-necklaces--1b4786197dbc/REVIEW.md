# Self-review

## Correctness — PASS
The result is an exact theorem for every positive ring length and every binary output necklace. Rank-nullity supplies the labeled fiber conditions, the rotation stabilizer gives an exact Burnside orbit count, and elementary divisor-sum identities evaluate every case. The arguments include length one and two and explicitly distinguish labeled and rotation-class fibers. Independent-of-formula enumeration over all 8,923 output necklaces of lengths one through sixteen and five witnesses matched. Tests are finite support, not an infinite proof.

## Originality — PASS, qualified
The closest source on the same quotient, Frati–Petak–Cheney (2024), visualizes necklace networks and Rule 90 examples but provides no all-length local indegree formula in terms of primitive period and parity. Martin–Odlyzko–Wolfram (1984) and Powley–Stepney (2009) give indexed state transition information, including uniform nonzero labeled fiber counts; these do not themselves distinguish the possible numbers of **rotation classes** above a particular output. Malcolm Black's adjacent-XOR necklace exposition is a stronger relevant route because its square is Rule 90 up to rotation, but its stated one-step and branching descriptions do not supply the explicit classification. The statement is not a mere change of notation from a labeled-fiber theorem. A historical-priority caveat remains for the Ducci-map literature and potentially overlooked formulas.

## Value — PASS
The necklace-network interpretation of elementary cellular automata explicitly motivates describing incoming edges. The theorem gives the complete exact local in-degree function for a standard map, including sharp gradations from one through four, identified by primitive-period arithmetic. It demonstrates precisely how rotation symmetries alter uniform labeled multiplicity; the result is useful for inverse-search and coarse-grained state graphs without requiring any downstream application theorem.

## Scope and limits
Only one synchronous Rule 90 update on binary rings is proved, identifying rotations but not reflections. The four-valued positive spectrum is conditional on ring size; the theorem itself covers all lengths. Historical priority is provisional; no independent audit has been completed.

Self-review: passed. Independent audit: not yet performed.
