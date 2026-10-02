# Review status

Scientific audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **PASS**. An independent S9 conjugacy-class transition calculation reproduces H((6,2,1),(5,4);3)=324 and H((3,3,3),(5,4);3)=40. Peeling the last transposition from (5,4) gives exactly the five children (9), (4,4,1), (4,3,2), (5,3,1), (5,2,2) with transition multiplicities 20,5,5,4,2, and the independently recomputed two-step factors give contributions -135,-48,-40,-37,-24, summing to -284. The off-wall proper-subset-sum check justifies connected=disconnected for these endpoints.

Originality: **PASS**. Targeted Resultary and literature searches found the exact statement only in this record. Shadrin-Shapiro-Vainshtein prove the distinct neighboring-chamber wall-crossing formula, while Cavalieri-Johnson-Markwig develop the chamber structure; neither inspected source states this endpoint-specific five-term last-transposition identity or the numbers 324 and 40. The claim is therefore best-knowledge original as an explicit finite class-algebra computation, with residual risk from unindexed tables.

Scientific value: **FAIL**. The final claim is an arbitrary degree-9 numerical specialization of standard Frobenius/class-algebra and cut-and-join machinery. The selected endpoint partitions and two-wall segment are not shown to be extremal, minimal, a natural classification boundary, or needed for a motivated downstream question; the record itself disclaims the more substantive single-wall wall-crossing interpretation. Reproducibility and exactness alone do not supply the required mathematical motivation.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
