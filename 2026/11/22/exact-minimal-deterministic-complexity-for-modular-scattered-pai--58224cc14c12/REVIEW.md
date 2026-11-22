# Scientific review: exact modular scattered-pair state complexity with a forbidden factor

## Correctness — PASS
The theorem specifies complete DFAs, admissible parameters and the distinction between contiguous avoidance and scattered counts. The word \(0\,1^{t+1}(01)^{k-1}0^j\) proves reachability of each active triple; the zero fibres of the affine suffix function \(c+ab+(a+1)d\) distinguish modular counters even for composite moduli; a run-boundary suffix distinguishes different active trailing-zero lengths. Both terminal right languages are identified explicitly. The 117 independent DFA minimizations and 51,175 direct-membership comparisons corroborate the general proof but are not substituted for it.

## Originality — PASS, with residual priority uncertainty
Inspected the published constrained-avoidance prefix-sorting result and the exact unrestricted modular scattered-pattern state theorem in full, comparing the statements and parameter implications. The first lacks modular scattered-pair constraints and uses a different partial-automaton measure; the second counts the modular occurrences of a longer scattered pattern without forbidding it contiguously. The 2020 binomial-equivalence paper concerns equivalence classes and the nil-2 group rather than minimal complete automata for this intersection. Relevant indexed research and targeted literature searches revealed no dominating formula for this joint language. Absence from searches is not a uniqueness proof; undiscovered equivalent literature remains a risk.

## Value — PASS
Modular scattered-pair counts are natural streaming statistics; forbidding a long zero-run immediately before a one models a local coding or source constraint. Their intersection has a state cost not supplied by separate language-recognition counts. Its sharp \(rm^2+2\) complexity and the exact collapse of terminal-run signatures resolve a two-parameter natural family, rather than an arbitrary finite slice.

## Limits
The result is binary, concerns one modular count and one forbidden factor, and addresses complete DFAs only. The bounded checks do not establish the infinite theorem without the mathematical proof; historical publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
