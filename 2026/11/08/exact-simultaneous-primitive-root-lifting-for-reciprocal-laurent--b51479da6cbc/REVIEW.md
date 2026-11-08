# Review of the simultaneous primitive-root lifting theorem

## Correctness — PASS
The prime-square primitive-root criterion follows from cyclic unit groups and an exact lifting argument. For any finite-field primitive seed \(a\), both \(x\) and \(x+arepsilon x^{-1}\) have nonvanishing first derivatives at the relevant residue classes, so each has exactly one forbidden lift modulo \(p^2\). Their overlap gives exactly \(p-2\) or \(p-1\) permitted first lifts, and each persists through exactly \(p^{k-2}\) lifts modulo \(p^k\). The cited finite-field theorem and direct small-prime exceptions close the existence statement. The supplied independent-of-proof brute-force checker confirmed the predictions for 44 prime-square sign cases and 24 prime-cube seed fibers. Computations do not certify unbounded parameters.

## Originality — PASS, with priority risk
Sun's Conjecture 4.10 asks for simultaneous primitive roots modulo powers of primes; the finite-field Corollary 2 of Cohen, Oliveira e Silva, Sutherland and Trudgian supplies the \(k=1\) seed classification, but does not state a prime-power residue-ring lifting theorem or exact \(p-2\)/\(p-1\) fiber count. Carella's later article concerns primitive-root behavior across levels for a fixed integer, not the inverse-Laurent two-function fiber problem. Searches of published mathematical result summaries did not identify an equivalent statement. An unindexed independent lifting argument or an equivalent earlier result remains possible; finite searches are not proof of priority. The exact numerical-overlap test is new as stated relative to the inspected comparisons.

## Mathematical value — PASS
The target is a specific explicitly formulated conjecture about modular primitive roots, not an arbitrary substitution. Besides obtaining complete existence and exception classification across all prime powers, the theorem determines an exact natural lifting invariant for every admissible base root, including the change when two first-order obstructions coincide. That structural dichotomy applies to arbitrarily high prime powers and directly informs future enumeration and least-witness questions. The result does not settle short intervals or a closed formula for the seed count.

## Closest literature and limitations
Sun, arXiv:1405.0290, Conjecture 4.10; Cohen et al., arXiv:1711.06392, Corollary 2; Carella, arXiv:2501.10399. The comparison does not claim that all historical literature is indexed or that an independent mathematical expert has assessed the proof. Existence invokes the finite-field corollary; the exact prime-power lifting is established in the proof.

Self-review: passed. Independent audit: not yet performed.
