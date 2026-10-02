# Scientific audit — 2026-10-01

## Final claim

Exact d=9 genus-0 double Hurwitz jump 324 to 40 with five-term cut/join decomposition

## Correctness — PASS

An independent S9 conjugacy-class transition calculation reproduces H((6,2,1),(5,4);3)=324 and H((3,3,3),(5,4);3)=40. Peeling the last transposition from (5,4) gives exactly the five children (9), (4,4,1), (4,3,2), (5,3,1), (5,2,2) with transition multiplicities 20,5,5,4,2, and the independently recomputed two-step factors give contributions -135,-48,-40,-37,-24, summing to -284. The off-wall proper-subset-sum check justifies connected=disconnected for these endpoints.

## Originality — PASS

Targeted Resultary and literature searches found the exact statement only in this record. Shadrin-Shapiro-Vainshtein prove the distinct neighboring-chamber wall-crossing formula, while Cavalieri-Johnson-Markwig develop the chamber structure; neither inspected source states this endpoint-specific five-term last-transposition identity or the numbers 324 and 40. The claim is therefore best-knowledge original as an explicit finite class-algebra computation, with residual risk from unindexed tables.

## Scientific value — FAIL

The final claim is an arbitrary degree-9 numerical specialization of standard Frobenius/class-algebra and cut-and-join machinery. The selected endpoint partitions and two-wall segment are not shown to be extremal, minimal, a natural classification boundary, or needed for a motivated downstream question; the record itself disclaims the more substantive single-wall wall-crossing interpretation. Reproducibility and exactness alone do not supply the required mathematical motivation.

## Sources inspected

- **S. Shadrin, M. Shapiro, A. Vainshtein, On double Hurwitz numbers in genus 0** (https://arxiv.org/abs/math/0611442): RELATED_NOT_EXACT_COVERAGE. The paper studies piecewise polynomiality and differences across a single resonance wall; the audited identity is explicitly a last-transposition decomposition across endpoints separated by two walls.
- **R. Cavalieri, P. Johnson, H. Markwig, Chamber Structure of Double Hurwitz Numbers** (https://arxiv.org/abs/1003.1805): BROADER_FRAMEWORK. It develops the chamber framework, not the exact degree-9 endpoint computation.

## Residual risks

- An unindexed finite Hurwitz table could contain the same numbers.
- The value failure is intrinsic to the selected specialization, not a correctness defect.

## Disposition

**failed** — at least one required scientific axis does not pass. The original scientific files are preserved unchanged as evidence.
