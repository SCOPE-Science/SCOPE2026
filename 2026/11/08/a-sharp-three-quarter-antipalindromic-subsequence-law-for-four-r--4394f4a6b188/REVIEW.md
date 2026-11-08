# Scientific review

## Correctness — PASS

The statement fixes four positive circular run lengths, uses one circular traversal, and separates the only possible two- and four-run antipalindromic output structures. The four two-run candidate bounds have explicit cut-and-skip constructions, and the two four-run candidates follow from outer/inner complement symmetry. The balanced simplification is an algebraic identity; the sharp minimum and equality cases follow from an elementary contradictory-inequality argument and explicit witnesses. The separately implemented dynamic verifier checks 625 positive run quadruples against all circular rotations and checks the closed-form balanced identities and finite extremal profiles. Residual correctness risk lies only in a potential unrecognized structural output configuration; the run-count proof rules this out in the stated domain.

## Originality — PASS, qualified

The most pertinent full primary text is Müllner and Ryzhikov (arXiv:1901.07502), which states the general balanced circular antipalindrome conjecture, reports a weaker general lower bound, and studies constructions involving many runs; its inspected Sections 1–5 do not assert this complete four-run optimization or sharp three-quarter extremal law. Earlier cyclic-LCS algorithms and later LCS-uniqueness work solve different general computational questions, rather than giving the present exact optimization and minimax statements. Actual searches examined the expressions 'four runs', 'four blocks', reverse complement, cyclic common subsequence, three-quarter bounds, and the guiding conjecture. Searches of related mathematical statements found no direct dominating statement. Failure to find a result is not a uniqueness guarantee; unpublished or unindexed equivalents remain possible.

## Mathematical value — PASS

The motivating question is the longstanding balanced circular antipalindromic-subsequence lower-bound problem. A restricted class with four runs is natural because it is the first nontrivial balanced class beyond two runs; the exact six-term formula also applies to unequal frequencies. The sharp three-quarter guarantee is stronger than the conjectural two-thirds benchmark within this class, and the equality classification identifies its precise obstruction. It does not purport to solve the general conjecture or to count embeddings.

## Closest literature and limitations

- Müllner–Ryzhikov (2019), arXiv:1901.07502, Sections 1–5: the primary relevant conjectural framework; no inspected four-run exact classification.
- Chowdhury–Hasan–Iqbal–Rahman (2009), arXiv:0911.5031: general cyclic-LCS algorithm; no identified sharp four-run antipalindrome formula.
- Wang (2023), arXiv:2301.03827: LCS uniqueness questions for comparisons of linear and circular sequences, a distinct objective and input model.

Residual risks: unindexed equivalent formulas and implicit treatment of the four-run class in an unrelated combinatorics-on-words study. All claims are restricted to four positive circular runs. Finite verification is not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
