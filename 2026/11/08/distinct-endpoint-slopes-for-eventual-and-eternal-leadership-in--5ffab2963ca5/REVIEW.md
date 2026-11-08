# Review: Distinct endpoint slopes for eventual and eternal leadership

## Correctness — PASS
The claim concerns two separate one-sided limits as retention \(p\uparrow1\). The proof checks the exact conditionally exchangeable two-table Pólya process, distinguishes eventual strictly greater limiting share from at-least-once strict takeover, and derives the Beta-integral weights \(2^{-r}\) and \(2^{-r}+r\int_0^{1/2}x^r/(1-x)\,dx\). The finite-birth expansion is justified because two fixed birth events have joint probability at most \((1-p)^2\). Crucially, an explicit exponentially small tail bound handles histories without early new tables, while a finite-state continuity lemma handles histories with early births. Positive-sum evaluation gives slopes \(1\) and \(3/2\). The finite rational checker passed; its results are not substituted for the infinite-time argument. For the one-time limit, a finite-family squeeze avoids relying on interchange of an infinite maximum and an infinite-time limit.

## Originality — PASS (provisional)
The closest source, Zheng, arXiv:2606.01881 (2026), establishes the two root-leadership probabilities, their positivity and their qualitative monotonicity/continuity, with an exponential challenger estimate. The exact, unequal one-sided derivatives and leading transient-leadership gap are not implications of those qualitative theorems. Baur, arXiv:1407.2508, analyzes a different joint regime in which the retention probability varies with the tree size. Targeted mathematical-record searches and accessible published descriptions did not identify the same endpoint coefficients. The closest 2026 full text could not be inspected; exact historical priority remains provisional and should be independently checked.

## Mathematical value — PASS
The distinction between being the ultimate largest component and never losing leadership is the central dynamic versus static issue in recursive-tree percolation. The sharp constants show that temporary losses account for exactly one-third of the first-order eternal-leadership failure coefficient, even as percolation becomes deterministic. The two-event comparison is a natural structural quantity and requires control of infinitely many potential challengers, not merely a finite-state calculation.

## Closest literature and limitations
Y. Zheng, *Can the root cluster remain largest forever in random recursive tree percolation?*, arXiv:2606.01881 (first submitted 2026-06-01). E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508. The theorem provides only the first one-sided derivative at \(p=1\), not a global formula for either leadership probability or a coupled finite-size scaling theorem. Full-text noncoverage and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
