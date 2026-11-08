# Self-review

**Correctness — PASS.** The proof parameterizes every two-state bireversible transducer by a switch-coloring and two compatible output permutations; the two Burnside fixed-point counts are independently derived. The decisive even-cycle step comes from how a cycle of even length splits under squaring. Direct machine/orbit enumeration through four letters agrees exactly with the general formula, and integer-arithmetic calculations through nine letters agree with the listed initial values. Finite tests do not prove the unlimited formula; the Burnside argument does.

**Originality — PASS under accessible comparisons.** Woryna (2017) gives a partition compatibility identity for two-state bireversible transducers but not a cycle-index count of isomorphism types. Godin (2019), Proposition 3.2, bounds a probability and does not compute the orbit spectrum. Curtin--Savchuk (2026) develops a broader combinatorial/isotopy framework, but its full text could not be inspected; the available abstract and detailed overview do not state these standard-isomorphism orbit numbers. published-finding corpus searches of bireversibility, isomorphism, Burnside enumeration and cycle polynomial variants revealed no matching exact result. Absence from the search is not a uniqueness proof, and coverage implicit in the inaccessible 2026 full text remains the principal historical-priority risk.

**Value — PASS.** Classifying all machines up to the natural symmetries, rather than merely counting labeled transition tables, is a substantive combinatorial invariant of the two-state transducer family. The second Burnside term is sensitive to the odd/even cycle splitting and gives a uniform all-alphabet enumeration rather than a tiny finite census. It clarifies the distinction between ordinary Mealy isomorphism and the broader Latin-style isotopy relations.

**Independent-validation limit.** The proof and checker have not been validated independently; they provide a reproducible self-review.

Self-review: passed. Independent audit: not yet performed.
