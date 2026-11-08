# Scientific review

## Correctness — PASS

The domain is all binary words of length \(n\ge5\), with one arbitrary five-position permutation and the identity included. Classifying a nonidentity output by the endpoints of its changed interval proves the binomial local formula. The sixteen-state recurrence optimizes that formula over *all* source words and retains tie multiplicities. The explicitly printed sixteen pairs at length sixteen and the exact equality \(V_{19}(s)=(h_{16}(s)+16,c_{16}(s))\) are verified by `check.py` and yield an all-length induction. Direct output enumeration cross-checks every word of lengths five through twelve; this is a cross-check, not the infinite proof. The only finite certificate dependencies are integer binomial coefficients, maximum and tie-sum transitions in the embedded standalone program.

## Originality — PASS, with priority caveat

The most important direct prior result is Chen and Milenkovic, arXiv:2610.15701v1, Section II: an exact **individual-input** sphere formula and the random-input mean, neither of which is claimed here. Section IV concerns coding bounds. We inspected the relevant full HTML sections, searched within the manuscript for five-window and extremal formulae, and compared the logical strength of the results. The per-word formula implies an efficient route to *computing* the optimum but does not state, directly yield without a separate optimization, or enumerate the new three-periodic all-length maximizing structure. An existing all-alphabet local-volume result likewise does not give the optimum; a four-window exact maximum has a different domain. Targeted mathematical-literature and searchable mathematical-record queries revealed no explicit equivalent. The search is not a proof of worldwide priority; unindexed or inaccessible work remains a risk.

## Mathematical value — PASS

The source's coding problem is naturally sensitive to the *worst-case* number of outcomes produced by one permutation burst. The exact five-window answer and enumeration of all maximizing words identify a three-periodic extremal law, including transient exceptional counts, whereas the already known four-window behavior is linear and has a fixed six-extremizer pattern. The result is an infinite sharp characterization, not a numerical increment to a small lookup table. The finite-state identity provides a reusable rigorous optimization certificate for related constrained burst channels. It does not claim a new coding-rate theorem.

## Scope and limitations

No higher-alphabet, larger-window, or multiple-error theorem is claimed. The exact recurrence checks are self-review and do not constitute independent audit or definitive priority confirmation.

Self-review: passed. Independent audit: not yet performed.
