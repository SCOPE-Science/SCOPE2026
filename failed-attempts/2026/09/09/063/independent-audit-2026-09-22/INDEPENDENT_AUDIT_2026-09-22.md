# Independent audit — 2026/09/09/063

## Correctness — FAIL for the research claim as a whole; numerical Selmer entries PASS

I independently rebuilt the odd Monsky matrices from the Legendre symbols and verified their F2 ranks 4 and 2, yielding 2-Selmer dimensions 2 at 51 and 4 at 219 under Das–Mondal's open formula (3.3). Exhaustive integer enumeration of 2x²+y²+8z²=n and 2x²+y²+32z²=n gave (A,B)=(24,16) and (48,24), respectively. Those numerical calculations are sound.

The record's material claim that the rank/Sha allocation at 219 is “open” is false in the relevant prior data: Noam Elkies's original OEIS rank-2 sequence A062695 lists 219, with source references to preexisting congruent-number tables. Independently, (x,y)=(507,10296) lies on y²=x³−219²x and is non-torsion (y≠0), so the rank-zero alternative in the record is already excluded even without that table. Given the established rank 2 and verified Selmer rank 2, Sha[2] has dimension 0. This contradicts the claimed unresolved rank-zero/visible-Sha allocation. No new Sha visibility follows.

## Originality — FAIL

The specific 219 rank-2 entry predates this record in Elkies's data, and the two Selmer dimensions are immediate four-by-four instances of Monsky's established matrix. A two-point +2 difference with no family or rank/Sha novelty is not an original research result. The accepted target's (3,5) dimensions were already impossible for a full-rational-2-torsion curve whose Selmer dimensions have the Monsky parity in this pair.

## Scientific value — FAIL as a research record

The corrected Selmer arithmetic is useful for detecting an erroneous target, but the unresolved-looking 219 arithmetic is already resolved and no new generalization, visible Sha class, or analytical certificate is provided. The exact computations belong as reproducibility examples, not an accepted frontier result.

## Sources

- Original RESULT.md and METADATA.json; independent F2 elimination, Tunnell enumeration and point substitution above.
- Das–Mondal, Section 3, https://arxiv.org/html/2604.26183v1 .
- Noam D. Elkies, original sequence A062695 (219 listed among rank-2 congruent-number twists), https://oeis.org/A062695 .
