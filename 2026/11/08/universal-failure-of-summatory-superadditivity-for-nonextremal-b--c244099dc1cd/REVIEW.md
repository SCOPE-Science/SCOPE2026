# Self-review

**Correctness — PASS.** Every potential digit-window occurrence lies in an explicitly defined integer interval. Counting these interval elements at the three given cutoffs gives \(1\), \(4\), and \(4\) exactly for every \(h\ge3\) and every strict interior \(v\). The bounds on \(v\) justify all exclusions, so this is an infinite proof, not a finite extrapolation. The independent string and bit-window implementations agree through length \(10\).

**Originality — PASS in inspected evidence.** Sobolewski–Spiegelhofer's 2023 work gives shifted binary-block count distributions, rather than summatory Graham inequalities. Allouche–Stipulanti explicitly ask about inequalities for other blocks. The later all-words Gaussian theorem also concerns distributions, not the exact finite inequality. A reported positive superadditivity result for all-one blocks is disjoint from the present strict-interior family. Targeted mathematical searches and the inspected published sources showed no implication covering the new statement. There remains a risk from unindexed equivalent work; the all-one result was available only through an indexed scientific summary.

**Mathematical value — PASS.** This supplies a uniform explicit obstruction in a published direction, excluding all but two candidate leading-one words at every length. The boundary conditions explain why the standard all-one situation is genuinely exceptional. It does not resolve the other boundary case or classify blocks beginning with zero.

Self-review: passed. Independent audit: not yet performed.
